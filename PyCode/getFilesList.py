import os

target_path = "D:\Lib\PCL\PCL1111/3rdParty\VTK\lib"
files = os.listdir(target_path)

file_list_path = "D:\Lib/vtk_lib_list.txt"
file_list = open(file_list_path, 'w')

for sub_file in files:
    if os.path.isfile(os.path.join(target_path, sub_file)):
        file_list.write(sub_file+'\n')

file_list.close()
