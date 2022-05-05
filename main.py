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
from shutil import move
from datetime import date
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
ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL2_THEMAS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\', file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
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
            print(f'{file_name} AAA ')
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
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color) 
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Erro e forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)        
                        pass

                if not str(ROOT + '\\') in str(caminho):
                    dir_tmp, arquivo = os.path.split(caminho)
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho)                    
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\' + file_name
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color) 
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Erro e forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)         
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
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color) 
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Erro e forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)                   
                        pass

                if not str(ROOT) in caminho:
                    dir_tmp = str(caminho)
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho) 
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + file_name
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)
                        except IOError:
                            move(old_end, new_end)
                            print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Erro e forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)                    
                        pass

            elif not os.path.exists(str(caminho)):
                #print(' O Diretório que você quer mudar em' , caminho,' os arquivos não existe, verifique se há algum erro !!')
                pass
        else:
            pass

    elif type(caminhos) != list:
        #print(f'O caminho {caminhos} que você passou não é uma lista!!')
        # aqui ele segue se for um arquivo
        if os.path.isfile(caminhos) and os.path.exists(caminhos):
            dir_file, file_name = os.path.split(caminhos)
            print(f'{file_name} BBB ')
            # ajustando nomes 
            if str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos) 
                dir_tmp = dir_tmp.replace(ROOT + '\\', '')
            # criando pasta e removendo arquivo
                if os.path.exists(str(dir_tmp)):    
                    old_end = str(caminhos)
                    #new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\' + file_name
                    print(new_end, 'new_end 1')
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(old_end, new_end)
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)                       
                    pass

            if not str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos)
                if os.path.exists(str(dir_tmp)):                         
                    old_end = str(caminhos)                    
                    #new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\' + file_name
                    print(new_end, 'new_end 2')
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(old_end, new_end)
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)                        
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
                    print(new_end, 'new_end 3')
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(old_end, new_end)
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)                      
                    pass

            if not str(ROOT + '\\') in str(caminhos):
                dir_tmp = str(caminhos).split('\\', 0)[-1]
                print(dir_tmp, 'dir_tmp 4')
                dir_file, file_name = os.path.split(caminhos)
                print(f'{caminhos} BBB ')
                print(f'{file_name} AAA ')
                if os.path.exists(str(dir_tmp)):                         
                    old_end = str(caminhos) 
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + file_name
                    print(new_end, 'new_end 4')
                    try:
                        os.makedirs(new_end)
                        shutil.move(str(old_end), str(new_end), copy_function=str(new_end))
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Fazendo Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)
                    except IOError:
                        move(str(old_end), str(new_end))
                        print(red + f'folder > old ', f'=' + reset_color, blue + f' {old_end} ' + reset_color, red + f'>Forçando Back_Up> > new ' + reset_color,  green + f'{new_end}' + reset_color)            
                    pass

        if not os.path.exists(caminhos):
            #print(' O Diretório que você quer mudar :', caminhos ,' os arquivos não existe, verifique se há algum erro !!')
            pass
    else:
        print('Não temos nada para alterar aqui !!')
# ----------------- | -----------------         Renomear Arquivos     ---------------- | ------------------ #
def renameDirRom(caminho, list_rom_wrong_name, list_rom_official_name):
    for Path in caminho :
        if os.path.exists(str(Path)) and os.path.isdir(Path):
            Dir, Nome = os.path.split(Path)  
            for erroName, offialName in zip(list_rom_wrong_name, list_rom_official_name):
                if erroName == Nome != offialName:
                    old_file = os.path.join(Dir, Nome)
                    for indice, elemento in enumerate(list_rom_wrong_name):
                        if elemento == Nome:
                            for official_indice, official_elemento in enumerate(list_rom_official_name):
                                if elemento == Nome and indice == official_indice:
                                    old_file = os.path.join(Dir, Nome)
                                    tmp_file = os.path.join(Dir, Nome).replace(elemento, '_~|(Name~tmp)|~_')
                                    new_file = tmp_file.replace('_~|(Name~tmp)|~_', official_elemento)

                                    if old_file != new_file:
                                        try:
                                            os.rename(old_file, new_file)
                                            print(f'folder index {indice} = {old_file}  >> name index = {official_indice} | {new_file}')
                                        except:
                                            pass  
                                    if Path !=  old_file != new_file:
                                        print(f'Esta pasta = {Path} não parece ser um sistema valido')
    for file in caminho :
        if os.path.exists(str(file)) and os.path.isfile(file):
            Dir, Nome = os.path.split(file) 
            fileName, Ext = os.path.splitext(Nome)
            for erroName, offialName in zip(list_rom_wrong_name, list_rom_official_name):
                if erroName == fileName != offialName:
                    old_file = os.path.join(Dir, fileName + Ext)                    
                    for indice, elemento in enumerate(list_rom_wrong_name):
                        if elemento == fileName:
                            for official_indice, official_elemento in enumerate(list_rom_official_name):
                                if elemento == fileName and indice == official_indice:
                                    old_file = os.path.join(Dir, fileName + Ext)
                                    tmp_file = os.path.join(Dir, fileName + Ext).replace(elemento, '_~|(Name~tmp)|~_')
                                    new_file = tmp_file.replace('_~|(Name~tmp)|~_', official_elemento)
                                    if old_file != new_file:
                                        try:
                                            if os.path.exists(new_file):
                                                move(old_file, new_file)
                                                print(f'folder index {indice} = {old_file}  >SOBREPONDO> name index = {official_indice} | {new_file}')
                                        except:
                                            pass
                                    print((str(Path)), '>old',old_file , '>new', new_file)    
                                    if file !=  old_file != new_file:
                                        print(f'Esta pasta = {file} não parece ser um sistema valido')     
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
def Ajuste_Texto_InSettings(NomeDoSystema, texto, tipoArquivo):
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
                                print(LINHA_SETTINGS, '<<<<<< C')
                                

                        return LINHA_SETTINGS
    elif type(SYSTEM_NAME) != list:
        SETTINGS_FILE = os.path.join(ROOT, 'collections', SYSTEM_NAME, TYPE_FILE_TXT)
        if TYPE_FILE_TXT == 'settings.conf': 
            if os.path.exists(SETTINGS_FILE):
                SETTINGS_FILE = os.path.join(ROOT, 'collections', SYSTEM_NAME, TYPE_FILE_TXT) 
                with open(SETTINGS_FILE, 'r') as settings_file:
                    settings_file_lines = settings_file.readlines()
                    for line in settings_file_lines:
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
            return ROMS_XML_LIST
    if type(SYSTEM_NAME) != list:
        systemXML = os.path.join(ROOT + '\\meta\\hyperlist\\', str(SYSTEM_NAME) + '.xml')
        if os.path.exists(systemXML):
            tree = ET.parse(systemXML)
            root = tree.getroot()
            ROMS_XML_LIST = [game.attrib['name'] for game in root.findall("./game")]
            return ROMS_XML_LIST
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

