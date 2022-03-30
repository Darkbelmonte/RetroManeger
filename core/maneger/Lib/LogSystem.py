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

import sys
sys.path  #executar um script python de um diretório dentro de outro script que está em outro diretório?
#import <arquivo>
#import arquivo.py
#sys.insert(1, os.getcwd()) 

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
# -----------------    LOG   ------------------ #
# ____   CONSTRUINDO LOG DE EXECUSÃO   ________ #
import logging

'''
   A formatação abaixo permite personalizarmos
   a forma como o log será mostrado para nós.
'''
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
'''
   Aqui definimos as configurações do modulo.

   filename = 'nome do arquivo em que vamos salvar a mensagem do log.'
   filemode = 'É a forma em que o arquivo será gravado.'
   level = 'Level em que o log atuará'
   format = 'Formatação da mensagem do log'
'''
logging.basicConfig(filename='exemplo.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

'''
   O objeto getLogger() permite que retornemos
   varias instancias de logs.
'''
# Instancia do objeto getLogger()
logger = logging.getLogger('root')

def fullname_LOG(primeiro_nome: str, segundo_nome: str) -> str:
    """
        Essa função recebe o primeiro nome e o segundo nome de uma pessoa e retorna o nome completo dela.
    """

    # Aqui, verificamos se os parametros passados são do tipo string (str)
    if isinstance(primeiro_nome, str) and isinstance(segundo_nome, str):
        logger.info(f'{primeiro_nome} {segundo_nome}')
        return primeiro_nome + segundo_nome
    else:
        logger.error(
            f'{primeiro_nome} type: {type(primeiro_nome)} - {segundo_nome} type: {type(segundo_nome)}'
        )
        
# -----------------    CAMINHOS   ------------------ #
# _________   DEFINIR LOCAIS DE ACESSO  ____________ #
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

# -----------------   FUNÇÃO   ------------------ #
# ________   RENAME GENERICO COM REPLCE  ________ #
# USANDO O Geral PARA RENOMAR OUTRAS PASTAS
def separar_nomearquivo(caminho):
    '''Recebe um endereço e retorna o nome do arquivo e sua extensão'''
    # apenas o nome com a extensão
    nome_arquivo = os.path.basename(caminho)
    # separa o nome e a extensão em uma tupla
    return os.path.splitext(nome_arquivo)

def listar_diretorios(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            #return path
            #print(path)
            return(path)
        else:
            listar_diretorios(path)

#print(listar_diretorios(currentdir))

def renamefoldes(caminho):
    for path, folders, files in tqdm(os.walk(currentdir, topdown=True), desc =" - Verificação Renomeando Arquivos"):
        for folder in folders:
            for erroName, offialName in zip(df['wrong_name'], df['official_name']):
                if erroName == folder:
                    old_file = os.path.join(path, [folder][0])
                    #print(old_file)
                    
                    for indice, elemento in enumerate(df['wrong_name']):
                        #print('indicet   | elemento')       # regra de formatação para impressão que diz para alinhar 
                        #print (f"{indice:<10}|{elemento}") # o índice a esquerda, com 10 espaços, com o uso do :<10 dentro da chave
                        #regra de formatação para fazer na horizontal
                        #print(f"Índices: {list(range(len(elemento)))}")
                        #print(f"Likes  : {elemento}")
                        if elemento == folder:
                            #print (f"{indice:<10}|{elemento}")
                            
                            for official_indice, official_elemento in enumerate(df['official_name']):
                                if elemento == folder and indice == official_indice:
                                    #print (f"{indice:<10}|{official_elemento}")
                                    
                                    old_file = os.path.join(path, folder)
                                    tmp_file = os.path.join(path, folder).replace(elemento, '_(C+Rtmp)_')
                                    new_file = tmp_file.replace('_(C+Rtmp)_', official_elemento)
                                    
                                    if old_file != new_file:

                                        print(f'folder index {indice} = {old_file}  >> name index = {official_indice} | {new_file}')
                                        try:
                                            os.rename(old_file, new_file)
                                        except:
                                            os.rename(old_file, new_file)
                                        pass
                                        try:
                                            os.rename(old_file, new_file)
                                        except:
                                            os.rename(old_file, new_file)
                                        pass

def renamefiles(caminho):                                    
    for path, folders, files in tqdm(os.walk(str(listar_diretorios(currentdir)), topdown=False), desc =" - Verificação Renomeando Arquivos"):
        for file in files:
            fileDivExt = separar_nomearquivo(file)
            fileNoExt = fileDivExt[0]
            Ext = fileDivExt[1]
            print(file)
            for erroName, offialName in zip(df['wrong_name'], df['official_name']):
                if erroName == fileNoExt:
                    for indice, elemento in enumerate(df['wrong_name']):
                        if elemento == fileNoExt:
                            for official_indice, official_elemento in enumerate(df['official_name']):
                                if elemento == fileNoExt and indice == official_indice:
                                    old_file = os.path.join(path, str(file))
                                    tmp_file = os.path.join(path, str(fileNoExt)).replace(elemento, '_(C+Rtmp)_')
                                    new_file = tmp_file.replace('_(C+Rtmp)_', str(official_elemento))
                                    #if not os.path.isfile(new_file) and os.path.exists(old_file):
                                    #if not os.path.isfile(new_file + str(Ext)):
                                        
                                    print(f'file index {indice} = {old_file}  >> name index = {official_indice} | {new_file + str(Ext)}') 

                                    try:
                                        os.rename(old_file, new_file + str(Ext))
                                    except:
                                        os.rename(old_file, new_file + str(Ext))
                                    pass
                                    try:
                                        os.rename(old_file, new_file + str(Ext))
                                    except:
                                        os.rename(old_file, new_file + str(Ext))
                                    pass  


#if(os.name == "nt"):
#    os.system("python3 covid19/san_covid19(Windows).py")
#else:
#    os.system("python3 covid19/'san_covid19(linux).py'")

#if __name__ == '__main__':
#    cmd = r"python /caminho/para/a/pasta/main.py -username abcd -password 1234"
#    subprocess.call(cmd, shell=True)
def main(args):
    print(__file__)
    print(os.path.abspath(os.path.dirname(__file__)))
 
    return 0
 
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    # Gerando um executável
    # Para gerar um executável digite no terminal:
    # pyinstaller --name exp1 --log-level DEBUG --onefile --clean  exp1.py

import os.path as op
def main(args):
 
    try:
        this_file = __file__
    except NameError:
        this_file = sys.argv[0]
 
    this_file = op.abspath(this_file)
 
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = op.dirname(this_file)
 
    print(application_path)
 
    return 0
 
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
