import json
import os
from globalVals import *

def deleteSaveFile(filename):
    overwrite = open(getFilePath(filename), 'w')
    overwrite.write('')
    overwrite.close()

def newSaveFile(filename, data):
    newFile = open(getFilePath(filename), 'w')
    newFile.write(json.dumps(data['data']))
    newFile.close()

def overwriteFile(filename, data):
    if not saveFileIsEmpty(filename):
        deleteSaveFile(filename)

    newSaveFile(filename, data)

def loadSaveFile(filename):
    loadFile = open(getFilePath(filename), 'r')

    gameObj = {
        'file': filename,
        'data': {}
    }

    if not saveFileIsEmpty(filename):
        gameObj['data'] = json.loads(loadFile.read())
    loadFile.close()

    return gameObj

def selectGameObject(filename):
    gameConfig.selectedGame = loadSaveFile(filename)

def getFilePath(filename):
    return os.path.join('saves', filename)

def getSaveFiles():
    saves = []
    for file in os.listdir(os.path.join('saves')):
        if file.endswith('.json'):
            saves.append(loadSaveFile(file))
    return saves

def saveFileIsEmpty(filename):
    return os.stat(getFilePath(filename)).st_size == 0

def saveGame():
    pass    