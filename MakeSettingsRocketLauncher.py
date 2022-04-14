# Programa para limpar a estrutura do RetroFe
# Retirada de arquivos não uteis
# declarando libs
from ast import Return
from genericpath import exists
from importlib.resources import path
import os
import shutil
from shutil import move
from tkinter.messagebox import NO
import pandas as pd  # para ler, visualizar e printar infos do df
import os.path
from datetime import date
from datetime import datetime
import numpy as np 
import xml.etree.ElementTree as ET
from io import StringIO

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
print('Sistema Operacional :', cyan + os.name + reset_color)
#cmd = 'date'
#print('Em que século você esta :', os.system(date))
print('Sript excutado :', yellow +  os.path.basename(__file__) + reset_color)
print('Localização :',  yellow +  (__file__) + reset_color)
# Para obter o caminho absoluto
dir_path = os.path.dirname(os.path.realpath(__file__))
# -------------------------------------------------- #

# -----------------    CAMINHOS   ------------------ #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #
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
print(red + "ROOT : ", ROOT + reset_color)
os.chdir(ROOT)
# -----------------    CAMINHOS   ------------------ #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #

FILE_CSV_FIX_NAME_SYSTEM = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem.csv'
FILE_CSV_FIX_NAME_SYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem_Tmp.csv'
FILE_CSV_FIX_NAME_CLEAN = ROOT + '\\core\\maneger\\Data\\Fix_NameClean.csv'
FILE_CSV_FIX_NAME_CLEAN_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameClean_Tmp.csv'
FILE_CSV_DIRSYSTEM = ROOT + '\\core\\maneger\\Data\\DirSystem.csv'
FILE_CSV_DIRSYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\DirSystem_Tmp.csv'
# -------------------   FUNÇÃO   ------------------- #
# ----------------- Manipular CSV ------------------ #
# _________     IMPORTAR ARQUIVOS   ________________ #
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

# -----------------    CAMINHOS   ------------------ #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #

