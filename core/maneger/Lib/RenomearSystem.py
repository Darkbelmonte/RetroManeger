# Programa para limpar a estrutura do RetroFe
# Retirada de arquivos não uteis
# declarando libs
import os
import shutil
import shutil, tempfile
from tqdm import tqdm
from tkinter import Label
from turtle import clear, goto
import pandas as pd  # para ler, visualizar e printar infos do df
import numpy as np
import itertools
from os import walk
import csv
import os.path
from pathlib import Path
from collections import OrderedDict


import sys
sys.path  #executar um script python de um diretório dentro de outro script que está em outro diretório?
#import <arquivo>
#import arquivo.py
#sys.insert(1, os.getcwd()) 

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
currentdir = os.getcwd()
VALIDAR_ROOT = [f for f in os.listdir(currentdir) if os.path.isdir(currentdir + '\\' + f) if f == 'core' ]
chck_root = __file__.split('\\')
contador = 0

try:
    while (chck_root[-contador] != 'core'):      
        ROOT = '\\'.join(chck_root[0:-((contador + 1))])
        contador   = contador + 1
        ROOT = ROOT
        print('Diretório ROOT :',  yellow +  (ROOT) + reset_color)
        print()

except ValueError as ex:
    print(ex, 'verifique o diretório Raiz da instalação do seu RetroFE')

# IndexError if the value is out of the list index...
except IndexError as ex:
    print(ex, 'erro de index')
print('Diretório ROOT Fix:',  yellow +  (ROOT) + reset_color)
print('Diretório atual', currentdir, 'vai ser alterado para :', ROOT)
# change the current working directory
# to specified path
#os.chdir('c:\\gfg_dir')
# initial directory
cwd = os.getcwd()
 
# some non existing directory
fd = ROOT + '\\'
os.chdir(ROOT + '\\')
# trying to insert to false directory
try:
    os.chdir(fd)
    print("Inserting inside-", os.getcwd())
     
# Caching the exception   
except:
    print("Something wrong with specified\
          directory. Exception- ", sys.exc_info())
           
# handling with finally         
finally:
    print("Restoring the path")
    os.chdir(cwd)
    print("Current directory is-", os.getcwd())
print('Agora o diretório de trabalho é o ', currentdir, ', pois foi alterado :', ROOT)

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

# ----------------- USO DO PANDAS ------------------ #
# _________   CRIAÇÃO DO DATAFRAME  ________________ #
# Pd de nomes errados x officiais
file_backup(FILE_CSV_FIX_NAME_SYSTEM)
df = pd.read_csv(FILE_CSV_FIX_NAME_SYSTEM_TMP, encoding='latin-1', sep=';')

df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))

# Diretórios
file_backup(FILE_CSV_DIRSYSTEM)
DirSystem_df = pd.read_csv(FILE_CSV_DIRSYSTEM_TMP, encoding='latin-1', sep=';')

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_DIR_NAME'])
DirSystem_df.dropna(subset=['ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT'])
ITEMS_COLLECTION_DIR_NAME = list(set(DirSystem_df['ITEMS_COLLECTION_DIR_NAME'].tolist()))
ITEMS_COLLECTION_DIR_NAME = list(OrderedDict.fromkeys(ITEMS_COLLECTION_DIR_NAME))
ITEMS_COLLECTION_DIR_NAME = [x for x in ITEMS_COLLECTION_DIR_NAME if x != 'nan']
#ITEMS_COLLECTION_DIR_NAME = ITEMS_COLLECTION_DIR_NAME_FIX


ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT = list(set(DirSystem_df['ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT'].tolist()))
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_FIX = [x for x in ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT if x != 'nan']



#print(ITEMS_COLLECTION_DIR_NAME, 'ITEMS_COLLECTION_DIR_NAME')
#print(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_FIX, 'ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_FIX')

# -----------------   FUNÇÃO   ------------------ #
# ________   RENAME GENERICO COM REPLCE  ________ #

files = []
path = ITEMS_COLLECTION_DIR_NAME
for caminho in ITEMS_COLLECTION_DIR_NAME:
    print(caminho, 'caminho 0')
    for (dirpath, dirnames, filenames) in walk(str(caminho)):
        print(dirpath, 'A')
        print(dirnames, 'B')
        print(filenames, 'C')
        files.extend(filenames)
    break
print(files)


#renamefoldes(ITEMS_COLLECTION_DIR_NAME_FIX)
#renamefoldes(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_FIX)
