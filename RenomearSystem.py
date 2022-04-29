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
from datetime import date
from datetime import datetime
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
# limpar terminal antes de executar 
print("\n" * os.get_terminal_size().lines)
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
# ------------    OUTROS PROCESSOS   ---------------- #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #
import sys
sys.path  #executar um script python de um diretório dentro de outro script que está em outro diretório?
# SCRIPT
MODULE_DIR_SYSTEM = 'core\\maneger\\Lib\\'
MODULE_DIR_SYSTEM_NAME = 'DirSystem.py'
MODULE_DIR_RENAME_SYSTEM_MANUAL = ROOT + '\\meta\\rename\\'
# ------------    OUTROS PROCESSOS   ---------------- #

spec = importlib.util.spec_from_file_location(MODULE_DIR_SYSTEM_NAME, MODULE_DIR_SYSTEM + MODULE_DIR_SYSTEM_NAME)
modulevar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulevar)
#modulevar.printingstatement()
#...

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

file_backup(FILE_CSV_SETTINGS)
settings_df = pd.read_csv(FILE_CSV_SETTINGS_TMP, encoding='utf-8', sep=';')
settings_midia_name = settings_df['MIDIA_VARIABLE'].tolist()
# Diretórios

INSTALLED_SYSTEMS = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\') if not f in ['Main','_common']]
ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
ITEMS_COLLECTION_DIR_NAME = list(set([os.path.join(ROOT + '\\collections\\', file) for file in os.listdir(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\' + file)]))
ITEMS_COLLECTION_NAME__CONTENT = list(set([(file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if os.path.isdir(ROOT + '\\collections\\' + file + '\\' + file2)]))
ITEMS_COLLECTION_FILE_CONF = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.conf')]))
ITEMS_COLLECTION_FILE_SUB = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.sub')]))
ITEMS_COLLECTION_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.txt')]))
ITEMS_COLLECTION_FILE_PNG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.png')]))
ITEMS_COLLECTION_FILE_JPG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.jpg')]))
ITEMS_COLLECTION_FILE_MP4 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.mp4')]))
ITEMS_COLLECTION_FILE_MP3 = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.mp3')]))
ITEMS_COLLECTION_FILE_AVI = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.avi')]))
ITEMS_COLLECTION_FILE_OGG = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.ogg')])) 
ITEMS_COLLECTION_FILE_ICO = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2 + '\\', file3) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in ITEMS_COLLECTION_NAME__CONTENT if os.path.exists(ROOT + '\\collections\\' + file + '\\' + file2) for file3 in os.listdir(ROOT + '\\collections\\' + file + '\\' + file2) if os.path.isfile(ROOT + '\\collections\\' + file + '\\' + file2 + '\\' + file3) if file3.endswith('.ico')]))
TEMS_LAYOUTS_DIR_COLLECTION_CONTENT = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections\\' + file2 + '\\', file3) for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') for file2 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections') if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) for file3 in os.listdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2) if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections\\' + file2)])) 
ITEMS_META_NAME = [f for f in os.listdir(ROOT + '\\meta\\') if os.path.exists(ROOT + '\\meta\\') if os.path.isdir(ROOT + '\\meta\\')]
ITEMS_META_FILE_XML = list(set([os.path.join(ROOT + '\\meta\\' + file + '\\', file2) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file) for file2 in os.listdir(ROOT + '\\meta\\' + file) if file2.endswith('.xml')]))
EMPTY = []
print(red + 'DATA ATUAL :' + reset_color, yellow +  DATA_HORA_ATUAIS_FORMATADO_HORA + reset_color)
# !-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÃO DE RENOMEAR OS SISTEMAS
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
 # !-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÃO DE RENOMEAR OS SISTEMAS
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
                                    #print((str(Path)), '>old',old_file , '>new', new_file)    
                                    if Path !=  old_file != new_file:
                                        print(f'Esta pasta = {Path} não parece ser um sistema valido')
    for file in caminho :
        if os.path.exists(str(file)) and os.path.isfile(file):
            Dir, Nome = os.path.split(file) 
            fileName, Ext = os.path.splitext(Nome)
            #print("Root part of '% s':" % Dir, Nome)
            #print("File part of '% s':" % fileName, Ext)

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
# --------   LISTA E CRIA PASTAS DE MIDIA    -------- #
#    ESTRUTURA FAKE PARA CRIAR PASTAS E LISTAR        #
def list_End_make_media_Settings(NomeDoSystema):
    if type(NomeDoSystema) == list:
        for System_Name in NomeDoSystema:
            lts_Edit_media_settings = []
            for media_settings in settings_midia_name:
                Edit_media_settings = media_settings.replace('media.', '').lstrip()
                lts_Edit_media_settings.append(Edit_media_settings)
                Excluir_media_settings = ['meda.<filetype>','None','<filetype>','list.includeMissingItems','list.extensions','list.menuSort','list.romHierarchy','list.truRIP','launcher','metadata.type']
                tmpw = np.array(lts_Edit_media_settings)
                tmpz = np.array(Excluir_media_settings)
                Manter_Midias = list(set(np.setdiff1d(tmpw, tmpz)))
                Manter_Midias = [i for i in Manter_Midias if i]

                for midia in Manter_Midias:
                    if str(System_Name) != 'Main' :  
                        if str(System_Name) != '_common':
                            if str(System_Name) != 'None':
                                if midia != 'list.path':

                                    Fake_FolderMidia = ROOT + '\\collections\\' + System_Name + '\\medium_artwork\\' + str(midia)

                                    if not os.path.exists(str(Fake_FolderMidia)):
                                        os.makedirs(Fake_FolderMidia)
                                        print(f'Criando Pasta {Fake_FolderMidia}') 
                                    if os.path.exists(str(Fake_FolderMidia)):
                                        pass
                                    else :
                                        print(f'Pasta {Fake_FolderMidia} não existe')
    elif type(NomeDoSystema) != list:                    
        lts_Edit_media_settings = []
        for media_settings in settings_midia_name:
            Edit_media_settings = media_settings.replace('media.', '').lstrip()
            lts_Edit_media_settings.append(Edit_media_settings)
            Excluir_media_settings = ['meda.<filetype>','None','<filetype>','list.includeMissingItems','list.extensions','list.menuSort','list.romHierarchy','list.truRIP','launcher','metadata.type']
            tmpw = np.array(lts_Edit_media_settings)
            tmpz = np.array(Excluir_media_settings)
            Manter_Midias = list(set(np.setdiff1d(tmpw, tmpz)))
            Manter_Midias = [i for i in Manter_Midias if i]

            for midia in Manter_Midias:
                if str(NomeDoSystema) != 'Main' :  
                    if str(NomeDoSystema) != '_common':
                        if str(NomeDoSystema) != 'None':
                            if midia != 'list.path':

                                Fake_FolderMidia = ROOT + '\\collections\\' + NomeDoSystema + '\\medium_artwork\\' + str(midia)

                                if not os.path.exists(str(Fake_FolderMidia)):
                                    os.makedirs(Fake_FolderMidia)
                                    print(f'Criando Pasta {Fake_FolderMidia}') 
                                if os.path.exists(str(Fake_FolderMidia)):
                                    pass
                                else :
                                    print(f'Pasta {Fake_FolderMidia} não existe')                   
    return Manter_Midias    
