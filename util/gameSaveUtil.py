import json
import os
from globalVals import *

def deleteSaveFile(filename):
    overwrite = open(getFilePath(filename), 'w')
    overwrite.write('')
    overwrite.close()

def newSaveFile(filename, data):
    newFile = open(getFilePath(filename), 'w')
    newFile.write(json.dumps(data))
    newFile.close()

def overwriteFile(filename, data):
    if not saveFileIsEmpty(filename):
        deleteSaveFile(filename)

    newSaveFile(filename, data)

def loadSaveFile(filename):
    loadFile = open(getFilePath(filename), 'r')
    gameObj = json.loads(loadFile.read())
    loadFile.close()

    return gameObj

def selectGameObject(filename):
    self.selectedGame = loadSaveFile(filename)

def getFilePath(filename):
    return os.path.join('saves', filename)

def getSaveFiles():
    return ['save1.json', 'save2.json', 'save3.json']

def saveFileIsEmpty(filename):
    return os.stat(filename).st_size == 0