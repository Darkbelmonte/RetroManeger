import os
import shutil
from shutil import move
import numpy as np # linear algebra
import pandas as pd  # para ler, visualizar e printar infos do df
from datetime import date
from datetime import datetime
import xml.etree.ElementTree as ET
# ! ----------------------------------------------------------------------------------------------------- ! #
#                                    !!       BASE DO SCRIPT      !!                                        #
#
# ! ----------------------------------------------------------------------------------------------------- ! #
# limpar terminal antes de executar 
print("\n" * os.get_terminal_size().lines)
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
print(red + 'Sistema Operacional :' + reset_color, cyan + os.name + reset_color)
#print('Em que século você esta :', os.system(date))
print(red + 'Sript excutado :' + reset_color, yellow +  os.path.basename(__file__) + reset_color)
print(red + 'Localização :' + reset_color,  yellow +  (__file__) + reset_color)
# Para obter o caminho absoluto
dir_path = os.path.dirname(os.path.realpath(__file__))
# -------------------------------------------------- #
# -------------------------------------------------- #
# -----------------    CAMINHOS   ------------------ #
# _________  DEFINIR CONFIGURAÇÕES INICIAIS________  #
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
print(red + "ROOT : " + reset_color, yellow +   ROOT + reset_color)
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
BEFORE_DIR = ((os.path.dirname(os.path.realpath(__file__))).split('\\', -1)[-2]) + '\\'
BACKUP_DIR = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup'
BACKUP_DIR_ROM = BEFORE_DIR + (ROOT.split('\\', -1)[-1]) + '_Backup' + '\\Roms'
DATA_ATUAL = date.today()
DATA_HORA_ATUAIS = datetime.now()
DATA_HORA_ATUAIS_FORMATADO = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H-%M')
DATA_HORA_ATUAIS_FORMATADO_HORA = DATA_HORA_ATUAIS.strftime('%d-%m-%Y %H') + 'h'
INSTALLED_SYSTEMS = [f for f in os.listdir(ROOT + '\\collections\\') if os.path.exists(ROOT + '\\collections\\') if os.path.isdir(ROOT + '\\collections\\') if not f in ['Main','_common']]
ITEMS_META_NAME = [f for f in os.listdir(ROOT + '\\meta\\') if os.path.exists(ROOT + '\\meta\\') if os.path.isdir(ROOT + '\\meta\\')]
ITEMS_META_FILE_XML = list(set([os.path.join(ROOT + '\\meta\\' + file + '\\', file2) for file in ITEMS_META_NAME if os.path.exists(ROOT + '\\meta\\' + file) if os.path.isdir(ROOT + '\\meta\\' + file) for file2 in os.listdir(ROOT + '\\meta\\' + file) if file2.endswith('.xml')]))
ITEMS_COLLECTION_FILE_TXT = list(set([os.path.join(ROOT + '\\collections\\' + file + '\\' + file2) for file in INSTALLED_SYSTEMS if os.path.exists(ROOT + '\\collections\\' + file) for file2 in os.listdir(ROOT + '\\collections\\' + file) if file2.endswith('.txt')]))
EMPTY = []
print(red + 'DATA ATUAL :' + reset_color, yellow +  DATA_HORA_ATUAIS_FORMATADO_HORA + reset_color)
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
# _________     CRIAÇÃO DO DATAFRAME    ____________ #
# Pd de nomes errados x officiais
file_backup(FILE_CSV_SETTINGS)
settings_df = pd.read_csv(FILE_CSV_SETTINGS_TMP, encoding='utf-8', sep=';')
settings_midia_name = settings_df['MIDIA_VARIABLE'].tolist()

file_backup(FILE_CSV_FIX_NAME_SYSTEM)
df = pd.read_csv(FILE_CSV_FIX_NAME_SYSTEM_TMP, encoding='utf-8', sep=';')
df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))

file_backup(FILE_CSV_FIX_NAME_CLEAN)
clean_df = pd.read_csv(FILE_CSV_FIX_NAME_CLEAN_TMP, encoding='utf-8', sep=';')

dirclean = clean_df['dirclean'].tolist()
limpar = clean_df['clean'].tolist()
emulador = clean_df['emulador'].tolist()
categoria = clean_df['categoria'].tolist()

