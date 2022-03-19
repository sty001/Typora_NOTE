"""
webserver.py
用python实现一个HTTP Web服务器，她知道如何运行服务器端CGI脚本；
从当前工作目录提供文件和脚本、，python脚本必须存储在webdir\cgi-bin或webdir\htbin中；
"""

import os,sys
from http.server import HTTPServer, CGIHTTPRequestHandler
webdir='.'
port=80

os.chdir(webdir)
srvradder=("",port)
srvrobj=HTTPServer(srvradder,CGIHTTPRequestHandler)
srvrobj.serve_forever()