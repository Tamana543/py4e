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

# challenge : Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
# The directory search should be done recursively. This means that the search should also include all subdirectories in the given path

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
    