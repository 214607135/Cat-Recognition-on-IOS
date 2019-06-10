"""
    Author:Yiwen Gao

"""
import os


def rename(path):
    folderlist = os.listdir(path)          
    for folder in folderlist:     
        inner_path = os.path.join(path, folder)
        total_num_folder = len(folderlist)       
        filelist = os.listdir(inner_path)        
        i = 0
        for item in filelist:
            i += 1
            total_num_file = len(filelist)                                  
            src = os.path.join(os.path.abspath(inner_path), item)           
            dst = os.path.join(os.path.abspath(inner_path), str(folder) + 
            '_' + str(i).zfill(4) + '.jpg')                        
            os.rename(src, dst)

# if __name__ == "__main__":
#     path =  'D:/2019 Summer Term/Project/test3/'
#     rename(path)