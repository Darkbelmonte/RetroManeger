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

# -----   INICIO DAS DEFINIÇÃO DAS FUNÇÕES   ------- #
# _________     CRIAÇÃO DO DATAFRAME    ____________ #
# verificar se todos os arquivos old_file foram movidos para new_file, caso não tenha sido movido, mover para pasta de BACKUP
# --------   BACKUP - NOMES NA LISTA NEGRA    -------- #
# RETIRAR TODAS AS PASTAS DE ACORDO COM CLEANLIST      #
def Backup_default(caminho):
    if os.path.isfile(ROOT + '\\' + caminho) and os.path.exists(ROOT + '\\' + caminho):
        old_end = ROOT + '\\' + caminho
        dir_tmp, arquivo = os.path.split(caminho) 
        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
        try:
            os.makedirs(new_end)
            shutil.move(old_end, new_end, copy_function=new_end)
            print(f'folder {old_end}  >Fazendo Back_Up> CleanList = {new_end}')
        except IOError:
            move(old_end, new_end)
            print(f'folder {old_end}  >Erro e forçando Back_Up> CleanList = {new_end}')            
        pass
    elif os.path.isdir(caminho) and os.path.exists(caminho):
        old_end = caminho 
        dir_tmp = caminho.split('\\', 0)[-1] 
        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
        try:
            os.makedirs(new_end)
            shutil.move(old_end, new_end, copy_function=new_end)
            print(f'folder {old_end}  >Fazendo Back_Up> Unofficialname = {new_end}')
        except IOError:
            move(old_end, new_end)
            print(f'folder {old_end}  >Erro e forçando Back_Up> Unofficialname = {new_end}')            
        pass
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

# --------   BACKUP - NOMES NÃO CONHECIDOS    -------- #
# RETIRAR TODAS AS PASTAS QUE NÃO TEM NOME RECONHECIDO #
lst_Nome_Cam = []
def Backup_OutOftheSystema(list_caminhos):
    # Retirando nomes errados em collection list_unofficial
    for itens_existentes in list_caminhos:
        # separando nome do caminho
        DirCam, Nome_Cam = os.path.split(itens_existentes)
        lst_Nome_Cam.append(Nome_Cam)

        # criando lista de nomes a serém ignorados
        nome_errado = list(set(df['wrong_name'].tolist()))
        nome_oficial = list(set(df['official_name'].tolist()))
        juntar_lst_ignorar = nome_errado + nome_oficial 

        # verificando se o nome do arquivo existe na lista de nomes a serão ignorados
        tmpw = np.array(lst_Nome_Cam)
        tmpz = np.array(juntar_lst_ignorar)
        lst_final_remove = list(set(np.setdiff1d(tmpw, tmpz)))

        # adicionando caminho ao item a ser removido do sistema
        Dir_lst_final_remove = [DirCam + '\\' + nome for nome in lst_final_remove]
        
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

# substituir os padrões combinados com os padrões de nomes
# %BASE_MEDIA_PATH% = ROOT
# %ITEM_COLLECTION_NAME% = ITEM_COLLECTION_NAME
# %ITEM_FILEPATH% = Retorne_ROM_do_XML(NomeDoArquivoSistemaXML)
def ConverterNomes(linhadotexto, systema):
    if '%RETROFE_PATH%' or '%BASE_MEDIA_PATH%' or '%ITEM_COLLECTION_NAME%' in linhadotexto:
        linhadotexto = '%RETROFE_PATH%'.replace('%RETROFE_PATH%', ROOT)
        linhadotexto = '%BASE_MEDIA_PATH%'.replace('%BASE_MEDIA_PATH%', ROOT + '\\collections\\' + systema + '\\medium_artwork\\')
        linhadotexto = '%ITEM_COLLECTION_NAME%'.replace('%ITEM_COLLECTION_NAME%', ROOT + '\\collections\\' + systema)     
    
    return linhadotexto

# ---------   CAMINHOS CONTIDOS NO SETTINGS    ---------- #
# RETORNAR OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE #

