# ORGANISING DESKTOP
import os
import shutil
print('Please wait, process is running...')

systemdrivename=os.getenv('systemdrive')
username=os.getenv('username')
homedir=systemdrivename+'\\users\\'+username

for (dirname,dirs,files) in os.walk(homedir+'\\desktop'):	
	for file in files:
		try:
			filepath=os.path.join(dirname,file)
			ext=file.split('.')[-1]
			if ext!='exe' and ext!='lnk':
				if os.path.isdir(homedir+'\\documents\\'+ext):
					pass
				else: os.mkdir(homedir+'\\documents\\'+ext)
				if os.path.exists(homedir+'\\documents\\'+ext+'\\'+file):
					os.remove(homedir+'\\documents\\'+ext+'\\'+file)
				shutil.move(filepath,homedir+'\\documents\\'+ext)
		except:
			pass		
	break
input('Desktop has been organized.')
