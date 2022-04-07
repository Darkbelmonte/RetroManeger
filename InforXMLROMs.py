# -*- coding: utf-8 -*-
# manipular aquivos de texto no xml da pasta meta no hyperlist
import xml.etree.ElementTree as ET
import xml.sax
import os
import pandas as pd
# ---------------------- DEFINIÇÃO DE CORES ---------------------- #
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
# informações do script
print(cyan + '*--- INFO SCRIPT : ', os.path.basename(__file__).split('.')[0].upper(), '----------------------------------*' + reset_color)
print(blue + '| Sript excutado : ' + reset_color, yellow +  os.path.basename(__file__) + reset_color)
print(blue + '| Localização : ' + reset_color,  yellow +  (__file__) + reset_color)
print(cyan + '*---------------------------------------------------------------*' + reset_color)
# ----------------- DEFINIÇÃO DO DIRETÓRIO ROOT ------------------ #
# idenfificar o diretório do projeto e definir que o diretório ROOT sempre será o root + '/core'
ROOT = os.path.dirname(os.path.abspath(__file__)) if 'core' in os.listdir(os.path.dirname(os.path.abspath(__file__))) else "\\".join(((os.path.realpath(__file__)).split('\\', -1)[0:3]))
DATA_MANEGER_DATA = ROOT + '\\core\\maneger\\' + 'Data\\'
FILE_CSV_DIR_NAME_SYSTEM = DATA_MANEGER_DATA + 'DirSystem.csv'
FILE_CSV_FIX_NAME_SYSTEM = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem.csv'
FILE_CSV_FIX_NAME_SYSTEM_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameSystem_Tmp.csv'
FILE_CSV_FIX_NAME_CLEAN = ROOT + '\\core\\maneger\\Data\\Fix_NameClean.csv'
FILE_CSV_FIX_NAME_CLEAN_TMP = ROOT + '\\core\\maneger\\Data\\Fix_NameClean_Tmp.csv'
# importar CSV com os nomes dos sistemas da pasta FILE_CSV_DIR_NAME_SYSTEM e retornar um dataframe
DirSystem_df = pd.read_csv(FILE_CSV_DIR_NAME_SYSTEM, sep=';', encoding='utf-8')
ITEMS_META_FILE_XML_LIST = list(set(DirSystem_df['ITEMS_META_FILE_XML'].tolist()))
#ITEMS_LAYOUTS_FILE_XML = list(set(DirSystem_df['ITEMS_LAYOUTS_FILE_XML'].tolist()))

ITEMS_COLLECTION_FILE_BAT = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_BAT'].tolist()))
ITEMS_EMULATORS_FILE_BAT = list(set(DirSystem_df['ITEMS_EMULATORS_FILE_BAT'].tolist()))
ITEMS_COLLECTION_FILE_CONTENT_BAT = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_CONTENT_BAT'].tolist()))