global LINHA_SETTINGS_LST
RETURN_SETTING = []
def Texto_InSettings(NomeDoSystema, texto, tipoArquivo):
    dir_pre_system, nome_system = os.path.split(NomeDoSystema)   # separando nome do systema
    INF_SETTINGS = ROOT + '\\collections\\' + nome_system + '\\' + tipoArquivo
    #print(NomeDoSystema, '>', tipoArquivo, '>', INF_SETTINGS)
    if os.path.isfile(str(INF_SETTINGS)) == True:

        if tipoArquivo == 'settings.conf':
            try:
                arquivo = open(str(INF_SETTINGS), 'r')
                for linha in arquivo:
                    if linha == "":
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\' + str(texto).replace('=', '').lstrip()
                        Inf_texto_proc = ""
                    if '#' + texto in linha:
                        LINHA_SETTINGS_LST = ROOT + '\\collections\\' + nome_system + '\\medium_artwork\\' + str(texto).replace('=', '').lstrip()
                        Inf_texto_proc = "#"
                    if texto + '= %ITEM_COLLECTION_NAME%' in linha:
                        LINHA_SETTINGS_LST = nome_system + str(texto).replace('=', '').lstrip()
                        Inf_texto_proc = "#"
                    elif texto in linha :
                        LINHA_SETTINGS_LST = ROOT + '\\' + linha.split('=')[1].replace('\n', '').lstrip() 
                        Inf_texto_proc = texto
                        #RETURN_SETTING.append(ROM_DIR_NO_SETTINGS_LST)
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
                #Inf_texto_proc = texto
                #for linha in LINHA_SETTINGS_LST_TMP:
                #    LINHA_SETTINGS_LST = linha.replace('\n', '').lstrip() 
                        #RETURN_SETTING.append(ROM_DIR_NO_SETTINGS_LST)
            except IOError:
                print('Erro ao ler arquivo de settings')
            finally:
                arquivo.close()
    else:   
        return 'Não existe arquivo de settings'
    return LINHA_SETTINGS_LST
    #print(LINHA_SETTINGS_LST, '>', texto, '<<< teste LINHA_SETTINGS_LST :', nome_system, '>', tipoArquivo )



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
                #print(f'Infor de {systemNameInstalado} > esta send lido nos arquivos no Dir = {systemXML}', ' <-linha 284')

                    tree = ET.parse(systemXML)
                    root = tree.getroot()
                    categorias = list(set([elem.tag for elem in root.iter()]))
                    ROMS_XML_LIST = [game.attrib['name'] for game in root.findall("./game")]
                        #DESCRIPTION_XML_LIST = [inf.text for inf in root.findall("./game/description")]
            return ROMS_XML_LIST

# ----------------------------------------------------------------------------- #
# localizar quais ROMS estão no XML e quais estão no Dir do SETTINGS e remover
# as não officiais #
#Retorne_ROM_do_XML(NomeDoArquivoSistemaXML)
# 1 - verificar se existe XML do sistema com o nome das ROMS
# 2 - verificar se existe Dir da ROMs do SETTINGS
# 3 - verificar se existe Dir da ROMs do SETTINGS