# ! ----------------------------------------------------------------------------------------------------- ! #
# ! ---------------------------------!!       BASE DO MENU        !!    --------------------------------- ! #
# ! ----------------------------------------------------------------------------------------------------- ! #
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
            ''' + reset_color)
    return str(input(red + 'Escolha uma opção: ' + reset_color))
# ! ----------------------------------------------------------------------------------------------------- ! #
ACTION_MENU = menu()
# ! ----------------------------------------------------------------------------------------------------- ! #
if ACTION_MENU == '1':
    print(cyan + 'Iniciando os procedimentos de renomear os seus sistemas...' + reset_color)
    renameDir(INSTALLED_SYSTEMS_DIR)
    renameDir(ITEMS_META_FILE_XML)
    renameDir(ITEMS_LAYOUTS_DIR__COLLECTION_LEVEL0)
    print(cyan + 'Renomeando concluido!' + reset_color)
    print(red + 'voltando ao menu!' + reset_color)
    menu()
if ACTION_MENU == '2':
    print(cyan + 'Iniciando os procedimentos de renomear os seus Emuladores...' + reset_color)
    renameDir(ITEMS_EMULATORS_DIR_NAME)
    print(cyan + 'Renomeando concluido!' + reset_color)
    print(red + 'voltando ao menu!' + reset_color)
    menu()
if ACTION_MENU == '3':
    print(cyan + 'Iniciando os procedimentos para movimentar pastas com midias para a pasta padrão artwork...' + reset_color)
    LTS_DIR_MIDIA = []
    for System_Name in INSTALLED_SYSTEMS:
        RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
        list(set(RETURN_MEDIA_NAME))
        for Search_Texto in RETURN_MEDIA_NAME:
            if Search_Texto != 'list.path' and os.path.exists(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) and os.listdir(str(get_dir_settings(System_Name,Search_Texto, 'settings.conf'))) != []:
                DIR_MIDIA = str(get_dir_settings(System_Name, Search_Texto, 'settings.conf')) if os.listdir(str(get_dir_settings(System_Name, Search_Texto, 'settings.conf'))) != [] else ''
                Dir_medium_artwork, Name_medium_artwork = os.path.split(DIR_MIDIA)
                Dir_collections, Name_Systema = os.path.split(Dir_medium_artwork)
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
    print(cyan + 'Vamos limpar pastas desnecessárias!' + reset_color)
    Backup_EmptyFolders()
    print(cyan + 'Renomeando concluido!' + reset_color)
    print(red + 'voltando ao menu!' + reset_color)
    menu()
if ACTION_MENU == '4':
    print(cyan + 'Retirar todas as midias que não estejam renomeadas conforme o nome das ROMs no .XML ...' + reset_color)
    for System_Name in INSTALLED_SYSTEMS:
        RETURN_MEDIA_NAME = sorted(list(set(listar_artwork_folders(System_Name))))
        for Search_Texto in RETURN_MEDIA_NAME:
            if (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != [] and (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != None and (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != 'NoneType':
            #print(cyan + f'Verificando {RETURN_MEDIA_NAME} existe...' + reset_color)
                REMOVE_UNOFICIAL = (str(Remove_Files_System_Unofficial(System_Name, Search_Texto)))
                print(red + f'No seu sistema tem ', f':' + reset_color, blue + f' {len(REMOVE_UNOFICIAL)} ' + reset_color, red + f' arquivos de MIDIAS Itens que não correpondem as suas ROMs e serão removidas para ' + reset_color,  green + f'{BACKUP_DIR}\\UNOFFIAL {DATA_HORA_ATUAIS_FORMATADO} ' + reset_color)            
                for dir_file in REMOVE_UNOFICIAL:
                    if os.path.exists(dir_file):
                        make_backup_default(dir_file, 'UNOFFIAL ')
            #criar_log_auditoria(System_Name, 'media.', DIR_REMOVE_FILES, MISSING_FILES)
    print(cyan + 'Arquivos terirados com sucesso !' + reset_color)
    print(red + 'voltando ao menu!' + reset_color)
    menu()