FILE_CSV_FIX_NAME_SYSTEM = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem.csv'
FILE_CSV_FIX_NAME_SYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem_Tmp.csv'
FILE_CSV_FIX_NAME_CLEAN = ROOT + '\\core\\maneger\\Data\\Fix_Clean.csv'
FILE_CSV_FIX_NAME_CLEAN_TMP = ROOT + '\\core\\maneger\\Data\\Fix_Clean_Tmp.csv'
FILE_CSV_DIRSYSTEM = ROOT + '\\core\\maneger\\Data\\DirSystem.csv'
FILE_CSV_DIRSYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\DirSystem_Tmp.csv'
BEFORE_DIR = ((os.path.dirname(os.path.realpath(__file__))).split('\\', -1)[-2]) + '\\'
BACKUP_DIR = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup'
BACKUP_DIR_ROM = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup' + '\\Roms'
DATA_ATUAL = date.today()
DATA_HORA_ATUAIS = datetime.now()
DATA_HORA_ATUAIS_FORMATADO = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H-%M')
ITEMS_COLLECTION_NAME = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\')]
ITEMS_COLLECTION_DIR_NAME = list(set([os.path.join(ROOT + '\\collections\\', file) for file in os.listdir(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\' + file)]))
ITEMS_COLLECTION_DIR__CONTENT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_COLLECTION_NAME__CONTENT = list(set([(file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_EMULATORS_NAME = list(set([f for f in os.listdir(ROOT + '\\emulators\\') if os.path.exists(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\')]))
ITEMS_EMULATORS_DIR_NAME = list(set([os.path.join(ROOT + '\\emulators\\', file) for file in os.listdir(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\' + file)]))
#ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
#ITEMS_LAYOUTS_DIR_COLLECTION = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))
ITEMS_COLLECTION_FILE_CONF = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.conf')]))
ITEMS_META_NAME = [f for f in os.listdir(ROOT + '\\meta\\') if os.path.exists(ROOT + '\\meta\\') if os.path.isdir(ROOT + '\\meta\\')]
ITEMS_META_DIR_NAME = list(set([os.path.join(ROOT + '\\meta\\', file) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file)]))
ITEMS_META_FILE_XML = list(set([os.path.join(ROOT + '\\meta\\' + file + '\\', file2) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file) for file2 in os.listdir(ROOT + '\\meta\\' + file) if file2.endswith('.xml')]))
ITEMS_COLLECTION_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.txt')]))
ROMS_NAME_REAL_LIST = []
EMPTY = []
ITEMS_ROCKETLAUNCHER_NAME = list(set([file for file in os.listdir(ROOT + '\\RocketLauncher') if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
ITEMS_ROCKETLAUNCHER_DIR_NAME = list(set([os.path.join(ROOT + '\\RocketLauncher\\', file) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.exists(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
ITEMS_ROCKETLAUNCHER_DIR_CONTENT = list(set([os.path.join(ROOT + '\\RocketLauncher\\' + file, file2) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2)]))
ITEMS_ROCKETLAUNCHER_SETTINGS_NAME = [f for f in os.listdir(ROOT + '\\RocketLauncher\\Settings') if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + f) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + f)]
ITEMS_ROCKETLAUNCHER_DIR_SETTINGS = list(set([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file)]))
ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Settings\\' + file) if file2.endswith('.ini')])) 

# -----------------    CONSTRUÇÃO DAS COFIGURAÇÕES   ------------------ #
# _________    FAZER PASTAS E CONFIGURAÇÕES NO SETTINGS    ____________ #
def makePathSettingsMakeSettingsRocketLauncher(nameSystem):

    DirNameSystem = os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + nameSystem)
    if not os.path.exists(DirNameSystem) and os.path.exists(ROOT + '\\collections\\' + nameSystem + '\\' + 'settings.conf') and nameSystem != 'Main':
        os.makedirs(DirNameSystem)
    return DirNameSystem
# _________    LER CONFIGURAÇÕES DO SETTINGS RETROFE   ____________ #
global LINHA_SETTINGS_LST
RETURN_SETTING = []
def Texto_InSettings(NomeDoSystema, texto, tipoArquivo):
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

# -----------------   MAQUINA DE ESTADOS    ------------------ #
# __        busca linha por linha de um dado arquivo        __ #
def pesquisar_registro( AQUIVO, TEXTO ):
    with open(AQUIVO,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if TEXTO not in line:
                f.write(line)
        f.truncate()

# -----------------    APLICAÇÃO DAS COFIGURAÇÕES   ------------------ #
# _________    FAZER PASTAS E CONFIGURAÇÕES NO SETTINGS    ____________ #
RomPathtmp = []
listRomexclude = []
for NomeSystema in ITEMS_COLLECTION_NAME:  
    makePathSettingsMakeSettingsRocketLauncher(NomeSystema)

    RomPathlist= Texto_InSettings(NomeSystema, 'list.path', 'settings.conf')
    RomExtList = str(Texto_InSettings(NomeSystema, 'list.extensions', 'settings.conf')).replace(' ', '|') 
    EmuladorList = os.path.splitext(str(Texto_InSettings(NomeSystema, 'executable', '.conf')))[0]
    EmuladorName = 'RetroArch'

    INF_EMU_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Emulators.ini'
    INF_BEZEL_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Bezel.ini'
    INF_GOPTIONS_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Game Options.ini'
    INF_GAME_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Games.ini'
    INF_PAUSE_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Pause.ini'
    INF_PLUGUINS_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'Plugins.ini' 
    INF_ROCKETLAUNCHER_INI = ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema + '\\' + 'RocketLauncher.ini'
    INF_ROCKETLAUNCHER_SETTINGS_INI = ROOT + '\\RocketLauncher\\RocketLauncherUI\\Settings\\Frontends.ini'
    INF_MENU = ROOT + '\\collections\\Main\\' + 'menu.txt'
    INF_MENU_FOLDER = ROOT + '\\collections\\Main\\menu' 


    if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + NomeSystema):
        # Construção do arquivo Emulators.ini
        meuArquivo = open(str(INF_EMU_INI), 'w')
        meuArquivo.write('[ROMS]'+ '\n')
        meuArquivo.write('Default_Emulator=' + '\n')
        EditRomPathlist = (RomPathlist.replace(ROOT, '..') + '\n')[0:-2]
        meuArquivo.write('Rom_Path=' + (EditRomPathlist.replace('\\', '', 0) ) + '\n')
        meuArquivo.close()

        meuArquivo = open(INF_EMU_INI, 'a') 
        meuArquivo.write('[' + EmuladorName + ']' + '\n')
        EditRomExtList = (RomExtList.replace(',', '|'))
        meuArquivo.write('Rom_Extension=' + EditRomExtList + '\n')
        meuArquivo.write('Emu_Path=..\\emulators\\RetroArch\\retroarch.exe' '\n')
        meuArquivo.write('Module=RetroArch.ahk' + '\n')
        meuArquivo.write('Pause_Save_State_Keys={F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F2 down}{F2 up}' + '\n')
        meuArquivo.write('Pause_Load_State_Keys={F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}|{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F6 down}{F6 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F7 down}{F7 up}{F4 down}{F4 up}' + '\n')
        meuArquivo.close()
        if EmuladorName == 'RetroArch': 
            buffer = StringIO()
            buffer2 = StringIO()

            with open(str(INF_EMU_INI), 'r+') as stream:
                for index, line in enumerate(stream):
                    # index == 1 representa a segunda linha do arquivo:
                    buffer.write('Default_Emulator=RetroArch\n' if index == 1 else line)
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
        #meuArquivo = open(str(INF_MENU), 'r+')
        #meuArquivo.write(NomeSystema + '\n')
        #meuArquivo.close()

        if not os.path.exists(INF_MENU_FOLDER):
            os.makedirs(INF_MENU_FOLDER)
        meuArquivo = open(str(INF_MENU_FOLDER + '\\' + NomeSystema + '.txt'), 'a')
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

        if os.path.exists(RomPathlist[0:-1]):
            EditRomExtList2 = EditRomExtList.split('|')
            for ext in EditRomExtList2:
                RomsScamA = [(file.replace('.' + ext,'')) for file in os.listdir(RomPathlist[0:-1]) if file.endswith(ext)]
                RomsScamB = [(file.replace('.' + ext,'') + '\n') for file in os.listdir(RomPathlist[0:-1]) if file.endswith(ext)]

                for rom in RomsScamB:                                       
                    meuArquivo = open(str(ROOT + '\\collections\\' + NomeSystema + '\\' + 'include.txt'), 'a')
                    meuArquivo.write(str(rom))
                    meuArquivo.close()
                # retirar roms da lista de exclusão em exclude.txt
                if os.path.exists(ROOT + '\\collections\\' + NomeSystema + '\\exclude.txt'):
                    for RomExclude in Texto_InSettings(NomeSystema, '','exclude.txt'):
                        pesquisar_registro(ROOT + '\\collections\\' + NomeSystema + '\\' + 'include.txt', RomExclude)

