# -*- coding: utf-8 -*-

from operator import index
import os
from tqdm import tqdm
import pandas as pd
import numpy as np
import logging
# -----------------    CAMINHOS   ------------------ #
# _________  DEFINIR CONFIGURAÇÕES INICIAIS________ #
# Formatação de cores para o Print no terminal 
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"

# --------------------------------------------------------
# INFORMAÇÕES INICIAIS 
print(cyan + 'INFO SCRIPT' + reset_color)
print('Sript excutado :', yellow +  os.path.basename(__file__) + reset_color)
print('Localização :',  yellow +  (__file__) + reset_color)
# -------------------------------------------------- #
# --------------------------------------------------------
# INFORMAÇÕES INICIAIS LOG
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename='log_' + os.path.basename(__file__) + '.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)
# Instancia do objeto getLogger()
logger = logging.getLogger('root')
# -----------------    CAMINHOS   ------------------ #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #
currentdir = os.getcwd()
VALIDAR_ROOT = [f for f in os.listdir(currentdir) if os.path.isdir(currentdir + '\\' + f) if f == 'core' ]

chck_root = __file__.split('\\')
contador = 0
if VALIDAR_ROOT[0] == 'core':
    ROOT = currentdir
else:
    while (chck_root[-contador] != 'core'):      
        ROOT = '\\'.join(chck_root[0:-((contador + 1))])
        contador   = contador + 1
        ROOT = ROOT

print('Diretório ROOT :',  yellow +  (ROOT) + reset_color)
print()
# -------------------------------------------------- #

# Definindo a pasta a ser consultada
DATA_MANEGER_DATA = ROOT + '\\core\\maneger\\' + 'Data\\'
#filecsv_namefix = currentdir + '\\core\\maneger\\Data\\datadir.csv'
FILE_CSV_FIX_NAME_SYSTEM = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem.csv'
#filecsv_nametemp = currentdir + '\\core\\maneger\\Data\\datadir_temp.csv'
FILE_CSV_FIX_NAME_SYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem_Tmp.csv'
#listcsv_clean = currentdir + '\\core\\maneger\\Data\\cleandir.csv'
FILE_CSV_FIX_NAME_CLEAN = ROOT + '\\core\\maneger\\Data\\Fix_NameClean.csv'
#listcsv_cleantemp = currentdir + '\\core\\maneger\\Data\\cleandir_temp.csv'
FILE_CSV_FIX_NAME_CLEAN_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameClean_Tmp.csv'

#TESTE_UM_TIPO_MEDIA = [f for f in os.listdir('.') if f.endswith('.txt')]
ITEMS_COLLECTION_NAME = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\')]
ITEMS_COLLECTION_DIR_NAME = ([os.path.join(ROOT + '\\collections\\', file) for file in os.listdir(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\' + file)])
ITEMS_COLLECTION_DIR__CONTENT = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)])
ITEMS_COLLECTION_NAME__CONTENT = ([(file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)])
ITEMS_COLLECTION_FILE_CONF = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.conf')])
ITEMS_COLLECTION_FILE_SUB = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.sub')])
ITEMS_COLLECTION_FILE_TXT = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.txt')])
ITEMS_COLLECTION_FILE_PNG = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.png')])
ITEMS_COLLECTION_FILE_JPG = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.jpg')])

ITEMS_COLLECTION_FILE_AVI = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.avi')])
ITEMS_COLLECTION_FILE_MP4 = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.mp4')])
ITEMS_COLLECTION_FILE_MP3 = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.mp3')])
ITEMS_COLLECTION_FILE_OGG = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if file3.endswith('.ogg')])



#ITEMS_COLLECTION_FILE_CONTENT_TXT = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.txt')])


ITEMS_COLLECTION_FILE_CONTENT_PNG = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\') if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')])
print(ITEMS_COLLECTION_FILE_CONTENT_PNG)

ITEMS_COLLECTION_FILE_CONTENT_JPG = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.jpg')])
ITEMS_COLLECTION_FILE_CONTENT_AVI = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.avi')])
ITEMS_COLLECTION_FILE_CONTENT_MP4 = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.mp4')])
ITEMS_COLLECTION_FILE_CONTENT_MP3 = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.mp3')])
ITEMS_COLLECTION_FILE_CONTENT_OGG = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.ogg')])

