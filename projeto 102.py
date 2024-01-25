import os
import shutil

fromdir = "C:/Users/leona/Downloads/"
todir = "C:/Users/leona/Documents/"

listfiles = os.listdir(fromdir)
print(listfiles) 

for file in listfiles:
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)

    if extension in [".txt",".doc", ".docx", ".pdf"]:
        path1 = fromdir + file
        path2 = todir + "downloads/"
        path3 = todir + "downloads/" + file
        
        if os.path.exists(path2):
            print("movendo arquivo", file) 
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("movendo arquivo", file) 
            shutil.move(path1, path3)


