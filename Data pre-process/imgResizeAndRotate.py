import glob
import os
import cv2
import delFile
from PIL import Image


def rotate_270(imgae):
    """
    将图片旋转270度
    """
# 读取图像
    im = Image.open(imgae)
# im.show()
# 指定逆时针旋转的角度
    im_rotate = im.rotate(270)
# im_rotate.show()
    return im_rotate

def createFile(path):
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
    # 如果不存在则创建目录
    # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
    # 如果目录存在则不创建，并提示目录已存在
        print('%s 目录已存在' % path)
        return False


def main():
    path = 'D:/VideoPhotos/hongshi/'
    createFile('D:/VideoPhotos/hongshi_rotate')
    createFile('D:/VideoPhotos/hongshi_flip_horizontal')

    dirs = os.listdir(path)
    for dir in dirs:
    # print(dir)
        createFile('D:/VideoPhotos/hongshi_rotate/' + dir)
        createFile('D:/VideoPhotos/hongshi_flip_horizontal/' + dir)

        images = glob.glob(path + dir + r"\*.jpg")
        for image in images:
            image_name = image[image.find("\\"):]
            print(image_name)
            rotate_270(image).save('D:/VideoPhotos/hongshi_rotate/' 
            + dir +image_name)

def imgresize(path,outdir,width,height):
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for root , dirs, files in os.walk(path):
        for file in files:
            im = Image.open(path+file)
            if not im.mode == 'RGB':
                im = im.convert('RGB')
        # im.show()
        # resize image to 640*640
            im_resized = im.resize((width, height), Image.ANTIALIAS)
            im_resized.save(os.path.join(outdir,file),'jpeg',quality=90)
        

# def img_resize(img_file, path_save, width,height):
#     img = Image.open(img_file)
#     new_image = img.resize((width,height),Image.BILINEAR)
#     new_image.save(os.path.join(path_save,os.path.basename(img_file)))

if __name__ == '__main__':
    for keyword in ['Siamese cat', 'Scottish Fold cat','Abyssinian cat',
                'Bengal cat','Bombay cat','Birman cat','British Shorthair cat',
                'Maine Coon cat','Persian cat','Egyptian Mau cat',
                'Sphynx cat','Ragdoll cat','Russian Blue cat','American Shorthair cat',
                'Exotic cat','Siberian cat','American Bobtail cat'
    ]:
        path = {'D:/2019 Summer Term/Project/test1/{}/'.format(keyword)}
        outdir = {'D:/2019 Summer Term/Project/test1/{}/test/'.format(keyword)}
        pathlist = [i for i in path]
        outdirlist = [j for j in outdir]
        print(pathlist)
        print(outdirlist)
        print(delFile.count(pathlist[0]))
        imgresize(pathlist[0],outdirlist[0],640,640)
    # path = 'D:/2019 Summer Term/Project/test1/Abyssinian cat/'
    # outdir = 'D:/2019 Summer Term/Project/test1/Abyssinian cat/test/'
    

        
        

    # print(path)
    # print(outdir)
    # for i in range(0,16):
    #     imgresize(pathlist[i],outdirlist[i],640,640)

    # dirs = os.listdir(path)
    # for dir in dirs:
    #     print(dir)