import os,random
path="PUT YOUR PATH"
files=os.listdir(path)
to_del=[]

def choose_files(files,half):
    for i in files:
        r=random.randint(0,1)
        if r==1:  #to del
            to_del.append(i)
            files.remove(i)
    while len(to_del)<half:
        choose_files(files,len(files)/2)

choose_files(files,len(files)/2)
for i in to_del:
    os.remove(f"{path}/{i}")
print("snapped")