ITEMS_EMULATORS_NAME = [f for f in os.listdir(ROOT + '\\emulators\\') if os.path.exists(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\')]
ITEMS_EMULATORS_DIR_NAME = ([os.path.join(ROOT + '\\emulators\\', file) for file in os.listdir(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\' + file)])
ITEMS_EMULATORS_DIR__CONTENT = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if os.path.isdir(ROOT + '\\emulators\\' + file + '\\' + file2)])
ITEMS_EMULATORS_FILE_INI = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.ini')])
ITEMS_EMULATORS_FILE_CFG = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.cfg')])
ITEMS_EMULATORS_FILE_LPL = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.lpl')])
ITEMS_EMULATORS_FILE_EXE = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.exe')])

ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
ITEMS_LAYOUTS_DIR_NAME = ([os.path.join(ROOT + '\\layouts\\', file) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file)])
ITEMS_LAYOUTS_FILE_XML = ([os.path.join(ROOT + '\\layouts\\' + file + '\\', file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file) for file2 in os.listdir(ROOT + '\\layouts\\' + file) if file2.endswith('.xml')])
ITEMS_LAYOUTS_DIR_COLLECTION = ([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')])
ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT =([os.path.join(file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT = ([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)]) 
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS = ([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\', file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)]) 
ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT = ([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3)]) 
ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML = ([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.xml')])
ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG = ([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.png')])

ITEMS_ROCKETLAUNCHER_NAME = ([file for file in os.listdir(ROOT + '\\RocketLauncher') if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)])
ITEMS_ROCKETLAUNCHER_DIR_NAME = ([os.path.join(ROOT + '\\RocketLauncher\\', file) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.exists(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)])
ITEMS_ROCKETLAUNCHER_DIR_CONTENT = ([os.path.join(ROOT + '\\RocketLauncher\\' + file, file2) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2)])
ITEMS_ROCKETLAUNCHER_SETTINGS_NAME = [f for f in os.listdir(ROOT + '\\RocketLauncher\\Settings') if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + f) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + f)]
ITEMS_ROCKETLAUNCHER_DIR_SETTINGS = ([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file)])
ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI = ([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Settings\\' + file) if file2.endswith('.ini')]) 
ITEMS_ROCKETLAUNCHER_DATA_NAME = ([file for file in os.listdir(ROOT + '\\RocketLauncher\\Data')]) 
ITEMS_ROCKETLAUNCHER_DIR_DATA = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\' + file) for file in os.listdir(ROOT + '\\RocketLauncher\\Data')]) 
ITEMS_ROCKETLAUNCHER_FILE_DATA_INI = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')]) 
ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\Game Info\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')]) 
ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\History\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')]) 
ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\Language\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')]) 
ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\Moves List\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.dat')]) 
ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI = ([os.path.join(ROOT + '\\RocketLauncher\\Data\\Statistics\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.dat')]) 

ITEMS_ROCKETLAUNCHER_MEDIA_NAME = ([file for file in os.listdir(ROOT + '\\RocketLauncher\\Media')]) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA = ([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file) for file in os.listdir(ROOT + '\\RocketLauncher\\Media')]) 
ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME =  ([file2 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file)]) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM =  ([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file)]) 
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME =  ([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2)]) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM =  ([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2)]) 
#ITEMS_ROCKETLAUNCHER_FILE_MEDIA_ROM_PNG =  ([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME   for file3 in ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if file4.endswith('.png')]) 

# obtenha a lista de tuplas de duas listas
# e mescle-as usando zip().
#InfoDirLits = list(zip(ITEMS_COLLECTION_NAME, ITEMS_COLLECTION_DIR_NAME,ITEMS_COLLECTION_DIR__CONTENT ,ITEMS_COLLECTION_FILE_CONF ,ITEMS_COLLECTION_FILE_SUB ,ITEMS_EMULATORS_NAME ,ITEMS_EMULATORS_DIR_NAME ,ITEMS_EMULATORS_DIR__CONTENT ,ITEMS_EMULATORS_FILE_INI ,ITEMS_EMULATORS_FILE_CFG ,ITEMS_EMULATORS_FILE_LPL ,ITEMS_EMULATORS_FILE_EXE ,ITEMS_LAYOUTS_NAME ,ITEMS_LAYOUTS_DIR_NAME ,ITEMS_LAYOUTS_FILE_XML ,ITEMS_LAYOUTS_DIR_COLLECTION ,ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT ,ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT ,ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS ,ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT,ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML ,ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG ,ITEMS_ROCKETLAUNCHER_NAME ,ITEMS_ROCKETLAUNCHER_DIR_NAME ,ITEMS_ROCKETLAUNCHER_DIR_CONTENT ,ITEMS_ROCKETLAUNCHER_SETTINGS_NAME ,ITEMS_ROCKETLAUNCHER_DIR_SETTINGS ,ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI ,ITEMS_ROCKETLAUNCHER_DATA_NAME ,ITEMS_ROCKETLAUNCHER_DIR_DATA ,ITEMS_ROCKETLAUNCHER_FILE_DATA_INI ,ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI ,ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI ,ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI ,ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT ,ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI ,ITEMS_ROCKETLAUNCHER_MEDIA_NAME ,ITEMS_ROCKETLAUNCHER_DIR_MEDIA ,ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME ,ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM ,ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME ,ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM))
#InfoColumns = 'ITEMS_COLLECTION_NAME', 'ITEMS_COLLECTION_DIR_NAME','ITEMS_COLLECTION_DIR__CONTENT' ,'ITEMS_COLLECTION_FILE_CONF' ,'ITEMS_COLLECTION_FILE_SUB' ,'ITEMS_EMULATORS_NAME' ,'ITEMS_EMULATORS_DIR_NAME' ,'ITEMS_EMULATORS_DIR__CONTENT' ,'ITEMS_EMULATORS_FILE_INI' ,'ITEMS_EMULATORS_FILE_CFG' ,'ITEMS_EMULATORS_FILE_LPL' ,'ITEMS_EMULATORS_FILE_EXE' ,'ITEMS_LAYOUTS_NAME' ,'ITEMS_LAYOUTS_DIR_NAME' ,'ITEMS_LAYOUTS_FILE_XML' ,'ITEMS_LAYOUTS_DIR_COLLECTION' ,'ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT' ,'ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT' ,'ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS' ,'ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT','ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML' ,'ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG' ,'ITEMS_ROCKETLAUNCHER_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_CONTENT' ,'ITEMS_ROCKETLAUNCHER_SETTINGS_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_SETTINGS' ,'ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI' ,'ITEMS_ROCKETLAUNCHER_DATA_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_DATA' ,'ITEMS_ROCKETLAUNCHER_FILE_DATA_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT' ,'ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI' ,'ITEMS_ROCKETLAUNCHER_MEDIA_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_MEDIA' ,'ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM' ,'ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM'
# converte uma lista de tuplas num DataFrame
#DirSystem_df = pd.DataFrame(InfoDirLits, columns=['ITEMS_COLLECTION_NAME', 'ITEMS_COLLECTION_DIR_NAME','ITEMS_COLLECTION_DIR__CONTENT' ,'ITEMS_COLLECTION_FILE_CONF' ,'ITEMS_COLLECTION_FILE_SUB' ,'ITEMS_EMULATORS_NAME' ,'ITEMS_EMULATORS_DIR_NAME' ,'ITEMS_EMULATORS_DIR__CONTENT' ,'ITEMS_EMULATORS_FILE_INI' ,'ITEMS_EMULATORS_FILE_CFG' ,'ITEMS_EMULATORS_FILE_LPL' ,'ITEMS_EMULATORS_FILE_EXE' ,'ITEMS_LAYOUTS_NAME' ,'ITEMS_LAYOUTS_DIR_NAME' ,'ITEMS_LAYOUTS_FILE_XML' ,'ITEMS_LAYOUTS_DIR_COLLECTION' ,'ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT' ,'ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT' ,'ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS' ,'ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT','ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML' ,'ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG' ,'ITEMS_ROCKETLAUNCHER_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_CONTENT' ,'ITEMS_ROCKETLAUNCHER_SETTINGS_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_SETTINGS' ,'ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI' ,'ITEMS_ROCKETLAUNCHER_DATA_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_DATA' ,'ITEMS_ROCKETLAUNCHER_FILE_DATA_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI' ,'ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT' ,'ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI' ,'ITEMS_ROCKETLAUNCHER_MEDIA_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_MEDIA' ,'ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM' ,'ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME' ,'ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM'])

s1=pd.Series(ITEMS_COLLECTION_NAME,name='ITEMS_COLLECTION_NAME')
s2=pd.Series(ITEMS_COLLECTION_DIR_NAME,name='ITEMS_COLLECTION_DIR_NAME')
s3=pd.Series(ITEMS_COLLECTION_DIR__CONTENT ,name='ITEMS_COLLECTION_DIR__CONTENT')
s4=pd.Series(ITEMS_COLLECTION_FILE_CONF,name='ITEMS_COLLECTION_FILE_CONF')
s5=pd.Series(ITEMS_COLLECTION_FILE_SUB,name='ITEMS_COLLECTION_FILE_SUB')
s6=pd.Series(ITEMS_EMULATORS_NAME,name='ITEMS_EMULATORS_NAME')
s7=pd.Series(ITEMS_EMULATORS_DIR_NAME,name='ITEMS_EMULATORS_DIR_NAME')
s8=pd.Series(ITEMS_EMULATORS_DIR__CONTENT,name='ITEMS_EMULATORS_DIR__CONTENT')
s9=pd.Series(ITEMS_EMULATORS_FILE_INI,name='ITEMS_EMULATORS_FILE_INI')
s10=pd.Series(ITEMS_EMULATORS_FILE_CFG,name='ITEMS_EMULATORS_FILE_CFG')
s11=pd.Series(ITEMS_EMULATORS_FILE_LPL,name='ITEMS_EMULATORS_FILE_LPL')
s12=pd.Series(ITEMS_EMULATORS_FILE_EXE,name='ITEMS_EMULATORS_FILE_EXE')
s13=pd.Series(ITEMS_LAYOUTS_NAME,name='ITEMS_LAYOUTS_NAME')
s14=pd.Series(ITEMS_LAYOUTS_DIR_NAME,name='ITEMS_LAYOUTS_DIR_NAME')
s15=pd.Series(ITEMS_LAYOUTS_FILE_XML,name='ITEMS_LAYOUTS_FILE_XML')
s16=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION,name='ITEMS_LAYOUTS_DIR_COLLECTION')
s17=pd.Series(ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT,name='ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT')
s18=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT,name='ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT')
s19=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS,name='ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS')
s20=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT,name='ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT')
s21=pd.Series(ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML,name='ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML')
s22=pd.Series(ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG,name='ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG')
s23=pd.Series(ITEMS_ROCKETLAUNCHER_NAME,name='ITEMS_ROCKETLAUNCHER_NAME')
s24=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_NAME,name='ITEMS_ROCKETLAUNCHER_DIR_NAME')
s25=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_CONTENT,name='ITEMS_ROCKETLAUNCHER_DIR_CONTENT')
s26=pd.Series(ITEMS_ROCKETLAUNCHER_SETTINGS_NAME,name='ITEMS_ROCKETLAUNCHER_SETTINGS_NAME')
s27=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_SETTINGS,name='ITEMS_ROCKETLAUNCHER_DIR_SETTINGS')
s28=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI,name='ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI')
s29=pd.Series(ITEMS_ROCKETLAUNCHER_DATA_NAME,name='ITEMS_ROCKETLAUNCHER_DATA_NAME')
s30=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_DATA,name='ITEMS_ROCKETLAUNCHER_DIR_DATA')
s31=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_DATA_INI,name='ITEMS_ROCKETLAUNCHER_FILE_DATA_INI')
s32=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI,name='ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI')
s33=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI,name='ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI')
s34=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI,name='ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI')
s35=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT,name='ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT')
s36=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI,name='ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI')
s37=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_NAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_NAME')
s38=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA')
s39=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME')
s40=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM')
s41=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME')
s42=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM')