# --------   BACKUP - PASTAS VAZIAS    -------- #
# RETIRAR TODAS AS PASTAS VAZIAS DO DIRETÓRIO   #
def Backup_EmptyFolders():
    for root, dirs, files in os.walk(ROOT): 
        if not len(dirs) and not len(files): 
            EMPTY.append(root) 

    for emptydir in EMPTY:
        emptybackupDir = str(emptydir).replace(ROOT, BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO) 
        try:
            shutil.move(emptydir, emptybackupDir, copy_function=emptybackupDir)
            print(f'folder {emptydir}  >Fazendo Back_Up de Pasta Vazia> name = {emptybackupDir}')
        except OSError as error:
            print('remover vazia para backup -> ', error)
        pass    
# !-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ! ----------------------------------------------------------------------------------------------------- ! #
# ---------   CAMINHOS CONTIDOS NO SETTINGS    ---------- #
# RETORNAR OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE #
#global RETURN_LINE
def get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, TYPE_FILE_TXT):
    global RETURN_LINE    
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
                                RETURN_LINE = RETURN_LINE
                            elif not str(ROOT + '\\') in str(RETURN_LINE):
                                RETURN_LINE = ROOT + '\\' + RETURN_LINE[0]   
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




# !-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




renameDir(ITEMS_COLLECTION_DIR_NAME)
renameDir(ITEMS_COLLECTION_FILE_TXT)
renameDir(ITEMS_COLLECTION_FILE_SUB)
renameDir(ITEMS_COLLECTION_FILE_PNG)
renameDir(ITEMS_COLLECTION_FILE_JPG)
renameDir(ITEMS_COLLECTION_FILE_ICO)
renameDir(ITEMS_COLLECTION_FILE_CONF)
renameDir(ITEMS_COLLECTION_FILE_MP4)
renameDir(ITEMS_COLLECTION_FILE_AVI)
renameDir(ITEMS_COLLECTION_FILE_OGG)
renameDir(ITEMS_COLLECTION_FILE_MP3)

