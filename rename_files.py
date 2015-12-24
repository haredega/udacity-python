#Importing needed libraries
import os
import string



def rename_files():
    #Get files
    file_list = os.listdir(os.path.dirname(__file__))
    print(file_list)
    #Rename files
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,'0123456789'))

rename_files()
