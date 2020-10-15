#Multiple File Renamer
import os
path = (r" ")   #address of your file location, fill your dataset address within the double quotes.
for count, filename in enumerate(os.listdir(path)):
    loc = os.path.splitext(path+filename)
    count +=0    #Change count value here accordingly to fit your code, if you want numbering from n, make sure you set count value n-1
    rename =str(count)+".jpg"  #For the rename part, feel free to add additional text along with enumeration, before the "+.jpg"
    os.rename(path+'/'+filename, path+'/'+rename)