renameDir(TEMS_LAYOUTS_DIR_COLLECTION_CONTENT)
renameDir(ITEMS_LAYOUTS_DIR_COLLECTION_CONTENT_THEMAS)
renameDir(ITEMS_META_FILE_XML)




# ! ----------------------------------------------------------------------------------------------------- ! #
# Renomear ROMS com base no arquivo CSV 'Fix_System_Name'#
for System_Name in INSTALLED_SYSTEMS:
    RETURN_MEDIA_NAME = sorted(list(set(list_End_make_media_Settings(System_Name))))
    for Search_Texto in RETURN_MEDIA_NAME:
        if Search_Texto != '' and os.path.exists(get_caminhos_settings(System_Name, Search_Texto, 'settings.conf')) and os.listdir(get_caminhos_settings(System_Name,Search_Texto, 'settings.conf')) != []:

            SYSTEM_NAME_TMP = MODULE_DIR_RENAME_SYSTEM_MANUAL + 'Fix_' + System_Name + '.csv'
            print(SYSTEM_NAME_TMP, '<<<<<< SYSTEM_NAME_TMP')
            if os.path.exists(get_caminhos_settings(System_Name, 'list.path', 'settings.conf')) and os.path.exists(SYSTEM_NAME_TMP) and os.listdir(get_caminhos_settings(System_Name, 'list.path', 'settings.conf')) != [] and os.listdir(get_caminhos_settings(System_Name, 'list.path', 'settings.conf')) != None:
                print(SYSTEM_NAME_TMP, '<<<<<< SYSTEM_NAME_TMP 222222222')
                ROM_DIR = (get_caminhos_settings(System_Name,'list.path', 'settings.conf'))
                MEDIA_DIR = (get_caminhos_settings(System_Name, Search_Texto, 'settings.conf'))
                
                System_Name_ROM_df = pd.read_csv(SYSTEM_NAME_TMP, encoding='utf-8', sep=';', header=None)
                rom_wrong_name = list(set(System_Name_ROM_df['rom_wrong_name'].tolist()))
                rom_official_name = list(set(System_Name_ROM_df['rom_official_name'].tolist()))

                renameDirRom(ROM_DIR, rom_wrong_name, rom_official_name)
                renameDirRom(MEDIA_DIR, rom_wrong_name, rom_official_name)
Backup_EmptyFolders()
        