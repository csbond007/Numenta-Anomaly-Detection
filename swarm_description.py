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

SWARM_DESCRIPTION = {
  "includedFields": [
    {
      "fieldName": "timestamp",
      "fieldType": "datetime"
    },
    {
      "fieldName": "heartbeat",
      "fieldType": "float",
      "maxValue": 300.0,
      "minValue": 0.0
    },
    {
      "fieldName": "V3",
      "fieldType": "int"
    },
    {
      "fieldName": "V4",
      "fieldType": "float"
    },
    {
      "fieldName": "V5",
      "fieldType": "float"
    },
    {
      "fieldName": "V6",
      "fieldType": "float"
    },
    {
      "fieldName": "V7",
      "fieldType": "float"
    },
    {
      "fieldName": "V8",
      "fieldType": "float"
    },
    {
      "fieldName": "V9",
      "fieldType": "float"
    },
    {
      "fieldName": "V10",
      "fieldType": "float"
    },
    {
      "fieldName": "V11",
      "fieldType": "float"
    },
    {
      "fieldName": "V12",
      "fieldType": "float"
    },
    {
      "fieldName": "V13",
      "fieldType": "float"
    },
    {
      "fieldName": "V14",
      "fieldType": "float"
    },
    {
      "fieldName": "V15",
      "fieldType": "float"
    },
    {
      "fieldName": "V16",
      "fieldType": "float"
    },
    {
      "fieldName": "V17",
      "fieldType": "float"
    },
    {
      "fieldName": "V18",
      "fieldType": "float"
    },
    {
      "fieldName": "V19",
      "fieldType": "float"
    },
    {
      "fieldName": "V20",
      "fieldType": "float"
    },
    {
      "fieldName": "V21",
      "fieldType": "float"
    },
    {
      "fieldName": "V22",
      "fieldType": "float"
    },
    {
      "fieldName": "V23",
      "fieldType": "float"
    },
    {
      "fieldName": "V24",
      "fieldType": "float"
    },
    {
      "fieldName": "V25",
      "fieldType": "float"
    },
    {
      "fieldName": "V26",
      "fieldType": "float"
    },
    {
      "fieldName": "V27",
      "fieldType": "float"
    },
    {
      "fieldName": "V28",
      "fieldType": "float"
    },
    {
      "fieldName": "V29",
      "fieldType": "float"
    },
    {
      "fieldName": "V30",
      "fieldType": "float"
    },
    {
      "fieldName": "V31",
      "fieldType": "float"
    },
    {
      "fieldName": "V32",
      "fieldType": "float"
    },
    {
      "fieldName": "V33",
      "fieldType": "float"
    },
    {
      "fieldName": "V34",
      "fieldType": "float"
    },
    {
      "fieldName": "V35",
      "fieldType": "float"
    },
    {
      "fieldName": "V36",
      "fieldType": "float"
    },
    {
      "fieldName": "V37",
      "fieldType": "float"
    },
    {
      "fieldName": "V38",
      "fieldType": "float"
    },
    {
      "fieldName": "V39",
      "fieldType": "float"
    },
    {
      "fieldName": "V40",
      "fieldType": "float"
    },
    {
      "fieldName": "V41",
      "fieldType": "float"
    },
    {
      "fieldName": "V42",
      "fieldType": "float"
    },
    {
      "fieldName": "V43",
      "fieldType": "float"
    },
    {
      "fieldName": "V44",
      "fieldType": "float"
    },
    {
      "fieldName": "V45",
      "fieldType": "float"
    },
    {
      "fieldName": "V46",
      "fieldType": "float"
    },
    {
      "fieldName": "V47",
      "fieldType": "float"
    },
    {
      "fieldName": "V48",
      "fieldType": "float"
    },
    {
      "fieldName": "V49",
      "fieldType": "float"
    },
    {
      "fieldName": "V50",
      "fieldType": "float"
    },
    {
      "fieldName": "V51",
      "fieldType": "float"
    },
    {
      "fieldName": "V52",
      "fieldType": "float"
    },
    {
      "fieldName": "V53",
      "fieldType": "float"
    },
    {
      "fieldName": "V54",
      "fieldType": "float"
    }
  ],
  "streamDef": {
    "info": "heart-beat",
    "version": 1,
    "streams": [
      {
        "info": "Rec Center",
        "source": "file://heart-beat.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },

  "inferenceType": "TemporalAnomaly",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "heartbeat"
  },
  "iterationCount": -1,
  "swarmSize": "small"
}
