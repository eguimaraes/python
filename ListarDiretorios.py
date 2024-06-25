#https://www.geeksforgeeks.org/python-list-files-in-a-directory/
import os
path = "C://Users//Vanshi//Desktop//gfg"
dir_list = os.listdir(path)
print("Diretorios '", path, "' :")
# prints all files
print(dir_list)
