# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np 
import shutil # copiar arquivos
import shutil, tempfile # carregar informações do CSV FILE_CSV_FIX_NAME_SYSTEM
from shutil import move # move arquivos
from operator import index
# ---------------------- DEFINIÇÃO DE CORES ---------------------- #
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
# este script é responsável por usar o nome __file__ para pegar o nome do arquivo e fazer a edição no arquivo settings.conf do diretório ROOT
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

DATA_MANEGER_DATA = ROOT + '\\core\\maneger\\' + 'Data\\'
FILE_CSV_DIRSYSTEM = ROOT + '\\core\\maneger\\Data\\DirSystem.csv'
FILE_CSV_DIRSYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\DirSystem_Tmp.csv'
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
# Diretórios

DirSystem_df = pd.read_csv(FILE_CSV_DIRSYSTEM, encoding='utf-8', sep=';', low_memory=False)

DirSystem_df.dropna(subset=['ITEMS_LAYOUTS_NAME'])
ITEMS_LAYOUTS_NAME_TPM = list(set(DirSystem_df['ITEMS_LAYOUTS_NAME'].tolist()))
ITEMS_LAYOUTS_NAME = [x for x in ITEMS_LAYOUTS_NAME_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_NAME__CONTENT'])
ITEMS_COLLECTION_NAME__CONTENT_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_NAME__CONTENT'].tolist()))
ITEMS_COLLECTION_NAME__CONTENT = [x for x in ITEMS_COLLECTION_NAME__CONTENT_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_DIR__CONTENT'])
ITEMS_COLLECTION_DIR__CONTENT_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_DIR__CONTENT'].tolist()))
ITEMS_COLLECTION_DIR__CONTENT = [x for x in ITEMS_COLLECTION_DIR__CONTENT_TPM if x != 'nan']

print(os.path.realpath(__file__))
print(ITEMS_COLLECTION_DIR__CONTENT)
