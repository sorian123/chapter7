import pyscreenshot as ImageGrab
import time


def run(**args):
	cs=ImageGrab.grab()
	return cs
	filename=time.strftime("%Y-%m-%d-%H:%M:%S")
	ImageGrab.grab().save(filename, "JPEG")
	ss=open(filename, 'rb')
	jk=ss.read(2000000)
	ss.close()
	return jk

def xx():
	a=1
	return a
