import os
import string
dirName = "D:/postgraduateworking/tongji/images/"         #最后要加双斜杠，不然会报错
li=os.listdir(dirName)
for filename in li:
    newname = filename
    newname = newname.split(".")
    if newname[-1]=="jpg":
        newname[-1]="png"
        newname = str.join(".",newname)  #这里要用str.join
        filename = dirName+filename
        newname = dirName+newname
        os.rename(filename,newname)
        print(newname,"updated successfully")