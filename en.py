import base64
import os

xx=os.listdir("data")
print(len(xx))
for s in range(1,len(xx)-1):
	print(xx[s])
	k=os.listdir("data/" + xx[s])

	for q in range(0,len(k)-1):
		z=open('data/' + xx[s] + '/' + k[q], 'rb')
		x=z.read(10000)
		j=base64.b64decode(x)
		z.close()
		f=open('/root/datas/' + k[q], 'wb')
		f.write(j)
		f.close()

