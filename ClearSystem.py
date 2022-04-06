# Programa para limpar a estrutura do RetroFe
# Retirada de arquivos não uteis
# declarando libs
import os
import shutil
from shutil import move
from tkinter.messagebox import NO
import pandas as pd  # para ler, visualizar e printar infos do df
import os.path
from datetime import date
from datetime import datetime
import numpy as np 
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
ITEMS_LAYOUTS_NAME = [f for f in os.listdir(ROOT + '\\layouts\\') if os.path.exists(ROOT + '\\layouts\\') if os.path.isdir(ROOT + '\\layouts\\')]
ITEMS_LAYOUTS_DIR_COLLECTION = list(set([os.path.join(ROOT + '\\layouts\\' + file + '\\collections') for file in ITEMS_LAYOUTS_NAME if os.path.exists(ROOT + '\\layouts\\' + file + '\\collections') if os.path.isdir(ROOT + '\\layouts\\' + file + '\\collections')]))

EMPTY = []

# _________   CRIAÇÃO DO DATAFRAME  ________________ #
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

# verificar se todos os arquivos old_file foram movidos para new_file, caso não tenha sido movido, mover para pasta de BACKUP
def Backup_default(caminho):
    if os.path.isfile(ROOT + '\\' + caminho) and os.path.exists(ROOT + '\\' + caminho):
        old_end = ROOT + '\\' + caminho
        dir_tmp, arquivo = os.path.split(caminho) 
        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp + '\\'
        try:
            os.makedirs(new_end)
            shutil.move(old_end, new_end, copy_function=new_end)
            print(f'folder {old_end}  >Fazendo Back_Up> name = {new_end}')
        except IOError:
            print(f'folder {old_end}  >Erro e forçando Back_Up> name = {new_end}')
            move(old_end, new_end)
        pass


    elif os.path.isdir(caminho) and os.path.exists(caminho):
        old_end = caminho 
        dir_tmp = caminho.split('\\', 0)[-1] 
        new_end = BACKUP_DIR + '\\' + DATA_HORA_ATUAIS_FORMATADO + '\\' + dir_tmp
        try:
            os.makedirs(new_end)
            shutil.move(old_end, new_end, copy_function=new_end)
            #print(f'folder {old_end}  >Fazendo Back_Up> name = {new_end}')
        except IOError:
            #print(f'folder {old_end}  >Erro e dorçando Back_Up> name = {new_end}')
            move(old_end, new_end)
        pass


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
            #print('remover pasta para backup -> ', error)
        pass
        # print(emptybackupDir, 'emptybackupDir')

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
                print(f'folder {nome_remove}  >Fazendo Back_Up> name = {new_end}')
            except IOError:
                print(f'folder {nome_remove}  >Erro e forçando Back_Up> name = {new_end}')
                move(nome_remove, new_end)
            pass



# função para renomear os nomes com base na verificação se existe o nome no wrongmName para o systemName
def clean_list():
    for dirremove, remove, emul, systema in zip(dirclean, limpar, emulador, categoria):
        Backup_default(str(dirremove))


# excutar funções de limpeza do sistema

clean_list()
Backup_OutOftheSystema(ITEMS_COLLECTION_DIR_NAME)
Backup_OutOftheSystema(ITEMS_EMULATORS_DIR_NAME)
Backup_OutOftheSystema(ITEMS_LAYOUTS_DIR_COLLECTION)
Backup_EmptyFolders()