# ! ----------------------------------------------------------------------------------------------------- ! #
#                                !!       1º ETAPA DO SCRIPT      !!                                        #
#                                        LER ARQUIVO SETTINGS                                               #
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
# ---------   LIMPAR ARQUIVOS PRE DEFINIDOS    ---------- #
#             LIMPAR ARQUIVOS DESNECESSÁRIOS              #
def clean_list():
    for dirremove, remove, emul, systema in zip(dirclean, limpar, emulador, categoria):
        make_backup_default(str(dirremove),'PRE_DEFINIDOS')        
# ---------   LER INFORMAÇÕES DO XML PARA PEGAR NOMES     ---------- #
#   TRABALHAR INFORMAÇÕES DO XML VERSUS OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE          #
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

# ---------   CONSTRUIR DIRETÓRIOS COM ARQUIVOS A REMOVER     ---------- #
#                   COSNTRUIR INFORMAÇÕES DE RETIRADA                    #
def criar_lista_de_arquivos_para_remover( Dri_remove_str, file_remove_list, Extension_remove_list):
    #criar_lista_de_arquivos_para_remover(ROM_DIR, REMOVE_FILES, REAL_EXT_FILES))))
    print(file_remove_list, 'file_remove_list')
    #print(Extension_remove_list, 'Extension_remove_list')
    LIST_DIR_REMOVE_FILES = []
    REAL_EXT = list(set([x for x in Extension_remove_list if x != '']))
    print(REAL_EXT, 'REAL_EXT')
    for x in REAL_EXT:
        for REMOVE in file_remove_list:
            print('>>>>>>>>>> >>>>>>>>>>> >>>>>>>>', REMOVE, 'EXT' ,x)
            DIR_REMOVE_FILES = str(Dri_remove_str) + '\\' + str(REMOVE) + str(x).lstrip()
            print(DIR_REMOVE_FILES, 'DIR_REMOVE_FILES')
            if os.path.exists(DIR_REMOVE_FILES) and os.path.isfile(DIR_REMOVE_FILES) == True:
                LIST_DIR_REMOVE_FILES.append(DIR_REMOVE_FILES)
    return LIST_DIR_REMOVE_FILES
