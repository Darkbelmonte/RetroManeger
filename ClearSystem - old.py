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
import itertools
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
BEFORE_DIR = ((os.path.dirname(os.path.realpath(__file__))).split('\\', -1)[-2]) + '\\'
BACKUP_DIR = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup'
BACKUP_DIR_ROM = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup' + '\\Roms'
DATA_ATUAL = date.today()
DATA_HORA_ATUAIS = datetime.now()
DATA_HORA_ATUAIS_FORMATADO = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H-%M')
DATA_HORA_ATUAIS_FORMATADO_HORA = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H') + 'h'
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

# -----------------    CAMINHOS   ------------------ #
# _________     CRIAÇÃO DO DATAFRAME    ____________ #
# Pd de nomes errados x officiais
file_backup(FILE_CSV_FIX_NAME_SYSTEM)
df = pd.read_csv(FILE_CSV_FIX_NAME_SYSTEM_TMP, encoding='utf-8', sep=';')

file_backup(FILE_CSV_FIX_NAME_CLEAN)
clean_df = pd.read_csv(FILE_CSV_FIX_NAME_CLEAN_TMP, encoding='utf-8', sep=';')

df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))

dirclean = clean_df['dirclean'].tolist()
limpar = clean_df['clean'].tolist()
emulador = clean_df['emulador'].tolist()
categoria = clean_df['categoria'].tolist()

