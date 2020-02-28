
import paramiko
import os

ip = '192.168.1.13'
user  = 'root'
passwd    = 'nepe'
port   = 2222 
comando      = 'ls'
 
conexion = paramiko.Transport((ip, port))
conexion.connect(username = user, password = passwd)
 
canal = conexion.open_session()
canal.exec_command(comando)
 
salida = canal.makefile('rb', -1).readlines()
if salida:
	print salida
else:
	print canal.makefile_stderr('rb', -1).readlines()
conexion.close()