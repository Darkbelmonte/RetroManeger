# Programa para limpar a estrutura do RetroFe
# Retirada de arquivos não uteis
# declarando libs
import os
import shutil
import shutil, tempfile
from shutil import move
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
import importlib.util

import sys
sys.path  #executar um script python de um diretório dentro de outro script que está em outro diretório?
# SCRIPT
MODULE_DIR_SYSTEM = 'core\\maneger\\Lib\\'
MODULE_DIR_SYSTEM_NAME = 'DirSystem.py'

spec = importlib.util.spec_from_file_location(MODULE_DIR_SYSTEM_NAME, MODULE_DIR_SYSTEM + MODULE_DIR_SYSTEM_NAME)
modulevar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulevar)
#modulevar.printingstatement()
#...

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



# ----------------- USO DO PANDAS ------------------ #
# _________   CRIAÇÃO DO DATAFRAME  ________________ #
# Pd de nomes errados x officiais
print(FILE_CSV_FIX_NAME_SYSTEM_TMP, 'tese do FILE_CSV_FIX_NAME_SYSTEM_TMP')
file_backup(FILE_CSV_FIX_NAME_SYSTEM)
df = pd.read_csv(FILE_CSV_FIX_NAME_SYSTEM_TMP, encoding='utf-8', sep=';')

df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))

# Diretórios
file_backup(FILE_CSV_DIRSYSTEM)
DirSystem_df = pd.read_csv(FILE_CSV_DIRSYSTEM_TMP, encoding='utf-8', sep=';', low_memory=False)

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_DIR_NAME'])
ITEMS_COLLECTION_DIR_NAME_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_DIR_NAME'].tolist()))
ITEMS_COLLECTION_DIR_NAME_TPM = list(OrderedDict.fromkeys(ITEMS_COLLECTION_DIR_NAME_TPM))
ITEMS_COLLECTION_DIR_NAME = [x for x in ITEMS_COLLECTION_DIR_NAME_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT'])
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_TPM = list(set(DirSystem_df['ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT'].tolist()))
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_TPM = list(OrderedDict.fromkeys(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_TPM))
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT = [x for x in ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_FILE_TXT'])
ITEMS_COLLECTION_FILE_TXT_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_TXT'].tolist()))
ITEMS_COLLECTION_FILE_TXT_TPM = list(OrderedDict.fromkeys(ITEMS_COLLECTION_FILE_TXT_TPM))
ITEMS_COLLECTION_FILE_TXT = [x for x in ITEMS_COLLECTION_FILE_TXT_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_FILE_SUB'])
ITEMS_COLLECTION_FILE_SUB_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_TXT'].tolist()))
ITEMS_COLLECTION_FILE_SUB_TPM = list(OrderedDict.fromkeys(ITEMS_COLLECTION_FILE_SUB_TPM))
ITEMS_COLLECTION_FILE_SUB = [x for x in ITEMS_COLLECTION_FILE_SUB_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_FILE_PNG'])
ITEMS_COLLECTION_FILE_PNG_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_TXT'].tolist()))
ITEMS_COLLECTION_FILE_PNG_TPM = list(OrderedDict.fromkeys(ITEMS_COLLECTION_FILE_PNG_TPM))
ITEMS_COLLECTION_FILE_PNG = [x for x in ITEMS_COLLECTION_FILE_PNG_TPM if x != 'nan']

DirSystem_df.dropna(subset=['ITEMS_COLLECTION_FILE_JPG'])
ITEMS_COLLECTION_FILE_JPG_TPM = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_TXT'].tolist()))
ITEMS_COLLECTION_FILE_JPG_TPM = list(OrderedDict.fromkeys(ITEMS_COLLECTION_FILE_JPG_TPM))
ITEMS_COLLECTION_FILE_JPG = [x for x in ITEMS_COLLECTION_FILE_JPG_TPM if x != 'nan']

def renameDir(caminho):
    for Path in caminho :
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
                                            print(f'folder index {indice} = {old_file}  >> name index = {official_indice} | {new_file}')
                                        except:
                                            pass
                                    #print((str(Path)), '>old',old_file , '>new', new_file)    
                                    if Path !=  old_file != new_file:
                                        print(f'Esta pasta = {Path} não parece ser um sistema valido')
    for file in caminho :
        if os.path.exists(str(file)) and os.path.isfile(file):
            Dir, Nome = os.path.split(file) 
            fileName, Ext = os.path.splitext(Nome)
            #print("Root part of '% s':" % Dir, Nome)
            #print("File part of '% s':" % fileName, Ext)

            for erroName, offialName in zip(df['wrong_name'], df['official_name']):
                if erroName == fileName != offialName:
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
                                            #if not os.path.exists(new_file):
                                            #    os.rename(old_file, new_file)
                                            #    print(f'folder index {indice} = {old_file}  >> name index = {official_indice} | {new_file}')
                                            if os.path.exists(new_file):
                                                move(old_file, new_file)
                                                print(f'folder index {indice} = {old_file}  >SOBREPONDO> name index = {official_indice} | {new_file}')
                                        except:
                                            pass
                                    print((str(Path)), '>old',old_file , '>new', new_file)    
                                    if file !=  old_file != new_file:
                                        print(f'Esta pasta = {file} não parece ser um sistema valido')
            





renameDir(ITEMS_COLLECTION_DIR_NAME)
renameDir(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT)
renameDir(ITEMS_COLLECTION_FILE_TXT)
renameDir(ITEMS_COLLECTION_FILE_SUB)
renameDir(ITEMS_COLLECTION_FILE_PNG)
renameDir(ITEMS_COLLECTION_FILE_JPG)

