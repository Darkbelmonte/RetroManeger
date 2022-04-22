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
#cmd = 'date'
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
# ! ----------------------------------------------------------------------------------------------------- ! #
#                                !!       1º ETAPA DO SCRIPT      !!                                        #
#                                        LER ARQUIVO SETTINGS                                               #
# ! ----------------------------------------------------------------------------------------------------- ! #
# ---------   CAMINHOS CONTIDOS NO SETTINGS    ---------- #
# RETORNAR OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE #
def get_caminhos_settings(SYSTEM_NAME,TEXT_SEARCHED, TYPE_FILE_TXT):
    SETTINGS_FILE = os.path.join(ROOT, 'collections', SYSTEM_NAME, TYPE_FILE_TXT)
    if os.path.exists(SETTINGS_FILE):
        if TYPE_FILE_TXT == 'settings.conf':
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
            with open(SETTINGS_FILE, 'r') as arquivo:
                LINHA_SETTINGS_TMP = arquivo.readlines()
                LINHA_SETTINGS_TMP[0:-1].append(LINHA_SETTINGS_TMP[-1])
                LINHA_SETTINGS = [LINHA_SETTINGS_TMP[i].replace('\n', '') for i in range(len(LINHA_SETTINGS_TMP))]
                LINHA_SETTINGS = LINHA_SETTINGS
            return LINHA_SETTINGS
# ---------   LER INFORMAÇÕES DO XML PARA PEGAR NOMES     ---------- #
#   TRABALHAR INFORMAÇÕES DO XML VERSUS OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE          #
global ROMS_XML_LIST
def get_name_rom_xml(SYSTEM_NAME):
    systemXML = os.path.join(ROOT + '\\meta\\hyperlist\\', str(SYSTEM_NAME) + '.xml')
    if os.path.exists(systemXML):
        tree = ET.parse(systemXML)
        root = tree.getroot()
        ROMS_XML_LIST = [game.attrib['name'] for game in root.findall("./game")]
    return ROMS_XML_LIST

# ---------   CONSTRUIR DIRETÓRIOS COM ARQUIVOS A REMOVER     ---------- #
#                   COSNTRUIR INFORMAÇÕES DE RETIRADA                    #
def criar_lista_de_arquivos_para_remover( Dri_remove_str, file_remove_list, Extension_remove_list):
    LIST_DIR_REMOVE_FILES = []
    REAL_EXT = set([x for x in Extension_remove_list if x != ''])
    for EXT in REAL_EXT:
        for REMOVE in file_remove_list:
            DIR_REMOVE_FILES = str(Dri_remove_str) + '\\' + str(REMOVE) + str(EXT).lstrip()
            if os.path.exists(DIR_REMOVE_FILES) and os.path.isfile(DIR_REMOVE_FILES) == True:
                LIST_DIR_REMOVE_FILES.append(DIR_REMOVE_FILES)
    return LIST_DIR_REMOVE_FILES
# --------          BACKUP - CRIAÇÃO DA PASTA            -------- #
#     AVALIA E CONSTROI A ESTRUTURA DE BACKUP  E FAZ O BACKUP     #
def make_backup_default(caminhos):
    #print(type(caminhos), 'type')
    if type(caminhos) == list:
        #print('Vejo que temos uma lista de sistemas, vamos lá !!')
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
            pass
            #print('Não temos nada para alterar aqui !!')

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
# --------   LISTA E CRIA PASTAS DE MIDIA    -------- #
#    ESTRUTURA FAKE PARA CRIAR PASTAS E LISTAR        #
def list_End_make_media_Settings(NomeDoSystema):    
    lts_Edit_media_settings = []
    for media_settings in settings_midia_name:
        Edit_media_settings = media_settings.replace('media.', '').lstrip()
        lts_Edit_media_settings.append(Edit_media_settings)

        Excluir_media_settings = ['meda.<filetype>','None','<filetype>','list.path','list.includeMissingItems','list.extensions','list.menuSort','list.romHierarchy','list.truRIP','launcher','metadata.type']

        tmpw = np.array(lts_Edit_media_settings)
        tmpz = np.array(Excluir_media_settings)
        Manter_Midias = list(set(np.setdiff1d(tmpw, tmpz)))
        Manter_Midias = [i for i in Manter_Midias if i]

        for midia in Manter_Midias:
            if str(NomeDoSystema) != 'Main' :  
                if str(NomeDoSystema) != '_common':
                    if str(NomeDoSystema) != 'None':

                        Fake_FolderMidia = ROOT + '\\collections\\' + NomeDoSystema + '\\medium_artwork\\' + str(midia)

                        if not os.path.exists(str(Fake_FolderMidia)):
                            os.makedirs(Fake_FolderMidia)
                            print(f'Criando Pasta {Fake_FolderMidia}') 
                        if os.path.exists(str(Fake_FolderMidia)):
                            #print(f'Pasta {Fake_FolderMidia} já existe')
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

