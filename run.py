#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------
"""
Groups together code used for creating a NuPIC model and dealing with IO.
(This is a component of the One Hot Gym Anomaly Tutorial.)
"""
import importlib
import sys
import csv
#import datetime
from datetime import datetime
import pandas as pd
from cassandra.cluster import Cluster
from nupic.frameworks.opf.modelfactory import ModelFactory
import time
import nupic_anomaly_output


DESCRIPTION = (
  "Starts a NuPIC model from the model params returned by the swarm\n"
  "and pushes each line of input from the gym into the model. Results\n"
  "are written to an output file (default) or plotted dynamically if\n"
  "the --plot option is specified.\n"
)

DATA_FILE = "heart-beat"
DATA_DIR = "." # "/home/ksaha/Data/Data_Run"
MODEL_PARAMS_DIR = "./model_params"
INPUT_DATA = "anomaly-data.csv" # "%s/%s.csv" % (DATA_DIR, DATA_FILE.replace(" ", "_"))
# '7/2/10 0:00'
DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
#DATE_FORMAT = "%m/%d/%y %H:%M"

def createModel(modelParams):
  """
  Given a model params dictionary, create a CLA Model. Automatically enables
  inference for kw_energy_consumption.
  :param modelParams: Model params dict
  :return: OPF Model object
  """
  model = ModelFactory.create(modelParams)
  model.enableInference({"predictedField": "heartbeat"})
  return model


def getModelParamsFromName():
  """
  Given a gym name, assumes a matching model params python module exists within
  the model_params directory and attempts to import it.
  :return: OPF Model params dictionary
  """
  importName = "model_params.%s_model_params" % (
    DATA_FILE.replace(" ", "_").replace("-", "_")
  )
  print "Importing model params from %s" % importName
  try:
    importedModelParams = importlib.import_module(importName).MODEL_PARAMS
  except ImportError:
    raise Exception("No model params exist for '%s'. Run swarm first!"
                    % DATA_FILE)
  return importedModelParams


def runIoThroughNupic(model):
  """
  Handles looping over the input data and passing each row into the given model
  object, as well as extracting the result object and passing it into an output
  handler.
  :param inputData: file path to input data CSV
  :param model: OPF Model object
  """
  counter = 0
  
  output = nupic_anomaly_output.NuPICFileOutput(DATA_FILE)

  cluster = Cluster(['10.10.40.138'])
  session = cluster.connect('hotgym')  # key-space = hotgym
  print ("Connected!")

  num_records_index = 0
  total_records = 10 #129962  # -1 
  patient_id = '101'
  
  # Master Data Source
  df = pd.read_csv(INPUT_DATA)
  
  time_diff = datetime.strptime(str(datetime.utcnow()), DATE_FORMAT)

  while(num_records_index < total_records):

        print "Processing record = %i ..." % num_records_index
        val_time_stamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
	        
        val_heartbeat = str(df.iloc[num_records_index,1])

	val_activity = str(df.iloc[num_records_index,2])

        CQL_Insert_String = "INSERT INTO data_input_11_18_10 (patient_id,time_stamp, heartbeat, activity) " + \
                             "VALUES ('" + patient_id + "','"+ val_time_stamp + "','" + \
                            val_heartbeat + "','" + val_activity +"');"

        session.execute(CQL_Insert_String)
        
        # Add the record from the actual data source to the Cassandra input table
        ## Read back the latest row added from Cassandra input table
        CQLString = "SELECT * FROM data_input_11_18_10  LIMIT 1;" 
        rows = session.execute(CQLString)
        for user_row in rows:
                data_df = pd.DataFrame({'col_1' : [user_row.time_stamp], \
					'col_2' : [user_row.heartbeat],
					'col_3' : [user_row.activity]})

        datetime_str = str(data_df.iloc[0,0])
        if len(datetime_str) == 19:     # Taking care of the parsing error when no millisecs are present in timestamp
                counter += 1
                datetime_str = datetime_str +".001"
        
	timestamp = datetime.strptime(str(datetime_str), DATE_FORMAT) 
		
        heartbeat = float(data_df.iloc[0,1])
        activity = data_df.iloc[0,2]
        ## Code for mapping activity to be written
             
        result = model.run({
                            "timestamp": timestamp,
                            "heartbeat": heartbeat
                           })
        
        prediction = result.inferences["multiStepBestPredictions"][1]
        anomalyScore = result.inferences["anomalyScore"]
        ## Write this anomaly score to the Cassandra output table
        
        anomalyLikelihood = output.write(timestamp, heartbeat, prediction, anomalyScore)

	time_diff = timestamp - time_diff
	print time_diff

        output_timestamp = str(timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
        print output_timestamp, heartbeat, prediction, anomalyScore, anomalyLikelihood 
        
        CQL_Output_String = "INSERT INTO data_output_11_18_10 (patient_id,timestamp,heartbeat, \
                             prediction,anomalyScore,anomalyLikelihood,activity) " + "VALUES ('" + \
                             patient_id + "','"+ output_timestamp + "','" + str(heartbeat) + \
			     "','" + str(prediction) + "','" + str(anomalyScore) + "','" + \
			     str(anomalyLikelihood) + "','" + str(activity) + "');"

        session.execute(CQL_Output_String)

        if anomalyScore > 0.0:
		
		CQL_Anomaly_String = "INSERT INTO data_anomaly_11_18_10 (patient_id,timestamp,heartbeat, \
        	                      prediction,anomalyScore,anomalyLikelihood,activity,record_num) " + \
                                     "VALUES ('" + patient_id + "','"+ output_timestamp + "','" + str(heartbeat) + \
                        	      "','" + str(prediction) + "','" + str(anomalyScore) + "','" + \
                             str(anomalyLikelihood) + "','" + str(activity) + "','" + str(num_records_index+1) + "');"

        	session.execute(CQL_Anomaly_String)
	
	# Just for statistics gathering. Will remove this table	
	CQL_time_diff_String = "INSERT INTO data_time_diff_11_18_10 (patient_id,timestamp,time_diff) " + \
			        "VALUES ('" + patient_id + "','"+ output_timestamp + "','" + str(time_diff) + "');"


        session.execute(CQL_time_diff_String)
               
	time_diff = timestamp  
        # To simulate real-time case we add delay here

  #      print("Waiting for the next record. Delay is 1 sec")

  #      time.sleep(.001)
	
        num_records_index += 1

  print("counter value+++++++++++++++++++++++++++++")
  print counter


def runModel():
  """
  Assumes the gynName corresponds to both a like-named model_params file in the
  model_params directory, and that the data exists in a like-named CSV file in
  the current directory.
  """
  print "Creating model from %s..." % DATA_FILE
  model = createModel(getModelParamsFromName())
  runIoThroughNupic(model)

if __name__ == "__main__":
  print DESCRIPTION
  start_time = time.time()
  runModel()
  print("--Total Time Taken = %s seconds ------------------------" % (time.time() - start_time))
  print("-- Per row avg -- = % d milliseconds -------------------" % ((time.time() - start_time)/129962*1000))