ITEMS_COLLECTION_FILE_SUB = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_SUB'].tolist()))
ITEMS_COLLECTION_FILE_TXT = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_TXT'].tolist()))
ITEMS_COLLECTION_FILE_CONF = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_CONF'].tolist()))
ITEMS_COLLECTION_FILE_CONTENT_TXT = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_CONTENT_TXT'].tolist()))
ITEMS_COLLECTION_FILE_CONTENT_SUB = list(set(DirSystem_df['ITEMS_COLLECTION_FILE_CONTENT_SUB'].tolist()))
ITEMS_EMULATORS_FILE_INI = list(set(DirSystem_df['ITEMS_EMULATORS_FILE_INI'].tolist()))
ITEMS_EMULATORS_FILE_CFG = list(set(DirSystem_df['ITEMS_EMULATORS_FILE_CFG'].tolist()))
ITEMS_EMULATORS_FILE_LPL = list(set(DirSystem_df['ITEMS_EMULATORS_FILE_LPL'].tolist()))
ITEMS_LAUNCHERS_FILE_CFG = list(set(DirSystem_df['ITEMS_LAUNCHERS_FILE_CFG'].tolist()))
ITEMS_ROCKETLAUNCHER_SETTINGS_NAME = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_SETTINGS_NAME'].tolist()))

ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_SETTINGS_INI'].tolist()))
ITEMS_ROCKETLAUNCHER_FILE_DATA_INI = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_DATA_INI'].tolist()))
ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_GAMEINFO_INI'].tolist()))
ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_HISTORY_INI'].tolist()))
ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_LANGUAGE_INI'].tolist()))
ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_MOVESLIST_DAT'].tolist()))
ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_FILE_STATISTICS_INI'].tolist()))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_TXT = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_TXT'].tolist()))
ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_TXT = list(set(DirSystem_df['ITEMS_ROCKETLAUNCHER_DIR_MEDIA_ROM_DIR_CONTENT_ROMNAME_CONTENT_TXT'].tolist()))
# definição das variáveis globais
global SettingsRomPath
lromName = []
lstoryfile = []
lCurrentData = []
ltype = []
lformat = []
lyear = []
lrating = []
lstars = []
ldescription = []
lstory = []
lmanufacturer = []
lyear = []
lgenre = []
lrating = []
lplayers = []
lctrltype = []
lbuttons = []
ljoyways = []
lscore = []
lcloneof = []
lcrc = []
lplaycount = []
llastplayed = []
ldesc = []
lpublisher = []
ldeveloper = []
lreleasedate = []
lfavorite = []
lhidden = []
lkidgame = []
lpath = []
lname = []

# identificar game em xml no diretório meta
def get_game_xml(path_xml):
    # identificar o game em xml no diretório meta
    tree = ET.parse(path_xml)
    root = tree.getroot()
    game = root.find('description')
    return game



class XLSHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
        self.story = ""
        self.manufacturer = ""
        self.year = ""
        self.genre = ""
        self.rating = ""
        self.players = ""
        self.ctrltype = ""
        self.buttons = ""
        self.joyways = ""
        self.score = ""
        self.cloneof = ""
        self.crc = ""
        self.playcount = ""
        self.lastplayed = ""
        self.desc = ""
        self.publisher = ""
        self.developer = ""
        self.releasedate = ""
        self.favorite = ""
        self.hidden = ""
        self.kidgame = ""
        self.path = ""
        self.name = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if (tag == "game"):
            romName = attributes["name"]
            lromName.append(romName)
            storyfile = (romName + "." + "txt")
            lstoryfile.append(storyfile)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "type":
            type_xls = self.type
            ltype.append(type_xls)
        elif self.CurrentData == "format":
            format_xls = self.format
            lformat.append(format_xls)
        elif self.CurrentData == "year":
            year_xls = self.year
            lyear.append(year_xls)
        elif self.CurrentData == "rating":
            rating_xls = self.rating
            lrating.append(rating_xls)
        elif self.CurrentData == "stars":
            stars_xls = self.stars
            lstars.append(stars_xls)
        elif self.CurrentData == "description":
            description_xls = self.description
            ldescription.append(description_xls)
        elif self.CurrentData == "story":
            lstory.append(self.story)

            #print('B ',self.story)
            #print(lstory)

        elif self.CurrentData == "manufacturer":
            manufacturer_xls = self.manufacturer
            lmanufacturer.append(manufacturer_xls)
        elif self.CurrentData == "genre":
            genre_xls = self.genre
            lgenre.append(genre_xls)
        elif self.CurrentData == "players":
            players_xls = self.players
            lplayers.append(players_xls)
        elif self.CurrentData == "ctrltype":
            ctrltype_xls = self.ctrltype
            lyear.append(ctrltype_xls)
        elif self.CurrentData == "buttons":
            buttons_xls = self.buttons
            lbuttons.append(buttons_xls)
        elif self.CurrentData == "joyways":
            joyways_xls = self.joyways
            ljoyways.append(joyways_xls)
        elif self.CurrentData == "cloneof":
            cloneof_xls = self.cloneof
            lyear.append(cloneof_xls)
        elif self.CurrentData == "crc":
            crc_xls = self.crc
            lcrc.append(crc_xls)
        elif self.CurrentData == "playcount":
            playcount_xls = self.playcount
            lplaycount.append(playcount_xls)
        elif self.CurrentData == "lastplayed":
            lastplayed_xls = self.lastplayed
            llastplayed.append(lastplayed_xls)
        elif self.CurrentData == "desc":
            desc_xls = self.desc
            ldesc.append(desc_xls)
        elif self.CurrentData == "publisher":
            publisher_xls = self.publisher
            lpublisher.append(publisher_xls)
        elif self.CurrentData == "developer":
            developer_xls = self.developer
            ldeveloper.append(developer_xls)
        elif self.CurrentData == "releasedate":
            releasedate_xls = self.releasedate
            lreleasedate.append(releasedate_xls)
        elif self.CurrentData == "favorite":
            favorite_xls = self.favorite
            lfavorite.append(favorite_xls)
        elif self.CurrentData == "hidden":
            hidden_xls = self.hidden
            lhidden.append(hidden_xls)
        elif self.CurrentData == "kidgame":
            kidgame_xls = self.kidgame
            lkidgame.append(kidgame_xls)
        elif self.CurrentData == "path":
            path_xls = self.path
            lpath.append(path_xls)
        elif self.CurrentData == "name":
            name_xls = self.name
            lname.append(name_xls)
        elif self.CurrentData == "score":
            score_xls = self.score
            lscore.append(score_xls)
        elif self.CurrentData == "story":
            story_xls = self.story
            lstory.append(story_xls)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content
        elif self.CurrentData == "story":
            self.story = content
        elif self.CurrentData == "manufacturer":
            self.manufacturer = content
        elif self.CurrentData == "genre":
            self.genre = content
        elif self.CurrentData == "players":
            self.players = content
        elif self.CurrentData == "ctrltype":
            self.ctrltype = content
        elif self.CurrentData == "buttons":
            self.buttons = content
        elif self.CurrentData == "joyways":
            self.joyways = content
        elif self.CurrentData == "cloneof":
            self.cloneof = content
        elif self.CurrentData == "crc":
            self.crc = content
        elif self.CurrentData == "playcount":
            self.playcount = content
        elif self.CurrentData == "lastplayed":
            self.lastplayed = content
        elif self.CurrentData == "desc":
            self.desc = content
        elif self.CurrentData == "publisher":
            self.publisher = content
        elif self.CurrentData == "developer":
            self.developer = content
        elif self.CurrentData == "releasedate":
            self.releasedate = content
        elif self.CurrentData == "favorite":
            self.favorite = content
        elif self.CurrentData == "hidden":
            self.hidden = content
        elif self.CurrentData == "kidgame":
            self.kidgame = content
        elif self.CurrentData == "path":
            self.path = content
        elif self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "score":
            self.score = content

for systemXML in ITEMS_META_FILE_XML_LIST:
    if os.path.isfile(str(systemXML)) == True:
         # create an XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        # override the default ContextHandler
        Handler = XLSHandler()
        parser.setContentHandler(Handler)
        parser.parse(str(systemXML))

# ler informações dos arquivos .conf , .txt e .bat 
def ler_arquivos_TXT(caminho_arquivo):
    if os.path.isfile(str(caminho_arquivo)) == True:
        arquivo = open(str(caminho_arquivo), 'r')
        linhas = arquivo.readlines()
        arquivo.close()
        return linhas


for linha in ITEMS_COLLECTION_FILE_CONF:
    print(linha)
    print(ler_arquivos_TXT(linha))