# --------          BACKUP - CRIAÇÃO DA PASTA            -------- #
#     AVALIA E CONSTROI A ESTRUTURA DE BACKUP  E FAZ O BACKUP     #
def make_backup_default(caminhos, observação):
    if type(caminhos) == list:
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
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\'
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
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp + '\\'
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
                # criando pasta e removendo arquivo                
                    if os.path.isdir(str(dir_tmp)) and os.path.exists(str(dir_tmp)):    
                        old_end = str(caminho)                          
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {yellow + old_end + reset_color}  > Fazendo Back_Up> CleanList = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {cyan + old_end + reset_color}  > Erro e forçando Back_Up> CleanList = {new_end}')            
                        pass

                if not str(ROOT) in caminho:
                    dir_tmp = str(caminho)
                    if os.path.exists(str(dir_tmp)):                         
                        old_end = str(caminho) 
                        new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO_HORA + '\\' + dir_tmp

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
                #print(' O Diretório que você quer mudar em' , caminho,' os arquivos não existe, verifique se há algum erro !!')
                pass
        else:
            pass

    elif type(caminhos) != list:
        #print(f'O caminho {caminhos} que você passou não é uma lista!!')
        # aqui ele segue se for um arquivo
        if os.path.isfile(caminhos) and os.path.exists(caminhos):
            # ajustando nomes 
            if str(ROOT + '\\') in str(caminhos):
                dir_tmp, arquivo = os.path.split(caminhos) 
                dir_tmp = dir_tmp.replace(ROOT + '\\', '')
            # criando pasta e removendo arquivo
                if os.path.exists(str(dir_tmp)):    
                    old_end = str(caminhos)
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
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
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
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
            # criando pasta e removendo arquivo                
                if os.path.isdir(str(dir_tmp)) and os.path.exists(str(dir_tmp)):    
                    old_end = str(caminhos)                          
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
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
                    new_end = BACKUP_DIR + '\\' + observação + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
                    try:
                        os.makedirs(new_end)
                        shutil.move(old_end, new_end, copy_function=new_end)
                        print(f'folder {old_end}  >Fazendo Back_Up>  = {new_end}')
                    except IOError:
                        move(old_end, new_end)
                        print(f'folder {old_end}  >Erro e forçando Back_Up>  = {new_end}')            
                    pass

        if not os.path.exists(caminhos):
            #print(' O Diretório que você quer mudar :', caminhos ,' os arquivos não existe, verifique se há algum erro !!')
            pass
    else:
        print('Não temos nada para alterar aqui !!')
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
# ---------   SALVAR LOG COM ARQUIVOS QUE FORAM REMOVIDOS     ---------- #
#               LOG DE ARQUIVOS REMOVIDOS E FALTANTES                    #
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
# ! ----------------------------------------------------------------------------------------------------- ! #
def Remove_Files_System_Unofficial(SYSTEM_NAME, TEXT_SEARCHED):
    global RETURN_FUNCTION_UNOFFICIAL
    RETURN_FUNCTION_UNOFFICIAL = []
    #ROM_DIR = (get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, 'settings.conf'))
    DEFAULT_DIR = (get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, 'settings.conf'))
    REAL_FILES = [os.path.splitext(f)[0] for f in os.listdir(DEFAULT_DIR) if os.path.isfile(os.path.join(DEFAULT_DIR, f))]
    REAL_EXT_FILES = list(set([os.path.splitext(f)[1] for f in os.listdir(str(DEFAULT_DIR)) if os.path.isfile(os.path.join(str(DEFAULT_DIR), f))]))
    REAL_EXT = set([x for x in REAL_EXT_FILES if x != ''])
    EXCLUIR_TXT_LIST = (get_caminhos_settings(SYSTEM_NAME,'', 'exclude.txt')) if (get_caminhos_settings(SYSTEM_NAME,'', 'exclude.txt')) != None else [] 
    INCLUDE_TXT_LIST = (get_caminhos_settings(SYSTEM_NAME,'', 'include.txt')) if (get_caminhos_settings(SYSTEM_NAME,'', 'include.txt')) != None else [] 
    ROMS_XML_LIST = get_name_rom_xml(SYSTEM_NAME) if get_name_rom_xml(SYSTEM_NAME) != None else [] 
    DEFAULT_LIST = ['default','EstaESomenteUmaListaFake']
    TOTAL_ROMS_VALIDAS = ROMS_XML_LIST + EXCLUIR_TXT_LIST + INCLUDE_TXT_LIST + DEFAULT_LIST
    tmpw = np.array(REAL_FILES)
    tmpz = np.array(TOTAL_ROMS_VALIDAS)
    REMOVE_FILES = list(set(np.setdiff1d(tmpw, tmpz)))
    REMOVE_FILES = [i for i in REMOVE_FILES if i]

    tmpx = np.array(TOTAL_ROMS_VALIDAS)
    tmpy = np.array(REAL_FILES)
    MISSING_FILES = list(set(np.setdiff1d(tmpx, tmpy))) 
    MISSING_FILES = [w for w in MISSING_FILES if w]

    for EXT in REAL_EXT:
        for REMOVE in REMOVE_FILES:
            DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
            if os.path.exists(DIR_REMOVE_FILES) and os.path.isfile(DIR_REMOVE_FILES) == True:
                DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
                RETURN_FUNCTION_UNOFFICIAL.append(DIR_REMOVE_FILES)
                RETURN_FUNCTION_UNOFFICIAL = list(set(RETURN_FUNCTION_UNOFFICIAL))

                #print(RETURN_FUNCTION_UNOFFICIAL, 'RETURN_FUNCTION_UNOFFICIAL <<<<')
                criar_log_auditoria(SYSTEM_NAME, 'media.', DIR_REMOVE_FILES, MISSING_FILES)

    #return REAL_FILES, REAL_EXT_FILES, EXCLUIR_TXT_LIST, INCLUDE_TXT_LIST, ROMS_XML_LIST, MISSING_FILES
    return RETURN_FUNCTION_UNOFFICIAL
