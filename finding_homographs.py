""" 
W05 Lab: Path Homograph
Name: Gage Smith, Vinnicius Castro,  

requirements:
let the user input a file
let the user input a second file
compare file paths, canonize (reduce to most condensed filepath)
return a message confirming or denying that the paths are homographs.
"""



# canonicalization 
def remove_slashes(string_path):
    # idea: split up the string along the backslashes, and then remove anything that begins with a period
    
    
    
    character =  "\\"
    
    # string_list = string_path.split(character)


    string_list =  [string+character for string in string_path.split() if string]
    
    print(string_list)
    for string in string_list:
        if (string == "./" or string == "../"):
            string_list.pop()

def is_homograph(string1, string2):
    # check if two strings are homographs by comparing their canonical forms



# we need a homograph function
    
    
    
def main():
    print("input a file path")
    path_string = input()
    # Console.Readline()
    remove_slashes(path_string)
    is_homograph(path1, path2)

main()