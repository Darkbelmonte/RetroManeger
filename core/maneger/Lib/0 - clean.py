# Programa para limpar a estrutura do RetroFe
# Retirada de arquivos não uteis

import os
import shutil
import pandas as pd  # para ler, visualizar e printar infos do df

# ----------------- Informações ------------------ #
# _________            INICIAIS     ______________ #
print()
print('INFO SCRIPT')
print('Sript excutado :', os.path.basename(__file__))
print('Localização :', (__file__))
print()
# Para obter o caminho absoluto
dir_path = os.path.dirname(os.path.realpath(__file__))
# Para obter o caminho relativo:
cwd = os.getcwd()
#cd (f'{os.getcwd()}')

# ----------------- Manipular CSV ------------------ #
# _________     IMPORTAR ARQUIVOS   ________________ #
currentdir = os.getcwd()
filecsv_namefix = currentdir + '\\core\\maneger\\Data\\datadir.csv'
filecsv_nametemp = currentdir + '\\core\\maneger\\Data\\datadir_temp.csv'
listcsv_clean = currentdir + '\\core\\maneger\\Data\\cleandir.csv'
listcsv_cleantemp = currentdir + '\\core\\maneger\\Data\\cleandir_temp.csv'
dir_data_CSV = currentdir + '\\core\\maneger\\Data\\'
listcsv_inf_sys_data = currentdir + '\\core\\maneger\\Data\\inf_sys_data.csv'

# -------------------   FUNÇÃO   ------------------- #
# ----------------- Manipular CSV ------------------ #
# _________     IMPORTAR ARQUIVOS   ________________ #
def file_backup(file_a):
    file_temp = str(file_a).replace('.csv', '_temp.csv')
    if os.path.isfile(file_temp):
        try:
            os.remove(file_temp)
        except IOError:
            print(u'Arquivo Base CSV não encontrado!', file_temp, '\n','Vamos fazer a partir do original :', file_a)
            #print(filecsv_nametemp)
    if not os.path.isfile(file_temp):
        try:
            shutil.copyfile(file_a, file_temp)
        except IOError:
            print(u'Arquivo  Base CSV não encontrado!')
# ----------------- USO DO PANDAS ------------------ #
# _________   CRIAÇÃO DO DATAFRAME  ________________ #
# Pd de nomes errados x officiais
file_backup(filecsv_namefix)
df = pd.read_csv(filecsv_nametemp, encoding='latin-1', sep=';')

df.dropna(subset=['official_name'])
wrongmName = list(set(df['wrong_name'].tolist()))
systemName = list(set(df['official_name'].tolist()))

cdf = pd.read_csv(listcsv_cleantemp, encoding='latin-1', sep=';')
#print(cdf)
# Retirando nomes errados em collection
lixo = list(set(cdf['file'].tolist()))

def remove_lixo():
    for removelixo in lixo:
        try:
            os.remove(currentdir + '\\collections\\' + str(removelixo))
            os.remove(currentdir + '\\' + str(removelixo))
            os.remove(currentdir + '\\layouts\\' +  str(removelixo))
        except OSError as error:
            print('Remover arquivos desnecessários -> ', error)
        pass

remove_lixo()