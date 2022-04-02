# -*- coding: utf-8 -*-

from operator import index
import os
import pandas as pd
import numpy as np 
from tqdm import tqdm  # barra de progresso
import shutil # copiar arquivos
import shutil, tempfile # carregar informações do CSV FILE_CSV_FIX_NAME_SYSTEM
from shutil import move # move arquivos
import re # regular expression
# retorna uma lista das pastas da estrutura do sistema
# ---------------------- DEFINIÇÃO DE CORES ---------------------- #
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
# informações do script
print(cyan + '*--- INFO SCRIPT : ', os.path.basename(__file__).split('.')[0].upper(), '----------------------------------*' + reset_color)
print(blue + '| Sript excutado : ' + reset_color, yellow +  os.path.basename(__file__) + reset_color)
print(blue + '| Localização : ' + reset_color,  yellow +  (__file__) + reset_color)
print(cyan + '*---------------------------------------------------------------*' + reset_color)

# ----------------- DEFINIÇÃO DO DIRETÓRIO ROOT ------------------ #
# idenfificar o diretório do projeto e definir que o diretório ROOT sempre será o root + '/core'
ROOT = os.path.dirname(os.path.abspath(__file__)) if 'core' in os.listdir(os.path.dirname(os.path.abspath(__file__))) else "\\".join(((os.path.realpath(__file__)).split('\\', -1)[0:3]))
DATA_MANEGER_DATA = ROOT + '\\core\\maneger\\' + 'Data\\'
FILE_CSV_FIX_NAME_SYSTEM = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem.csv'
FILE_CSV_FIX_NAME_SYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem_Tmp.csv'
FILE_CSV_FIX_NAME_CLEAN = ROOT + '\\core\\maneger\\Data\\Fix_NameClean.csv'
FILE_CSV_FIX_NAME_CLEAN_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameClean_Tmp.csv'
# carregar informações do CSV FILE_CSV_FIX_NAME_SYSTEM
#verificar aquivo existe
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
# carregar informações do CSV FILE_CSV_FIX_NAME_SYSTEM
file_backup(FILE_CSV_FIX_NAME_SYSTEM)
df = pd.read_csv(FILE_CSV_FIX_NAME_SYSTEM_TMP, encoding='utf-8', sep=';')
df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))
# ------- FUNÇÃO PARA LER AS INFORMAÇÕES NOS DIRETÓRIOS ---------- #
# ler informações dos arquivos .conf , .txt e .bat 
def ler_arquivos_TXT(caminho_arquivo):
    if os.path.isfile(str(caminho_arquivo)) == True:
        arquivo = open(str(caminho_arquivo), 'r')
        linhas = arquivo.readlines()
        arquivo.close()
        return linhas

# Localizar informações especificas nas linhas dos arquivos de texto
def ler_arquivos_TXT_linhas(caminho_arquivo, Criterio):
    for erroName, offialName in zip(df['wrong_name'], df['official_name']):
        if os.path.isfile(str(caminho_arquivo)) == True:
            arquivo = open(str(caminho_arquivo), 'r')           
        
            Dir, Nome = os.path.split(caminho_arquivo)
            Dir, Nome = os.path.split(Dir) # Separa o diretório e o nome do arquivo
            for linha in arquivo:
                    if linha == "":
                        pass
                    if '#' + Criterio in linha:
                        #SettingsRomPath = "collections\\" + str(systemName[0]) + '\\roms'
                        pass
                    elif Criterio in linha:
                        Valor_Criterio = linha.split('=')[1].replace('\n', '')
                        return Nome + ':' + Valor_Criterio 
            
            
            arquivo.close()

        #linhas = arquivo.readlines()
        #arquivo.close()
        #return linhas[linha_inicial:linha_final]

# --------- DEFINIÇÃO DAS LISTAS DOS OUTROS DIRETÓRIOS ------------ #
print(blue + '| Definindo os diretórios...' + reset_color)
print(blue + '| Diretório ROOT : ' + reset_color, yellow + ROOT + reset_color)
print(blue + '| Diretório DATA_MANEGER_DATA : ' + reset_color, yellow + DATA_MANEGER_DATA + reset_color)
print(blue + '| Diretórios sendo scaneados : ' + reset_color, yellow + ROOT + reset_color)

