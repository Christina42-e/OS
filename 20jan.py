import os 
import shutil
#create a new directory
os.mkdir("test_directory")
#change the current working directory to new directory
os.chdir("test_directory")
print("Current working directory:", os.getcwd())
#createt a text file in the directory
with open("example.txt", "w") as file:
    file.write("This is a test file")
#list file in the current directory
print("files in directory:", os.listdir())
#copy the file
shutil.copy("example.txt", "copy_example.txt")
#move the copied file to new location (remaining it in process)
shutil.move("copy_example.txt", "../moved_example.txt")
#go back to parent directory
os.chdir("..")

#remove the test directory and its contents
shutil.rmtree("test_directory")
os.remove("moved_example.txt") #remove the moved files
print("Cleanup completed!")