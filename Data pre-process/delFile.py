"""
    Author:Yiwen Gao

"""
import os
import hashlib
from time import clock as now

def getmd5(filename):
    file_txt = open(filename,'rb').read()
    m = hashlib.md5(file_txt)
    return m.hexdigest()

def delNonjpg(path):
    count = 0
    for root , dirs, files in os.walk(path):
        for name in files:
            extension = os.path.splitext(name)[1]
            #if name.endswith(".png") or name.endswith(".gif"):
            if extension.lower() not in [
                    '.jpg', '.jpeg']:
                #print(extension)
                os.remove(os.path.join(root, name))
                count += 1
                print ("Delete File: " + os.path.join(root, name),count)
    print(count)

def count(path):
    pngCount  =0
    jpgCount  =0
    jpegCount =0
    JPGCount  =0
    gifCount  =0
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".png"):
                pngCount += 1
                print ("png File: " + os.path.join(root, name),count)
            elif name.endswith(".gif"):
                gifCount += 1
            elif name.endswith(".jpg"):
                jpgCount += 1
            elif name.endswith(".jpeg"):
                jpegCount += 1
            elif name.endswith(".JPG"):
                JPGCount += 1
    print("pngCount=",pngCount," jpgCount=",jpgCount,
    " jpgeCount=",jpegCount, 
    " JPGCount=",JPGCount, " gifCount=",gifCount)



def dupliremove(path):
    #path = raw_input("path: ")
    all_md5 = {}
    all_size = {}
    total_file=0
    total_delete=0
    start=now()
    for file in os.listdir(path):
        total_file += 1
        real_path=os.path.join(path,file)
        if os.path.isfile(real_path) == True:
            size = os.stat(real_path).st_size
            name_and_md5=[real_path,'']
            if size in all_size.keys():
                new_md5 = getmd5(real_path)
                if all_size[size][1]=='':
                    all_size[size][1]=getmd5(all_size[size][0])
                if new_md5 in all_size[size]:
                    print ('Delete',file)
                    os.remove(os.path.join(path, file))
                    total_delete += 1
                else:
                    all_size[size].append(new_md5)
            else:
                all_size[size]=name_and_md5
    end = now()
    time_last = end - start
    print ('Total Files：',total_file)
    print ('Delete Files：',total_delete)
    #print ('Time ：',time_last,'s')

# if __name__ == "__main__":
#     path = 'D:/2019 Summer Term/Project/test1/Abyssinian cat'
#     #delNonjpg(path)
#     #count(path)
#     dupliremove(path)
    