ITEMS_COLLECTION_NAME = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\')]
ITEMS_COLLECTION_DIR_NAME = list(set([os.path.join(ROOT + '\\collections\\', file) for file in os.listdir(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\' + file)]))
ITEMS_COLLECTION_DIR__CONTENT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_COLLECTION_NAME__CONTENT = list(set([(file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_COLLECTION_FILE_CONF = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.conf')]))
ITEMS_COLLECTION_FILE_SUB = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.sub')]))
ITEMS_COLLECTION_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.txt')]))
ITEMS_COLLECTION_FILE_PNG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.png')]))
ITEMS_COLLECTION_FILE_JPG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.jpg')]))
ITEMS_COLLECTION_FILE_MP4 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.mp4')]))
ITEMS_COLLECTION_FILE_MP3 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.mp3')]))
ITEMS_COLLECTION_FILE_AVI = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.avi')]))
ITEMS_COLLECTION_FILE_OGG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.ogg')])) 
ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT = list(set([(file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3)]))
ITEMS_COLLECTION_FILE_CONTENT_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.txt')]))
ITEMS_COLLECTION_FILE_CONTENT_PNG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3)   for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')]))
ITEMS_COLLECTION_FILE_CONTENT_JPG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3)   for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.jpg')]))
ITEMS_COLLECTION_FILE_CONTENT_MP4 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3)   for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp4')]))
ITEMS_COLLECTION_FILE_CONTENT_MP3 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3)   for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp3')]))
ITEMS_COLLECTION_FILE_CONTENT_OGG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3)   for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ogg')]))
ITEMS_COLLECTION_FILE_CONTENT_SUB = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3)   for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.sub')]))
ITEMS_EMULATORS_NAME = list(set([f for f in os.listdir(ROOT + '\\emulators\\') if os.path.exists(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\')]))
ITEMS_EMULATORS_DIR_NAME = list(set([os.path.join(ROOT + '\\emulators\\', file) for file in os.listdir(ROOT + '\\emulators\\') if os.path.isdir(ROOT + '\\emulators\\' + file)]))
ITEMS_EMULATORS_DIR__CONTENT = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if os.path.isdir(ROOT + '\\emulators\\' + file + '\\' + file2)]))
ITEMS_EMULATORS_FILE_INI = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.ini')]))
ITEMS_EMULATORS_FILE_CFG = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.cfg')]))
ITEMS_EMULATORS_FILE_LPL = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.lpl')]))
ITEMS_EMULATORS_FILE_EXE = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.exe')]))
ITEMS_LAUNCHERS_FILE_CFG = list(set([os.path.join(ROOT + '\\launchers.windows\\' + file + '\\' + file2) for file in os.listdir(ROOT + '\\launchers.windows\\') if os.path.isdir(ROOT + '\\launchers\\' + file) for file2 in os.listdir(ROOT + '\\launchers\\' + file) if file2.endswith('.conf')]))
ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
ITEMS_LAYOUTS_DIR_NAME = list(set([os.path.join(ROOT + '\\layouts\\', file) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file)]))
ITEMS_LAYOUTS_FILE_XML = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\', file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file) if os.path.isdir(ROOT + '\\layouts\\' + file) for file2 in os.listdir(ROOT + '\\layouts\\' + file) if file2.endswith('.xml')]))
ITEMS_LAYOUTS_DIR_COLLECTION = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))
ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT = list(set([os.path.join(file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)]))
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\', file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\' + 'layout') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\layout\\' + file3)]))
ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML = list(set([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.xml')]))
ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG = list(set([os.path.join(file + '\\' + file2) for file in ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS if os.path.exists(file) if os.path.isdir(file) for file2 in os.listdir(file) if file2.endswith('.png')]))
ITEMS_META_NAME = [f for f in os.listdir(ROOT + '\\meta\\') if os.path.exists(ROOT + '\\meta\\') if os.path.isdir(ROOT + '\\meta\\')]
ITEMS_META_DIR_NAME = list(set([os.path.join(ROOT + '\\meta\\', file) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file)]))
ITEMS_META_FILE_XML = list(set([os.path.join(ROOT + '\\meta\\' + file + '\\', file2) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file) for file2 in os.listdir(ROOT + '\\meta\\' + file) if file2.endswith('.xml')]))
ITEMS_ROCKETLAUNCHER_NAME = list(set([file for file in os.listdir(ROOT + '\\RocketLauncher') if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
ITEMS_ROCKETLAUNCHER_DIR_NAME = list(set([os.path.join(ROOT + '\\RocketLauncher\\', file) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.exists(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file)]))
ITEMS_ROCKETLAUNCHER_DIR_CONTENT = list(set([os.path.join(ROOT + '\\RocketLauncher\\' + file, file2) for file in ITEMS_ROCKETLAUNCHER_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\' + file + '\\' + file2)]))
ITEMS_ROCKETLAUNCHER_SETTINGS_NAME = [f for f in os.listdir(ROOT + '\\RocketLauncher\\Settings') if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + f) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + f)]
ITEMS_ROCKETLAUNCHER_DIR_SETTINGS = list(set([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Settings\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file)]))
ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Settings\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_SETTINGS_NAME if os.path.isdir(ROOT + '\\RocketLauncher\\Settings\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Settings\\' + file) if file2.endswith('.ini')])) 
ITEMS_ROCKETLAUNCHER_DATA_NAME = list(set([file for file in os.listdir(ROOT + '\\RocketLauncher\\Data')])) 
ITEMS_ROCKETLAUNCHER_DIR_DATA = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\' + file) for file in os.listdir(ROOT + '\\RocketLauncher\\Data')])) 
ITEMS_ROCKETLAUNCHER_FILE_DATA_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')])) 
ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\Game Info\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')])) 
ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\History\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')])) 
ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\Language\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.ini')])) 
ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\Moves List\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.dat')])) 
ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Data\\Statistics\\', file2) for file in ITEMS_ROCKETLAUNCHER_DATA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Data\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Data\\' + file) if file2.endswith('.dat')])) 
ITEMS_ROCKETLAUNCHER_MEDIA_NAME = list(set([file for file in os.listdir(ROOT + '\\RocketLauncher\\Media')])) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file) for file in os.listdir(ROOT + '\\RocketLauncher\\Media')]))
ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME =  list(set([file2 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file)])) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM =  list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\', file2) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file) for file2 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file)])) 
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME =  list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2)])) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM =  list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2)])) 
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3)])) 
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_NAME_CONTENT_ROMNAME = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3)])) 
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_JPG = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.jpg')])) 
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_PNG = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_PDF = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.pdf')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_MP4 = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp4')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_MP3 = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp3')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_OGG = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ogg')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_WAV = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.wav')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_WMA = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.wma')]))
ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_TXT = list(set([file3 for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.txt')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_JPG = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.jpg')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_PNG = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_PDF = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.pdf')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_WMA = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.wma')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_WAV = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.wav')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_MP4 = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp4')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_MP3 = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp3')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_OGG = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ogg')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_TXT = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.txt')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_JPG = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.jpg')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_PNG = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.png')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MP3 = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp3')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_OGG = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.ogg')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_WAV = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.wav')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_WMA = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.wma')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MP4 = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mp4')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_AVI = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.avi')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MOV = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.mov')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_PDF = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.pdf')]))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_TXT = list(set([os.path.join(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_ROCKETLAUNCHER_MEDIA_NAME  for file2 in ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME if os.path.exists(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2) if os.path.isdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) for file4 in os.listdir(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3) if os.path.isfile(ROOT + '\\RocketLauncher\\Media\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.txt')]))
ITEMS_COLLECTION_FILE_BAT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.bat')]))
ITEMS_COLLECTION_FILE_CONTENT_BAT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\', file4) for file in ITEMS_COLLECTION_NAME if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) for file4 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2  + '\\' + file3) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3 + '\\' + file4) if file4.endswith('.bat')]))
ITEMS_EMULATORS_FILE_BAT = list(set([os.path.join(ROOT + '\\emulators\\' + file + '\\' + file2) for file in ITEMS_EMULATORS_NAME if os.path.exists(ROOT + '\\emulators\\' + file) for file2 in os.listdir(ROOT + '\\emulators\\' + file) if file2.endswith('.bat')]))

