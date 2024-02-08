# requirements:
# let the user input a file
# let the user input a second file
# compare file paths, canonize (reduce to most condensed filepath)
# return a message confirming or denying that the paths are homographs.



# canonicalization 
def canonicalize(string_path, cwd):
    string_path = ''.join('/' if c == '\\' else c for c in string_path) # Replace all \ with / in the path the user gives.
    full_relative = string_path.lower() # convert the path to lowercase, and set it as the full relative.
    if "c:" not in string_path:
        full_relative = cwd + "/" + string_path # If the user did not give an absolute path, add the cwd to the front.
    list_of_strings = full_relative.split("/") # Split the full relative path into a list on every /
    for i in range(0, len(list_of_strings)):
        if '' in list_of_strings:
            list_of_strings.remove('') # takes out any extra spaces that were produced by excesive ////
    absolutepath = [] # setup
    for item in list_of_strings:
        if item == "~":
            pass # dont do anythin if a ~ is present, we are already in the directory.
        elif item == "..":
            if len(absolutepath) > 1:
                absolutepath.pop(-1) # Remove the last directory input.
        elif item == ".":
            pass # nothing happens
        else:
            absolutepath.append(item) # add the directory into the absolutepath.
    absolutepath = "/".join(absolutepath) # adds the / back in between every item.
    return absolutepath # returns the path.
def are_homographs(filepath1, filepath2, cwd):
    return canonicalize(filepath1, cwd) == canonicalize(filepath2, cwd) # checks if the canonicalized versions are the same.
def main():
    cwd = "c:/users/bob" # our cwd
    print(f"current working directory: {cwd}\n") # display it
    path_string = input("input a file path1: ") # get input
    path_string2 = input("input a file path2: ")
    if are_homographs(path_string, path_string2, cwd): # check if they are right or wrong.
        print("The file paths are homographs :)")
    else:
        print("The file paths are not homographs :(")
main()