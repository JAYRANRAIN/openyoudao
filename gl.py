#encoding=utf-8
import os
import sys
global pre_text
global homedir
global origindir
global resultdir
global homeurl
global headyoudao
global bodystartyoudao

pre_text=""
cnt=0
userdir=os.path.expanduser('~')
cachedir = userdir + "/.openyoudao"
subcachedir = userdir + "/.openyoudao/cache"
logname = userdir + "/.openyoudao/openyoudao.log"
workdir = os.getcwd()
homedir = sys.path[0]
origindir = cachedir + "/origin.html"
resultdir = cachedir + "/result.html"
headyoudao = "/usr/share/openyoudao/construction/youdao/head.html"
bodystartyoudao = "/usr/share/openyoudao/construction/youdao/body-start.txt"
homeurl = "file:///home/bjzhangxin/.openyoudao/main.html"
indexurl = "file:///home/bjzhangxin/.openyoudao/index.html"
baseurlyoudao="http://dict.youdao.com/search?q="
