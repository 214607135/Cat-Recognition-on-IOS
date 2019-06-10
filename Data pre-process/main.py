"""
    Author:Yiwen Gao

"""
from PIL import Image
import os
import imgResizeAndRotate
import delFile
import rename
import shuffle


if __name__ == '__main__':
    for keyword in ['Siamese cat', 'Scottish Fold cat','Abyssinian cat',
                'Bengal cat','Bombay cat','Birman cat','British Shorthair cat',
                'Maine Coon cat','Persian cat','Egyptian Mau cat',
                'Sphynx cat','Ragdoll cat','Russian Blue cat','American Shorthair cat',
                'Exotic cat','Siberian cat','American Bobtail cat'
    ]:
        path = {'D:/2019 Summer Term/Project/test2/{}/'.format(keyword)}
        outdir = {'D:/2019 Summer Term/Project/test2/{}/test/'.format(keyword)}
        pathlist = [i for i in path]
        outdirlist = [j for j in outdir]
    

        # delFile.delNonjpg(pathlist[0])
        # delFile.count(pathlist[0])
        # delFile.dupliremove(pathlist[0])
        # imgResizeAndRotate.img_resize(pathlist[0],pathlist[0],640,640)
        # #imgResizeAndRotate.img_resize(path1,path1,640,640)
        # imgResizeAndRotate.img_rotate(pathlist[0],pathlist[0],90)
        
        
        
    path1 = 'D:/2019 Summer Term/Project/test2/'
    path2 = 'D:/2019 Summer Term/Project/Final DataSet/TrainSet2/'
    outdir1 = 'D:/2019 Summer Term/Project/Final DataSet/TestSet/'
    outdir2 = 'D:/2019 Summer Term/Project/Final DataSet/TrainSet1/'

    
    # rename.rename(path1)
    shuffle.shuffle(path1,outdir1,0.3)