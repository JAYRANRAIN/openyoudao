import os
import sys
import sqlite3
global keywordtext
global baseurl
#global lock
global prebaseurl
global homedir
global datadir
global historydir
global origindir
global resultdir
global url
global homeurl
global headyoudao
global bodystartyoudao
global bodystarticb
global bodyendicb
global headicb
keywordtext = ""
baseurl=""
#lock=0
datadir=os.path.expanduser('~') + "/.local/share/webkit/databases/file__0.localstorage"
prebaseurl=""
url=""
#homedir = os.getcwd()
homedir = sys.path[0]
historydir = homedir + "/cache/history.cache"
origindir = homedir + "/cache/origin.html"
resultdir = homedir + "/cache/result.html"
headyoudao = homedir + "/cache/construction/youdao/head.html"
headicb = homedir + "/cache/construction/icb/head.html"
bodystartyoudao = homedir + "/cache/construction/youdao/body-start.txt"
bodystarticb = homedir + "/cache/construction/icb/body-start.txt"
bodyendicb = homedir + "/cache/construction/icb/body-end.txt"
homeurl = "file://" + homedir + "/cache/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
baseurlicb="http://www.iciba.com/"
