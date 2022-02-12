import os
from os.path import *

m=open('m.txt','w+',encoding='utf-8')
v=open('v.txt','w+',encoding='utf-8')
a=open('a.txt','w+',encoding='utf-8')
d=open('d.txt','w+',encoding='utf-8')
p=open('p.txt','w+',encoding='utf-8')
pd=open('pd.txt','w+',encoding='utf-8')
f=open('f.txt','w+',encoding='utf-8')
g=open('g.txt','w+',encoding='utf-8')
z=['E:','D:','F:']
for j in z:
   if isdir(j) is True:
      for root,dirs,files in os.walk(j):
         for i in files:
            filename=join(root,i)
            g.write(filename)
            g.write('\n')
            if filename.endswith('mp3') or \
               filename.endswith('wma') or \
               filename.endswith('wav') or \
               filename.endswith('m4a'):
               m.write(filename)
               m.write('\n')
            elif filename.endswith('.mp4') or \
                 filename.endswith('.avi'):
               v.write(filename)
               v.write('\n')
            elif filename.endswith('.jpg') or \
                 filename.endswith('.png') or \
                 filename.endswith('.gif'):
               a.write(filename)
               a.write('\n')
            elif filename.endswith('doc') or \
                 filename.endswith('docx'):
               d.write(filename)
               d.write('\n')
            elif filename.endswith('ppt') or \
                 filename.endswith('pptx'):
               p.write(filename)
               p.write('\n')
            elif filename.endswith('pdf'):
               pd.write(filename)
               pd.write('\n')
         f.write(root)
         f.write('\n')
         g.write(root)
         g.write('\n')
m.close()
v.close()
a.close()
d.close()
p.close()
pd.close()
f.close()
g.close()
