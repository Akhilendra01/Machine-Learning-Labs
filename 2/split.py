import os

dir_name=input()

dir_name="./"+dir_name+"/"

test_files=[]
train_files=[]

os.mkdir(dir_name+"train")
os.mkdir(dir_name+"test")

for file in os.listdir(dir_name):
    if(file.find("tra")!=-1):
        os.rename(dir_name+file, dir_name+"train/"+file)
    else:
        os.rename(dir_name+file, dir_name+"test/"+file)
