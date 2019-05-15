import glob
import os

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
            flip_horizontal(image).save('D:/VideoPhotos/hongshi_flip_horizontal/'
            + dir + image_name)


if __name__ == '__main__':
    path = 'D:/2019 Summer Term/Project/test1/Abyssinian cat'
    dirs = os.listdir(path)
    for dir in dirs:
        print(dir)
    
    def imgresize(image):
        im = Image.open(image)
        #im.show()
 
        #resize image to 640*640
        im_resized = im.resize((640, 640))
        im_resized.save()