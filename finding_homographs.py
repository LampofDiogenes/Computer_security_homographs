""" 
W05 Lab: Path Homograph
Team members: Gage Smith, Vinnicius Castro, Kaleb Bradford, Cameron Lybbert 

requirements:
let the user input a file
let the user input a second file
compare file paths, canonize (reduce to most condensed filepath)
return a message confirming or denying that the paths are homographs.
"""



# canonicalization 
def remove_slashes(string_path):
    # idea: split up the string along the backslashes, and then remove anything that begins with a period
    
    
    # determining how to split the string
    backslash =  "\\"
    slash = "/"
    # keeping track of the index
    loop_amount = 0

    # for reference
    print(f"Original path: {string_path}")

    string_list = string_path.split(backslash)
    print(f"split path: {string_list}")

    for item in string_list:
        index = loop_amount

        if (item == "." or item == ""):
            string_list.pop(index)
        
        elif (item == ".."):
            string_list.pop(index)
            string_list.pop((index-1))
        
        loop_amount += 1

    true_string = ""

    for item in string_list:
        true_string += item

    return true_string
    
    
    
def main():
    print()
    print("input a file path")
    path_string = "C:\\users\..\\path.py" #input()
    # Console.Readline()
    new_string = remove_slashes(path_string)
    print(f"canonical string: {new_string}")
    print()

main()