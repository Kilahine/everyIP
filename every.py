import string
import os
import sys
MAX_IP=255
a=0
b=0
c=0
d=0
chainea =""
chaineb =""
chainec =""
#for a in range MAX_IP:
for a in range(0,255):
	chaine=""
	#print str(a) +"."
	chainea=str(a) +"."
	a=a+1
#	for b in range MAX_IP:
	for b in range (0,255):
		#print str(b)+"."
		chaineb=chainea + str(b) +"."
		b=b+1
#		for c in range MAX_IP:
		for c in range (0,255):
			#print str(c)+"."
			chainec=chaineb+str(c)+"."
			c=c+1
#			for d in range MAX_IP:
			for d in range (0,255):
				#print str(d) +"\n"
				#chaine=chaine+str(d)
				print chainec + str(d)
				#print chaine
				d=d+1