# --------          BACKUP - CRIAÇÃO DA PASTA            -------- #
#     AVALIA E CONSTROI A ESTRUTURA DE BACKUP  E FAZ O BACKUP     #
def Backup_default(caminhos):
    #print(type(caminhos), 'type')
    if type(caminhos) == list:
        print('Vejo que temos uma lista de sistemas, vamos lá !!')
        for caminho in caminhos:
            # aqui ele segue se for um arquivo
            if os.path.isfile(str(caminho)) and os.path.exists(str(caminho)):
                # ajustando nomes 
                if str(ROOT + '\\') in str(caminho):
                    dir_tmp, arquivo = os.path.split(caminho) 
                    dir_tmp = dir_tmp.replace(ROOT + '\\', '')
                # criando pasta e removendo arquivo
                    if os.path.exists(str(dir_tmp)):    
                        old_end = str(caminho)
                        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\'
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                        pass

                if not str(ROOT + '\\') in str(caminho):
                    dir_tmp, arquivo = os.path.split(caminho)
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho)                    
                        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\'
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                        pass
            # aqui ele segue se for uma pasta
            if os.path.isdir(str(caminho)) and os.path.exists(str(caminho)):
                # ajustando nomes 
                if str(ROOT) in caminho:
                    dir_tmp = str(caminho).replace(ROOT + '\\', '')
                    dir_tmp = dir_tmp.split('\\', 0)[-1]
                    #print(dir_tmp, 'dir_tmp linha 171')
                # criando pasta e removendo arquivo                
                    if os.path.isdir(str(dir_tmp)) and os.path.exists(str(dir_tmp)):    
                        old_end = str(caminho)                          
                        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                        pass

                if not str(ROOT) in caminho:
                    #dir_tmp = str(caminho).split('\\', 0)[-1]
                    dir_tmp = str(caminho)
                    #print(dir_tmp, 'dir_tmp linha 189')
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho) 
                        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp

                        print(old_end, 'old_end linha 194')
                        print(new_end, 'new_end linha 195')
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                        pass

            elif not os.path.exists(str(caminho)):
                print(' O Diretório que você quer mudar os arquivos não existe, verifique se há algum erro !!')
        else:
            print('Não temos nada para alterar aqui !!')

    elif type(caminhos) != list:
        print('O caminho que você passou não é uma lista, vamos  !!')
        # aqui ele segue se for um arquivo
        if os.path.isfile(caminhos) and os.path.exists(caminhos):
            # ajustando nomes 
            if str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos) 
                dir_tmp = dir_tmp.replace(ROOT + '\\', '')
            # criando pasta e removendo arquivo
                if os.path.exists(str(dir_tmp)):    
                    old_end = str(caminhos)
                    new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                    except IOError:
                        move(old_end, new_end)
                        print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                    pass

            if not str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos)
                if os.path.exists(str(dir_tmp)):                         
                    old_end = str(caminhos)                    
                    new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                    except IOError:
                        move(old_end, new_end)
                        print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                    pass
        # aqui ele segue se for uma pasta
        if os.path.isdir(str(caminhos)) and os.path.exists(str(caminhos)):
            # ajustando nomes 
            if str(ROOT + '\\') in str(caminhos):
                dir_tmp = str(caminhos).replace(ROOT + '\\', '')
                dir_tmp = dir_tmp.split('\\', 0)[-1]
                #print(dir_tmp, 'dir_tmp linha 171')
            # criando pasta e removendo arquivo                
                if os.path.isdir(str(dir_tmp)) and os.path.exists(str(dir_tmp)):    
                    old_end = str(caminhos)                          
                    new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                    except IOError:
                        move(old_end, new_end)
                        print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                    pass

            if not str(ROOT + '\\') in str(caminhos):
                dir_tmp = str(caminhos).split('\\', 0)[-1]
                if os.path.exists(str(dir_tmp)):                         
                    old_end = str(caminhos) 
                    new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
                    except IOError:
                        move(old_end, new_end)
                        print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
                    pass

        if not os.path.exists(caminhos):
            print(' O Diretório que você quer mudar :', caminhos ,' os arquivos não existe, verifique se há algum erro !!')
    else:
        print('Não temos nada para alterar aqui !!')


            
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
# -----------------   MAQUINA DE ESTADOS    ------------------ #
# __        busca linha por linha de um dado arquivo        __ #
def pesquisar_registro( AQUIVO, TEXTO_NOVO, TEXTO_ANTIGO ):
    with open(AQUIVO,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if TEXTO_ANTIGO in line:
                f.write(TEXTO_NOVO)
        f.truncate()

# -----------------   MAQUINA DE ESTADOS    ------------------ #
# __        busca linha por linha de um dado arquivo        __ #
def criar_settings( AQUIVO, TEXTO_NOVO, TEXTO_ANTIGO ):
    with open(AQUIVO,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if TEXTO_ANTIGO in line:
                f.write(TEXTO_NOVO)
        f.truncate()

# --------   CORREÇÃO DE NOMES NÃO VALIDOS  --------  #
# CORREÇÃO DOS PADRÃO DE NOMES DO RETROFE NO SETTINGS #
def ConverterNomes(linhadotexto, systema, termo):
    #print(linhadotexto, systema, termo ,'AA')
    if not os.path.exists(linhadotexto) and '%RETROFE_PATH%' in linhadotexto:
        linhadotexto = '%RETROFE_PATH%'.replace('%RETROFE_PATH%', ROOT)
    if not os.path.exists(linhadotexto) and '%BASE_MEDIA_PATH%' in linhadotexto:
        linhadotexto = '%BASE_MEDIA_PATH%'.replace('%BASE_MEDIA_PATH%', ROOT + '\\collections\\' + systema + '\\medium_artwork\\')
    if not os.path.exists(linhadotexto) and '%ITEM_COLLECTION_NAME%' in linhadotexto:
        linhadotexto = '%ITEM_COLLECTION_NAME%'.replace('%ITEM_COLLECTION_NAME%', systema)
    if not os.path.exists(linhadotexto) and '%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms' in linhadotexto:
        linhadotexto = '%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms'.replace('%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms', ROOT + '\\collections\\' + systema + '\\roms' )
    if not os.path.exists(linhadotexto) and '%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/' in linhadotexto:
        linhadotexto = '%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/'.replace('%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/', ROOT + '\\collections\\' + systema + '\\' )
    if not os.path.exists(linhadotexto) and '%BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/' in linhadotexto:
        linhadotexto = '%BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/'.replace('%BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/', ROOT + '\\collections\\' + systema + '\\medium_artwork\\')
    if not os.path.exists(linhadotexto) and '%BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/' + str(termo) in linhadotexto:
        linhadotexto = '%BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/' + str(termo).replace('%BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/' + str(termo), ROOT + '\\collections\\' + systema + '\\medium_artwork\\' + str(termo))
    elif os.path.exists(linhadotexto):
        linhadotexto = linhadotexto 
    #print(linhadotexto, systema, termo ,'BB')
    return linhadotexto

# --------   BACKUP - NOMES NÃO CONHECIDOS    -------- #
# RETIRAR TODAS AS PASTAS QUE NÃO TEM NOME RECONHECIDO #
lst_Nomes_Dos_Caminhos = []
def Backup_OutOftheSystema(list_caminhos):
    # Retirando nomes errados em collection list_unofficial
    for itens_existentes in list_caminhos:
        # separando nome do caminho
        Caminho, Nome_Caminho = os.path.split(itens_existentes)
        lst_Nomes_Dos_Caminhos.append(Nome_Caminho)
        # criando lista de nomes a serém ignorados
        nome_errado = list(set(df['wrong_name'].tolist()))
        nome_oficial = list(set(df['official_name'].tolist()))
        juntar_lst_ignorar = nome_errado + nome_oficial 
        # verificando se o nome do arquivo existe na lista de nomes a serão ignorados
        tmpw = np.array(lst_Nomes_Dos_Caminhos)
        tmpz = np.array(juntar_lst_ignorar)
        lst_final_remove = list(set(np.setdiff1d(tmpw, tmpz)))
        # adicionando caminho ao item a ser removido do sistema
        Dir_lst_final_remove = [Caminho + '\\' + nome for nome in lst_final_remove]        
        # removendo nomes não officiais 
        for nome_remove in Dir_lst_final_remove:
        # montando nome com o camiho e nome do arquivo
            Dir, nome = os.path.split(str(nome_remove))
            new_tmp_end = Dir.replace(ROOT, (BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO))
            new_end = os.path.join(new_tmp_end, nome)
            try:
                os.makedirs(new_end)
                shutil.move(nome_remove, new_end, copy_function=new_end)
                print(f'folder {nome_remove}  >Fazendo Back_Up> Unofficialname = {new_end}')
            except IOError:
                move(nome_remove, new_end)
                print(f'folder {nome_remove}  >Forçando Back_Up> Unofficialname = {new_end}')                
            pass

# ---------   CAMINHOS CONTIDOS NO SETTINGS    ---------- #
# RETORNAR OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE #

RETURN_SETTING = []
def Texto_InSettings(NomeDoSystema, texto, tipoArquivo):
    dir_pre_system, nome_system = os.path.split(NomeDoSystema)   # separando nome do systema
    INF_SETTINGS = ROOT + '\\collections\\' + nome_system + '\\' + tipoArquivo
    # print(NomeDoSystema, '>', tipoArquivo, '>', INF_SETTINGS)
    # Ajustar os nomes D:\RetroFE\%BASE_ITEM_PATH%\%ITEM_COLLECTION_NAME%\roms
    # pesquisar_registro(str(INF_SETTINGS), '%BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%', str(ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\') )
    if os.path.isfile(str(INF_SETTINGS)) == True:
        if tipoArquivo == 'settings.conf':
            try:
                arquivo = open(str(INF_SETTINGS), 'r')
                for linha in arquivo:
                    if linha == "":
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\' + str(texto).replace('=', '').lstrip()
                    if '#' + texto in linha:
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\' + str(texto).replace('=', '').lstrip()
                    if '# ' + texto in linha:
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\' + str(texto).replace('=', '').lstrip()
                    if '# media.' + str(texto).replace('# media.', '') in linha:
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\' + str(texto).replace('=', '').lstrip()
                        print('teste <<<<<<<<<<<< # media. >>>', '# media.' + str(texto).replace('# media.', ''))
                    if texto + '= %ITEM_COLLECTION_NAME%' in linha:
                        LINHA_SETTINGS_LST = nome_system + str(texto).replace('=', '').lstrip()
                    if texto + '= %BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms' in linha:
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\roms'
                    if texto == 'list.extensions' and 'list.extensions' in linha: 
                        LINHA_SETTINGS_LST = (linha.split('=')[1].replace('\n', '').lstrip()).replace(' ', '|')
                    #if not texto in linha:
                        #print(f'{texto} não encontrado em {INF_SETTINGS} tentando novamente com diretório Default')
                    #    LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system
                    elif texto in linha :
                        LINHA_SETTINGS_LST = ROOT + '\\' + linha.split('=')[1].replace('\n', '').lstrip() 
            except IOError:
                print('Erro ao ler arquivo de settings')
            finally:
                arquivo.close()

        if tipoArquivo == 'exclude.txt' or tipoArquivo == 'include.txt' or tipoArquivo == 'menu.txt':
            try:
                arquivo = open(str(INF_SETTINGS), 'r')
                LINHA_SETTINGS_TMP = arquivo.readlines()
                LINHA_SETTINGS_TMP = [LINHA_SETTINGS_TMP[i].replace('\n', '') for i in range(len(LINHA_SETTINGS_TMP))]
                LINHA_SETTINGS_LST = LINHA_SETTINGS_TMP[0:-1]
            except IOError:
                print('Erro ao ler arquivo de settings')
            finally:
                arquivo.close()
    else:   
        return 'Não existe arquivo de settings'
    return LINHA_SETTINGS_LST

# ---------   LIMPAR ARQUIVOS PRE DEFINIDOS    ---------- #
#             LIMPAR ARQUIVOS DESNECESSÁRIOS              #
def clean_list():
    for dirremove, remove, emul, systema in zip(dirclean, limpar, emulador, categoria):
        Backup_default(str(dirremove))

# ---------   LER ARQUIVO XML    ---------- #
# ---- BUSCAR NOMES DAS ROMS NO ARQUIVO --- #
def Retorne_ROM_do_XML(NomeDoArquivoSistemaXML):
# Coletar nomes das ROMs e informações adicionais do sistema no arquivo XML 
    systemXML = os.path.join(ROOT + '\\meta\\hyperlist\\', str(NomeDoArquivoSistemaXML) + '.xml')
    #print(ITEMS_META_FILE_XML)
    for systemXMLReal in ITEMS_META_FILE_XML:
        if systemXML == systemXMLReal:
            for systemNameInstalado in ITEMS_COLLECTION_NAME:
                Dir, FileXml = os.path.split(systemXML)
                FileXmlnoExt, ext = os.path.splitext(FileXml)
                if FileXmlnoExt == systemNameInstalado:
                    tree = ET.parse(systemXML)
                    root = tree.getroot()
                    categorias = list(set([elem.tag for elem in root.iter()]))
                    ROMS_XML_LIST = [game.attrib['name'] for game in root.findall("./game")]
            return ROMS_XML_LIST

# ----------------------------------------------------------------------------- #
# localizar quais ROMS estão no XML e quais estão no Dir do SETTINGS e remover
# as não officiais #
# Retorne_ROM_do_XML(NomeDoArquivoSistemaXML)
# 1 - verificar se existe XML do sistema
# 2 - Localizar o diretório das ROMS e verificar se existe o arquivo EXT 
# 3 - Pegar nomes no arquivo exclude e include e verificar se existe na lista
# 4 - Verificar se existe na lista de ROMS do XML e remover as que forem diferentes 
# 5 - realizar o backup das ROMS que não estão no XML

listRomExclude = []
listRomInclude = []
LIST_DIR_REMOVE_ROMS = []
def listar_itens_XMLCheckup_remove(NomeDoSystema, critério):
    if critério == 'list.path':
        INF_CRITÉRIO = 'ROMs'
    elif critério == 'media.' + str(critério).replace('media.', ''):
        INF_CRITÉRIO = str(critério).replace('media.', '')
        critério = 'media.' + str(critério).replace('media.', '')
    #print(INF_CRITÉRIO,  '!? INF_CRITÉRIO !?')
    INF_SETTINGS = ROOT + '\\collections\\' + NomeDoSystema + '\\' + 'settings.conf'
    # SE O SETTINGS ESTIVER COM ERRO, RETORNAR
    if os.path.isfile(str(INF_SETTINGS)) == True and os.path.getsize(str(INF_SETTINGS)) == 0:
        buffer = StringIO()
        with open(str(INF_SETTINGS), 'a') as stream:
            for index, line in enumerate(stream):
                # index == 1 representa a segunda linha do arquivo:
                buffer.write('# list.path = %BASE_ITEM_PATH%/%ITEM_COLLECTION_NAME%/roms\n' if index == 1 else line)
                buffer.write('list.includeMissingItems = true\n' if index == 2 else line)
                buffer.write('list.extensions = 7z,zip\n' if index == 3 else line)
                buffer.write('list.menuSort = true\n' if index == 4 else line)
                buffer.write('launcher = rocketlauncher\n' if index == 5 else line)
                buffer.write('# media.screenshot    = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/screenshot\n' if index == 6 else line)
                buffer.write('# media.screentitle   = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/screentitle\n' if index == 7 else line)
                buffer.write('# media.artwork_back  = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/artwork_back\n' if index == 8 else line)
                buffer.write('# media.artwork_front = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/artwork_front\n' if index == 9 else line)
                buffer.write('# media.logo          = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/logo\n' if index == 10 else line)
                buffer.write('# media.medium_back   = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/medium_back\n' if index == 11 else line)
                buffer.write('# media.medium_front  = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/medium_front\n' if index == 12 else line)
                buffer.write('# media.screenshot    = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/screenshot\n' if index == 13 else line)
                buffer.write('# media.screentitle   = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/screentitle\n' if index == 14 else line)
                buffer.write('# media.video         = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/video\n' if index == 15 else line)
                buffer.write('# media.cover         = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/cover\n' if index == 16 else line)
                buffer.write('# media.bezel         = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/bezel\n' if index == 17 else line)
                buffer.write('# media.banner        = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/banner\n' if index == 18 else line)
                buffer.write('# media.artwork_3d    = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/artwork_3d\n' if index == 19 else line)
                buffer.write('# media.story         = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/story\n' if index == 20 else line)
                buffer.write('# media.fanart        = %BASE_MEDIA_PATH%/%ITEM_COLLECTION_NAME%/medium_artwork/fanart\n' if index == 21 else line)
        with open(str(INF_SETTINGS), 'w') as stream:
            stream.write(buffer.getvalue())
            buffer.close()
            REAL_ROM = [os.path.splitext(f)[0] for f in os.listdir(str(ConverterNomes(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'), NomeDoSystema, str(critério).replace('media.', ''))))]
            REAL_EXT = [os.path.splitext(f)[1] for f in os.listdir(str(ConverterNomes(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'), NomeDoSystema, str(critério).replace('media.', ''))))]
    # SE O SETTINGS ESTIVER PREENCHIDO, CONTINUAR
    if os.path.isfile(str(INF_SETTINGS)) == True and os.path.getsize(str(INF_SETTINGS)) > 0:
        # LER O ARQUIVO DE SETTINGS
        REAL_ROM = [os.path.splitext(f)[0] for f in os.listdir(str(ConverterNomes(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'),NomeDoSystema, str(critério).replace('media.', ''))))]
        REAL_EXT = [os.path.splitext(f)[1] for f in os.listdir(str(ConverterNomes(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'),NomeDoSystema, str(critério).replace('media.', ''))))]
        #print(REAL_ROM)  
        #print(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'))
        #print(str(ConverterNomes(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'),NomeDoSystema, str(critério).replace('media.', ''))))  
    if os.path.isfile(ROOT + '\\collections\\' + NomeDoSystema + '\\exclude.txt') == True:
        for Romexclude in Texto_InSettings(NomeDoSystema, '','exclude.txt'):
            listRomExclude.append(Romexclude)
    if os.path.isfile(ROOT + '\\collections\\' + NomeDoSystema + '\\include.txt') == True:
        for Rominclude in Texto_InSettings(NomeDoSystema, '','include.txt'):
            listRomInclude.append(Rominclude)

    listRomIgnorarXML = Retorne_ROM_do_XML(NomeDoSystema)
    ListIgnoreDefault = ['default']
    #print(type(listRomExclude))
    #print(type(listRomInclude))
    #print(type(listRomIgnorarXML))
    #print(listRomIgnorarXML)
    #print(type(ListIgnoreDefault))
    #informações 
    

    IGNORE_ROM = ListIgnoreDefault + listRomExclude + listRomInclude + listRomIgnorarXML
    IGNORE_ROM = list(set(IGNORE_ROM))
    IGNORE_ROM = [x for x in IGNORE_ROM if x != '']
    TOTAL_ROMS_IGNORE = 'O SYSTEMA : ' + green + str(NomeDoSystema) + reset_color + ' TEM ' + cyan + str(len(IGNORE_ROM)) + ' ' + str(INF_CRITÉRIO) + reset_color + ' QUE SERÃO IGNORADAS'
    
    # PRINCIPAL DO SCANNER PARA OBTER O REMOVE_ROM
    tmpw = np.array(REAL_ROM)
    tmpz = np.array(IGNORE_ROM)
    REMOVE_ROMS = list(set(np.setdiff1d(tmpw, tmpz))) 

    # SCANNER PARA OBTER O MISSING_ROM
    tmpw = np.array(listRomIgnorarXML)
    tmpz = np.array(REAL_ROM)
    MISSING_ROM = list(set(np.setdiff1d(tmpw, tmpz))) 
    
    # ----------------------------------------------------------------------------------------------------------------------
    TOTAL_ROMS_REMOVE = 'O SYSTEMA : ' + green + str(NomeDoSystema) + reset_color + ' TEM ' + red + str(len(REMOVE_ROMS)) + ' ' + str(INF_CRITÉRIO)  + reset_color + ' QUE SERÃO VERIFICADAS'
    print(TOTAL_ROMS_IGNORE)
    print(TOTAL_ROMS_REMOVE)
    print('TOTAL DE ITENS QUE NÃO ESTÃO DE ACORDO COM O SEU XML É :', cyan +  str(len(REMOVE_ROMS)) + reset_color, 'PARA O SISTEMA :', green + str(NomeDoSystema) + reset_color)
    # ----------------------------------------------------------------------------------------------------------------------
    #print(REMOVE_ROMS)
    # adicionando REAL_EXT a lista de ROMS a serem removidas
    EXT_ROMS_SETTINGS = str(Texto_InSettings(NomeDoSystema, 'list.extensions', 'settings.conf')).split(',')
    REAL_EXT_REAL = set([x for x in REAL_EXT if x != ''])
    for ext in REAL_EXT_REAL:
        for removerom in REMOVE_ROMS:
            DIR_REMOVE_ROMS = ((ConverterNomes(Texto_InSettings(NomeDoSystema, critério, 'settings.conf'), NomeDoSystema, str(critério).replace('media.', '') )) + '\\' + str(removerom) + str(ext)).lstrip()
            if os.path.exists(DIR_REMOVE_ROMS) and os.path.isfile(DIR_REMOVE_ROMS) == True:
                # gravar em audit.log o que será removido
                if not os.path.exists(ROOT + '\\meta\\audit'):
                    os.makedirs(ROOT + '\\meta\\audit')

                INF_AUDITORIA = ROOT + '\\meta\\audit\\' + NomeDoSystema + ' Removido ' + DATA_HORA_ATUAIS_FORMATADO + '_audit.log'
                meuArquivo = open(str(INF_AUDITORIA), 'a')
                meuArquivo.write(DIR_REMOVE_ROMS + '\n')
                meuArquivo.close()

                INF_AUDITORIA_MISSING = ROOT + '\\meta\\audit\\' + NomeDoSystema + ' Missing ' + str(INF_CRITÉRIO) + ' ' + DATA_HORA_ATUAIS_FORMATADO + '_audit.log'
                meuArquivo = open(str(INF_AUDITORIA), 'a')
                meuArquivo.write(str(MISSING_ROM) + '\n')
                meuArquivo.close()

                #print(green + DIR_REMOVE_ROMS + reset_color)
                LIST_DIR_REMOVE_ROMS.append(DIR_REMOVE_ROMS)
                    
    return LIST_DIR_REMOVE_ROMS




def remove_roms_and_artworks_unsuported(NomeDoSystema):
    for sistema_ser_trabalhado in NomeDoSystema if type(NomeDoSystema) == list else [NomeDoSystema]:
        if os.path.exists(ROOT + '\\collections\\' + sistema_ser_trabalhado + '\\' + 'settings.conf') and sistema_ser_trabalhado != 'Main':
            print(green + sistema_ser_trabalhado  + reset_color, green + ' <<<<<<<<< ---- sistema_ser_trabalhado'  + reset_color)
            REMOVE_ROM = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'list.path')
            REMOVE_ARTWORK_BACK = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.artwork_back')
            REMOVE_ARTWORK_FRONT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.artwork_front')
            REMOVE_LOGO = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.logo')
            REMOVE_LOGO_1 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.logo_1')
            REMOVE_LOGO_2 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.logo_2')
            REMOVE_LOGO_3 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.logo_3')
            REMOVE_MEDIUM_BACK = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.medium_back')
            REMOVE_MEDIUM_FRONT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.medium_front')
            REMOVE_SCREENSHOT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenshot')
            REMOVE_SCREENTITLE = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screentitle')
            REMOVE_VIDEO = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.video')
            #REMOVE_SYSTEM_ARTWORK = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.system_artwork')
            REMOVE_FANART = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart')
            REMOVE_FANART_CG = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_cg')
            REMOVE_FANART_CHARGE = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_charge')
            REMOVE_FANART_OCIDENT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_ocident')
            REMOVE_FANART_ORIENT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_orient')
            REMOVE_FANART_CLASSIC = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_classic')
            REMOVE_FANART_DARK = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_dark')
            REMOVE_FANART_ABSTRACT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_style_1')
            REMOVE_FANART_STYLE_1 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_style_1')
            REMOVE_FANART_STYLE_2 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_style_2')
            REMOVE_FANART_STYLE_3 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_style_3')
            REMOVE_FANART_STYLE_4 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.fanart_style_4')
            REMOVE_STORY = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.story')
            REMOVE_ARTWORK_3D = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.artwork_3d')
            REMOVE_BANNER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.banner')
            REMOVE_BEZEL = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.bezel')
            REMOVE_COVER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.cover')
            REMOVE_MARQUEE = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.marquee')
            REMOVE_CABINETS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.cabinets')
            REMOVE_CHARACTER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.character')
            REMOVE_CHARACTER_1 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.character_1')
            REMOVE_CHARACTER_2 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.character_2')
            REMOVE_CHARACTER_3 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.character_3')
            REMOVE_COLOR = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.color')
            REMOVE_COLOR_1 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.color_1')
            REMOVE_COLOR_2 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.color_2')
            REMOVE_COLOR_3 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.color_3')
            REMOVE_CONTROLLER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.controller')
            REMOVE_DEVICE = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.device')
            REMOVE_EMBLEM = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.emblem')
            REMOVE_VIDEO_BORDER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.video_border')
            REMOVE_SPIN = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.spin')
            REMOVE_CPLAYOUTS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.cplayouts')
            REMOVE_ICON = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.icon')
            REMOVE_SCREENBACKGROUND = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenbackground')
            REMOVE_SCREENBOSSES = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenbosses')
            REMOVE_SCREENENDS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenends')
            REMOVE_SCREENHOWTO = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenhowto')
            REMOVE_SCREENOVER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenintro')
            REMOVE_SCREENSELECT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenselect')
            REMOVE_SCREENVERSUS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenversus')
            REMOVE_SCREENWARNING = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.screenwarning')
            REMOVE_TECHNICAL = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.tech')
            REMOVE_BACKGROUND = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.background')
            REMOVE_BACKGROUND_1 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.background_1')
            REMOVE_BACKGROUND_2 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.background_2')
            REMOVE_BACKGROUND_3 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.background_3')
            REMOVE_BAR = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.bar')
            REMOVE_TRANSLATION_ENG = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.translation')
            REMOVE_TRANSLATION_PTBR = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.translation_ptbr')
            REMOVE_TRANSLATION_ES = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.translation_es')
            REMOVE_TRANSLATION_FR = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.translation_fr')
            REMOVE_TRANSLATION_IT = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.translation_it')
            REMOVE_TRANSLATION_DE = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.translation_de')
            REMOVE_STATISTICS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.statistics')
            REMOVE_LAYER = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.layer')
            REMOVE_LAYER_1 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.layer_1')
            REMOVE_LAYER_2 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.layer_2')
            REMOVE_LAYER_3 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.layer_3')
            REMOVE_LAYER_4 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.layer_4')
            REMOVE_LAYER_5 = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.layer_5')
            REMOVE_MUSIC = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.music')
            REMOVE_SOUNDS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.sounds')
            REMOVE_MOVES_LISTS = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.moves_lists')
            REMOVE_VIDEOFILM = listar_itens_XMLCheckup_remove(sistema_ser_trabalhado, 'media.video_film')


            Backup_default(REMOVE_ROM)
            Backup_default(REMOVE_ARTWORK_BACK)
            Backup_default(REMOVE_ARTWORK_FRONT)
            Backup_default(REMOVE_LOGO)
            Backup_default(REMOVE_MEDIUM_BACK)
            Backup_default(REMOVE_MEDIUM_FRONT)
            Backup_default(REMOVE_SCREENSHOT)
            Backup_default(REMOVE_SCREENTITLE)
            Backup_default(REMOVE_VIDEO)
            #Backup_default(REMOVE_SYSTEM_ARTWORK)
            Backup_default(REMOVE_FANART)
            Backup_default(REMOVE_STORY)
            Backup_default(REMOVE_ARTWORK_3D)
            Backup_default(REMOVE_BANNER)
            Backup_default(REMOVE_BEZEL)
            Backup_default(REMOVE_COVER)
            Backup_default(REMOVE_MARQUEE)
            Backup_default(REMOVE_CABINETS)
            Backup_default(REMOVE_CHARACTER)
            Backup_default(REMOVE_COLOR)
            Backup_default(REMOVE_CONTROLLER)
            Backup_default(REMOVE_DEVICE)
            Backup_default(REMOVE_EMBLEM)
            Backup_default(REMOVE_VIDEO_BORDER)
            Backup_default(REMOVE_SPIN)
            Backup_default(REMOVE_CPLAYOUTS)
            Backup_default(REMOVE_ICON)
            Backup_default(REMOVE_SCREENBACKGROUND)
            Backup_default(REMOVE_SCREENBOSSES)
            Backup_default(REMOVE_SCREENENDS)
            Backup_default(REMOVE_SCREENHOWTO)
            Backup_default(REMOVE_SCREENOVER)
            Backup_default(REMOVE_SCREENSELECT)
            Backup_default(REMOVE_SCREENVERSUS)
            Backup_default(REMOVE_SCREENWARNING)
            Backup_default(REMOVE_TECHNICAL)
            Backup_default(REMOVE_BACKGROUND)
            Backup_default(REMOVE_BACKGROUND_1)
            Backup_default(REMOVE_BACKGROUND_2)
            Backup_default(REMOVE_BACKGROUND_3)
            Backup_default(REMOVE_COLOR_1)
            Backup_default(REMOVE_COLOR_2)
            Backup_default(REMOVE_COLOR_3)
            Backup_default(REMOVE_CHARACTER_1)
            Backup_default(REMOVE_CHARACTER_2)
            Backup_default(REMOVE_CHARACTER_3)
            Backup_default(REMOVE_FANART_ABSTRACT)
            Backup_default(REMOVE_FANART_CG)
            Backup_default(REMOVE_FANART_CHARGE)
            Backup_default(REMOVE_FANART_OCIDENT)
            Backup_default(REMOVE_FANART_ORIENT)
            Backup_default(REMOVE_FANART_CLASSIC)
            Backup_default(REMOVE_FANART_DARK)
            Backup_default(REMOVE_FANART_STYLE_1)
            Backup_default(REMOVE_FANART_STYLE_2)
            Backup_default(REMOVE_FANART_STYLE_3)
            Backup_default(REMOVE_FANART_STYLE_4)
            Backup_default(REMOVE_LOGO_1)
            Backup_default(REMOVE_LOGO_2)
            Backup_default(REMOVE_LOGO_3)
            Backup_default(REMOVE_BAR)
            Backup_default(REMOVE_TRANSLATION_ENG)
            Backup_default(REMOVE_TRANSLATION_PTBR)
            Backup_default(REMOVE_TRANSLATION_ES)
            Backup_default(REMOVE_TRANSLATION_FR)
            Backup_default(REMOVE_TRANSLATION_IT)
            Backup_default(REMOVE_TRANSLATION_DE)
            Backup_default(REMOVE_LAYER)
            Backup_default(REMOVE_LAYER_1)
            Backup_default(REMOVE_LAYER_2)
            Backup_default(REMOVE_LAYER_3)
            Backup_default(REMOVE_LAYER_4)
            Backup_default(REMOVE_LAYER_5)
            Backup_default(REMOVE_MUSIC)
            Backup_default(REMOVE_SOUNDS)
            Backup_default(REMOVE_MOVES_LISTS)
            Backup_default(REMOVE_STATISTICS)
            Backup_default(REMOVE_VIDEOFILM)
            


            


            
            #print(REMOVE_ROM)
            #print(REMOVE_ARTWORK_BACK)
            #print(REMOVE_ARTWORK_FRONT)
            #print(REMOVE_LOGO)
            #print(REMOVE_MEDIUM_BACK)
            #print(REMOVE_MEDIUM_FRONT)
            #print(REMOVE_SCREENSHOT)
            #print(REMOVE_SCREENTITLE)
            #print(REMOVE_VIDEO)
            #print(REMOVE_SYSTEM_ARTWORK)
            #print(REMOVE_FANART)
            #print(REMOVE_STORY)
            #print(REMOVE_ARTWORK_3D)
            #print(REMOVE_BANNER)
            #print(REMOVE_BEZEL)
            #print(REMOVE_COVER)
            #print(REMOVE_ALL)

# ----------------------------------------------------------------------------- #
# FUNÇÃO USADA PARA FAZER BACKUP DAS PASTAS ( CHAMADA NAS OUTRAS FUNÇÕES ) 
# Backup_default(caminho):
remove_roms_and_artworks_unsuported(ITEMS_COLLECTION_NAME)




