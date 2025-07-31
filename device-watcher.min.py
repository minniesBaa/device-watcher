K=False
H=None
from zeroconf import Zeroconf as L,ServiceBrowser as I
import time as J,sys as A,os
D=0
C={}
E=K
F=H
B=H
G=H
class M:
	def remove_service(I,zeroconf,type,name):
		F=name;global D;global E;global B;global C;global G
		if B is not H:
			if F==G:A.stdout.write(f"\rDevice status: ⡢⡂ offline ");A.stdout.flush()
			return
		if E:
			if any(F in A for A in C.values()):E=K;P(F)
	def add_service(I,zeroconf,type,name):
		E=name;global D;global B;global G;F=zeroconf.get_service_info(type,E)
		if F:
			H=F.parsed_addresses()[0]
			if H not in C.keys():C[H]=[E]
			else:C[H].append(E);D+=1
			if B:
				if F.parsed_addresses()[0]==B:G=E;A.stdout.write(f"\rDevice status: ⢄⠔ online ");A.stdout.flush()
	def update_service(A,zeroconf,type,name):0
class N:
	def __init__(A,zc):A.zc=zc;A.svc={}
	def remove_service(A,zeroconf,type,name):
		B=name
		if B in A.svc:A.svc[B].cancel();del A.svc[B]
	def add_service(A,zeroconf,type,name):
		B=name
		if B not in A.svc:A.svc[B]=I(A.zc,B,M())
	def update_service(A,zeroconf,type,name):0
def O():
	global D;global F;global E
	if os.name=='nt':C=os.system('cls')
	else:C=os.system('clear')
	F=L();G=N(F);K=I(F,'_services._dns-sd._udp.local.',G);B=['⣏⣸','⣏⣱','⣏⣩','⣏⣙','⣏⡹','⣏⢹','⡏⣹','⢏⣹','⣋⣹','⣍⣹','⣎⣹','⣇⣹'];B.extend(B);B.extend(B)
	for H in B:A.stdout.write(f"\r{H} Searching for your device. Make sure it is open/unlocked. {D} devices found");A.stdout.flush();J.sleep(.2)
	if D>0:A.stdout.write('\rNow close/lock your device.                                                               ');A.stdout.flush()
	E=True
	while True:J.sleep(20)
def P(d):
	global B;global C
	for(D,E)in C.items():
		if d in E:B=D
	A.stdout.write(f"\rFound device: {d} (IP {B})\n");A.stdout.flush();A.stdout.write(f"\rDevice status: ⡢⡂ offline ");A.stdout.flush()
O()
