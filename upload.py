from ftplib import FTP
import os
import time
import datetime
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

upload_ftp=config['FTP']['upload_ftp']



try:
	upload_ftp=config['FTP']['upload_ftp']
	upload_user = config['FTP']['upload_user']
	upload_password = config['FTP']['upload_password']

	path_imagem_origem = config['FTP']['path_imagem_origem']
	path_imagem_destino = config['FTP']['path_imagem_destino']

except:
	raise Exception('Dados de FTP não informados.')



ftp = FTP(upload_ftp,upload_user,upload_password,timeout=10000)

files =os.listdir(path_imagem_origem)

for imagem in files:

	f = open(path_imagem_origem + '/'+imagem, 'r')

	ftp.storbinary("STOR "+path_imagem_destino+"/new-imagem-temp.jpg",f)
	ftp.rename(path_imagem_destino+'/new-imagem-temp.jpg',path_imagem_destino+'/'+imagem)

	os.remove(path_imagem_origem+'/'+imagem)

ftp.close()

print 'FIM';