print(blue + '| Lendo informações dos arquivos de Settings no RetroFE...' + reset_color)

#SETTINGS_GERAL_SYSTEM = [ler_arquivos_TXT(linha) for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]
SETTINGS_RETORFE_INF_ROM = list(set([ler_arquivos_TXT_linhas(linha, 'list.path = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_GAMES_INCLUDE_TXT = list(set([ler_arquivos_TXT_linhas(linha, 'list.includeMissingItems = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_LIST_EXTENSIONS = list(set([ler_arquivos_TXT_linhas(linha, 'list.extensions = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_SORTED_ALPHABETICALLY = list(set([ler_arquivos_TXT_linhas(linha, 'list.menuSort = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_SEARCHED_ROM = list(set([ler_arquivos_TXT_linhas(linha, 'list.romHierarchy = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_SEARCHED_ROM_TRURIP = list(set([ler_arquivos_TXT_linhas(linha, 'list.truRIP = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_LAUCHER = list(set([ler_arquivos_TXT_linhas(linha, 'launcher = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_META_TYPE = list(set([ler_arquivos_TXT_linhas(linha, 'metadata.type = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_SCREENSHOT = list(set([ler_arquivos_TXT_linhas(linha, 'media.screenshot = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_SCREENTITLE = list(set([ler_arquivos_TXT_linhas(linha, 'media.screentitle = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_ARTWORK_BACK = list(set([ler_arquivos_TXT_linhas(linha, 'media.artwork_back = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_ARTWORK_FRONT = list(set([ler_arquivos_TXT_linhas(linha, 'media.artwork_front = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_MEDIUM_BACK = list(set([ler_arquivos_TXT_linhas(linha, 'media.medium_back = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_MEDIUM_FRONT = list(set([ler_arquivos_TXT_linhas(linha, 'media.medium_front = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_LOGO = list(set([ler_arquivos_TXT_linhas(linha, 'media.logo = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_LOGO2 = list(set([ler_arquivos_TXT_linhas(linha, 'media.logo2 = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_VIDEO = list(set([ler_arquivos_TXT_linhas(linha, 'media.video = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_DEVICE = list(set([ler_arquivos_TXT_linhas(linha, 'media.device = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_STORY = list(set([ler_arquivos_TXT_linhas(linha, 'media.story = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_STORY1 = list(set([ler_arquivos_TXT_linhas(linha, 'media.story1 = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BEZEL = list(set([ler_arquivos_TXT_linhas(linha, 'media.bezel = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BANNER = list(set([ler_arquivos_TXT_linhas(linha, 'media.banner = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_FANART = list(set([ler_arquivos_TXT_linhas(linha, 'media.fanart = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_COVER = list(set([ler_arquivos_TXT_linhas(linha, 'media.cover = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_COVER2 = list(set([ler_arquivos_TXT_linhas(linha, 'media.cover2 = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_FANARTLEFT = list(set([ler_arquivos_TXT_linhas(linha, 'media.fanartleft = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_FANARTSYS = list(set([ler_arquivos_TXT_linhas(linha, 'media.fanartsys = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_CONTROLLER = list(set([ler_arquivos_TXT_linhas(linha, 'media.controller = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_POINTER = list(set([ler_arquivos_TXT_linhas(linha, 'media.pointer = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_CHARACTER = list(set([ler_arquivos_TXT_linhas(linha, 'media.character = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_CHARACTER_A = list(set([ler_arquivos_TXT_linhas(linha, 'media.character_a = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_CHARACTER_B = list(set([ler_arquivos_TXT_linhas(linha, 'media.character_b = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_CHARACTER_C = list(set([ler_arquivos_TXT_linhas(linha, 'media.character_c = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BACKGROUND = list(set([ler_arquivos_TXT_linhas(linha, 'media.background = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BORDER = list(set([ler_arquivos_TXT_linhas(linha, 'media.Border = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BACKGROUND_SYSTEM = list(set([ler_arquivos_TXT_linhas(linha, 'media.backgroundsystem = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_COLOR = list(set([ler_arquivos_TXT_linhas(linha, 'media.color = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_COLOR_A = list(set([ler_arquivos_TXT_linhas(linha, 'media.color_a = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_COLOR_B = list(set([ler_arquivos_TXT_linhas(linha, 'media.color_b = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_CONSOLE = list(set([ler_arquivos_TXT_linhas(linha, 'media.console = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BACKGROUND_A = list(set([ler_arquivos_TXT_linhas(linha, 'media.background_a = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))
SETTINGS_RETORFE_BRAND = list(set([ler_arquivos_TXT_linhas(linha, 'media.brand = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))

print(blue + '| Lendo informações dos arquivos de Bat no RetroFE...' + reset_color)
SETTINGS_RETORFE_BRAND = list(set([ler_arquivos_TXT_linhas(linha, 'media.brand = ') for linha in ITEMS_COLLECTION_FILE_CONF if os.path.isfile(linha)]))



print(cyan + '*---------------------------------------------------------------*' + reset_color)
print(blue + '| Criando DataFrame com as inforações : ' + reset_color, yellow + DATA_MANEGER_DATA + 'DirSystem.csv' + reset_color)
s1=pd.Series(ITEMS_COLLECTION_NAME,name='ITEMS_COLLECTION_NAME')
s2=pd.Series(ITEMS_COLLECTION_DIR_NAME,name='ITEMS_COLLECTION_DIR_NAME')
s3=pd.Series(ITEMS_COLLECTION_DIR__CONTENT,name='ITEMS_COLLECTION_DIR__CONTENT')
s3=pd.Series(ITEMS_COLLECTION_NAME__CONTENT,name='ITEMS_COLLECTION_NAME__CONTENT')
s4=pd.Series(ITEMS_COLLECTION_FILE_CONF,name='ITEMS_COLLECTION_FILE_CONF')
s5=pd.Series(ITEMS_COLLECTION_FILE_SUB,name='ITEMS_COLLECTION_FILE_SUB')
s6=pd.Series(ITEMS_COLLECTION_FILE_TXT,name='ITEMS_COLLECTION_FILE_TXT')
s7=pd.Series(ITEMS_COLLECTION_FILE_PNG,name='ITEMS_COLLECTION_FILE_PNG')
s8=pd.Series(ITEMS_COLLECTION_FILE_JPG,name='ITEMS_COLLECTION_FILE_JPG')
s9=pd.Series(ITEMS_COLLECTION_FILE_MP4,name='ITEMS_COLLECTION_FILE_MP4')
s10=pd.Series(ITEMS_COLLECTION_FILE_MP3,name='ITEMS_COLLECTION_FILE_MP3')
s11=pd.Series(ITEMS_COLLECTION_FILE_AVI,name='ITEMS_COLLECTION_FILE_AVI')
s12=pd.Series(ITEMS_COLLECTION_FILE_OGG,name='ITEMS_COLLECTION_FILE_OGG')
s13=pd.Series(ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT,name='ITEMS_COLLECTION_NAME__CONTENT_IN_CONTENT')
s14=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_TXT,name='ITEMS_COLLECTION_FILE_CONTENT_TXT')
s15=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_PNG,name='ITEMS_COLLECTION_FILE_CONTENT_PNG')
s16=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_JPG,name='ITEMS_COLLECTION_FILE_CONTENT_JPG')
s17=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_MP4,name='ITEMS_COLLECTION_FILE_CONTENT_MP4')
s18=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_MP3,name='ITEMS_COLLECTION_FILE_CONTENT_MP3')
s19=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_OGG,name='ITEMS_COLLECTION_FILE_CONTENT_OGG')
s20=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_SUB,name='ITEMS_COLLECTION_FILE_CONTENT_SUB')
s21=pd.Series(ITEMS_EMULATORS_NAME,name='ITEMS_EMULATORS_NAME')
s22=pd.Series(ITEMS_EMULATORS_DIR_NAME,name='ITEMS_EMULATORS_DIR_NAME')
s23=pd.Series(ITEMS_EMULATORS_DIR__CONTENT,name='ITEMS_EMULATORS_DIR__CONTENT')
s24=pd.Series(ITEMS_EMULATORS_FILE_INI,name='ITEMS_EMULATORS_FILE_INI')
s25=pd.Series(ITEMS_EMULATORS_FILE_CFG,name='ITEMS_EMULATORS_FILE_CFG')
s26=pd.Series(ITEMS_EMULATORS_FILE_LPL,name='ITEMS_EMULATORS_FILE_LPL')
s27=pd.Series(ITEMS_EMULATORS_FILE_EXE,name='ITEMS_EMULATORS_FILE_EXE')
s28=pd.Series(ITEMS_LAUNCHERS_FILE_CFG,name='ITEMS_LAUNCHERS_FILE_CFG')
s29=pd.Series(ITEMS_LAYOUTS_NAME,name='ITEMS_LAYOUTS_NAME')
s30=pd.Series(ITEMS_LAYOUTS_DIR_NAME,name='ITEMS_LAYOUTS_DIR_NAME')
s31=pd.Series(ITEMS_LAYOUTS_FILE_XML,name='ITEMS_LAYOUTS_FILE_XML')
s32=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION,name='ITEMS_LAYOUTS_DIR_COLLECTION')
s33=pd.Series(ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT ,name='ITEMS_LAYOUTS_NAME_COLLECTION_CONTENT')
s34=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT ,name='ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT')
s35=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS ,name='ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS')
s36=pd.Series(ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT,name='ITEMS_LAYOUTS_DIR_COLLECTION_LAYOUTS_CONTENT')
s37=pd.Series(ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML,name='ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_XML')
s38=pd.Series(ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG,name='ITEMS_LAYOUTS_COLLECTION_CONTENT_THEMAS_FILE_PNG')
s39=pd.Series(ITEMS_META_NAME,name='ITEMS_META_NAME')
s40=pd.Series(ITEMS_META_DIR_NAME,name='ITEMS_META_DIR_NAME')
s41=pd.Series(ITEMS_META_FILE_XML,name='ITEMS_META_FILE_XML')
s42=pd.Series(ITEMS_ROCKETLAUNCHER_NAME ,name='ITEMS_ROCKETLAUNCHER_NAME')
s43=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_NAME,name='ITEMS_ROCKETLAUNCHER_DIR_NAME')
s44=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_CONTENT,name='ITEMS_ROCKETLAUNCHER_DIR_CONTENT')
s45=pd.Series(ITEMS_ROCKETLAUNCHER_SETTINGS_NAME,name='ITEMS_ROCKETLAUNCHER_SETTINGS_NAME')
s46=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_SETTINGS,name='ITEMS_ROCKETLAUNCHER_DIR_SETTINGS')
s47=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI,name='ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI')
s48=pd.Series(ITEMS_ROCKETLAUNCHER_DATA_NAME,name='ITEMS_ROCKETLAUNCHER_DATA_NAME')
s49=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_DATA,name='ITEMS_ROCKETLAUNCHER_DIR_DATA')
s50=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_DATA_INI,name='ITEMS_ROCKETLAUNCHER_FILE_DATA_INI')
s51=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI,name='ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI')
s52=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI,name='ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI')
s53=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI,name='ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI')
s54=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT,name='ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT')
s55=pd.Series(ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI,name='ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI')
s56=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_NAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_NAME')
s57=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA')
s58=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_SYSTEM_NAME')
s59=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_SYSTEM')
s60=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME')
s61=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM')
# ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM
s62=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME')
s63=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_NAME_CONTENT_ROMNAME,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_NAME_CONTENT_ROMNAME')
s64=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_JPG,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_JPG')
s65=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_PNG,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_PNG')
s66=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_PDF,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_PDF')
s67=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_MP4,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_MP4')
s68=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_MP3,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_MP3')
s69=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_OGG,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_OGG')
s70=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_WAV,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_WAV')
s71=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_WMA,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_WMA')
s72=pd.Series(ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_TXT,name='ITEMS_ROCKETLAUNCHER_MEDIA_ROM_NAME_CONTENT_ROMNAME_TXT')
s73=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_JPG,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_JPG')
s74=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_PNG,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_PNG')
s75=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_PDF,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_PDF')
s76=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_WMA,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_WMA')
s77=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_WAV,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_WAV')
s78=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_MP4,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_MP4')
s79=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_MP3,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_MP3')
s80=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_OGG,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_OGG')
s80=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_TXT,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_TXT')
s81=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_JPG,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_JPG')
s82=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_PNG,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_PNG')
s83=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MP3,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MP3')
s84=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_OGG,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_OGG')
s85=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_WAV,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_WAV')
s86=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_WMA,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_WMA')
s87=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MP4,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MP4')
s88=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_AVI,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_AVI')
s89=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MOV,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_MOV')
s90=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_PDF,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_PDF')
s91=pd.Series(ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_TXT,name='ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_TXT')
s92=pd.Series(ITEMS_COLLECTION_FILE_BAT,name='ITEMS_COLLECTION_FILE_BAT')
s93=pd.Series(ITEMS_COLLECTION_FILE_CONTENT_BAT,name='ITEMS_COLLECTION_FILE_CONTENT_BAT')
s94=pd.Series(ITEMS_EMULATORS_FILE_BAT,name='ITEMS_EMULATORS_FILE_BAT')

s95=pd.Series(SETTINGS_RETORFE_INF_ROM,name='SETTINGS_RETORFE_INF_ROM')
s96=pd.Series(SETTINGS_RETORFE_GAMES_INCLUDE_TXT,name='SETTINGS_RETORFE_GAMES_INCLUDE_TXT')
s97=pd.Series(SETTINGS_RETORFE_LIST_EXTENSIONS,name='SETTINGS_RETORFE_LIST_EXTENSIONS')
s98=pd.Series(SETTINGS_RETORFE_SORTED_ALPHABETICALLY,name='SETTINGS_RETORFE_SORTED_ALPHABETICALLY')
s99=pd.Series(SETTINGS_RETORFE_SEARCHED_ROM,name='SETTINGS_RETORFE_SEARCHED_ROM')
s100=pd.Series(SETTINGS_RETORFE_SEARCHED_ROM_TRURIP,name='SETTINGS_RETORFE_SEARCHED_ROM_TRURIP')
s101=pd.Series(SETTINGS_RETORFE_LAUCHER,name='SETTINGS_RETORFE_LAUCHER')
s102=pd.Series(SETTINGS_RETORFE_META_TYPE,name='SETTINGS_RETORFE_META_TYPE')
s103=pd.Series(SETTINGS_RETORFE_SCREENSHOT,name='SETTINGS_RETORFE_SCREENSHOT')
s104=pd.Series(SETTINGS_RETORFE_SCREENTITLE,name='SETTINGS_RETORFE_SCREENTITLE')
s105=pd.Series(SETTINGS_RETORFE_ARTWORK_BACK,name='SETTINGS_RETORFE_ARTWORK_BACK')
s106=pd.Series(SETTINGS_RETORFE_ARTWORK_FRONT,name='SETTINGS_RETORFE_ARTWORK_FRONT')
s107=pd.Series(SETTINGS_RETORFE_MEDIUM_BACK,name='SETTINGS_RETORFE_MEDIUM_BACK')
s108=pd.Series(SETTINGS_RETORFE_MEDIUM_FRONT,name='SETTINGS_RETORFE_MEDIUM_FRONT')
s109=pd.Series(SETTINGS_RETORFE_LOGO,name='SETTINGS_RETORFE_LOGO')
s110=pd.Series(SETTINGS_RETORFE_LOGO2,name='SETTINGS_RETORFE_LOGO2')
s111=pd.Series(SETTINGS_RETORFE_VIDEO,name='SETTINGS_RETORFE_VIDEO')
s112=pd.Series(SETTINGS_RETORFE_DEVICE,name='SETTINGS_RETORFE_DEVICE')

s113=pd.Series(SETTINGS_RETORFE_STORY,name='SETTINGS_RETORFE_STORY')
s114=pd.Series(SETTINGS_RETORFE_STORY1,name='SETTINGS_RETORFE_STORY1')
s115=pd.Series(SETTINGS_RETORFE_BEZEL,name='SETTINGS_RETORFE_BEZEL')
s116=pd.Series(SETTINGS_RETORFE_BANNER,name='SETTINGS_RETORFE_BANNER')
s117=pd.Series(SETTINGS_RETORFE_FANART,name='SETTINGS_RETORFE_FANART')
s118=pd.Series(SETTINGS_RETORFE_COVER,name='SETTINGS_RETORFE_COVER')
s119=pd.Series(SETTINGS_RETORFE_COVER2,name='SETTINGS_RETORFE_COVER2')
s120=pd.Series(SETTINGS_RETORFE_FANARTLEFT,name='SETTINGS_RETORFE_FANARTLEFT')
s121=pd.Series(SETTINGS_RETORFE_FANARTSYS,name='SETTINGS_RETORFE_FANARTSYS')
s122=pd.Series(SETTINGS_RETORFE_CONTROLLER,name='SETTINGS_RETORFE_CONTROLLER')
s123=pd.Series(SETTINGS_RETORFE_POINTER,name='SETTINGS_RETORFE_POINTER')
s124=pd.Series(SETTINGS_RETORFE_CHARACTER,name='SETTINGS_RETORFE_CHARACTER')
s125=pd.Series(SETTINGS_RETORFE_CHARACTER_A,name='SETTINGS_RETORFE_CHARACTER_A')
s126=pd.Series(SETTINGS_RETORFE_CHARACTER_B,name='SETTINGS_RETORFE_CHARACTER_B')
s127=pd.Series(SETTINGS_RETORFE_CHARACTER_C,name='SETTINGS_RETORFE_CHARACTER_C')
s128=pd.Series(SETTINGS_RETORFE_BACKGROUND,name='SETTINGS_RETORFE_BACKGROUND')
s129=pd.Series(SETTINGS_RETORFE_BORDER,name='SETTINGS_RETORFE_BORDER')
s130=pd.Series(SETTINGS_RETORFE_BACKGROUND_SYSTEM,name='SETTINGS_RETORFE_BACKGROUND_SYSTEM')
s131=pd.Series(SETTINGS_RETORFE_COLOR,name='SETTINGS_RETORFE_COLOR')
s132=pd.Series(SETTINGS_RETORFE_COLOR_A,name='SETTINGS_RETORFE_COLOR_A')
s133=pd.Series(SETTINGS_RETORFE_COLOR_B,name='SETTINGS_RETORFE_COLOR_B')
s134=pd.Series(SETTINGS_RETORFE_CONSOLE,name='SETTINGS_RETORFE_CONSOLE')
s135=pd.Series(SETTINGS_RETORFE_BACKGROUND_A,name='SETTINGS_RETORFE_BACKGROUND_A')
s136=pd.Series(SETTINGS_RETORFE_BRAND,name='SETTINGS_RETORFE_BRAND')

# --------- CONSTRUÇÃO DO DATAFRAME E ARQUIVO CSV ------------ #
# verificar se tem o arquivo DATA_MANEGER_DATA + 'DirSystem.csv' e deletar se tiver
print(cyan + '*---------------------------------------------------------------*' + reset_color)
print(blue + '| Manipulando aquivo para salvar CSV : ' + reset_color, yellow + DATA_MANEGER_DATA + 'DirSystem.csv' + reset_color)

if os.path.exists(DATA_MANEGER_DATA + 'DirSystem.csv'):
    os.remove(DATA_MANEGER_DATA + 'DirSystem.csv')
# salvar o arquivo CSV   
DirSystem_df = pd.concat([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s71,s72,s73,s74,s75,s76,s77,s78,s79,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89,s90,s91,s92,s93,s94,s95,s96,s97,s98,s99,s100,s101,s102,s103,s104,s105,s106,s107,s108,s109,s110,s111,s112,s113,s114,s115,s116,s117,s118,s119,s120,s121,s122,s123,s124,s125,s126,s127,s128,s129,s130,s131,s132,s133,s134,s135,s136], axis=1)
DirSystem_df.to_csv(DATA_MANEGER_DATA + 'DirSystem.csv', encoding='utf-8', sep=';', index=False)
print(blue + '|Processo de criação finalizado ' + reset_color, yellow + DATA_MANEGER_DATA + 'DirSystem.csv' + reset_color)
print(cyan + '*---------------------------------------------------------------*' + reset_color)
