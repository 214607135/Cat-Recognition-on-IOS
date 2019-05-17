import os, random, shutil

def moveFile(fileDir,tarDir):
        pathDir = os.listdir(fileDir)    
        filenumber=len(pathDir)
        ratio=0.1                          # shuffle ratio
        picknumber=int(filenumber*ratio)   # numbers of images to pick
        sample = random.sample(pathDir, picknumber)  #pick images
        #print (sample)
        for name in sample:
                shutil.move(fileDir+name, tarDir+name)
        return

if __name__ == '__main__':
	fileDir = 'D:/2019 Summer Term/Project/test3/Abyssinian cat/'    
	tarDir = 'D:/2019 Summer Term/Project/test3/shuffle/ '  
	moveFile(fileDir,tarDir)