# ! ----------------------------------------------------------------------------------------------------- ! #
def Remove_Files_System_NoRomFolder(SYSTEM_NAME, TEXT_SEARCHED):
    global RETURN_FUNCTION_NOT_ROM_FOLDER
    RETURN_FUNCTION_NOT_ROM_FOLDER = []
    #ROM_DIR = (get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, 'settings.conf'))
    DEFAULT_DIR = (get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, 'settings.conf'))
    ROM_DIR = (get_caminhos_settings(SYSTEM_NAME,'list.path', 'settings.conf'))
    REAL_FILES = [os.path.splitext(f)[0] for f in os.listdir(DEFAULT_DIR) if os.path.isfile(os.path.join(DEFAULT_DIR, f))]
    ROM_FILES = [os.path.splitext(f)[0] for f in os.listdir(ROM_DIR) if os.path.isfile(os.path.join(ROM_DIR, f))]
    REAL_EXT_FILES = list(set([os.path.splitext(f)[1] for f in os.listdir(str(DEFAULT_DIR)) if os.path.isfile(os.path.join(str(DEFAULT_DIR), f))]))
    REAL_EXT = set([x for x in REAL_EXT_FILES if x != ''])
    EXCLUIR_TXT_LIST = (get_caminhos_settings(SYSTEM_NAME,'', 'exclude.txt')) if (get_caminhos_settings(SYSTEM_NAME,'', 'exclude.txt')) != None else [] 
    INCLUDE_TXT_LIST = (get_caminhos_settings(SYSTEM_NAME,'', 'include.txt')) if (get_caminhos_settings(SYSTEM_NAME,'', 'include.txt')) != None else [] 
    ROMS_XML_LIST = get_name_rom_xml(SYSTEM_NAME) if get_name_rom_xml(SYSTEM_NAME) != None else [] 
    DEFAULT_LIST = ['default','EstaESomenteUmaListaFake']
    TOTAL_ROMS_VALIDAS = ROMS_XML_LIST + EXCLUIR_TXT_LIST + INCLUDE_TXT_LIST + DEFAULT_LIST
    tmpw = np.array(REAL_FILES)
    tmpz = np.array(ROM_FILES)
    REMOVE_FILES = list(set(np.setdiff1d(tmpw, tmpz)))
    REMOVE_FILES = [i for i in REMOVE_FILES if i]

    for EXT in REAL_EXT:
        for REMOVE in REMOVE_FILES:
            DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
            if os.path.exists(DIR_REMOVE_FILES) and os.path.isfile(DIR_REMOVE_FILES) == True:
                DIR_REMOVE_FILES = str(DEFAULT_DIR) + '\\' + str(REMOVE) + str(EXT).lstrip()
                RETURN_FUNCTION_NOT_ROM_FOLDER.append(DIR_REMOVE_FILES)
                RETURN_FUNCTION_NOT_ROM_FOLDER = list(set(RETURN_FUNCTION_NOT_ROM_FOLDER))

    #return REAL_FILES, REAL_EXT_FILES, EXCLUIR_TXT_LIST, INCLUDE_TXT_LIST, ROMS_XML_LIST, MISSING_FILES
    return RETURN_FUNCTION_NOT_ROM_FOLDER

# ! ----------------------------------------------------------------------------------------------------- ! #
for System_Name in INSTALLED_SYSTEMS:
    RETURN_MEDIA_NAME = sorted(list(set(list_End_make_media_Settings(System_Name))))
    for Search_Texto in RETURN_MEDIA_NAME:
        if Search_Texto != '' and os.path.exists(get_caminhos_settings(System_Name, Search_Texto, 'settings.conf')) and os.listdir(get_caminhos_settings(System_Name,Search_Texto, 'settings.conf')) != []:
            while (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != [] and (Remove_Files_System_Unofficial(System_Name, Search_Texto)) != None:
                DIR_REMOVE_FILES_UNOFFIAL = Remove_Files_System_Unofficial(System_Name, Search_Texto) if Remove_Files_System_Unofficial(System_Name, Search_Texto) != None else ''
                make_backup_default(DIR_REMOVE_FILES_UNOFFIAL, ' UNOFFIAL ')
                DIR_REMOVE_FILES_NOT_ROM_FOLDER = Remove_Files_System_NoRomFolder(System_Name, Search_Texto) if Remove_Files_System_NoRomFolder(System_Name, Search_Texto) != None else ''
                make_backup_default(DIR_REMOVE_FILES_NOT_ROM_FOLDER, ' NOT_ROM_FOLDER ')


# ! ----------------------------------------------------------------------------------------------------- ! #       
Backup_EmptyFolders()
clean_list()
