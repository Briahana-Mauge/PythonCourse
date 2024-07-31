from pathlib import Path
# reference a file or path on out computer...two types of pathes that can be used:

# Absolute Path (starts from the root of the harrd disk. ie ~)
# Relative Path (start from where we currently are)

path=Path("ecommerce") # this is the path we want in relation to where we are (relative)
print(path.exists()) # does this path exist?

# PATH METHODS
# Path() - the current directory
# path.exists() - returns bool about if a path exsists or not
# path.mkdir() - creates a new directory
# path.rmdir() - deletes a directory
# path.glob('search_pattern') -  for files and directories in current path and returns an object
            # search patterns: different ways to serch for files
           
''' 
            * - everything: all files and all directories
            *.* - all the files, no directories
            *.py - all python files
            *.pdf - all pdfs
'''

# Example: Get all python files in the current directory
new_path = Path()
for file in new_path.glob('*'):
    print(file)

# pypi.org contains lots of packages that you can install made from other people to import into your own project