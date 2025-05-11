import os
# os.mkdir("my_first_directory")
print(os.listdir)
# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
print(os.listdir())



# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
print(os.getcwd())
# os.chdir("my_second_directory")
print(os.getcwd())
os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory") # to remove an empty directory 
print(os.listdir())

os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory") # to remove a directory which contains another one inside 
print(os.listdir())

returned_value = os.system("mkdir my_first_directory") #  returns the value returned by the shell after running the command given
print(returned_value)