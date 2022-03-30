# -*- coding: utf-8 -*-

from operator import index
import os
from tqdm import tqdm
import pandas as pd

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

# format size application (converting B to KB, MB, GB, TB)
def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'bytes'
# --------------------------------------------------------
SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

def format_unidade_size(size_in_bytes):
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        size = size_in_bytes
        unidadesize = SIZE_UNITS[index]
        return size 
    except IndexError:
        return 'File too large'
# --------------------------------------------------------
def format_unidade_medida(size_in_bytes):
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        unidadesize = SIZE_UNITS[index]
        return unidadesize 
    except IndexError:
        return 'File too large'
# --------------------------------------------------------
def getFolderSize(folder):
    #if os.path.isdir(folder):
    total_size = os.path.getsize(folder)
        
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size


# -----------------    CAMINHOS   ------------------ #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #
currentdir = os.getcwd()
chck_root = __file__.split('\\')
contador = 0
while (chck_root[-contador] != 'core'):      
       ROOT = '\\'.join(chck_root[0:-((contador + 1))])
       contador   = contador + 1
ROOT = ROOT
print('Diretório ROOT :',  yellow +  (ROOT) + reset_color)
print()


sizecollections = getFolderSize('collections')
sizecore = getFolderSize('core')
sizeemulators = getFolderSize('emulators')
sizelaunchers = getFolderSize('launchers.windows')
sizelayouts = getFolderSize('layouts')
sizemeta = getFolderSize('meta')
sizetotal = sizecollections + sizecore + sizeemulators + sizelaunchers + sizelayouts + sizemeta

# Definindo a pasta a ser consultada
TESTE_UM_TIPO_MEDIA = [f for f in os.listdir('.') if f.endswith('.txt')]
ITEMS_COLLECTION_NAME = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\')]
ITEMS_COLLECTION_DIR_NAME = ([os.path.join(ROOT + '\\collections\\', file) for file in os.listdir(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\' + file)])
ITEMS_COLLECTION_DIR__CONTENT = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)])
ITEMS_COLLECTION_FILE_CONF = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.conf')])
ITEMS_COLLECTION_FILE_SUB = ([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.sub')])

ITEMS_EMULATORS_NAME = [f for f in os.listdir(ROOT + '\\emulators\\') if os.path.exists(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\')]
ITEMS_EMULATORS_DIR_NAME = ([os.path.join(ROOT + '\\emulators\\', file) for file in os.listdir(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\' + file)])
ITEMS_EMULATORS_DIR__CONTENT = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if os.path.isdir(ROOT + '\\emulators\\' + file + '\\' + file2)])
ITEMS_EMULATORS_FILE_INI = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.ini')])
ITEMS_EMULATORS_FILE_CFG = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.cfg')])
ITEMS_EMULATORS_FILE_LPL = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.lpl')])
ITEMS_EMULATORS_FILE_EXE = ([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.exe')])

ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
ITEMS_LAYOUTS_DIR_NAME = ([os.path.join(ROOT + '\\layouts\\', file) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file)])
ITEMS_LAYOUTS_FILE_XML = ([os.path.join(ROOT + '\\layouts\\', file) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file) if file.endswith('.xml')])
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

print(cyan + 'INICIANDO LEITURA ...' + reset_color)
print(red + 'Folder Size' + reset_color, yellow + 'core' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('core'))))), format_unidade_medida(sizecore) + reset_color)
print(red + 'Folder Size' + reset_color, yellow + 'emulators' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('emulators'))))), format_unidade_medida(sizeemulators) + reset_color)
for emulador in ITEMS_EMULATORS_NAME:
    print(red + '|' + reset_color, magenta + ' |____Folder Size' + reset_color, yellow + emulador + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('emulators\\' + emulador))))), format_unidade_medida(getFolderSize('emulators\\' + emulador)) + reset_color)
    for item in os.listdir(currentdir + '\\emulators\\' + emulador):
        try:
            print(red + '|' + reset_color, '', magenta + '|' + reset_color, '   |____Folder Size', yellow + item + reset_color, 'inside', yellow + emulador + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize(currentdir + '\\emulators\\' + emulador + '\\' + item))))), format_unidade_medida(getFolderSize(currentdir + '\\emulators\\' + emulador + '\\' + item)) + reset_color) 
        except:
                    pass
print(red + 'Folder Size' + reset_color, yellow + 'launchers' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('launchers.windows'))))), format_unidade_medida(sizelaunchers) + reset_color)
print(red + 'Folder Size' + reset_color, yellow + 'collections' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('collections'))))), format_unidade_medida(sizecollections) + reset_color)
for system in ITEMS_COLLECTION_NAME:
    print(red + '|' + reset_color, magenta + ' |____Folder Size' + reset_color, yellow + system + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('collections\\' + system))))), format_unidade_medida(getFolderSize('collections\\' + system)) + reset_color)
    for item in os.listdir(currentdir + '\\collections\\' + system):
        try:
            print(red + '|' + reset_color, '', magenta + '|' + reset_color, '   |____Folder Size', yellow + item + reset_color, 'inside', yellow + system + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize(currentdir + '\\collections\\' + system + '\\' + item))))), format_unidade_medida(getFolderSize(currentdir + '\\collections\\' + system + '\\' + item)) + reset_color)
        except:
            pass
print(red + 'Folder Size' + reset_color, yellow + 'layouts' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('layouts'))))), format_unidade_medida(sizelayouts) + reset_color)
for layout in ITEMS_LAYOUTS_NAME:
    print(red + '|' + reset_color, magenta + ' |____Folder Size' + reset_color, yellow + layout + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize(currentdir + '\\layouts\\' + layout))))), format_unidade_medida(getFolderSize(currentdir + '\\layouts\\' + layout)) + reset_color)
    if os.path.exists(currentdir + '\\layouts\\' + layout + '\\collections'):
        for item in os.listdir(currentdir + '\\layouts\\' + layout + '\\collections'):
            try:
                print(red + '|' + reset_color, '', magenta + '|' + reset_color, '   |____Folder Size', yellow + item + reset_color, 'inside', yellow + layout + '\\collections' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize(currentdir + '\\layouts\\' + layout + '\\collections' + '\\' + item))))), format_unidade_medida(getFolderSize(currentdir + '\\layouts\\' + layout + '\\collections\\' + item)) + reset_color)
            except:
                pass
print(red + 'Folder Size' + reset_color, yellow + 'meta' + reset_color, 'is', green + '%.2f' % float(format_unidade_size(int(str(getFolderSize('meta'))))), format_unidade_medida(sizemeta) + reset_color)
print(cyan + '____________________________________' + reset_color)
print('Total Folder Size ', 'is', green + '%.2f'%sizetotal, format_unidade_medida(sizetotal) + reset_color)
print()
