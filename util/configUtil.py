import os
import json
from globalVals import *

def createConfigFilePath():
    return os.path.join('assets', config.CFGFILE)

def loadConfig():
    cfg = createConfigFilePath()
    
    if os.path.isfile(cfg):
        # open the file
        cfgFile = open(cfg, 'r')

        # process
        cfgJson = json.loads(cfgFile.read())

        # set constants
        constants.SSIZE = (cfgJson['screenWidth'], cfgJson['screenHeight'])

        # set flags
        flags.DEBUG = cfgJson['debug']
        flags.USECUSTOMFONT = cfgJson['useCustomFont']

        # set asset values
        config.IMGPATH = cfgJson['imgsFolder']
        config.ICONPATH = cfgJson['iconsFolder']
        config.AUDIOPATH = cfgJson['audioFolder']
        config.FONTPATH = cfgJson['fontsFolder']

        # set fonts
        fonts.FSANS = cfgJson['sansSerifFont']
        fonts.FSERIF = cfgJson['serifFont']
        fonts.FMONO = cfgJson['monospaceFont']
        fonts.FCUST = cfgJson['customFont']
        if '.ttf' not in cfgJson['customFont']:
            fonts.FCUST = fonts.FCUST + '.ttf'

        # close
        cfgFile.close()