#encoding=utf-8 
from lxml import html
import popen2
import sqlite3
#import requests
import gl
import string
import sys
import webkit, gtk
import thread
import fusionyoudao
import fusionicb
import webshot
import record_xclip
import random
import os
from time import sleep
def inputconfig():
    while Alive :
  	  gl.prebaseurl = gl.baseurl
  	  conn = sqlite3.connect(gl.datadir)
  	  c = conn.cursor()
  	  c1 = conn.cursor()
  	  c.execute("select value from ItemTable where key = 'dict' ")
  	  c1.execute("select value from ItemTable where key = 'keyword' ")
  	  r= c.fetchone()
  	  r1= c1.fetchone()
  	  gl.baseurl= "".join(str(r[0]).split('\x00')) #str to string
  	  if(gl.prebaseurl !=gl.baseurl):
  	  	stext = "".join(str(r1[0]).split('\x00')) 
  	  	c.close()
  	  	c1.close()
  	  	conn.close
  	  	print stext 
  	  	os.system("/bin/echo -e  \'"+ stext  + "\' >> \'"+ gl.historydir + "\'")
          sleep(1)
def lookup():
    pre_text=""
    text=""
    #监视history.txt变化
    cmd = "tail -f " + gl.historydir 
    if(gl.baseurl==""):
        gl.baseurl=gl.baseurlyoudao
    myfile=os.popen(cmd)
    while True:
        text=myfile.readline().strip('\r\n\x00')
        if pre_text != text or gl.prebaseurl != gl.baseurl : # 或者不一定对lzt
            pre_text = text
            gl.prebaseurl =  gl.baseurl
            url= gl.baseurl + text                           #合成地址
            print url + "kkkkkkkkkkkk"                       #合成地址检测点1 
            os.system("curl -s -o \'" + gl.origindir +"\' \'" + url+ "\'")   #获得网页(非代理)
			#r = requests.get(url)                            #获得网页
			#doc = html.document_fromstring(r.text)
			#f_tar=open(gl.origindir,'w+')             #缓存原始网页
			#print >>f_tar,r.text
			#f_tar.close()
            #os.system("echo \"wait...\" > cache/result.html")         #清空最终缓冲增强程序稳健性
            if(gl.baseurl==gl.baseurlyoudao):
                fusionyoudao.reconstruct()                   #区分聚合
            if(gl.baseurl==gl.baseurlicb):
                fusionicb.reconstruct()
            gl.homeurl="file://" + gl.resultdir #合成最终缓冲访问地址
            window.load(gl.homeurl)                             #加载最终缓冲内容到浏览器
            window.show()                                    #显示结果

def webshow():
    global window
    global Alive
    window = webshot.Window()
    window.load(gl.homeurl)
    window.show() 
    gtk.main() 
    #Alive=0

def gettext():
    os.system("xclip -f /dev/null")           #清空剪切板
    os.system("/bin/echo "" > \'"+ gl.historydir + "\'")
    record_xclip.record_dpy.record_enable_context(record_xclip.ctx, record_xclip.record_callback)            
    record_xclip.record_dpy.record_free_context(record_xclip.ctx)

# Main thread
def main():

    #运行标志结束 
    global Alive
    Alive=1
    thread.start_new_thread(webshow,())
    sleep(0.1)
    thread.start_new_thread(gettext,())
    sleep(0.1)
    thread.start_new_thread(lookup,())
#sleep(1)
#thread.start_new_thread(inputconfig,())
    	
    while Alive:
        sleep(1)
        

    print 'All threads have terminated.'
if __name__ == '__main__':
    main()
