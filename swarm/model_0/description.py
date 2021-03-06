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


## This file defines parameters for a prediction experiment.

###############################################################################
#                                IMPORTANT!!!
# This params file is dynamically generated by the RunExperimentPermutations
# script. Any changes made manually will be over-written the next time
# RunExperimentPermutations is run!!!
###############################################################################


from nupic.frameworks.opf.expdescriptionhelpers import importBaseDescription

# the sub-experiment configuration
config ={
  'aggregationInfo' : {'seconds': 0, 'fields': [], 'months': 0, 'days': 0, 'years': 0, 'hours': 0, 'microseconds': 0, 'weeks': 0, 'minutes': 0, 'milliseconds': 0},
  'modelParams' : {'sensorParams': {'encoders': {u'timestamp_dayOfWeek': None, u'V41': None, u'V40': None, u'V43': None, u'V42': None, u'V45': None, u'V44': None, u'V47': None, u'V46': None, u'V49': None, u'V48': None, u'V23': None, u'V22': None, u'V21': None, u'V20': None, u'V27': None, u'V26': None, u'V25': None, u'V24': None, u'V29': None, u'V28': None, u'V3': None, u'V4': None, u'V5': None, u'V6': None, u'V7': None, u'V8': None, u'V9': None, u'heartbeat': {'maxval': 300.0, 'name': 'heartbeat', 'clipInput': True, 'minval': 0.0, 'n': 272, 'fieldname': 'heartbeat', 'w': 21, 'type': 'ScalarEncoder'}, u'V18': None, u'V54': None, u'V19': None, u'V52': None, u'V53': None, u'V50': None, u'V51': None, u'V30': None, u'V31': None, u'V32': None, u'V33': None, u'V34': None, u'V35': None, u'V36': None, u'V37': None, u'V12': None, u'V13': None, u'V10': None, u'V11': None, u'V16': None, u'V17': None, u'V14': None, u'V15': None, u'V38': None, u'V39': None, u'timestamp_timeOfDay': None, u'timestamp_weekend': None}}, 'spParams': {'synPermInactiveDec': 0.05015}, 'tpParams': {'minThreshold': 11, 'activationThreshold': 14, 'pamLength': 3}, 'clParams': {'alpha': 0.050050000000000004}},

}

mod = importBaseDescription('../description.py', config)
locals().update(mod.__dict__)
