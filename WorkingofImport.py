import sklearn as sk
print(sk.__version__)

import sys
print(sys.path)

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

"""
Awein is a user defined module and we have imported it for our use.
 
"""

import awein
awein.joke("I am a good boy")