#   SEaRCHING 10 BIGGEST FILES ON CURRENT SYSTEM
import os
from heapq import heappush, heapreplace


print('Please wait, process is running...')
try:
	systemdrivename=os.getenv('systemdrive')
	dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	iterdrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
	iterdrives.remove(systemdrivename)

	username=os.getenv('username')
	homedir=systemdrivename+'\\users\\'+username

	store=list()
	
	for (dirname,dirs,files) in os.walk(homedir+'\\downloads'):
		for file in files:
			try:
				if len(store)<10:
					heappush(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
					continue

				if os.path.getsize(os.path.join(dirname,file))>store[0][0]:
					heapreplace(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
			except:
				pass				

	for (dirname,dirs,files) in os.walk(systemdrivename+'\\users'):
		if dirname!=systemdrivename+'\\users\\vijay\\downloads':
			for file in files:
				try:
					if len(store)<10:
						heappush(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
						continue

					
					if os.path.getsize(os.path.join(dirname,file))>store[0][0]:
						heapreplace(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
				except:
					pass			

	for drivename in iterdrives:
		for (dirname,dirs,files) in os.walk(drivename+'\\'):
			for file in files:
				try:
					if os.path.getsize(os.path.join(dirname,file))>store[0][0]:
						heapreplace(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
				except:
					pass
except:
	store=list()
	paths=['/home/','/media/']
	for path in paths:
		for (dirname,dirs,files) in os.walk(path):
			for file in files:
				try:
					if len(store)<10:
						heappush(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
						continue
					
					if os.path.getsize(os.path.join(dirname,file))>store[0][0]:
						heapreplace(store,[os.path.getsize(os.path.join(dirname,file)),os.path.join(dirname,file)])
				except:
					pass				


store.sort(reverse=True)
print('10 biggest files on current system have been idendified as')
for item in store:
	print('%g MB @  %s'%(item[0]/1048576,item[1]))
input()