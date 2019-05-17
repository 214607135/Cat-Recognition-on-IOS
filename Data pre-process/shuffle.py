import os, random, shutil

def shuffle(filedir,outdir,ratio):
        pathDir = os.listdir(filedir)
        if not os.path.exists(outdir):
                os.makedirs(outdir)   
        filenumber=len(pathDir)
        picknumber=int(filenumber*ratio)   # numbers of images to pick
        sample = random.sample(pathDir, picknumber)  #pick images
        #print (sample)
        for name in sample:
                shutil.move(filedir+name, outdir+name)
        return

# if __name__ == '__main__':
# 	fileDir = 'D:/2019 Summer Term/Project/test3/Abyssinian cat/'    
# 	tarDir = 'D:/2019 Summer Term/Project/test3/shuffle/ '  
# 	shuffle(fileDir,tarDir)
