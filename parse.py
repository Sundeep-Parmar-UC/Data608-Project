import loadgame as lg
import parsemove as pm
import loadmove as lm

def Parse(uncompressFilePath):
    
    metric = [10,20,30,"Game","Moves",uncompressFilePath]
    successbit = True
    return metric,successbit
