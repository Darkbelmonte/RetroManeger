# menu para escolher todas as opções dos scripts de gerenciamento do RetroFe (RenomearSystem.py, ClearSystem.py, DirSystem.py, MakeSettingsRocketLauncher.py e MakeStructureDefault.py)
# Autor: Misael Oliveira
# Data: 04/05/2021
# Versão: 1.0
# Licença: GNU General Public License v3.0

# Importação de bibliotecas
import os
import sys
import shutil
import fileinput
import numpy as np
import pandas as pd  # para ler, visualizar e printar infos do df
from io import StringIO
from shutil import move
from datetime import date
from tkinter.tix import TEXT
from datetime import datetime
import xml.etree.ElementTree as ET

# _________  DEFINIR CONFIGURAÇÕES INICIAIS________ #
# limpar terminal antes de executar 
print("\n" * os.get_terminal_size().lines)
#   Formatação de cores para o Print no terminal 
reset_color = '\033[0m'
red = '\033[1;31;40m'
green = '\033[1;32;40m'
yellow = '\033[1;33;40m'
blue = '\033[1;34;40m'
magenta = '\033[1;35;40m'
cyan = '\033[1;36;40m'
#   Exibir mensagem de boas vindas! E exibir opções para o usuário escolher
print(f'{magenta}')
print(green + 'Olá, seja bem-vindo ao' + reset_color + yellow + ' RetroFe Menager!' + reset_color)
print(green + 'Este é um copilado de scripts para facilitar atividades de rotina no' + reset_color  + red + ' RefroFE' + reset_color)
print(yellow + 'Autor : Misael Oliveira ' + reset_color + ' (misael.junio.oliveira@gmail.com)')
print(yellow + 'Versão :' + reset_color + ' 1.0')
print(yellow + 'Disponivel' + reset_color + ' em https://github.com/Darkbelmonte/RetroManeger ')
print(yellow + 'Licença :' + reset_color + ' GNU General Public License v3.0\n')
# ---------------------------------------------------------#
# INFORMAÇÕES INICIAIS DO ESCRIPT EXECUTADO
print(cyan + '*---      INFO SCRIPT :   ', os.path.basename(__file__).split('.')[0].upper(), '     ----------------------------*' + reset_color)
print(magenta + '|      Sistema Operacional :' + reset_color, cyan + os.name.upper() + reset_color)
#cmd = 'date'
#print('Em que século você esta :', os.system(date))
print(magenta + '|      Sript excutado :     ' + reset_color, yellow +  os.path.basename(__file__) + reset_color)
print(magenta + '|      Localização :        ' + reset_color,  yellow +  (__file__) + reset_color)
print(cyan + '*-----------------------------------------------------------------*' + reset_color)
# -----------------------------------------------------------------#
# ----------------- DEFINIÇÃO DO DIRETÓRIO ROOT ------------------ #
# Localização do diretório ROOT
if os.path.exists("\\".join(((os.path.realpath(__file__)).split('\\', 7)[0:-1])) + '\\core'):
    ROOT = "\\".join(((os.path.realpath(__file__)).split('\\', 7)[0:-1]))
if os.path.exists("\\".join(((os.path.realpath(__file__)).split('\\', 6)[0:-1])) + '\\core'):
    ROOT = "\\".join(((os.path.realpath(__file__)).split('\\', 6)[0:-1]))
if os.path.exists("\\".join(((os.path.realpath(__file__)).split('\\', 5)[0:-1])) + '\\core'):
    ROOT = "\\".join(((os.path.realpath(__file__)).split('\\', 5)[0:-1]))
if os.path.exists("\\".join(((os.path.realpath(__file__)).split('\\', 4)[0:-1])) + '\\core'):
    ROOT = "\\".join(((os.path.realpath(__file__)).split('\\', 4)[0:-1]))
if os.path.exists("\\".join(((os.path.realpath(__file__)).split('\\', 3)[0:-1])) + '\\core'):
    ROOT = "\\".join(((os.path.realpath(__file__)).split('\\', 3)[0:-1]))
if os.path.exists("\\".join(((os.path.realpath(__file__)).split('\\', 2)[0:-1])) + '\\core'):
    ROOT = "\\".join(((os.path.realpath(__file__)).split('\\', 2)[0:-1]))
elif str(os.path.exists(os.path.realpath(__file__))) + '\\core':
    ROOT = os.path.dirname(os.path.abspath(__file__))
else:
    print(u'Diretório ROOT não encontrado!')
    exit()
