import os
import delFile
from PIL import Image

def img_resize(path,outdir,width,height):
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for root , dirs, files in os.walk(path):
        for file in files:
            im = Image.open(path+file)
            f,e = os.path.splitext(path+file)
            if not im.mode == 'RGB':
                im = im.convert('RGB')
        # im.show()
        # resize image to 640*640
            im_resized = im.resize((width, height), Image.ANTIALIAS)
            im_resized.save(f +'.jpg','jpeg',quality=90)

def img_rotate(path,outdir,degree):
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for root , dirs, files in os.walk(path):
        for file in files:
            im = Image.open(path+file)
            f,e = os.path.splitext(path+file)
            im_rotate1 = im.rotate(degree)
            im_rotate2 = im_rotate1.rotate(degree)
            im_rotate3 = im_rotate2.rotate(degree)
            im_rotate1.save(f + 'rotated1.jpg','jpeg',quality=90)
            im_rotate2.save(f + 'rotated2.jpg','jpeg',quality=90)
            im_rotate3.save(f + 'rotated3.jpg','jpeg',quality=90)
            


# if __name__ == '__main__':
#     for keyword in ['Siamese cat', 'Scottish Fold cat','Abyssinian cat',
#                 'Bengal cat','Bombay cat','Birman cat','British Shorthair cat',
#                 'Maine Coon cat','Persian cat','Egyptian Mau cat',
#                 'Sphynx cat','Ragdoll cat','Russian Blue cat','American Shorthair cat',
#                 'Exotic cat','Siberian cat','American Bobtail cat'
#     ]:
#         path = {'D:/2019 Summer Term/Project/test1/{}/'.format(keyword)}
#         outdir = {'D:/2019 Summer Term/Project/test1/{}/test/'.format(keyword)}
#         pathlist = [i for i in path]
#         outdirlist = [j for j in outdir]
#         print(pathlist)
#         print(outdirlist)
#         print(delFile.count(pathlist[0]))
#         img_resize(pathlist[0],outdirlist[0],640,640)




    # path = 'D:/2019 Summer Term/Project/test1/Abyssinian cat/'
    # outdir = 'D:/2019 Summer Term/Project/test1/Abyssinian cat/test/'
    

        
        

    # print(path)
    # print(outdir)
    # for i in range(0,16):
    #     imgresize(pathlist[i],outdirlist[i],640,640)

    # dirs = os.listdir(path)
    # for dir in dirs:
    #     print(dir)