listNoRomReal = []
listRomexclude = []
listRominclude = []
def Backup_OutOftheROMPath(ListaDeSistemas, Termo_a_ser_procurado):
    for systemNameInstalado in ListaDeSistemas:
        # 1 ) verificar XML
        systemXML2 = ROOT + '\\meta\\hyperlist\\' + systemNameInstalado + '.xml' 
        if os.path.isfile(systemXML2) == True:
        # 2 ) verificar Dir do SETTINGS
            #Termo_a_ser_procurado = 'list.path ='
            DirROMSettings = Texto_InSettings(systemNameInstalado, Termo_a_ser_procurado,'settings.conf')
            #DirROMSettings = Texto_InSettings(systemNameInstalado, 'list.path =','settings.conf')
            #DirROMSettings = ConverterNomes(DirROMSettings, systemNameInstalado)
            
            if os.path.exists(DirROMSettings):
                DirCam, Folder = os.path.splitext(DirROMSettings)
                # 3 ) verificar se existe ROMS no Dir do SETTINGS
                listRomReal = os.listdir(DirROMSettings)
                for RomReal in listRomReal:
                    NoRomReal, ExtRom = os.path.splitext(RomReal)
                    listNoRomReal.append(NoRomReal)
                    #listNoRomReal = listNoRomReal[0:-1]

                    # verificar se existe exclude.txt ou include.txt
            if os.path.isfile(ROOT + '\\collections\\' + systemNameInstalado + '\\exclude.txt') == True:
                for Romexclude in Texto_InSettings(systemNameInstalado, '','exclude.txt'):
                    listRomexclude.append(Romexclude)

            if os.path.isfile(ROOT + '\\collections\\' + systemNameInstalado + '\\include.txt') == True:
                for Rominclude in Texto_InSettings(systemNameInstalado, '','include.txt'):
                    listRominclude.append(Rominclude)

                listRomIgnorar = ['default'] + listRomexclude + listRominclude
                listRomIgnorar = list(set(listRomIgnorar))
                listRomIgnorar = [x for x in listRomIgnorar if x != '']

                listRomIgnorarXML = Retorne_ROM_do_XML(systemNameInstalado)
                    
                listRomIgnorarAll = listRomIgnorarXML + listRomIgnorar
                # verificando se o nome do arquivo existe na lista de nomes a serão ignorados
                tmpw = np.array(listNoRomReal)
                tmpz = np.array(listRomIgnorarAll)
                lst_final_remove = list(set(np.setdiff1d(tmpw, tmpz)))
                
                print(DirROMSettings, ' << DirROMSettings e as ROMs >>' , lst_final_remove)
                print(DirROMSettings, '>', Termo_a_ser_procurado, '<<< teste DirROMSettings :', systemNameInstalado)
                print(yellow + 'Varrendo o systema instlado:'+ reset_color, systemNameInstalado)
                print(yellow + 'Caminho do Settings A:'+ reset_color, DirROMSettings)
                DirROMSettings = ConverterNomes(DirROMSettings, systemNameInstalado)
                print(yellow + 'Caminho do Settings B:'+ reset_color, DirROMSettings)
                print(yellow + 'Arquivos encontrados no caminho:'+ reset_color, listNoRomReal)
                    # adicionando caminho ao item a ser removido do sistema
                Dir_lst_final_remove = [DirCam + '\\' + nome + ExtRom for nome in lst_final_remove]
                for RomRemove in lst_final_remove:
                    DirRomRemove = DirCam + '\\' + RomRemove + ExtRom
                    DirRomRemove_dir = DirCam + '\\' + RomRemove
                    if os.path.isfile(DirRomRemove) == True:
                        Dir, nome = os.path.split(str(DirRomRemove))
                        old_end = DirRomRemove
                        new_tmp_end = Dir.replace(ROOT, (BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO))
                        new_end = new_tmp_end
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {old_end}  >Fazendo Back_Up> ROM Unofficialname = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {old_end}  >Forçando Back_Up> ROM Unofficialname = {new_end}')                
                            pass
                    elif os.path.isdir(DirRomRemove_dir) == True:
                        Dir, nome = os.path.split(str(DirRomRemove_dir))
                        old_end = DirRomRemove_dir
                        new_tmp_end = Dir.replace(ROOT, (BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO))
                        new_end = new_tmp_end
                        try:
                            os.makedirs(new_end)
                            shutil.move(old_end, new_end, copy_function=new_end)
                            print(f'folder {old_end}  >Fazendo Back_Up> ROM Folder Unofficialname = {new_end}')
                        except IOError:
                            move(old_end, new_end)
                            print(f'folder {old_end}  >Forçando Back_Up> ROM Folder Unofficialname = {new_end}')                
                        pass
        # ----------------------------------------------------------------------------- #

        # ----------------------------------------------------------------------------- #

