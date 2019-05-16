from PIL import Image
import os
import imgResizeAndRotate
import delFile


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
        path1 = 'D:/2019 Summer Term/Project/test2/rotatetest/'
        outdir1 = 'D:/2019 Summer Term/Project/test2/rotatetest/test/'
        #delFile.delNonjpg(pathlist[0])
        delFile.count(pathlist[0])
        #delFile.dupliremove(pathlist[0])
    #     print(pathlist)
    #     print(outdirlist)
    #     print(delFile.count(pathlist[0]))
    #     imgResizeAndRotate.img_resize(pathlist[0],outdirlist[0],640,640)
        # imgResizeAndRotate.img_rotate(path1,path1,90)
        
        
        # for root , dirs, files in os.walk(path1):
        #     for file in files:
        #         im = Image.open(path1+file)
        #         f,e = os.path.splitext(path1+file)
        #         print(file)