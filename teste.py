#!/usr/bin/env python
import datetime
import requests
import socket

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

today = datetime.datetime.today()

values = {
    "nome": f"Tem_Internet__{is_connected()}___Produto_teste_data____{today:%d_%B_%Y__%H_h_%M_m_%S_s}",
}


headers = {
  'Content-Type': 'application/json'
}
request = requests.post('http://requestbin.net/r/1boo5tx1', data=values)
request

