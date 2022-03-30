# Programa para limpar a estrutura do RetroFe
# Retirada de arquivos não uteis

import os
import shutil
import zipfile

# ----------------- Manipular CSV ------------------ #
# _________     IMPORTAR ARQUIVOS   ________________ #
currentdir = os.getcwd()
filecsv_namefix = currentdir + '\\core\\maneger\\Data\\datadir.csv'
filecsv_nametemp = currentdir + '\\core\\maneger\\Data\\datadir_temp.csv'
listcsv_clean = currentdir + '\\core\\maneger\\Data\\cleandir.csv'
listcsv_cleantemp = currentdir + '\\core\\maneger\\Data\\cleandir_temp.csv'

systemNameReal = os.listdir(currentdir + '\\collections\\')
#print(systemNameReal)

layoutName = [linha for linha in os.listdir(currentdir + '\\layouts\\')]
#print(layoutName)

def make_path_fake():
    for layout_name in layoutName:
        print(layout_name)
        try:
            os.makedirs(currentdir + '\\collections\\')
            os.makedirs(currentdir + '\\layouts\\')
            os.makedirs(currentdir + '\\collections\\' + 'nes')
            os.makedirs(currentdir + '\\collections\\' + 'sms')
            os.makedirs(currentdir + '\\collections\\' + 'pce')
            os.makedirs(currentdir + '\\collections\\' + 'nes' + '\\roms\\')
            os.makedirs(currentdir + '\\collections\\' + 'sms' + '\\roms\\')
            os.makedirs(currentdir + '\\collections\\' + 'pce' + '\\roms\\')
        except OSError as error:
            #print('Remover arquivos desnecessários -> ', error)
            print()
        pass
        try:
            os.makedirs(currentdir + '\\layouts\\' + layout_name + '\\collections\\')
            print(currentdir + '\\layouts\\' + layout_name + '\\collections\\')
            os.makedirs(currentdir + '\\layouts\\' + 'str(layout_name_A)' + '\\collections')
            os.makedirs(currentdir + '\\layouts\\' + 'str(layout_name_B)' + '\\collections')
            os.makedirs(currentdir + '\\layouts\\' + 'str(layout_name_C)' + '\\collections')
            os.makedirs(currentdir + '\\layouts\\' + str(layout_name) + '\\collections')
            os.makedirs(currentdir + '\\layouts\\' + str(layout_name) + '\\collections\\' + '\\sms\\')
            os.makedirs(currentdir + '\\layouts\\' + str(layout_name) + '\\collections\\' + '\\msx\\')
            os.makedirs(currentdir + '\\layouts\\' + str(layout_name) + '\\collections\\' + '\\snes\\')
        except OSError as error:
            #print('Remover arquivos desnecessários -> ', error)
            print()
        pass

def make_path_fake_sys_real():
    try:
        nome_arquivo = currentdir + '\\collections\\' + systemNameReal + '\\roms\\' + 'arq01.txt'
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(u'Arquivo criado pois nao existia')
    #faca o que quiser
    arquivo.close()
    for sysname in systemNameReal:
        print(sysname)
        try:
            arquivo = open(currentdir + '\\collections\\' + systemNameReal + '\\roms\\' + 'arq01.txt','w')
            arquivo.write("Bóson Treinamentos\n")
            arquivo.write("Criando um arquivo de texto com Python\n")
            arquivo.write("Arquivo criado por Fábio dos Reis\n")
            arquivo.write("É isso ai pessoal!\n")
            arquivo.close()
        except OSError as error:
            #print('Remover arquivos desnecessários -> ', error)
            print()
        pass
        fake_fileDir = (currentdir + '\\collections\\' + systemNameReal + '\\roms\\')
        print(fake_fileDir)
        try:
            shutil.make_archive(fake_fileDir + 'teste_fake_rom', 'zip', fake_fileDir, 'arq01.txt')
            shutil.make_archive(fake_fileDir + 'teste_fake_rom_2', 'zip', fake_fileDir, 'arq01.txt')
        except OSError as error:
            #print('Remover arquivos desnecessários -> ', error)
            print()
        pass
    
def make_fake_text():
    # Criando e escrevendo em arquivos de texto (modo 'w').
    arquivo = open(currentdir + '\\collections\\' + 'pce' + '\\roms\\' + 'arq01.txt','w')
    arquivo.write("Bóson Treinamentos\n")
    arquivo.write("Criando um arquivo de texto com Python\n")
    arquivo.write("Arquivo criado por Fábio dos Reis\n")
    arquivo.write("É isso ai pessoal!\n")
    arquivo.close()

    arquivo = open(currentdir + '\\collections\\' + 'sms' + '\\roms\\' + 'arq02.txt','w')
    arquivo.write("Bóson Treinamentos\n")
    arquivo.write("Criando um arquivo de texto com Python\n")
    arquivo.write("Arquivo criado por Fábio dos Reis\n")
    arquivo.write("É isso ai pessoal!\n")
    arquivo.close()

    arquivo = open(currentdir + '\\collections\\' + 'nes' + '\\roms\\' + 'arq03.txt','w')
    arquivo.write("Bóson Treinamentos\n")
    arquivo.write("Criando um arquivo de texto com Python\n")
    arquivo.write("Arquivo criado por Fábio dos Reis\n")
    arquivo.write("É isso ai pessoal!\n")
    arquivo.close()

pce = currentdir + '\\collections\\' + 'pce' + '\\roms\\'
sms = currentdir + '\\collections\\' + 'sms' + '\\roms\\'
nes = currentdir + '\\collections\\' + 'nes' + '\\roms\\'
print(pce)
def make_zip_rom_fake_1():
    shutil.make_archive('final', 'zip', pce, 'arq01.txt')
    shutil.make_archive('final', 'zip', sms, 'arq02.txt')
    shutil.make_archive('final', 'zip', nes, 'arq03.txt')
    
    shutil.make_archive('teste_fake_rom', 'zip', pce, 'arq01.txt')
    shutil.make_archive('teste_fake_rom', 'zip', sms, 'arq02.txt')
    shutil.make_archive('teste_fake_rom', 'zip', nes, 'arq03.txt')
    
    shutil.make_archive(pce + '1943 Kai (Japan)', 'zip', pce, 'arq01.txt')
    shutil.make_archive(pce + 'Adventure Island (Japan)', 'zip', pce, 'arq01.txt')
    shutil.make_archive(pce + 'After Burner II (Japan)', 'zip', pce, 'arq01.txt')
    
    shutil.make_archive(sms + '20 em 1 (Brazil)', 'zip', sms, 'arq02.txt')
    shutil.make_archive(sms + 'Action Fighter (USA, Europe)', 'zip', sms, 'arq02.txt')
    shutil.make_archive(sms + 'Addams Family, The (Europe)', 'zip', sms, 'arq02.txt')
    
    shutil.make_archive(nes + '10-Yard Fight (USA, Europe)', 'zip', nes, 'arq03.txt')
    shutil.make_archive(nes + '1943 - The Battle of Midway (USA)', 'zip', nes, 'arq03.txt')
    shutil.make_archive(nes + '720 Degrees (USA)', 'zip', nes, 'arq03.txt')

   

make_path_fake()
#make_fake_text()
#make_zip_rom_fake_1()
#make_path_fake_sys_real()