# FUNÇÃO USADA PARA FAZER BACKUP DAS PASTAS ( CHAMADA NAS OUTRAS FUNÇÕES ) 
# Backup_default(caminho):
# RETIRAR TODAS AS PASTAS VAZIAS DO DIRETÓRIO   
# Backup_EmptyFolders():
#Backup_EmptyFolders()
#print(Backup_EmptyFolders())
#print('Backup_EmptyFolders')
# ----------------------------------------------------------------------------- #
# RETIRAR TODAS AS PASTAS QUE NÃO TEM NOME RECONHECIDO #
# Backup_OutOftheSystema(list_caminhos): # ITEMS_COLLECTION_DIR_NAME
#Backup_OutOftheSystema(ITEMS_COLLECTION_DIR_NAME)
#print(Backup_OutOftheSystema())
#print('Backup_OutOftheSystema')
# RETORNAR OS CAMINHOS ARMAZENADOS NO SETTINGS DO RETROFE #
# Texto_InSettings(list_caminhos, texto, tipoArquivo):
#Texto_InSettings(ITEMS_COLLECTION_DIR_NAME, 'list.path =', 'settings.conf')
#print(Texto_InSettings('Sega Master System', 'list.path =', 'settings.conf'), 'teste')
#print(Texto_InSettings(ITEMS_COLLECTION_DIR_NAME, 'list.path =', 'settings.conf'))
#print('Texto_InSettings', 'ok!!!!!!!!!!!!!!!!!!!!!!!!')
# LIMPAR ARQUIVOS DESNECESSÁRIOS   
# clean_list():
#clean_list()
#print(clean_list())
#print('clean_list')
# BUSCAR NOMES DAS ROMS NO ARQUIVO  #
# Retorne_ROM_do_XML(NomeDoArquivoSistemaXML): # ITEMS_COLLECTION_FILE_TXT
#Retorne_ROM_do_XML(ITEMS_COLLECTION_NAME)
#print(Retorne_ROM_do_XML('Sega Master System'))
#Retorne_ROM_do_XML(NomeDoArquivoSistemaXML)
# Backup_OutOftheROMPath(ListaDeSistemas):
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME)
#Backup_OutOftheROMPath(['Sega Master System'])
#print(Backup_OutOftheROMPath(['Sega Master System']))
#Backup_OutOftheArtwork_frontPath(['Sega Master System'])
#Backup_OutOftheArtwork_backPath(['Sega Master System'])
#Backup_OutOftheMedium_frontPath(['Sega Master System'])
#Backup_OutOftheMedium_backPath(['Sega Master System'])
#Backup_OutOftheScreenshotPath(['Sega Master System'])
#Backup_OutOftheScreentitlePath(['Sega Master System'])
#Backup_OutOftheFanartPath(['Sega Master System'])
#Backup_OutOftheLogoPath(['Sega Master System'])
#Backup_OutOftheVideoPath(['Sega Master System'])
#Backup_OutOftheStoryPath(['Sega Master System'])
#Backup_OutOftheAartwork_3dPath(['Sega Master System'])
#Backup_OutOftheBannerPath(['Sega Master System'])
#Backup_OutOftheBezelPath(['Sega Master System'])
#Backup_OutOftheCoverPath(['Sega Master System'])

#Backup_OutOftheROMPath(['Mame'])
#Backup_OutOftheArtwork_frontPath(['Mame'])
#Backup_OutOftheFanartPath(['Mame'])
#Backup_OutOftheLogoPath(['Mame'])
#Backup_OutOftheVideoPath(['Mame'])
Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'list.path')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.artwork_back')
Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.artwork_front')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.logo')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.medium_back')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.medium_front')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.screenshot')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.screentitle')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.video')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.system_artwork')
Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.fanart')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.story')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.artwork_3d')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.banner')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.bezel')
#Backup_OutOftheROMPath(ITEMS_COLLECTION_NAME, 'media.cover')

