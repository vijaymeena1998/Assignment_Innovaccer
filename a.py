''' COUNTING NUMBER OF DUPLICATE FILES:
									The program first stores all the drive names and then iterates through these drives. It stores some specific iterating files
 inside a dictionary with file-size as key and filename(not filepath) as value. Then it checks two conditions: FIRST-if same size( i.e. key) already exists inside
  dictionary and SECOND-whether its extension is same as that of current iterating file. If both of the conditions hold true then it considers it as 
  duplicate and updates duplicate file count.
  '''
import os
print('Please wait, process is running...')

systemdrivename=os.getenv('systemdrive')
dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
iterdrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
iterdrives.remove(systemdrivename)

username=os.getenv('username')
homedir=systemdrivename+'\\users'

iterdrives.insert(0,homedir)

import os
store=dict()
extensions={'mp3','mpa','wav','rar','zip','iso','exe','bmp','jpeg','jpg','png','gif','tiff','tif','ppt','docx','xlsx','pdf','3gp','avi','mkv','mp4','wmv','swf'}
c=0

for path in iterdrives:
	for (dirname,dirs,files) in os.walk(path+'\\'):
		for filename in files:
			ext=filename.split('.')[-1]
			if ext in extensions:
				filepath=os.path.join(dirname,filename)
				try:
					if (os.path.getsize(filepath) in store) and (ext==store[os.path.getsize(filepath)].split('.')[-1]):
						print('Found duplicate @',filepath)
						c=c+1
					else:	
						store[os.path.getsize(filepath)]=filename
				except:
					continue
					
print('Total number of duplicate files are',c)
input('press enter to exit')