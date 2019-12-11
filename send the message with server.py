# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:14 2019

@author: mücahit
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""DATA-BASE"""

from tkinter import *

import sqlite3
import socket
import threading


con=sqlite3.connect("mesajlar.db")

im=con.cursor()

def TabloOlustur():
    im.execute("CREATE TABLE IF NOT EXISTS mesajlar(Mesajlar TEXT)")
    con.commit()

TabloOlustur()

#1-PENCERE OLUŞTURMA
pencere = Tk()

# 2-TİTLE OF WİNDOW
pencere.title("İNPUT THE MESSAGE")

#3-ekranı sınırlandırma
pencere.resizable(FALSE,TRUE)

#4-PENCERE KONUM
pencere.geometry("1200x800+350+50")

# KULLANICIDAN VERİ ALMA
etiket=Label(text="PLEASE , YOU WRİTE THE MESSAGE İN THİS SPACE TO SEND")
etiket.pack(anchor="w",padx=20)

veri=Entry(bg="white" , fg="green" ) #Veri Girmek 
veri.pack(ipadx=520 , ipady = 50 )  #Veriyi şekillendirmek
etiket.config(font=("Comic Sans MS",15,"bold"))


ListeKutusu=Listbox()
ListeKutusu.pack(ipadx=50 , ipady = 20,anchor="w",padx=35 )
ListeKutusu.insert(0,"MESSAGE GİVEN LİKE BELOW:")

def verikaydet():
    ListeKutusu.insert(END,veri.get())
    info=veri.get()
    im.execute("INSERT INTO Mesajlar(Mesajlar) VALUES('"+info+"')")
    con.commit() 

verikaydet()

buton3=Button(text="EKLE",command= verikaydet)
buton3.pack()

mainloop()  

"""Verileri Çekiyoruz"""

im.execute("SELECT * FROM Mesajlar")

veriler=im.fetchall()

boyut=len(veriler)
print(boyut)
    
blog_1=[]
blog_2=[]
blog_3=[]
i=0
while 1:
    if  i < boyut/5:
        blog_1  +=veriler[i]
        i=i+1
    elif boyut/5 <= i < boyut/3:
        blog_2 +=veriler[i]
        i=i+1
        
    elif boyut/3 <= i < boyut:
        blog_3 +=veriler[i]
        i=i+1
       
    else:
        break

print(blog_1)
print(blog_2)
print(blog_3)




mesajlar= blog_1 + blog_2 + blog_3


mesajlar1=bytes(str(mesajlar) , 'utf-8')



print('\n\n\nGidecek olan Mesaj:',mesajlar)

print("-----------------------------------------------------")


#mesajlar_1=[i.decode('utf-8' for i in mesajlar)]
#bytes(mesajlar[1],'utf-8')
#SERVER
"""
bind_ip='192.168.2.129'
bind_port=1234

#Create a TCP/IP socket
server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# bind the socket to the port
server.bind((bind_ip,bind_port))
# listen for incoming connections
server.listen(5)

print("[*] Listening on {}:{} " .format(bind_ip , bind_port))

def handle_client_connection(client_socket):
    request=client_socket.recv(1024)
    print("received {}".format(request))
    client_socket.send(mesajlar)
    client_socket.close()

while True:
    client,addr=server.accept()
    print("Accepted connection from {}:{} ".format(addr[0],addr[1]))
    client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client),) 
    client_handler.start()

"""

#CLİENT
"""TCP ile veri gönderme"""
"""
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#GÖNDEREN VE ALAN

TCP_IP='192.168.2.129'
TCP_PORT=55857
adress=(TCP_IP , TCP_PORT)
#client.connect((target,port))
client.connect(adress)
client.sendall(b'hello , world')
while True:
    
    addr=client.recv(1024)
    if not addr:
        break
    client.sendall(addr)
print(addr)

"""


HOST = '192.168.2.51'  # The server's hostname or IP address
PORT = 8080  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mesajlar1)
    data = s.recv(1024)
    print('Received:', repr(data))
         
    
s.close()









