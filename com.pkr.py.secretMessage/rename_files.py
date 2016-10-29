import os

def rename_files(sPath):
    aFiles = os.listdir(sPath)
    saved_path = os.getcwd()
    os.chdir(sPath)
    for file_name in aFiles:
        os.rename(file_name, file_name.translate(file_name.maketrans("", "", "0123456789")))
        print("Renamed")
    os.chdir(saved_path)


rename_files("/home/codeartist/study/python/com.pkr.py.secretMessage/prank/prank")
