
'''
import os
if(not os.path.exists("Shifat")):
    #os.mkdir("Shifat")
    pass
for i in range(46, 100):
    os.mkdir("Shifat/Tutorial of Harry {i+1}")

'''

import os

folders = os.listdir("Shifat")
os.chdir("/Shifat")
print(os.getcwd())
for folder in folders:
    print(folder)
for folder in folders:
    os.rmdir(f"Tutorial of Harry 60")

print(folders)