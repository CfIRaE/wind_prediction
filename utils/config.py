import os

DATAFOLDER = os.path.join(os.getcwd(),"data")

SVM_PARAM  =  [
    {"e" : 0.5 , "s" : 0.5, "c" : 100},
    {"e" : 1 , "s" : 1, "c" : 100},
    {"e" : 0.5 , "s" : 1, "c" : 500},
    {"e" : 0.5 , "s" : 1, "c" : 1000},
]