# -----------------------------------------------------------------#
# -----------------          CAMINHOS           ------------------ #
# -----------------   DEFINIR LOCAIS DE ACESSO  ------------------ #
DATA_MANEGER_DATA = ROOT + '\\core\\maneger\\' + 'Data\\'
FILE_CSV_FIX_NAME_SYSTEM = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem.csv'
FILE_CSV_FIX_NAME_SYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem_Tmp.csv'
FILE_CSV_FIX_NAME_CLEAN = ROOT + '\\core\\maneger\\Data\\Fix_Clean.csv'
FILE_CSV_FIX_NAME_CLEAN_TMP = ROOT + '\\core\\maneger\\Data\\Fix_Clean_Tmp.csv'
FILE_CSV_DIRSYSTEM = ROOT + '\\core\\maneger\\Data\\DirSystem.csv'
FILE_CSV_DIRSYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\DirSystem_Tmp.csv'
FILE_CSV_SETTINGS = ROOT + '\\core\\maneger\\Data\\Settings_template.csv'
FILE_CSV_SETTINGS_TMP = ROOT + '\\core\\maneger\\Data\\Settings_template_Tmp.csv'
MODULE_DIR_SYSTEM = 'core\\maneger\\Lib\\'
MODULE_DIR_SYSTEM_NAME = 'DirSystem.py'
MODULE_DIR_RENAME_SYSTEM_MANUAL = ROOT + '\\meta\\rename\\'
DATA_ATUAL = date.today()
DATA_HORA_ATUAIS = datetime.now()
DATA_HORA_ATUAIS_FORMATADO = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H-%M')
DATA_HORA_ATUAIS_FORMATADO_HORA = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H') + 'h'
BEFORE_DIR = ((os.path.dirname(os.path.realpath(__file__))).split('\\', -1)[-2]) + '\\'
BACKUP_DIR = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup'
BACKUP_DIR_ROM = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup' + '\\Roms'
INSTALLED_SYSTEMS = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\') if not f in ['Main','_common']]
INSTALLED_SYSTEMS_DIR = list(set([os.path.join(ROOT + '\\collections\\', file) for file in INSTALLED_SYSTEMS if os.path.isdir(ROOT + '\\collections\\' + file)]))
ITEMS_COLLECTION_DIR_LEVEL0_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.txt')]))
ITEMS_COLLECTION_DIR_LEVEL0_FILE_CONF = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.conf')]))
ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('settings.conf')]))
ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 = list(set([(file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_COLLECTION_DIR__SYSTEM_LEVEL1 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_COLLECTION_NAME_MAIN_ARTWORK = [f for f in os.listdir(ROOT + '\\collections\\Main\\medium_artwork') if os.path.exists(ROOT + '\\collections\\Main\\medium_artwork\\') if os.path.isdir(ROOT + '\\collections\\Main\\medium_artwork\\')]
ITEMS_COLLECTION_DIR_MAIN_ARTWORK_CONTENT = list(set([(ROOT + '\\collections\\Main\\medium_artwork\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME_MAIN_ARTWORK if os.path.exists(ROOT + '\\collections\\Main\\medium_artwork\\' + file) for file2 in os.listdir(ROOT + '\\collections\\Main\\medium_artwork\\' + file) if os.path.isfile(ROOT + '\\collections\\Main\\medium_artwork\\' + file + '\\' + file2)]))        
#ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 = list(set([(file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3)]))
#ITEMS_COLLECTION_DIR__SYSTEM_LEVEL2 = list(set([(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3)]))
#ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2_FILE = list(set([(file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4)]))
#ITEMS_COLLECTION_DIR__SYSTEM_LEVEL2_FILE = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4)]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.txt')]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_PNG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_MP4 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp4')]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_MP3 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp3')]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_OGG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ogg')]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_AVI = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.avi')]))
#ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_ICO = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ico')]))
ITEMS_EMULATORS_NAME = list(set([f for f in os.listdir(ROOT + '\\emulators\\') if os.path.exists(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\')]))
ITEMS_EMULATORS_DIR_NAME = list(set([os.path.join(ROOT + '\\emulators\\', file) for file in os.listdir(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\' + file)]))
ITEMS_EMULATORS_DIR_LEVEL1 = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if os.path.isdir(ROOT + '\\emulators\\' + file + '\\' + file2)]))
ITEMS_EMULATORS_DIR_LEVEL0_FILE_INI = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.ini')]))
ITEMS_EMULATORS_DIR_LEVEL0_FILE_CFG = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.cfg')]))
ITEMS_EMULATORS_DIR_LEVEL0_FILE_LPL = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.lpl')]))
ITEMS_EMULATORS_DIR_LEVEL0_FILE_EXE = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.exe')]))
ITEMS_EMULATORS_DIR_LEVEL0_FILE_CFG = list(set([os.path.join(ROOT + '\\launchers.windows\\' + file + '\\' + file2) for file in os.listdir(ROOT + '\\launchers.windows\\') if os.path.isdir(ROOT + '\\launchers\\' + file) for file2 in os.listdir(ROOT + '\\launchers\\' + file) if file2.endswith('.conf')]))
ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
ITEMS_LAYOUTS_DIR_COLLECTION = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))
ITEMS_LAYOUTS_LEVEL0_FILE_XML = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\', file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file) for file2 in os.listdir(ROOT + '\\layouts\\' + file) if file2.endswith('.xml')]))
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL0 = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))
ITEMS_LAYOUTS_NAME_COLLECTION_LEVEL1 = list(set([os.path.join(file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)]))
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL1 = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\', file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if not os.path.isfile(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_LAYOUTS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3)]))
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS_FILE_XML = list(set([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.xml')]))
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS_FILE_PNG = list(set([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.png')]))
ITEMS_META_NAME = [f for f in os.listdir(ROOT + '\\meta\\') if os.path.exists(ROOT + '\\meta\\') if os.path.isdir(ROOT + '\\meta\\')]
ITEMS_META_DIR_NAME = list(set([os.path.join(ROOT + '\\meta\\', file) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file)]))
ITEMS_META_FILE_XML = list(set([os.path.join(ROOT + '\\meta\\' + file + '\\', file2) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file) for file2 in os.listdir(ROOT + '\\meta\\' + file) if file2.endswith('.xml')]))
ITEMS_ROCKETLAUNCHER_NAME = list(set([file for file in os.listdir(ROOT + '\\RocketLauncher') if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
ITEMS_ROCKETLAUNCHER_DIR_NAME = list(set([os.path.join(ROOT + '\\RocketLauncher\\', file) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.exists(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
ITEMS_ROCKETLAUNCHER_DIR_LEVEL1 = list(set([os.path.join(ROOT + '\\RocketLauncher\\' + file, file2) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2)]))
ITEMS_ROCKETLAUNCHER_SETTINGS_SYSTEM = [f for f in os.listdir(ROOT + '\\RocketLauncher\\Settings') if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + f) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + f)]
ITEMS_ROCKETLAUNCHER_DIR__LEVEL0_SETTINGS = list(set([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_SYSTEM if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file)]))
ITEMS_ROCKETLAUNCHER_FILE_LEVEL0_SETTINGS_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_SYSTEM if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Settings\\' + file) if file2.endswith('.ini')])) 
INF_ROCKETLAUNCHER_SETTINGS_INI = ROOT + '\\RocketLauncher\\RocketLauncherUI\\Settings\\Frontends.ini'
INF_MENU = ROOT + '\\collections\\Main\\' + 'menu.txt'
INF_MENU_FOLDER = ROOT + '\\collections\\Main\\menu' 
DIR_ROCKETLAUNCHERGUI = ROOT + '\\RocketLauncher\\RocketLauncherUI\\'
ROMS_NAME_REAL_LIST = []
EMPTY = []
# --------- DEFINIÇÃO DAS LISTAS DOS OUTROS DIRETÓRIOS ------------ #
print(blue + '| Definindo os diretórios...        ' + reset_color)
print(blue + '| Diretório ROOT :                  ' + reset_color, yellow + ROOT + reset_color)
print(blue + '| Diretório DATA_MANEGER_DATA :     ' + reset_color, yellow + DATA_MANEGER_DATA + reset_color)
print(blue + '| Sistemas instalados localizados:  ' + reset_color, yellow + str(len(INSTALLED_SYSTEMS)) , 'Systems in collections folder' + reset_color)
print(blue + '| Emuladores instalados localizados:' + reset_color, yellow + str(len(ITEMS_EMULATORS_NAME)) , 'Emulador in emulators folder' + reset_color)
print(blue + '| Temas instalados localizados:     ' + reset_color, yellow + str(len(ITEMS_LAYOUTS_NAME)) , 'Temas in layouts folder' + reset_color)
# ! ----------------------------------------------------------------------------------------------------- ! #
# ! -------------------------------!!       LISTA DE FUNÇÕES       !!    -------------------------------- ! #
# ! ----------------------------------------------------------------------------------------------------- ! #
# ----------------- | -----------------        Manipular CSV         ----------------- | ------------------ #
def file_backup(file_a):
    file_temp = str(file_a).replace('.csv', '_Tmp.csv')
    if os.path.isfile(file_temp):
        try:
            os.remove(file_temp)
        except IOError:
            print(u'Arquivo Base CSV não encontrado!', file_temp, '\n','Vamos fazer a partir do original :', file_a)
            #print(FILE_CSV_FIX_NAME_SYSTEM_TMP)
    if not os.path.isfile(file_temp):
        try:
            shutil.copyfile(file_a, file_temp)
        except IOError:
            print(u'Arquivo  Base CSV não encontrado!')
# ----------------- | -----------------  Criação de DataBases Panda  ----------------- | ------------------ #
file_backup(FILE_CSV_FIX_NAME_SYSTEM)
file_backup(FILE_CSV_SETTINGS)
file_backup(FILE_CSV_FIX_NAME_CLEAN)

df = pd.read_csv(FILE_CSV_FIX_NAME_SYSTEM_TMP, encoding='utf-8', sep=';')
settings_df = pd.read_csv(FILE_CSV_SETTINGS_TMP, encoding='utf-8', sep=';')
clean_df = pd.read_csv(FILE_CSV_FIX_NAME_CLEAN_TMP, encoding='utf-8', sep=';')

df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))
settings_midia_name = settings_df['MIDIA_VARIABLE'].tolist()
dirclean = clean_df['dirclean'].tolist()
limpar = clean_df['clean'].tolist()
emulador = clean_df['emulador'].tolist()
categoria = clean_df['categoria'].tolist()
# ----------------- | -----------------         Renomear Pastas     ----------------- | ------------------ #
def renameDir(caminho):
    for Path in caminho :
        #print(Path, '>>> Path <<<')
        if os.path.exists(str(Path)) and os.path.isdir(Path):
            Dir, Nome = os.path.split(Path)  
            for erroName, offialName in zip(df['wrong_name'], df['official_name']):
                if erroName == Nome != offialName:
                    old_file = os.path.join(Dir, Nome)

                    for indice, elemento in enumerate(df['wrong_name']):
                        if elemento == Nome:
                            for official_indice, official_elemento in enumerate(df['official_name']):
                                if elemento == Nome and indice == official_indice:
                                    old_file = os.path.join(Dir, Nome)
                                    tmp_file = os.path.join(Dir, Nome).replace(elemento, '_~|(Name~tmp)|~_')
                                    new_file = tmp_file.replace('_~|(Name~tmp)|~_', official_elemento)

                                    if old_file != new_file:
                                        try:
                                            os.rename(old_file, new_file)
                                            print(red + f'folder index {indice} ', f'=' + reset_color, blue + f' {old_file} ' + reset_color, red +  f' >> name index = {official_indice}' + reset_color, green + f' | {new_file}' + reset_color)
                                        except:
                                            pass    
                                    if Path !=  old_file != new_file:
                                        print(f'Esta pasta = {Path} não parece ser um sistema valido')
                #elif erroName != Nome != offialName:
                #    print(green +  f'Nenhum trabalho a ser feito aqui...vá jogar! ' + reset_color)
                #    break # break para não fazer nada se não for o nome correto

    for file in caminho :
        if os.path.exists(str(file)) and os.path.isfile(file):
            Dir, Nome = os.path.split(file) 
            fileName, Ext = os.path.splitext(Nome)
            for erroName, offialName in zip(df['wrong_name'], df['official_name']):
                if erroName == fileName != offialName:
                    #print(red + 'O sistema: {erroName} será alterado para' + reset_color, green + '{offialName}' + reset_color)
                    old_file = os.path.join(Dir, fileName + Ext)
                    
                    for indice, elemento in enumerate(df['wrong_name']):
                        if elemento == fileName:
                            for official_indice, official_elemento in enumerate(df['official_name']):
                                if elemento == fileName and indice == official_indice:
                                    old_file = os.path.join(Dir, fileName + Ext)
                                    tmp_file = os.path.join(Dir, fileName + Ext).replace(elemento, '_~|(Name~tmp)|~_')
                                    new_file = tmp_file.replace('_~|(Name~tmp)|~_', official_elemento)

                                    if old_file != new_file:
                                        try:
                                            os.rename(old_file, new_file)
                                            print(red + f'file > old ', f'=' + reset_color, blue + f' {old_file} ' + reset_color, red + f'file > new ' + reset_color,  green + f'{new_file}' + reset_color) 
                                        except:
                                            pass    
                                    #if Path !=  old_file != new_file:
                                    #    print(f'Esta pasta = {Path} não parece ser um sistema valido')
                        #elif erroName != fileName != offialName:
                        #    print(green +  f'Nenhum trabalho a ser feito aqui...vá jogar! ' + reset_color)
                        #    break                       

# ----------------- | -----------------         faz backup das pastas     ---------------- | ------------------ #
def make_backup_default(caminhos, observação):
    global file_name
    if type(caminhos) == list:
        for caminho in caminhos:
            dir_file, file_name = os.path.split(caminho) 
            # aqui ele segue se for um arquivo
            if os.path.isfile(str(caminho)) and os.path.exists(str(caminho)):
                # ajustando nomes 
                if str(ROOT + '\\') in str(caminho):
                    dir_tmp, arquivo = os.path.split(caminho) 
                    dir_tmp = dir_tmp.replace(ROOT + '\\', '')
                # criando pasta e removendo arquivo
                    if os.path.exists(str(dir_tmp)):    
                        old_end = str(caminho)
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\' + file_name
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)                                         
                            print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                 
                        pass

                if not str(ROOT + '\\') in str(caminho):
                    dir_tmp, arquivo = os.path.split(caminho)
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho)                    
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\' + file_name
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                  
                        pass
            # aqui ele segue se for uma pasta
            if os.path.isdir(str(caminho)) and os.path.exists(str(caminho)):
                # ajustando nomes 
                if str(ROOT) in caminho:
                    dir_tmp = str(caminho).replace(ROOT + '\\', '')
                    dir_tmp = dir_tmp.split('\\', 0)[-1]
                # criando pasta e removendo arquivo                
                    if os.path.isdir(str(dir_tmp)) and os.path.exists(str(dir_tmp)):    
                        old_end = str(caminho)                          
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + file_name
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                           
                        pass

                if not str(ROOT) in caminho:
                    dir_tmp = str(caminho)
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho) 
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + file_name
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                             
                        pass

            elif not os.path.exists(str(caminho)):
                #print(' O Diretório que você quer mudar em' , caminho,' os arquivos não existe, verifique se há algum erro !!')
                pass
        else:
            pass

    elif type(caminhos) != list:
        # aqui ele segue se for um arquivo
        if os.path.isfile(caminhos) and os.path.exists(caminhos):
            dir_file, file_name = os.path.split(caminhos)
            dir_LEVEL0, LEVEL0_name = os.path.split(dir_file)
            dir_LEVEL1, LEVEL1_name = os.path.split(dir_LEVEL0)
            dir_LEVEL2, LEVEL2_name = os.path.split(dir_LEVEL1) 
            print(red + f'IDENTIFICADO ', f'|' + reset_color, blue + f' {observação} FILE' + reset_color, red + f' Linha - level 0' + reset_color,  green + f'{caminhos}' + reset_color) 
            # ajustando nomes 
            if str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos) 
                dir_tmp = dir_tmp.replace(ROOT + '\\', '')
            # criando pasta e removendo arquivo   
                old_end = str(caminhos)
                #new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
                new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
                try:
                    os.makedirs(new_end)
                    shutil.move(old_end, new_end, copy_function=new_end)
                    print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                except IOError:
                    move(old_end, new_end)
                    print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                                  
                pass

            if not str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos)
                if os.path.exists(str(dir_tmp)):                         
                    old_end = str(caminhos)                    
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\' + file_name
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(old_end, new_end)
                        print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                                   
                    pass
        # aqui ele segue se for uma pasta
        if os.path.isdir(str(caminhos)) and os.path.exists(str(caminhos)):
            # ajustando nomes 
            if str(ROOT + '\\') in str(caminhos):
                dir_tmp = str(caminhos).replace(ROOT + '\\', '')
                dir_tmp = dir_tmp.split('\\', 0)[-1]
            # criando pasta e removendo arquivo                
                if os.path.isdir(str(dir_tmp)) and os.path.exists(str(dir_tmp)):    
                    old_end = str(caminhos)                          
                    #new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\' + file_name
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(old_end, new_end)
                        print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)                                 
                    pass

            if not str(ROOT + '\\') in str(caminhos):
                dir_tmp = str(caminhos).split('\\', 0)[-1]
                dir_file, file_name = os.path.split(caminhos)
                if os.path.exists(str(dir_tmp)):                         
                    old_end = str(caminhos) 
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + file_name
                    try:
                        os.makedirs(new_end)
                        shutil.move(str(old_end), str(new_end), copy_function=str(new_end))
                        print(red + f'ITEM        ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' MOVIDO PARA :' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(str(old_end), str(new_end))
                        print(red + f'ITEM       ', f'>| ' + reset_color, blue + f' {arquivo} ' + reset_color, red + f' FORÇADO MOVIMENTAÇÃO PARA :' + reset_color,  green + f'{new_end}' + reset_color)        
                    pass

        if not os.path.exists(caminhos):
            #print(' O Diretório que você quer mudar :', caminhos ,' os arquivos não existe, verifique se há algum erro !!')
            pass
    else:
        print('Não temos nada para alterar aqui !!')
# ----------------- | -----------------         Renomear Arquivos     ---------------- | ------------------ #
def renameDirRom(caminho, System_Name):
    if os.path.exists(str(caminho)) and os.path.isdir(caminho):
        for file in os.listdir(caminho):
            Dir, Nome = os.path.split(file)  
            fileName, Ext = os.path.splitext(Nome) # Separa o nome do arquivo e a extensão
            SYSTEM_NAME_TMP = MODULE_DIR_RENAME_SYSTEM_MANUAL + 'Fix_' + System_Name + '.csv'
            if os.path.exists(SYSTEM_NAME_TMP):
                System_Name_ROM_df = pd.read_csv(SYSTEM_NAME_TMP, encoding='utf-8', sep=';') # , header=None   
                for erroName, offialName in zip(System_Name_ROM_df['rom_wrong_name'], System_Name_ROM_df['rom_official_name']):
                    if erroName == fileName != offialName:
                        #print(red + f'O sistema: {erroName} será alterado para' + reset_color, green + f'{offialName}' + reset_color)
                        #print(red + f'{erroName}' + reset_color, '-', cyan + f'{fileName}' + reset_color, '-', green + f'{offialName}' + reset_color)
                        old_file = os.path.join(Dir, fileName + Ext)
                        #print(red + f'{caminho}\\{old_file}' + reset_color)
                        for indice_old, elemento in enumerate(System_Name_ROM_df['rom_wrong_name']):
                            #print(elemento, 'elemento')
                            if elemento == fileName:
                                #print(red + f'{elemento}' + reset_color, green + f'{fileName}' + reset_color,)
                                for official_indice, official_elemento in enumerate(System_Name_ROM_df['rom_official_name']):
                                    if elemento == fileName and indice_old == official_indice:
                                        #print(red + f'{elemento}' + reset_color, green + f'{official_elemento}' + reset_color,)
                                        old_file = os.path.join(Dir, fileName + Ext)
                                        tmp_file = os.path.join(Dir, fileName + Ext).replace(elemento, '_~|(Name~tmp)|~_')
                                        new_file = tmp_file.replace('_~|(Name~tmp)|~_', official_elemento)
                                        #print(red + f'O sistema: {old_file} será alterado para' + reset_color, green + f'{new_file}' + reset_color)
                                        if old_file != new_file:
                                            try:
                                                os.rename(f'{caminho}\\{old_file}', f'{caminho}\\{new_file}')
                                                print(red + f'folder index {indice_old} ', f'=' + reset_color, blue + f' {old_file} ' + reset_color, red +  f' >> name index = {official_indice}' + reset_color, green + f' | {caminho}\\{new_file}' + reset_color)
                                            except:
                                                pass    
                        if file !=  old_file != new_file:
                            print(f'Não há em {System_Name} arquivos para ser renomeados de acordo com sua lista .CSV in meta\\rename'.upper())


# ----------------- | -----------------              função de limpar pastas           ---------------- | ------------------ #
def Backup_EmptyFolders():
    for root, dirs, files in os.walk(ROOT): 
        if not len(dirs) and not len(files): 
            EMPTY.append(root) 
    for emptydir in EMPTY:
        emptybackupDir = str(emptydir).replace(ROOT, BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO) 
        try:
            shutil.move(emptydir, emptybackupDir, copy_function=emptybackupDir)
            #print(f'folder {emptydir}  >Fazendo Back_Up de Pasta Vazia> name = {emptybackupDir}')
        except OSError as error:
            print('remover vazia para backup -> ', error)
        pass   
# ----------------- | -----------------         Pegar as informações contidas no Settings     ---------------- | ------------------ #
global LINHA_SETTINGS_LST
RETURN_SETTING = []
def coleta_e_ajusta_Texto_InSettings(NomeDoSystema, texto, tipoArquivo):
    dir_pre_system, nome_system = os.path.split(NomeDoSystema)   # separando nome do systema
    INF_SETTINGS = ROOT + '\\collections\\' + nome_system + '\\' + tipoArquivo
    INF_LAUCHERS = ROOT + '\\launchers.windows\\' + nome_system + tipoArquivo
    #print(NomeDoSystema, '>', tipoArquivo, '>', INF_SETTINGS)
    if os.path.isfile(str(INF_SETTINGS)) == True:
        if tipoArquivo == 'settings.conf':
            arquivo = open(str(INF_SETTINGS), 'r')
            for linha in arquivo:
                if linha == "":
                    LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\roms\\'
                    return LINHA_SETTINGS_LST
                if '#' + texto in linha:
                    LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\roms\\'
                    return LINHA_SETTINGS_LST
                if texto + '= %ITEM_COLLECTION_NAME%' in linha:
                    LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\roms\\'
                    return LINHA_SETTINGS_LST
                if texto + ' = %BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms' in linha:
                    LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\roms\\'
                    return LINHA_SETTINGS_LST
                if texto + '= %BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms' in linha:
                    LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\roms\\'
                    return LINHA_SETTINGS_LST
                if 'list.extensions ' in linha:
                    LINHA_SETTINGS_LST = linha.split('=')[1].replace('\n', '').lstrip() 
                    return LINHA_SETTINGS_LST
                if 'list.extensions' in linha:
                    LINHA_SETTINGS_LST = linha.split('=')[1].replace('\n', '').lstrip()
                    return LINHA_SETTINGS_LST
                if ' list.extensions' in linha:
                    LINHA_SETTINGS_LST = linha.split('=')[1].replace('\n', '').lstrip()
                    return LINHA_SETTINGS_LST
                elif texto in linha :
                    LINHA_SETTINGS_LST = ROOT + '\\' + linha.split('=')[1].replace('\n', '').lstrip()
                    return LINHA_SETTINGS_LST

        if tipoArquivo == 'exclude.txt' or tipoArquivo == 'include.txt' or tipoArquivo == 'menu.txt':
            arquivo = open(str(INF_SETTINGS), 'r')
            LINHA_SETTINGS_TMP = arquivo.readlines()
            LINHA_SETTINGS_TMP = [LINHA_SETTINGS_TMP[i].replace('\n', '') for i in range(len(LINHA_SETTINGS_TMP))]
            LINHA_SETTINGS_LST = LINHA_SETTINGS_TMP[0:-1]

            return LINHA_SETTINGS_LST

# -------------- | ----------        outra forma de ser informações contidas no launchers.windows   --------- | --------------- #
def coleta_e_ajusta_Texto_InLaunchers(NomeDoSystema, texto, tipoArquivo):
    INF_SETTINGS = ROOT + '\\collections\\' + NomeDoSystema + '\\' + tipoArquivo
    INF_LAUCHERS = ROOT + '\\launchers.windows\\' + NomeDoSystema + tipoArquivo
    if os.path.isfile(str(INF_LAUCHERS)) == True:
        if tipoArquivo == '.conf':
            arquivo = open(str(INF_LAUCHERS), 'r')
            for linha in arquivo:
                if linha == "":
                    LINHA_SETTINGS_LST = ROOT + '\\emulators\\'
                    return LINHA_SETTINGS_LST
                elif texto in linha :
                    LINHA_SETTINGS_LST = ROOT + '\\' + linha.split('=')[1].replace('\n', '').lstrip()
                    
            return LINHA_SETTINGS_LST
# -------------- | ----------        pesquisar registro e excluir palavras   --------- | --------------- #
def pesquisar_registro_exlucluir_palavras( AQUIVO, TEXTO ):
    with open(AQUIVO,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if TEXTO not in line:
                f.write(line)
        f.truncate()
# ----------------- | -----------------         alterar informações no texto de arquivos     ---------------- | ------------------ #
def replacement_in_text(file, previousw, nextw):
    for line in fileinput.input(file, inplace=1):
        line = line.replace(previousw, nextw + '\n')
        sys.stdout.write(line)
# ----------------- | -----------------         Pegar as informações contidas no Settings     ---------------- | ------------------ #
def get_dir_settings(SYSTEM_NAME,TEXT_SEARCHED, TYPE_FILE_TXT):
    global RETURN_LINE  
    RETURN_LINE = []  
    if type(SYSTEM_NAME) == list:
        for System_Name in SYSTEM_NAME:
            if type(TEXT_SEARCHED) == list:
                for Search_Texto in TEXT_SEARCHED:        
                    if TYPE_FILE_TXT == 'settings.conf':     
                        SETTINGS_FILE = os.path.join(ROOT, 'collections', System_Name, TYPE_FILE_TXT)
                        if os.path.exists(SETTINGS_FILE):
                            with open(SETTINGS_FILE, 'r') as settings_file:
                                settings_file_lines = settings_file.readlines()
                                for line in settings_file_lines:
                                    if Search_Texto in line:
                                        RETURN_LINE = line.split('=', 1)[1].lstrip()
                                        RETURN_LINE = RETURN_LINE.replace('\n', '').lstrip()
                                        RETURN_LINE = RETURN_LINE.split(',')
                                        if str(ROOT + '\\') in str(RETURN_LINE):
                                            RETURN_LINE = RETURN_LINE
                                            RETURN_LINE.append(RETURN_LINE, '<<<<<< A')
                                        elif not str(ROOT + '\\') in str(RETURN_LINE):
                                            RETURN_LINE = [ROOT + '\\' + RETURN_LINE[0]]
                                            if os.path.exists(RETURN_LINE) == True:
                                                RETURN_LINE = RETURN_LINE
                                                list(RETURN_LINE).append(RETURN_LINE)
                                                print(RETURN_LINE, '<<<<<< B')
                            return RETURN_LINE
                    if TYPE_FILE_TXT == 'exclude.txt' or TYPE_FILE_TXT == 'include.txt' or TYPE_FILE_TXT == 'menu.txt':
                        SETTINGS_FILE = os.path.join(ROOT, 'collections', System_Name, TYPE_FILE_TXT)
                        if os.path.exists(SETTINGS_FILE):
                            with open(SETTINGS_FILE, 'r') as arquivo:
                                LINHA_SETTINGS_TMP = arquivo.readlines()
                                LINHA_SETTINGS_TMP[0:-1].append(LINHA_SETTINGS_TMP[-1])
                                LINHA_SETTINGS = [LINHA_SETTINGS_TMP[i].replace('\n', '') for i in range(len(LINHA_SETTINGS_TMP))]
                                if LINHA_SETTINGS == 'None' or LINHA_SETTINGS == 'NoneType': 
                                    LINHA_SETTINGS = []
                                LINHA_SETTINGS = LINHA_SETTINGS
                                LINHA_SETTINGS.append(LINHA_SETTINGS)
                                #print(LINHA_SETTINGS, '<<<<<< C')
                                

                        return LINHA_SETTINGS
    elif type(SYSTEM_NAME) != list:
        SETTINGS_FILE = os.path.join(ROOT, 'collections', SYSTEM_NAME, TYPE_FILE_TXT)
        if TYPE_FILE_TXT == 'settings.conf': 
            if os.path.exists(SETTINGS_FILE):
                SETTINGS_FILE = os.path.join(ROOT, 'collections', SYSTEM_NAME, TYPE_FILE_TXT) 
                #print(SETTINGS_FILE,"SETTINGS_FILE")
                with open(SETTINGS_FILE, 'r') as settings_file:
                    settings_file_lines = settings_file.readlines()
                    for line in settings_file_lines:
                        #print(line, TEXT_SEARCHED,"SETTINGS_FILE")
                        if TEXT_SEARCHED in line:
                            RETURN_LINE = line.split('=', 1)[1].lstrip()
                            RETURN_LINE = RETURN_LINE.replace('\n', '').lstrip()
                            RETURN_LINE = RETURN_LINE.split(',')
                            if str(ROOT + '\\') in str(RETURN_LINE):
                                print('oi eu estou aqui!! line', RETURN_LINE)
                                if os.path.exists(RETURN_LINE) == True:
                                    RETURN_LINE = RETURN_LINE

                            elif not str(ROOT + '\\') in str(RETURN_LINE):
                                RETURN_LINE = ROOT + '\\' + RETURN_LINE[0]   
                                if os.path.exists(RETURN_LINE) == True:
                                    RETURN_LINE = RETURN_LINE
                return RETURN_LINE

        if TYPE_FILE_TXT == 'exclude.txt' or TYPE_FILE_TXT == 'include.txt' or TYPE_FILE_TXT == 'menu.txt':
            if os.path.exists(SETTINGS_FILE):
                SETTINGS_FILE = os.path.join(ROOT, 'collections', SYSTEM_NAME, TYPE_FILE_TXT)
                with open(SETTINGS_FILE, 'r') as arquivo:
                    LINHA_SETTINGS_TMP = arquivo.readlines()
                    LINHA_SETTINGS_TMP[0:-1].append(LINHA_SETTINGS_TMP[-1])
                    LINHA_SETTINGS = [LINHA_SETTINGS_TMP[i].replace('\n', '') for i in range(len(LINHA_SETTINGS_TMP))]
                    if LINHA_SETTINGS == 'None' or LINHA_SETTINGS == 'NoneType': 
                        LINHA_SETTINGS = []
                    LINHA_SETTINGS = LINHA_SETTINGS
                return LINHA_SETTINGS
# ----------------- | -----------------         criar pastas de midia fake arquivos     ---------------- | ------------------ #
def listar_artwork_folders(NomeDoSystema):
    if type(NomeDoSystema) == list:
        for System_Name in NomeDoSystema:
            lts_Edit_media_settings = []
            lts_Real_Midias = []

            if ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS != 'None' or ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS != 'NoneType' or ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS != []: 
                        for dir_settings in ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS:
                            caminho_A, settings_A = os.path.split(dir_settings)
                            caminho_B, sistema_instalado_A = os.path.split(caminho_A)
                            with open(dir_settings, 'r') as settings_file:
                                settings_file_lines = settings_file.readlines()
                                for line in settings_file_lines:
                                    Real_Midias = str(str(line.split('=', 1)[0].lstrip().rsplit()).replace('media.', '').lstrip()).replace('list.', '').lstrip()[0]
                                    lts_Real_Midias.append(Real_Midias[2:-2])

            for media_settings in settings_midia_name:
                Edit_media_settings = str(media_settings).replace('media.', '').lstrip()
                lts_Edit_media_settings.append(Edit_media_settings)

                lts_Edit_media_settings = lts_Edit_media_settings + lts_Real_Midias
                Excluir_media_settings = ['meda.<filetype>','None','<filetype>','list.includeMissingItems','list.extensions','list.menuSort','list.romHierarchy','list.truRIP','launcher','metadata.type']
                
                tmpw = np.array(lts_Edit_media_settings)
                tmpz = np.array(Excluir_media_settings)
                Manter_Midias = list(set(np.setdiff1d(tmpw, tmpz)))
                Manter_Midias = [i for i in Manter_Midias if i]
                
    elif type(NomeDoSystema) != list:                    
        lts_Edit_media_settings = []
        lts_Real_Midias = []
        if ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS != 'None' or ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS != 'NoneType' or ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS != []: 
                        for dir_settings in ITEMS_COLLECTION_DIR_LEVEL0_FILE_SETTINGS:
                            caminho_A, settings_A = os.path.split(dir_settings)
                            caminho_B, sistema_instalado_A = os.path.split(caminho_A)
                            with open(dir_settings, 'r') as settings_file:
                                settings_file_lines = settings_file.readlines()
                                for line in settings_file_lines:
                                    Real_Midias = str(line.split('=', 1)[0].lstrip().rsplit()).replace('media.', '').lstrip()
                                    lts_Real_Midias.append(Real_Midias[2:-2])
                                    #print(Real_Midias[2:-2], 'Real_Midias')

        for media_settings in settings_midia_name:
            Edit_media_settings = media_settings.replace('media.', '').lstrip()
            lts_Edit_media_settings.append(Edit_media_settings)

            lts_Edit_media_settings = lts_Edit_media_settings + lts_Real_Midias
            Excluir_media_settings = ['meda.<filetype>','None','<filetype>','list.includeMissingItems','list.extensions','list.menuSort','list.romHierarchy','list.truRIP','launcher','metadata.type']
                
            tmpw = np.array(lts_Edit_media_settings)
            tmpz = np.array(Excluir_media_settings)
            Manter_Midias = list(set(np.setdiff1d(tmpw, tmpz)))
            Manter_Midias = [i for i in Manter_Midias if i]
                 
    return Manter_Midias  
# ----------------- |   --------- |   pegar o nomes das ROMS contidos no .XML do sistema    --------- |   ------------------ #
global ROMS_XML_LIST
def get_name_rom_xml(SYSTEM_NAME):
    if type(SYSTEM_NAME) == list:
        for System_Name in SYSTEM_NAME:
            systemXML = os.path.join(ROOT + '\\meta\\hyperlist\\', str(System_Name) + '.xml')
            if os.path.exists(systemXML):
                tree = ET.parse(systemXML)
                root = tree.getroot()
                ROMS_XML_LIST = [game.attrib['name'] for game in root.findall("./game")]
                #print(cyan + f'ANALISANDO O XML ', f' DO SISTEMA : ' + reset_color, blue + f' {System_Name} ' + reset_color, cyan + f' VOCÊ POSSUIM EM SUA COLERAÇÃO : ' + reset_color,  green + f'{len(ROMS_XML_LIST)}' + reset_color,  red + f' ROMs' + reset_color)        
            return ROMS_XML_LIST
    if type(SYSTEM_NAME) != list:
        systemXML = os.path.join(ROOT + '\\meta\\hyperlist\\', str(SYSTEM_NAME) + '.xml')
        if os.path.exists(systemXML):
            tree = ET.parse(systemXML)
            root = tree.getroot()
            ROMS_XML_LIST = [game.attrib['name'] for game in root.findall("./game")]
            #print(cyan + f'ANALISANDO O XML ', f' DO SISTEMA : ' + reset_color, blue + f' {SYSTEM_NAME} ' + reset_color, cyan + f' VOCÊ POSSUIM EM SUA COLERAÇÃO : ' + reset_color,  green + f'{len(ROMS_XML_LIST)}' + reset_color,  red + f' ROMs' + reset_color)        
            return ROMS_XML_LIST

# ----------------- |   --------- |   pegar o nomes das ROMS contidos no .XML do sistema    --------- |   ------------------ #
global INFO_GAME_LIST
def get_info_gamelist_xml(SYSTEM_NAME, SEARCH_ATIBUTE):
    if type(SYSTEM_NAME) == list:
        for System_Name in SYSTEM_NAME:
            systemXML = os.path.join(ROOT + '\\collections\\', str(System_Name),'gamelist' + '.xml')
            if os.path.exists(systemXML):
                tree = ET.parse(systemXML)
                root = tree.getroot()
                INFO_GAME_LIST = [game.attrib[SEARCH_ATIBUTE] for game in root.findall("./game")]
                #print(cyan + f'ANALISANDO O XML ', f' DO SISTEMA : ' + reset_color, blue + f' {System_Name} ' + reset_color, cyan + f' VOCÊ POSSUIM EM SUA COLERAÇÃO : ' + reset_color,  green + f'{len(ROMS_XML_LIST)}' + reset_color,  red + f' ROMs' + reset_color)        
            return INFO_GAME_LIST
    if type(SYSTEM_NAME) != list:
        systemXML = os.path.join(ROOT + '\\meta\\hyperlist\\', str(SYSTEM_NAME) + '.xml')
        if os.path.exists(systemXML):
            tree = ET.parse(systemXML)
            root = tree.getroot()
            INFO_GAME_LIST = [game.attrib['name'] for game in root.findall("./game")]
            #print(cyan + f'ANALISANDO O XML ', f' DO SISTEMA : ' + reset_color, blue + f' {SYSTEM_NAME} ' + reset_color, cyan + f' VOCÊ POSSUIM EM SUA COLERAÇÃO : ' + reset_color,  green + f'{len(ROMS_XML_LIST)}' + reset_color,  red + f' ROMs' + reset_color)        
            return INFO_GAME_LIST

# ----------------- |      criar arquivo de .log para as movimentações requisitadas      | ------------------ #
def criar_log_auditoria(SYSTEM_NAME, TEXT_SEARCHED, LIST_DIR_REMOVE_FILES, MISSING_FILES):    
    # GRAVAR LOG DE REMOÇÃO
    INF_CRITERIO = (str(TEXT_SEARCHED).replace('media.', '')).replace('list.path', 'ROMS').lstrip()
    if not os.path.exists(ROOT + '\\meta\\audit'):
        os.makedirs(ROOT + '\\meta\\audit')
    
    INF_AUDITORIA = ROOT + '\\meta\\audit\\' + SYSTEM_NAME + ' Removido ' + DATA_HORA_ATUAIS_FORMATADO + '_audit.log'
    with open(INF_AUDITORIA, 'a') as meuArquivo:
        meuArquivo.write(str(LIST_DIR_REMOVE_FILES) + '\n')
        meuArquivo.close()

    INF_AUDITORIA_MISSING = ROOT + '\\meta\\audit\\' + SYSTEM_NAME + ' Missing ' + str(INF_CRITERIO) + ' ' + DATA_HORA_ATUAIS_FORMATADO + '_audit.log'
    with open(INF_AUDITORIA_MISSING, 'a') as meuArquivo:
        meuArquivo.write(str(MISSING_FILES) + '\n')
        meuArquivo.close()
# ----------------- |      criar lista de nomes de arquivos diferentes dos nomes contidos no .XML do sistema      | ------------------ #
def Remove_Files_System_Unofficial(SYSTEM_NAME, TEXT_SEARCHED):
    global RETURN_FUNCTION_UNOFFICIAL
    RETURN_FUNCTION_UNOFFICIAL = []
    #ROM_DIR = (get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, 'settings.conf'))
    #DEFAULT_DIR = (Ajuste_Texto_InSettings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf'))
    #DEFAULT_DIR = (get_dir_settings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf'))
    if os.path.exists(str(get_dir_settings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf'))) and (str(get_dir_settings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf')) != 'None' or str(get_dir_settings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf')) != 'NoneType' or str(get_dir_settings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf')) != []):
        DEFAULT_DIR = (str(get_dir_settings(SYSTEM_NAME, TEXT_SEARCHED, 'settings.conf')))
        #print(DEFAULT_DIR, 'DEFAULT_DIR')
        REAL_FILES = [os.path.splitext(f)[0] for f in os.listdir(str(DEFAULT_DIR)) if os.path.isfile(os.path.join(str(DEFAULT_DIR), f))]
        REAL_EXT_FILES = list(set([os.path.splitext(f)[1] for f in os.listdir(str(DEFAULT_DIR)) if os.path.isfile(os.path.join(str(DEFAULT_DIR), f))]))
        REAL_EXT = set([x for x in REAL_EXT_FILES if x != ''])
        EXCLUIR_TXT_LIST = (get_dir_settings(SYSTEM_NAME,'', 'exclude.txt')) if (get_dir_settings(SYSTEM_NAME,'', 'exclude.txt')) != None else [] 
        INCLUDE_TXT_LIST = (get_dir_settings(SYSTEM_NAME,'', 'include.txt')) if (get_dir_settings(SYSTEM_NAME,'', 'include.txt')) != None else [] 
        ROMS_XML_LIST = get_name_rom_xml(SYSTEM_NAME) if get_name_rom_xml(SYSTEM_NAME) != None else [] 
        DEFAULT_LIST = ['default','EstaESomenteUmaListaFake']
        TOTAL_ROMS_VALIDAS = ROMS_XML_LIST + EXCLUIR_TXT_LIST + INCLUDE_TXT_LIST + DEFAULT_LIST

        tmpw = np.array(REAL_FILES)
        tmpz = np.array(TOTAL_ROMS_VALIDAS)
        REMOVE_FILES = list(set(np.setdiff1d(tmpw, tmpz)))
        REMOVE_FILES = [i for i in REMOVE_FILES if i]
        #print(SYSTEM_NAME, 'SYSTEM_NAME :', REMOVE_FILES, 'REMOVE_FILES')

        tmpx = np.array(TOTAL_ROMS_VALIDAS)
        tmpy = np.array(REAL_FILES)
        MISSING_FILES = list(set(np.setdiff1d(tmpx, tmpy))) 
        MISSING_FILES = [w for w in MISSING_FILES if w]

        if TEXT_SEARCHED == 'list.path':
            print(cyan + f'ANALISANDO O XML ', f' DO SISTEMA : '.upper() + reset_color, blue + f' {SYSTEM_NAME} '.upper() + reset_color, cyan + f' VOCÊ POSSUIM EM SUA COLERAÇÃO : '.upper() + reset_color,  green + f'{len(ROMS_XML_LIST)}' + reset_color,  red + f' ROMs'.upper() + reset_color) 
            print(cyan + f'LOCALIZAMOS '.upper() + reset_color, blue + f' {len(REAL_FILES)} '.upper() + reset_color, cyan + f' SUA COLERAÇÃO! DE ACORDO COM O XML FALTAM '.upper() + reset_color,  green + f'{len(ROMS_XML_LIST) - len(REAL_FILES)}' + reset_color,  red + f'{TEXT_SEARCHED}'.upper() + reset_color) 
        
        for EXT in REAL_EXT:
            for REMOVE in REMOVE_FILES:
                DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
                #print(DIR_REMOVE_FILES, 'DIR_REMOVE_FILES')
                if os.path.exists(DIR_REMOVE_FILES) and os.path.isfile(DIR_REMOVE_FILES) == True:
                    DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
                    RETURN_FUNCTION_UNOFFICIAL.append(DIR_REMOVE_FILES)
                    RETURN_FUNCTION_UNOFFICIAL = list(set(RETURN_FUNCTION_UNOFFICIAL))
                    #print(RETURN_FUNCTION_UNOFFICIAL, 'RETURN_FUNCTION_UNOFFICIAL')

                    #print(RETURN_FUNCTION_UNOFFICIAL, 'RETURN_FUNCTION_UNOFFICIAL <<<<')
                    

        #return RETURN_FUNCTION_UNOFFICIAL, REAL_FILES, REAL_EXT_FILES, EXCLUIR_TXT_LIST, INCLUDE_TXT_LIST, ROMS_XML_LIST, MISSING_FILES
        return RETURN_FUNCTION_UNOFFICIAL
# ----------------- |      criar lista de nomes de arquivos diferentes dos nomes contidos no .CSV do sistema      | ------------------ #
def Make_remove_System_Name_Unofficial(list_Dir_System_Name):
    global RETURN_FUNCTION_NAME_UNOFFICIAL
    RETURN_FUNCTION_NAME_UNOFFICIAL = []
    if os.path.exists(str(list_Dir_System_Name)) and (str(list_Dir_System_Name) != 'None' or str(list_Dir_System_Name) != 'NoneType' or str(list_Dir_System_Name) != []):
        DEFAULT_DIR = list_Dir_System_Name
        REAL_FILES = [os.path.splitext(f)[0] for f in os.listdir(str(list_Dir_System_Name)) if os.path.isfile(os.path.join(str(list_Dir_System_Name), f))]
        REAL_EXT_FILES = list(set([os.path.splitext(f)[1] for f in os.listdir(str(list_Dir_System_Name)) if os.path.isfile(os.path.join(str(list_Dir_System_Name), f))]))
        REAL_EXT = set([x for x in REAL_EXT_FILES if x != ''])
        EXCLUIR_TXT_LIST = systemName
        DEFAULT_LIST = ['_common','Main','default','layouts','info','exclude','include','medium_artwork','system_artwork','roms']
        TOTAL_SYSTEM_VALIDAS = EXCLUIR_TXT_LIST + DEFAULT_LIST

        print(DEFAULT_DIR, 'DEFAULT_DIR')
        print(REAL_FILES, 'REAL_FILES')
        print(REAL_EXT_FILES, 'REAL_EXT_FILES')
        print(REAL_EXT, 'REAL_EXT')
        print(EXCLUIR_TXT_LIST, 'EXCLUIR_TXT_LIST')
        print(DEFAULT_LIST, 'DEFAULT_LIST')
        print(TOTAL_SYSTEM_VALIDAS, 'TOTAL_SYSTEM_VALIDAS')




        tmpw = np.array(REAL_FILES)
        tmpz = np.array(TOTAL_SYSTEM_VALIDAS)
        REMOVE_FILES = list(set(np.setdiff1d(tmpw, tmpz)))
        REMOVE_FILES = [i for i in REMOVE_FILES if i]

        print(REMOVE_FILES, 'REMOVE_FILES')

        tmpx = np.array(TOTAL_SYSTEM_VALIDAS)
        tmpy = np.array(REAL_FILES)
        MISSING_FILES = list(set(np.setdiff1d(tmpx, tmpy))) 
        MISSING_FILES = [w for w in MISSING_FILES if w]

        for EXT in REAL_EXT:
            for REMOVE in REMOVE_FILES:
                DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
                if os.path.exists(DIR_REMOVE_FILES) and os.path.isfile(DIR_REMOVE_FILES) == True:
                    DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
                    RETURN_FUNCTION_NAME_UNOFFICIAL.append(DIR_REMOVE_FILES)
                    RETURN_FUNCTION_NAME_UNOFFICIAL = list(set(RETURN_FUNCTION_NAME_UNOFFICIAL))

        return RETURN_FUNCTION_NAME_UNOFFICIAL


# ----------------- |      Construir configurações especificas para os emuladores      | ------------------ #
def localizar_emulador(NomeSystema):
    if NomeSystema == 'Microsoft Xbox 360':
        EmuladorName = 'Xenia'
        EmuladorExe = 'xenia.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        Skipchecks= 'false'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension, Skipchecks]
    if NomeSystema == 'Microsoft Xbox':
        EmuladorName = 'Xemu'
        EmuladorExe = 'xemu.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''        
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Nintendo 3DS':
        EmuladorName = 'Citra'
        EmuladorExe = 'citra.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''        
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Nintendo GameCube':
        EmuladorName = 'dolphin'
        EmuladorExe = 'Dolphin.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Nintendo WiiWare':
        EmuladorName = 'dolphin'
        EmuladorExe = 'Dolphin.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = '{Shift <+ F1 down}'
        Emu_Load_State = '{F1 down}'
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''        
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Nintendo Wii':
        EmuladorName = 'Dolphin'
        CAPTURAR_EXE = [exe for exe in os.listdir(ROOT + '\\emulators\\' + NomeSystema) if os.path.exists(ROOT + '\\emulators\\' + NomeSystema) if os.path.isdir(ROOT + '\\emulators\\' + NomeSystema) if exe.endswith('.exe')]
        EmuladorExe = CAPTURAR_EXE[0]
        EmuPathName = 'Nintendo Wii'
        Emu_Save_State = '{Shift <+ F1 down}'
        Emu_Load_State = '{F1 down}'
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Nintendo Switch':
        EmuladorName = 'Cemu'
        EmuladorExe = 'Cemu.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Sony PlayStation Vita':
        EmuladorName = 'Vita3K'
        EmuladorExe = 'Vita3K.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Sony PlayStation Portable':
        EmuladorName = 'PPSSPP'
        EmuladorExe = 'PPSSPPWindows64.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Sony PlayStation':
        EmuladorName = 'DuckStation'
        EmuladorExe = 'duckstation-nogui-x64-ReleaseLTCG.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = '{F2 down}'
        Emu_Load_State = '{F1 down}'
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Sony PlayStation 2':
        EmuladorName = 'PCSX2'
        CAPTURAR_EXE = [exe for exe in os.listdir(ROOT + '\\emulators\\' + NomeSystema) if os.path.exists(ROOT + '\\emulators\\' + NomeSystema) if os.path.isdir(ROOT + '\\emulators\\' + NomeSystema) if exe.endswith('.exe')]
        EmuladorExe = CAPTURAR_EXE[0]
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Sony PlayStation 3':
        EmuladorName = 'RPCS3'
        EmuladorExe = 'rpcs3.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    if NomeSystema == 'Nintendo Switch':
        EmuladorName = 'Yuzu'
        EmuladorExe = 'yuzu.exe'
        EmuPathName = NomeSystema
        Emu_Save_State = ''
        Emu_Load_State = ''
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
    else:
        EmuladorName = 'RetroArch'
        EmuPathName = 'RetroArch'
        EmuladorExe = 'retroarch.exe'
        Emu_Save_State = '{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}'
        Emu_Load_State = '{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}'
        Emu_Save_State_Path = ''
        Emu_bios_Path = ''
        Emu_config_File = ''
        Emu_cheats_Folder = ''
        Emu_Bezel_Folder = ''
        Emu_Art_Folder = ''
        Emu_controllerProfiles_Folder = ''
        EmuladorNameAlt = ''
        Rom_Match_Extension = 'true'
        return [EmuladorName, EmuPathName, Emu_Save_State, Emu_Load_State, EmuladorExe, Emu_Save_State_Path, Emu_bios_Path, Emu_config_File, Emu_cheats_Folder, Emu_Bezel_Folder, Emu_Art_Folder, Emu_controllerProfiles_Folder, EmuladorNameAlt, Rom_Match_Extension]
# _________    FAZER PASTAS E CONFIGURAÇÕES NO SETTINGS    ____________ #
def Make_folder_Settings_RocketLauncher(nameSystem):

    DirNameSystem = os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + nameSystem)
    if not os.path.exists(DirNameSystem) and os.path.exists(ROOT + '\\collections\\' + nameSystem + '\\' + 'settings.conf') and nameSystem != 'Main':
        os.makedirs(DirNameSystem)
    return DirNameSystem

# _________    FAZER PASTAS E CONFIGURAÇÕES NO SETTINGS    ____________ #
def make_dir_settings_RocketLauncher():
    RomPathtmp = []
    listRomexclude = []
    for NomeSystema in INSTALLED_SYSTEMS: 

        INF_EMU_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Emulators.ini'
        INF_BEZEL_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Bezel.ini'
        INF_GOPTIONS_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Game Options.ini'
        INF_GAME_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Games.ini'
        INF_PAUSE_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Pause.ini'
        INF_PLUGUINS_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Plugins.ini' 
        INF_ROCKETLAUNCHER_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'RocketLauncher.ini'

        Make_folder_Settings_RocketLauncher(NomeSystema)

        RomPathlist= coleta_e_ajusta_Texto_InSettings(NomeSystema, 'list.path', 'settings.conf')
        #print(RomPathlist, '>', NomeSystema, '>', 'list.path', ' jksdhsajdkhasj kjkhd jkhsadjkh a')
        RomExtList = str(coleta_e_ajusta_Texto_InSettings(NomeSystema, 'list.extensions', 'settings.conf')).replace(' ', '|') 
        EmuladorList = os.path.splitext(str(coleta_e_ajusta_Texto_InSettings(NomeSystema, 'executable', '.conf')))[0]

        print(red + EmuladorList + reset_color)
        print(red + localizar_emulador(NomeSystema)[0], '> localizar nome do emulador' + reset_color)
        
        if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema) and not os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Emulators.ini') and not os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'RocketLauncher.ini'):
            # Construção do arquivo Emulators.ini
            meuArquivo = open(str(INF_EMU_INI), 'w')
            meuArquivo.write('[ROMS]'+ '\n')
            meuArquivo.write('Default_Emulator=' + '\n')
            EditRomPathlist = (RomPathlist.replace(ROOT, '..') + '\n')[0:-1]
            #print(EditRomPathlist, '>', NomeSystema, '>', 'EditRomPathlist', ' jksdhsajdkhasj kjkhd jkhsadjkh a')
            #print('Rom_Path=' + (EditRomPathlist.replace('\\', '', 0) ) + '\n')
            meuArquivo.write('Rom_Path=' + (EditRomPathlist.replace('\\', '', 0) ) + '\n')
            meuArquivo.close()
            print('>', NomeSystema, '>', localizar_emulador(NomeSystema)[0], ' EmuladorName ', localizar_emulador(NomeSystema)[1], ' EmuPathName ' + '\n')    
            meuArquivo = open(INF_EMU_INI, 'a') 
            meuArquivo.write('[' + localizar_emulador(NomeSystema)[0] + ']' + '\n')
            EditRomExtList = (RomExtList.replace(',', '|'))
            meuArquivo.write('Rom_Extension=' + EditRomExtList + '\n')
            meuArquivo.write('Emu_Path=..\\emulators\\' + localizar_emulador(NomeSystema)[1] + '\\' + localizar_emulador(NomeSystema)[4] + '\n')
            meuArquivo.write('Module=' + localizar_emulador(NomeSystema)[0] + '.ahk' + '\n')
            meuArquivo.write('Pause_Save_State_Keys= ' + localizar_emulador(NomeSystema)[2] + '\n')
            meuArquivo.write('Pause_Load_State_Keys= ' + localizar_emulador(NomeSystema)[3] + '\n')
            meuArquivo.close()
            if localizar_emulador(NomeSystema)[0] == localizar_emulador(NomeSystema)[0]: 
                buffer = StringIO()
                buffer2 = StringIO()

                with open(str(INF_EMU_INI), 'r+') as stream:
                    for index, line in enumerate(stream):
                        # index == 1 representa a segunda linha do arquivo:
                        buffer.write('Default_Emulator= ' + localizar_emulador(NomeSystema)[0] + '\n' if index == 1 else line)
                with open(str(INF_EMU_INI), 'w') as stream:
                    stream.write(buffer.getvalue())
                    buffer.close()
                
                #with open(str(INF_ROCKETLAUNCHER_INI), 'r+') as stream:
                #    for index, line in enumerate(stream):
                #        # index == 1 representa a segunda linha do arquivo:
                #        buffer2.write('Rom_Match_Extension=true\n' if index == 1 else line)
                #with open(str(INF_ROCKETLAUNCHER_INI), 'w') as stream:
                #    stream.write(buffer2.getvalue())
                #    buffer.close()
            
            # Construção do arquivo Bezel.ini
            meuArquivo = open(str(INF_BEZEL_INI), 'w')
            meuArquivo.write('[Settings]'+ '\n')
            meuArquivo.write('Bezel_Supported_Image_Files=use_global'+ '\n')
            meuArquivo.write('Game_Monitor=use_global'+ '\n')
            meuArquivo.write('Bezel_Delay=use_global'+ '\n')
            meuArquivo.write('[Bezel Change]'+ '\n')
            meuArquivo.write('Bezel_Transition_Duration=use_global'+ '\n')
            meuArquivo.write('Bezel_Save_Selected=use_global'+ '\n')
            meuArquivo.write('Extra_FullScreen_Bezel=use_global'+ '\n')
            meuArquivo.write('[Background]'+ '\n')
            meuArquivo.write('Background_Change_Timer=use_global'+ '\n')
            meuArquivo.write('Background_Transition_Animation=use_global'+ '\n')
            meuArquivo.write('Background_Transition_Duration=use_global'+ '\n')
            meuArquivo.write('Use_Backgrounds=use_global'+ '\n')
            meuArquivo.write('[Bezel Change Keys]'+ '\n')
            meuArquivo.write('Next_Bezel_Key=use_global'+ '\n')
            meuArquivo.write('Previous_Bezel_Key=use_global'+ '\n')
            meuArquivo.write('[Instruction Cards General Settings]'+ '\n')
            meuArquivo.write('IC_Positions=use_global'+ '\n')
            meuArquivo.write('IC_Transition_Animation=use_global'+ '\n')
            meuArquivo.write('IC_Transition_Duration=use_global'+ '\n')
            meuArquivo.write('IC_Enable_Transition_Sound=use_global'+ '\n')
            meuArquivo.write('IC_Scale_Factor=use_global'+ '\n')
            meuArquivo.write('IC_Save_Selected=use_global'+ '\n')
            meuArquivo.write('[Instruction Cards Menu]'+ '\n')
            meuArquivo.write('IC_Left_Menu_Positions=use_global'+ '\n')
            meuArquivo.write('IC_Left_Menu_Number_of_List_Items=use_global'+ '\n')
            meuArquivo.write('IC_Right_Menu_Positions=use_global'+ '\n')
            meuArquivo.write('[Instruction Cards Visibility]'+ '\n')
            meuArquivo.write('IC_Display_Card_on_Startup=use_global'+ '\n')
            meuArquivo.write('IC_Random_Slide_Show_Timer=use_global'+ '\n')
            meuArquivo.write('IC_Toggle_Visibility_Key=use_global'+ '\n')
            meuArquivo.write('[Instruction Cards Keys Change Mode 1]'+ '\n')
            meuArquivo.write('IC_Left_Menu_Key=use_global'+ '\n')
            meuArquivo.write('IC_Right_Menu_Key=use_global'+ '\n')
            meuArquivo.write('[Instruction Cards Keys Change Mode 2]'+ '\n')
            meuArquivo.write('IC_Change_Active_Instruction_Card_Key=use_global'+ '\n')
            meuArquivo.write('IC_Previous_Instruction_Card_Key=use_global'+ '\n')
            meuArquivo.write('IC_Next_Instruction_Card_Key=use_global'+ '\n')
            meuArquivo.write('[Instruction Cards Keys Change Mode 3]'+ '\n')
            meuArquivo.write('IC_1_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_2_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_3_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_4_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_5_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_6_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_7_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_8_Previous_Key=use_global'+ '\n')
            meuArquivo.write('IC_1_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_2_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_3_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_4_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_5_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_6_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_7_Next_Key=use_global'+ '\n')
            meuArquivo.write('IC_8_Next_Key=use_global'+ '\n')
            meuArquivo.close()

    # Construção do arquivo Bezel.ini
            meuArquivo = open(str(INF_BEZEL_INI), 'w')
            meuArquivo.write(''+ '\n')
            meuArquivo.close()
    # Construção do arquivo Game Options.ini
            meuArquivo = open(str(INF_GOPTIONS_INI), 'w')
            meuArquivo.write(''+ '\n')
            meuArquivo.close()
    # Construção do arquivo Games.ini
            meuArquivo = open(str(INF_GAME_INI), 'w')
            meuArquivo.write(''+ '\n')
            meuArquivo.close()
    # Construção do arquivo Pause.ini
            meuArquivo = open(str(INF_PAUSE_INI), 'w')
            meuArquivo.write(''+ '\n')
            meuArquivo.close()
    # Construção do arquivo Plugins.ini
            meuArquivo = open(str(INF_PLUGUINS_INI), 'w')
            meuArquivo.write(''+ '\n')
            meuArquivo.close()
    # Construção do arquivo Plugins.ini
            meuArquivo = open(str(INF_ROCKETLAUNCHER_INI), 'w')
            meuArquivo.write('[Settings]'+ '\n')
            meuArquivo.write('Rom_Match_Extension=true'+ '\n')
            meuArquivo.close()

    # Construção do arquivo RocketLauncherUI.ini
            meuArquivo = open(str(INF_ROCKETLAUNCHER_SETTINGS_INI), 'r+')
            meuArquivo.write('[Settings]'+ '\n')
            meuArquivo.write('Default_Frontend=RetroFE'+ '\n')
            meuArquivo.write('[RocketLauncherUI]'+ '\n')
            meuArquivo.write('Path=.\RocketLauncherUI.exe'+ '\n')
            meuArquivo.write('RLUI_Plugin=Auto'+ '\n')
            meuArquivo.write('RL_Plugin=Default'+ '\n')
            meuArquivo.write('[RetroFE]'+ '\n')
            meuArquivo.write('Path=..\\..\\RetroFE.LNK'+ '\n')
            meuArquivo.write('RLUI_Plugin=RetroFE'+ '\n')
            meuArquivo.write('RL_Plugin=RetroFE'+ '\n')
            meuArquivo.close()

    # -----------------    APLICAÇÃO DAS COFIGURAÇÕES   ------------------ #
    # _________             COLOCAR SISTEMAS NO MENU          ____________ #

            if not os.path.exists(INF_MENU_FOLDER):
                os.makedirs(INF_MENU_FOLDER)
            meuArquivo = open(str(INF_MENU_FOLDER + '\\' + NomeSystema + '.txt'), 'a')
            meuArquivo.write(''+ '\n')
            meuArquivo.close()
            
            if not os.path.exists(INF_MENU_FOLDER):
                os.makedirs(INF_MENU_FOLDER)
            if not os.path.exists(INF_MENU_FOLDER + '\\' + NomeSystema + '.txt'):
                meuArquivo = open(str(INF_MENU_FOLDER + '\\' + NomeSystema + '.txt'), 'w')
                meuArquivo.write(''+ '\n')
                meuArquivo.close()
    
    # -----------------    OTIMIZAÇÃO DO RETROFE   ------------------ #
    # _______ FAZER LISTA INCLUDE.TXT NAS PASTAS DO SISTEMA  ________ #
            # remover arquivo include.txt
            if os.path.exists(ROOT + '\\collections\\' + NomeSystema + '\\' + 'include.txt'):
                try:
                    os.remove(ROOT + '\\collections\\' + NomeSystema + '\\' + 'include.txt')
                except:
                    pass
            
            # criar arquivo include.txt
            if not os.path.exists(str(RomPathlist)):
                # tentar corrigir nome
                RomPathlist = RomPathlist[0:-1]

            if os.path.exists(str(RomPathlist)):
                print(green + RomPathlist[0:-1]  + reset_color, yellow + ' < -- Caminho das ROMS'  + reset_color)
                EditRomExtList2 = EditRomExtList.split('|')
                
                for ext in EditRomExtList2:
                    RomsScamA = [(file.replace('.' + ext,'')) for file in os.listdir(str(RomPathlist)) if file.endswith(ext)]
                    RomsScamB = [(file.replace('.' + ext,'') + '\n') for file in os.listdir(str(RomPathlist)) if file.endswith(ext)]



                    for rom in RomsScamB:                                       
                        meuArquivo = open(str(ROOT + '\\collections\\' + NomeSystema + '\\' + 'include.txt'), 'a')
                        meuArquivo.write(str(rom))
                        meuArquivo.close()
                    # retirar roms da lista de exclusão em exclude.txt
                    if os.path.exists(ROOT + '\\collections\\' + NomeSystema + '\\exclude.txt'):
                        for RomExclude in coleta_e_ajusta_Texto_InSettings(NomeSystema, '','exclude.txt'):
                            pesquisar_registro_exlucluir_palavras(ROOT + '\\collections\\' + NomeSystema + '\\' + 'include.txt', RomExclude)
                print(green + NomeSystema  + reset_color, yellow + ' < -- teve o arquivo include.txt criado para maior ótimização'  + reset_color)

            INF_MENU_FOLDER_FILE = [(os.path.splitext(f)[0])  for f in os.listdir(INF_MENU_FOLDER) if os.path.exists(INF_MENU_FOLDER) if os.path.isdir(INF_MENU_FOLDER) if os.path.isfile(INF_MENU_FOLDER + '\\' + f)]
            #meuArquivo = open(str(INF_MENU), 'w')
            #print(INF_MENU_FOLDER_FILE, 'INF_MENU_FOLDER_FILE')
            #meuArquivo.write(str(INF_MENU_FOLDER_FILE)[1:-1].replace('\n', ' '))
            #meuArquivo.close()

            #with open(str(INF_MENU), 'a') as stream:
            meuArquivo = open(str(INF_MENU), 'w')
            meuArquivo.write(NomeSystema + '\n')
            meuArquivo.close()


            stream = open(str(INF_MENU), 'r+')
            for line in stream:
                for word in INF_MENU_FOLDER_FILE:
                    if word == line.strip():
                        pass
                    else:
                        stream.write(word + '\n')
                        print(red + word + reset_color, cyan + ' < -- verificando sistema no menu'  + reset_color)
                        print(red + word + reset_color, cyan + ' < -- Line do sistema no menu'  + reset_color)
                    #if word in line:
                    
            # adicionar sistema ao menu
                    # a = (line.strip(), '¬', word + '\n\r')
                    # stream.writelines(a)
                    # stream.flush()
                        
                        #break
            stream.close()
# vamos coletar os caminhos das roms no arquivo settings.conf que estão nas pastas ./collections/<nome da coleção>
# Função para coletar os caminhos das roms no arquivo settings.conf que estão nas pastas ./collections/<nome da coleção>
# SOMENTE COLETA DE DADOS
# -----------------------------------------------------------------#

RETURN_SETTING = []
def Info_Texto_InSettings(NomeDoSystema, texto, tipoArquivo):
    dir_pre_system, nome_system = os.path.split(NomeDoSystema)   # separando nome do systema
    INF_SETTINGS = ROOT + '\\collections\\' + nome_system + '\\' + tipoArquivo
    INF_LAUCHERS = ROOT + '\\launchers.windows\\' + nome_system + tipoArquivo
    #print(NomeDoSystema, '>', tipoArquivo, '>', INF_SETTINGS)
    if os.path.isfile(str(INF_SETTINGS)) == True:
        if tipoArquivo == 'settings.conf':
            arquivo = open(str(INF_SETTINGS), 'r')
            for linha in arquivo:
                if texto in linha :
                    LINHA_SETTINGS_LST = linha.split('=')[1].replace('\n', '').lstrip()
                    return LINHA_SETTINGS_LST

        if tipoArquivo == 'exclude.txt' or tipoArquivo == 'include.txt' or tipoArquivo == 'menu.txt':
            arquivo = open(str(INF_SETTINGS), 'r')
            LINHA_SETTINGS_TMP = arquivo.readlines()
            LINHA_SETTINGS_TMP = [LINHA_SETTINGS_TMP[i].replace('\n', '') for i in range(len(LINHA_SETTINGS_TMP))]
            LINHA_SETTINGS_LST = LINHA_SETTINGS_TMP[0:-1]

            return LINHA_SETTINGS_LST

# -------------- | ----------        pesquisar registro e excluir palavras   --------- | --------------- #
def input_Texto_InSettings( AQUIVO, TEXTO ):
    with open(AQUIVO,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if TEXTO not in line:
                f.write(line)
        f.truncate()
# ----------------- | -----------------         alterar informações no texto de arquivos     ---------------- | ------------------ #
def replacement_in_text(file, previousw, nextw):
    # print(file, 'file')
    # print(previousw, 'previousw')
    # print(nextw, 'nextw')
    for line in fileinput.input(file, inplace=1):
        # print(line, 'line_1')
        line = line.replace(previousw, nextw + '\n')
        # print(line, 'line_2')
        sys.stdout.write(line)

# -----------------------------------------------------------------#
# Função para corrigir caminhos com o nome correto do nome_system ./collections/<nome da coleção>
# -----------------------------------------------------------------#
def fix_dir_InSettings():
    for System_Name in INSTALLED_SYSTEMS:
        SETTINGS_FILE = os.path.join(ROOT, 'collections', System_Name, 'settings.conf')
        TEXTO_ORIGINAL = str(Info_Texto_InSettings(System_Name, 'list.path', 'settings.conf'))
        caminho_A, nome_A = os.path.split(TEXTO_ORIGINAL)
        caminho_B, nome_B = os.path.split(caminho_A)
        TEXTO_MODIFICADO = os.path.join("collections", System_Name,"roms")
        
        # corrigir caminhos com o nome correto do nome_system ./collections/<nome da coleção>
        if nome_B != System_Name and nome_B != '':
        #    print(nome_B,'|>-nome_B-<|')
        # Coleta as informações de login do usuário
            print(yellow + f'__________________________________________________________________________________________'.upper() + reset_color)
            print(yellow + f'| Apresentando inconsistencias localizadas'.upper() + reset_color)
            print(yellow + f'| Nome descrito no dir da rom é :'.upper() + reset_color,red + f'{nome_B}'.upper() + reset_color, yellow + f'Porém estamos Avaliando o Sistema :'.upper() + reset_color, green + f'{System_Name}'.upper() + reset_color)
            print(yellow + f'| abaixo teriamos a proposta de correção do caminho ('.upper(), red + f'vermelho'.upper() + reset_color, yellow + f'original e o'.upper() + reset_color , green + f'verde'.upper() + reset_color, yellow + f'é o proposto )'.upper() + reset_color)
            print(yellow + f'|' + reset_color,red + f'{TEXTO_ORIGINAL}' + reset_color, yellow + f' =:> ' + reset_color, green + f'{TEXTO_MODIFICADO}' + reset_color)
            print(yellow + f'|__________________________________________________________________________________________'.upper() + reset_color)
            fix_line = input(yellow + f' Digite Y/N se você deseja corrigir o caminho da ROM, conforme acima: '.upper() + reset_color)
            if fix_line == 'Y':
                replacement_in_text( SETTINGS_FILE, TEXTO_ORIGINAL, TEXTO_MODIFICADO)


                    

# ! ----------------------------------------------------------------------------------------------------- ! #
# ! ---------------------------------!!       BASE DO MENU        !!    --------------------------------- ! #
# ! ----------------------------------------------------------------------------------------------------- ! #
def executar_menu():
    if ACTION_MENU == '1':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Iniciando os procedimentos de renomear os seus sistemas...'.upper() + reset_color)
        renameDir(INSTALLED_SYSTEMS_DIR)
        renameDir(ITEMS_META_FILE_XML)
        renameDir(ITEMS_ROCKETLAUNCHER_DIR__LEVEL0_SETTINGS)

        ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 = list(set([(file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3)]))
        ITEMS_COLLECTION_DIR__SYSTEM_LEVEL2 = list(set([(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3)]))
        ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2_FILE = list(set([(file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4)]))
        ITEMS_COLLECTION_DIR__SYSTEM_LEVEL2_FILE = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4)]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.txt')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_PNG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_MP4 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp4')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_MP3 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp3')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_OGG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ogg')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_AVI = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.avi')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_ICO = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ico')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_JPG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.jpg')]))
        ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_JPG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL1 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME_SYSTEM_LEVEL2 if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.jpg')]))
        
        ITEMS_COLLECTION_NAME_MAIN_ARTWORK = [f for f in os.listdir(ROOT + '\\collections\\Main\\medium_artwork') if os.path.exists(ROOT + '\\collections\\Main\\medium_artwork\\') if os.path.isdir(ROOT + '\\collections\\Main\\medium_artwork\\')]
        ITEMS_COLLECTION_DIR_MAIN_ARTWORK_CONTENT = list(set([(ROOT + '\\collections\\Main\\medium_artwork\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME_MAIN_ARTWORK if os.path.exists(ROOT + '\\collections\\Main\\medium_artwork\\' + file) for file2 in os.listdir(ROOT + '\\collections\\Main\\medium_artwork\\' + file) if os.path.isfile(ROOT + '\\collections\\Main\\medium_artwork\\' + file + '\\' + file2)]))
        ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
        ITEMS_LAYOUTS_DIR_COLLECTION = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))
        ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL0 = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))
        ITEMS_LAYOUTS_NAME_COLLECTION_LEVEL1 = list(set([os.path.join(file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)]))
        ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL1 = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
        ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\', file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
        ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_LAYOUTS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3)]))
        ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS_FILE_XML = list(set([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.xml')]))
        ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS_FILE_PNG = list(set([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.png')]))

        ITEMS_ROCKETLAUNCHER_NAME = list(set([file for file in os.listdir(ROOT + '\\RocketLauncher') if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
        ITEMS_ROCKETLAUNCHER_DIR_NAME = list(set([os.path.join(ROOT + '\\RocketLauncher\\', file) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.exists(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
        ITEMS_ROCKETLAUNCHER_DIR_LEVEL1 = list(set([os.path.join(ROOT + '\\RocketLauncher\\' + file, file2) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2)]))
        ITEMS_ROCKETLAUNCHER_DIR_LEVEL2 = list(set([os.path.join(ROOT + '\\RocketLauncher\\' + file + '\\' + file2, file3) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2)]))
        ITEMS_ROCKETLAUNCHER_SETTINGS_SYSTEM = [f for f in os.listdir(ROOT + '\\RocketLauncher\\Settings') if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + f) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + f)]

        renameDir(ITEMS_COLLECTION_DIR_MAIN_ARTWORK_CONTENT)
        renameDir(ITEMS_COLLECTION_DIR__SYSTEM_LEVEL2)
        renameDir(ITEMS_COLLECTION_DIR__SYSTEM_LEVEL2_FILE)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_TXT)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_PNG)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_MP4)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_MP3)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_OGG)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_AVI)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_ICO)
        renameDir(ITEMS_COLLECTION_DIR_SYSTEM_LEVEL2_FILE_JPG)
        renameDir(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL0)
        renameDir(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL1)
        renameDir(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS)
        renameDir(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_LAYOUTS)
        renameDir(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS_FILE_PNG)
        renameDir(ITEMS_ROCKETLAUNCHER_DIR_LEVEL2)
        

        print(cyan + 'Renomeando concluido!'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '2':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Iniciando os procedimentos de renomear os seus Emuladores...'.upper() + reset_color)
        renameDir(ITEMS_EMULATORS_DIR_NAME)
        renameDir(ITEMS_ROCKETLAUNCHER_DIR__LEVEL0_SETTINGS)
        renameDir(ITEMS_ROCKETLAUNCHER_DIR__LEVEL0_SETTINGS)
        print(cyan + 'Renomeando concluido!'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '3':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Iniciando os procedimentos para movimentar pastas com midias para a pasta padrão artwork...'.upper() + reset_color)
        LTS_DIR_MIDIA = []
        for System_Name in INSTALLED_SYSTEMS:
            RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
            list(set(RETURN_MEDIA_NAME))
            for Search_Texto in RETURN_MEDIA_NAME:
                if Search_Texto != 'list.path' and os.path.exists(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) and os.listdir(str(get_dir_settings(System_Name,Search_Texto, 'settings.conf'))) != []:
                    DIR_MIDIA = str(get_dir_settings(System_Name, Search_Texto, 'settings.conf')) if os.listdir(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) != [] else ''
                    Dir_medium_artwork, Name_medium_artwork = os.path.split(DIR_MIDIA)
                    Dir_collections, Name_Systema = os.path.split(Dir_medium_artwork)
                    fix_dir_InSettings()
                    if Name_medium_artwork != 'roms':
                        if Name_medium_artwork != 'medium_artwork': 
                            if Name_Systema != 'medium_artwork': 
                                old_dir = Dir_medium_artwork + '\\' + Name_medium_artwork
                                files = os.listdir(old_dir)
                                new_dir = os.path.join(Dir_medium_artwork, 'medium_artwork', Name_medium_artwork)
                                if not os.path.exists(new_dir):
                                    mode = 0o666
                                    try:
                                        #os.mkdir(os.path.join(Dir_medium_artwork, 'medium_artwork'))
                                        os.makedirs(new_dir, mode, exist_ok = True)
                                        #print("Directory '%s' created successfully" %new_dir)
                                    except OSError as error:
                                        print("Directory '%s' can not be created" %new_dir)
                                if os.path.exists(new_dir):
                                    for file in files:
                                        new_path = shutil.move(f'{old_dir}\\{file}', new_dir)
                                        print(cyan + f'Pasta de media ' + reset_color, yellow + f'{Name_medium_artwork} ' + reset_color, cyan + 'foi movida de ' + reset_color,  red + f'{old_dir}' + reset_color, cyan + ' para' + reset_color, green + f'{new_dir}' + reset_color)  
                        
                         
                            if Name_Systema == 'medium_artwork': 
                                old_dir = Dir_medium_artwork + '\\' + Name_medium_artwork + '\\' + 'roms'
                                new_dir = os.path.join(Dir_medium_artwork, Name_medium_artwork)                                
                                if os.path.exists(old_dir):
                                    files = os.listdir(old_dir)
                                    for file in files:
                                        new_file = os.path.join(new_dir, file)
                                        if not os.path.exists(new_file):
                                            new_path = shutil.move(f'{old_dir}\\{file}', new_dir)
                                            print(cyan + f'mover aquivos ' + reset_color, yellow + f'{old_dir} ' + reset_color, cyan + 'para >> ' + reset_color,  red + f'{new_dir}' + reset_color, cyan + ' o arquivo ' + reset_color, green + f'{file}' + reset_color)  
        
        
        print(cyan + 'Vamos limpar pastas desnecessárias!'.upper() + reset_color)
        Backup_EmptyFolders()
        print(cyan + 'Renomeando concluido!'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '4':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Retirar todas as midias que não estejam renomeadas conforme o nome das ROMs no .XML ...'.upper() + reset_color)
        for System_Name in INSTALLED_SYSTEMS:
            RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
            for Search_Texto in RETURN_MEDIA_NAME:
                if (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != [] and (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != None and (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != 'NoneType':
                #print(cyan + f'Verificando {RETURN_MEDIA_NAME} existe...' + reset_color)
                    REMOVE_UNOFICIAL = (Remove_Files_System_Unofficial(System_Name, Search_Texto))
                    REMOVE_UNOFICIAL = list(set(REMOVE_UNOFICIAL))
                    print(red + f'No seu sistema tem '.upper(), f':' + reset_color, blue + f' {len(REMOVE_UNOFICIAL)} ' + reset_color, red + f' arquivos de MIDIAS Itens que não correpondem as suas ROMs e serão removidas para '.upper() + reset_color,  green + f'{BACKUP_DIR}\\UNOFFIAL {DATA_HORA_ATUAIS_FORMATADO} '.upper() + reset_color)            
                    print(red + f'IDENTIFICADO ', f'|' + reset_color, blue + f' {Search_Texto} FILE'.upper() + reset_color, red + f' NO SISTEMA ' + reset_color,  green + f'{System_Name}'.upper() + reset_color)
                    for dir_file in REMOVE_UNOFICIAL:
                        if os.path.exists(dir_file):
                            make_backup_default(dir_file, 'UNOFFIAL ')
                #criar_log_auditoria(System_Name, 'media.', DIR_REMOVE_FILES, MISSING_FILES)
        print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '5':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'RENOMEAR ROMS E MIDAS DE ACORDO COM O NOME DO CSV ( A LISTA QUE VOCÊ MONTOU CASO EXISTA) ...'.upper() + reset_color)
        for System_Name in INSTALLED_SYSTEMS:
            RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
            for Search_Texto in RETURN_MEDIA_NAME:
                if Search_Texto != '' and os.path.exists(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) and os.listdir(str(get_dir_settings(System_Name,Search_Texto, 'settings.conf'))) != [] and os.listdir(str(get_dir_settings(System_Name,Search_Texto, 'settings.conf'))) != None:
                    SYSTEM_NAME_TMP = MODULE_DIR_RENAME_SYSTEM_MANUAL + 'Fix_' + System_Name + '.csv'
                    if os.path.exists(get_dir_settings(System_Name, 'list.path', 'settings.conf')) and os.path.exists(SYSTEM_NAME_TMP) and os.listdir(get_dir_settings(System_Name, 'list.path', 'settings.conf')) != [] and os.listdir(get_dir_settings(System_Name, 'list.path', 'settings.conf')) != None:
                        ROM_DIR = (get_dir_settings(System_Name,'list.path', 'settings.conf'))
                        MEDIA_DIR = (get_dir_settings(System_Name, Search_Texto, 'settings.conf'))
                
                        if os.path.exists(SYSTEM_NAME_TMP):
                            System_Name_ROM_df = pd.read_csv(SYSTEM_NAME_TMP, encoding='utf-8', sep=';') # , header=None                            
                            rom_wrong_name_lts = list(set(System_Name_ROM_df['rom_wrong_name'].tolist()))
                            rom_official_name_lts = list(set(System_Name_ROM_df['rom_official_name'].tolist()))
                            if rom_wrong_name_lts != [] or rom_wrong_name_lts != None and rom_official_name_lts != [] or rom_official_name_lts != None:
                                renameDirRom(ROM_DIR, System_Name)
                                renameDirRom(MEDIA_DIR, System_Name)
                            else:

                                print(red + f'Não há nomes de ROMs para renomear para o sistema: '.upper()+ reset_color + blue + f' {System_Name} ' + reset_color)

        print(cyan + 'Arquivos RENOMEADOS com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '6':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'organizar centralizando as midias dos sistemas no diretório main do seu sistema ...'.upper() + reset_color)
        for System_Name in INSTALLED_SYSTEMS:
            RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
            for Search_Texto in RETURN_MEDIA_NAME:
                if Search_Texto != ''  != 'list.path' and os.path.exists(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) and os.listdir(str(get_dir_settings(System_Name,Search_Texto, 'settings.conf'))) != []:
                    SYSTEM_FOLDER_EXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + 'system_artwork' + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file + '\\' + 'system_artwork') for file2 in os.listdir(ROOT + '\\collections\\' + file + '\\' + 'system_artwork')]))
                    for file in SYSTEM_FOLDER_EXT:
                        #print(file, '> SYSTEM_FOLDER_EXT')
                        Dir__LEVEL0, nome_ext_LEVEL0 = os.path.split(file)
                        nome_LEVEL0, ext_LEVEL0 = os.path.splitext(nome_ext_LEVEL0)
                        Dir_LEVEL1, nome_LEVEL1 = os.path.split(Dir__LEVEL0)
                        Dir_LEVEL2, nome_LEVEL2 = os.path.split(Dir_LEVEL1)

                        #print(red + 'nome_ext_LEVEL0'.upper() + reset_color, f'{nome_ext_LEVEL0}')
                        #print(red + 'Dir__LEVEL0'.upper() + reset_color, f'{Dir__LEVEL0}')
                        #print(red + 'nome_LEVEL0'.upper() + reset_color, f'{nome_LEVEL0}')
                        #print(red + 'ext_LEVEL0'.upper() + reset_color, f'{ext_LEVEL0}')
                        #print(red + 'nome_LEVEL1'.upper() + reset_color, f'{nome_LEVEL1}')
                        #print(red + 'nome_LEVEL2'.upper() + reset_color, f'{nome_LEVEL2}')

                        if not os.path.exists(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}'))):
                            mode = 0o666
                            try:
                                os.mkdir(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}')))
                                os.makedirs(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}')), mode, exist_ok = True)                        
                                print( cyan + "Directory '%s' created successfully" %(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}'.upper() + reset_color))))
                            except OSError as error:
                                print(red + "Directory '%s' can not be created" %(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}'.upper() + reset_color))))
                                #raise
                        # mover as pastas caso não existem para o sistema
                        if os.path.exists(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}'))) and not os.path.exists((os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}') + '\\' + nome_LEVEL2 + ext_LEVEL0))):
                            try:
                                os.rename((os.path.join(ROOT + '\\collections\\' + nome_LEVEL2 + '\\' + 'system_artwork' + '\\' + nome_LEVEL0)), (os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}') + '\\' + nome_LEVEL2 + ext_LEVEL0)))
                                print(cyan + f'Pasta em {Dir__LEVEL0} foi o arquivo {nome_LEVEL0} foi movido para ' + (os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}') + '\\' + nome_LEVEL2 + ext_LEVEL0)) + reset_color)
                            except OSError as error:
                                print(red + f'Pasta em {Dir__LEVEL0} não foi movida para ' + (os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}') + '\\' + nome_LEVEL2 + ext_LEVEL0)) + reset_color)
                        elif os.path.exists(os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}'))) and os.path.exists((os.path.join(ROOT + '\\collections\\Main\\medium_artwork\\' + (f'{nome_LEVEL0}') + '\\' + nome_LEVEL2 + ext_LEVEL0))):
                            print(cyan + f'Já existe {nome_LEVEL2 + ext_LEVEL0} em Main vou remover ele para backup'.upper() + reset_color)
                            if os.path.exists(file):
                                make_backup_default(file, 'MIDIA JÁ EXISTE NO MAIN ')
                                Backup_EmptyFolders()

        print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '7':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Limpar arquivos desnecessários para o seu sistema, isso vai liberar espaço ...'.upper() + reset_color)
        for dirremove, remove, emul, systema in zip(dirclean, limpar, emulador, categoria):
            make_backup_default(str(dirremove),'PRE_DEFINIDOS')  
            make_backup_default(str(remove),'PRE_DEFINIDOS')  
            print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
            print(red + 'voltando ao menu!'.upper() + reset_color)
            menu()
    if ACTION_MENU == '8':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + ' GO! MAKE - AUTOMATIZAR AS CONFIGURAÇÕES DO ROCKETLAUNCHER ...'.upper() + reset_color)
        make_dir_settings_RocketLauncher()
        print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '9':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'ajustar o arquivo settings de cada sistema para corresponder as pastas e ao sistema ...'.upper() + reset_color)
       

        for System_Name in INSTALLED_SYSTEMS: 
            RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
            for Search_Texto in RETURN_MEDIA_NAME:
                if Search_Texto != ''  != 'list.path' and os.path.exists(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) and os.listdir(str(get_dir_settings(System_Name,Search_Texto, 'settings.conf'))) != []:

                    #coleta_e_ajusta_Texto_InSettings(System_Name, Search_Texto, 'settings.conf')
                    #get_dir_settings(System_Name, Search_Texto, 'settings.conf')
                    #replacement_in_text(file, previousw, nextw)


                    DIR_MIDIA = str(get_dir_settings(System_Name, Search_Texto, 'settings.conf')) if os.listdir(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) != [] else ''
                    caminho_A, nome_A = os.path.split(DIR_MIDIA)
                    caminho_B, nome_B = os.path.split(caminho_A)

                    print(caminho_A, 'caminho_A', nome_A, 'nome_A')
                    print(caminho_B, 'caminho_B', nome_B, 'nome_B')

                    if nome_B != 'medium_artwork':
                        old_dir = caminho_A + '\\' + nome_A
                        files = os.listdir(old_dir)
                        new_dir = os.path.join(caminho_A, 'medium_artwork', nome_A)

                        print(old_dir, 'old_dir')
                        print(new_dir, 'new_dir')
                        TYPE_FILE_TXT = 'settings.conf'
                        if TYPE_FILE_TXT == 'settings.conf':     
                            SETTINGS_FILE = os.path.join(ROOT, 'collections', System_Name, TYPE_FILE_TXT)
                            TEXTO_NOVO = new_dir.replace(ROOT + '\\', 'media.' + Search_Texto + ' = ' )

                            settings_file = open(SETTINGS_FILE, 'r')
                            settings_file_lines = settings_file.readlines()
                            for line in settings_file_lines:
                                if Search_Texto in line:
                                    TEXTO_ANTIGO = line.lstrip()
                                    settings_file.close()
                            
                                    SETTINGS_PATH = os.path.join(ROOT, 'collections', System_Name, 'settings.conf')
                                    replacement_in_text(SETTINGS_FILE, TEXTO_ANTIGO, TEXTO_NOVO)



            print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
            print(red + 'voltando ao menu!'.upper() + reset_color)
            menu()
    if ACTION_MENU == '10':
        print(cyan + 'Atalizar lista de sistemas validos e otimizar lançamento de roms com a criação do include.txt na pasta decada sistema ...'.upper() + reset_color)
        for System_Name in INSTALLED_SYSTEMS:

            if not os.path.exists(INF_MENU_FOLDER):
                os.makedirs(INF_MENU_FOLDER)
            if not os.path.exists(INF_MENU_FOLDER + '\\' + System_Name + '.txt'):
                meuArquivo = open(str(INF_MENU_FOLDER + '\\' + System_Name + '.txt'), 'w')
                meuArquivo.write(''+ '\n')
                meuArquivo.close()

            RomPathlist= coleta_e_ajusta_Texto_InSettings(System_Name, 'list.path', 'settings.conf')
            RomExtList = str(coleta_e_ajusta_Texto_InSettings(System_Name, 'list.extensions', 'settings.conf')).replace(' ', '|') 
            EmuladorList = os.path.splitext(str(coleta_e_ajusta_Texto_InSettings(System_Name, 'executable', '.conf')))[0]
            EditRomExtList = (RomExtList.replace(',', '|'))

            if os.path.exists(ROOT + '\\collections\\' + System_Name + '\\' + 'include.txt'):
                try:
                    os.remove(ROOT + '\\collections\\' + System_Name + '\\' + 'include.txt')
                except:
                    pass
            # criar arquivo include.txt
            if not os.path.exists(str(RomPathlist)):
                # tentar corrigir nome
                RomPathlist = RomPathlist[0:-1]

            if os.path.exists(str(RomPathlist)):
                print(green + RomPathlist[0:-1]  + reset_color, yellow + ' < -- Caminho das ROMS'  + reset_color)
                EditRomExtList2 = EditRomExtList.split('|')
                for ext in EditRomExtList2:
                    RomsScamA = [(file.replace('.' + ext,'')) for file in os.listdir(str(RomPathlist)) if file.endswith(ext)]
                    RomsScamB = [(file.replace('.' + ext,'') + '\n') for file in os.listdir(str(RomPathlist)) if file.endswith(ext)]
                    for rom in RomsScamB:                                       
                        meuArquivo = open(str(ROOT + '\\collections\\' + System_Name + '\\' + 'include.txt'), 'a')
                        meuArquivo.write(str(rom))
                        meuArquivo.close()
                # retirar roms da lista de exclusão em exclude.txt
                if os.path.exists(ROOT + '\\collections\\' + System_Name + '\\exclude.txt'):
                    for RomExclude in coleta_e_ajusta_Texto_InSettings(System_Name, '','exclude.txt'):
                        pesquisar_registro_exlucluir_palavras(ROOT + '\\collections\\' + System_Name + '\\' + 'include.txt', RomExclude)
                        print(green + System_Name  + reset_color, yellow + ' < -- teve o arquivo include.txt criado para maior ótimização'  + reset_color)

        INF_MENU_FOLDER_FILE = [(os.path.splitext(f)[0])  for f in os.listdir(INF_MENU_FOLDER) if os.path.exists(INF_MENU_FOLDER) if os.path.isdir(INF_MENU_FOLDER) if os.path.isfile(INF_MENU_FOLDER + '\\' + f)]
        meuArquivo = open(str(INF_MENU), 'w')
        meuArquivo.write(System_Name + '\n')
        meuArquivo.close()
        stream = open(str(INF_MENU), 'r+')
        for line in stream:
            for word in INF_MENU_FOLDER_FILE:
                if word == line.strip():
                    pass
                else:
                    stream.write(word + '\n')
                    print(red + word + reset_color, cyan + ' < -- verificando sistema no menu'  + reset_color)
                    print(red + word + reset_color, cyan + ' < -- Line do sistema no menu'  + reset_color)
        stream.close()


        print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
    if ACTION_MENU == '11':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Limpar arquivos desnecessários para o seu sistema, isso vai liberar espaço ...'.upper() + reset_color)
        for dirremove, remove, emul, systema in zip(dirclean, limpar, emulador, categoria):
            make_backup_default(str(dirremove),'PRE_DEFINIDOS')  
            make_backup_default(str(remove),'PRE_DEFINIDOS')  
            print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
            print(red + 'voltando ao menu!'.upper() + reset_color)
            menu()
    if ACTION_MENU == '12':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'Retirar todas as pasta e arquivos que não estejam renomeadas conforme o system ...'.upper() + reset_color)

        
        ITEMS_COLLECTION_NAME_MAIN_ARTWORK = [f for f in os.listdir(ROOT + '\\collections\\Main\\medium_artwork') if os.path.exists(ROOT + '\\collections\\Main\\medium_artwork\\') if os.path.isdir(ROOT + '\\collections\\Main\\medium_artwork\\')]
        ITEMS_COLLECTION_DIR_MAIN_ARTWORK_CONTENT = list(set([(ROOT + '\\collections\\Main\\medium_artwork\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME_MAIN_ARTWORK if os.path.exists(ROOT + '\\collections\\Main\\medium_artwork\\' + file) for file2 in os.listdir(ROOT + '\\collections\\Main\\medium_artwork\\' + file) if os.path.isfile(ROOT + '\\collections\\Main\\medium_artwork\\' + file + '\\' + file2)]))
        
        #print(ITEMS_COLLECTION_DIR_MAIN_ARTWORK_CONTENT)

        Make_remove_System_Name_Unofficial(INSTALLED_SYSTEMS_DIR)
        Make_remove_System_Name_Unofficial(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL0)
        Make_remove_System_Name_Unofficial(ITEMS_ROCKETLAUNCHER_DIR__LEVEL0_SETTINGS)
        Make_remove_System_Name_Unofficial(ITEMS_COLLECTION_DIR_MAIN_ARTWORK_CONTENT)

        print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()    

# ler informações no gamelist.xml e criar um arquivo .txt na pasta story de cada collection com a info <desc>
    if ACTION_MENU == '13':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU '.upper() + reset_color)
        print(cyan + 'ler informações no gamelist.xml e criar um arquivo .txt na pasta story de cada collection com a info <desc> ...'.upper() + reset_color)
        for dir in os.listdir(ROOT + '\\collections'):
            print(get_info_gamelist_xml('Nintendo 64DD', 'name'))




        menu()    
    

    if ACTION_MENU == '0':
        print(ACTION_MENU, cyan + ' EXECUTANDO O MENU 1'.upper() + reset_color)
        print(cyan + 'Limpar arquivos desnecessários para o seu sistema, isso vai liberar espaço ...'.upper() + reset_color)
        ACTION_MENU == '1'
        executar_menu()
        ACTION_MENU == '2'
        executar_menu()
        ACTION_MENU == '3'
        executar_menu()
        ACTION_MENU == '4'
        executar_menu()
        ACTION_MENU == '6'
        executar_menu()
        ACTION_MENU == '7'
        executar_menu()
        ACTION_MENU == '8'
        executar_menu()
        ACTION_MENU == '9'
        executar_menu()
        ACTION_MENU == '10'
        executar_menu()
        ACTION_MENU == '11'
        executar_menu()

        print(cyan + 'Arquivos retirados com sucesso !'.upper() + reset_color)
        print(red + 'voltando ao menu!'.upper() + reset_color)
        menu()
                                # --------- DEFINIÇÃO DO MENU ------------ #
def menu():
    print(cyan + '''
                MENU:
                [0] - Fazer todas as verificações e atividades de otimização
                [1] - Renomear - Coleções   Ex:. (a2600) -> (Atari 2600)              [6]  - Clean - Organizar Coleções em Main Folder
                [2] - Renomear - Emuladores Ex:. (Cemu) -> (Nintendo Wii U)           [7]  - Clean - Limpar aquivos desnecessários do sistema 
                [3] - Clean - Organizar Coleções e SubColeções ArtWorks               [8]  - Make - Automatizar as configurações do RocketLauncher  
                [4] - Clean - Retirar arquivos desnecessários na pastas de midias     [9]  - Make - Ajustar as configurações do Settings RetroFe 
                [5] - Clean - Retirar arquivos desnecessários na pastas de ROMS       [10] - Make - Otimizar lançamentos de ROMS       
                [11] - Sair
            '''.upper() + reset_color)
    return str(input(red + 'Escolha uma opção: '.upper() + reset_color))
# ! ----------------------------------------------------------------------------------------------------- ! #
ACTION_MENU = menu()
menu()
# ! ----------------------------------------------------------------------------------------------------- ! #
executar_menu()