s43=pd.Series(ITEMS_COLLECTION_NAME__CONTENT,name='ITEMS_COLLECTION_NAME__CONTENT')
s44=pd.Series(ITEMS_COLLECTION_FILE_TXT,name='ITEMS_COLLECTION_FILE_TXT')
s45=pd.Series(ITEMS_COLLECTION_FILE_PNG,name='ITEMS_COLLECTION_FILE_PNG')
s46=pd.Series(ITEMS_COLLECTION_FILE_JPG,name='ITEMS_COLLECTION_FILE_JPG')

s47=pd.Series(ITEMS_COLLECTION_FILE_AVI,name='ITEMS_COLLECTION_FILE_AVI')
s48=pd.Series(ITEMS_COLLECTION_FILE_MP4,name='ITEMS_COLLECTION_FILE_MP4')
s49=pd.Series(ITEMS_COLLECTION_FILE_MP3,name='ITEMS_COLLECTION_FILE_MP3')
s50=pd.Series(ITEMS_COLLECTION_FILE_OGG,name='ITEMS_COLLECTION_FILE_OGG')

s51=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_TXT,name='ITEMS_COLLECTION_FILE_CONTENT_TXT')
s52=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_PNG,name='ITEMS_COLLECTION_FILE_CONTENT_PNG')
s53=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_JPG,name='ITEMS_COLLECTION_FILE_CONTENT_JPG')
s54=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_AVI,name='ITEMS_COLLECTION_FILE_CONTENT_AVI')
s55=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_MP4,name='ITEMS_COLLECTION_FILE_CONTENT_MP4')
s56=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_MP3,name='ITEMS_COLLECTION_FILE_CONTENT_MP3')
s57=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_OGG,name='ITEMS_COLLECTION_FILE_CONTENT_OGG')

if os.path.isfile(DATA_MANEGER_DATA + 'DirSystem.csv'):
    try:
        os.remove(DATA_MANEGER_DATA + 'DirSystem.csv')
        os.remove(DATA_MANEGER_DATA + 'DirSystem_Tmp.csv')
    except IOError:
        print(u'CSV antigo deletado!', '\n','Vamos fazer a partir do original :', DATA_MANEGER_DATA + 'DirSystem.csv')

DirSystem_df = pd.concat([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10 ,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 ,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30 ,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57], axis=1)
DirSystem_df.to_csv(DATA_MANEGER_DATA + 'DirSystem.csv', encoding='utf-8', sep=';')

def teste_print(palavra):
    print('teste', palavra)