#ROM_DIR = (get_caminhos_settings('Mame','list.path', 'settings.conf'))
#REAL_FILES = [os.path.splitext(f)[0] for f in os.listdir(ROM_DIR) if os.path.isfile(os.path.join(ROM_DIR, f))]
#REAL_EXT_FILES = [os.path.splitext(f)[1] for f in os.listdir(str(ROM_DIR)) if os.path.isfile(os.path.join(str(ROM_DIR), f))]
#EXCLUIR_TXT_LIST = (get_caminhos_settings('Mame','', 'exclude.txt'))
#INCLUDE_TXT_LIST = (get_caminhos_settings('Mame','', 'include.txt'))
#ROMS_XML_LIST = get_name_rom_xml('Mame')
#DEFAULT_LIST = ['default','EstaESomenteUmaListaFake']
#IGNORE_FILE = EXCLUIR_TXT_LIST + INCLUDE_TXT_LIST + DEFAULT_LIST + ROMS_XML_LIST
#   CRIAR LISTA DE ARQUIVOS PARA REMOÇÃO
#tmpw = np.array(REAL_FILES)
#tmpz = np.array(IGNORE_FILE)
#REMOVE_FILES = list(set(np.setdiff1d(tmpw, tmpz)))
#   SCANNER PARA OBTER O MISSING_FILES
#tmpx = np.array(IGNORE_FILE)
#tmpy = np.array(REAL_FILES)
#MISSING_FILES = list(set(np.setdiff1d(tmpx, tmpy))) 
#REMOVE_LIST_FINAL = criar_lista_de_arquivos_para_remover(ROM_DIR, REMOVE_FILES, REAL_EXT_FILES)
#GRAVAR_LOG = criar_log_auditoria('Mame', 'media.', REMOVE_LIST_FINAL, MISSING_FILES)
# ! ----------------------------------------------------------------------------------------------------- ! #

for System_Name in INSTALLED_SYSTEMS:
    RETURN_MEDIA_NAME = sorted(list(set(list_End_make_media_Settings(System_Name))))
    for Search_Texto in RETURN_MEDIA_NAME:
        ROM_DIR = (get_caminhos_settings(System_Name , Search_Texto, 'settings.conf'))
        REAL_FILES = [os.path.splitext(f)[0] for f in os.listdir(ROM_DIR) if os.path.isfile(os.path.join(ROM_DIR, f))]
        REAL_EXT_FILES = [os.path.splitext(f)[1] for f in os.listdir(str(ROM_DIR)) if os.path.isfile(os.path.join(str(ROM_DIR), f))]
        EXCLUIR_TXT_LIST = (get_caminhos_settings(System_Name,'', 'exclude.txt'))
        INCLUDE_TXT_LIST = (get_caminhos_settings(System_Name,'', 'include.txt'))
        ROMS_XML_LIST = get_name_rom_xml(System_Name)
        DEFAULT_LIST = ['default','EstaESomenteUmaListaFake']
        IGNORE_FILE = EXCLUIR_TXT_LIST + INCLUDE_TXT_LIST + DEFAULT_LIST + ROMS_XML_LIST
        #   CRIAR LISTA DE ARQUIVOS PARA REMOÇÃO
        tmpw = np.array(REAL_FILES)
        tmpz = np.array(IGNORE_FILE)
        REMOVE_FILES = list(set(np.setdiff1d(tmpw, tmpz)))
        #   SCANNER PARA OBTER O MISSING_FILES
        tmpx = np.array(IGNORE_FILE)
        tmpy = np.array(REAL_FILES)
        MISSING_FILES = list(set(np.setdiff1d(tmpx, tmpy))) 
        REMOVE_LIST_FINAL = criar_lista_de_arquivos_para_remover(ROM_DIR, REMOVE_FILES, REAL_EXT_FILES)
        GRAVAR_LOG = criar_log_auditoria(System_Name, Search_Texto, REMOVE_LIST_FINAL, MISSING_FILES)
# ! ----------------------------------------------------------------------------------------------------- ! #
        make_backup_default(REMOVE_LIST_FINAL)
# ! ----------------------------------------------------------------------------------------------------- ! #








    
