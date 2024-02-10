cwd = "c:/users/bob" # our cwd

def canonicalize(string_path, cwd):
    string_path = ''.join('/' if c == '\\' else c for c in string_path) # Replace all \ with / in the path the user gives.
    string_path = ''.join('' if c == ' ' else c for c in string_path) # Replace all ' ' with '' in the path the user gives.

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
            if len(absolutepath) > 0:
                absolutepath.pop(-1) # Remove the last directory input.
        elif item == ".":
            pass # nothing happens
        else:
            absolutepath.append(item) # add the directory into the absolutepath.

    absolutepath = "/".join(absolutepath) # adds the / back in between every item.

    return absolutepath # returns the path.

def are_homographs(filepath1, filepath2, cwd):
    return canonicalize(filepath1, cwd) == canonicalize(filepath2, cwd) # checks if the canonicalized versions are the same.

def user_input():
    print(f"\ncurrent working directory: {cwd}\n") # display it
    path_string = input("input a file path1: ") # get input
    path_string2 = input("input a file path2: ")
    if are_homographs(path_string, path_string2, cwd): # check if they are right or wrong.
        print("The file paths are homographs :)")
    else:
        print("The file paths are not homographs :(")

def test_homograph():
    homographs = [("././test.txt", "test.txt"), 
                  ("../bob/folder/test.txt", "./folder/test.txt"), 
                  ("~/folder/test.txt", "../bob/folder/../folder/test.txt"),
                  ("../../users/bob/test.txt", "test.txt"),
                  ("./folder/..///test.txt", "test.txt"),
                  ("././././folder/test.txt", "../bob/folder/test.txt"),
                  ("~/test.txt", "~/folder/../test.txt"),
                  ("../test.txt", "../../users/test.txt"),
                  ("test.txt", "../bob/test.txt"),
                  ("./././test.txt", "./test.txt")]
    
    nonhomographs = [("../text.txt", "text.txt"),
                     ("/users/bob/../text.txt", "/text.txt"),
                     ("/users/bob/../text.txt", "/users/alice/text.txt"),
                     ("../test.txt", "test.txt"),
                     ("../bob/./././/../test.txt", "../../test.txt"),
                     ("bob/test.txt", "test.txt"),
                     ("./test.txt", "C:/users/karen/test.txt"),
                     ("../test.txt","test.txt"),
                     ("C:/users/bob/test.txt","c:/users/karen/test.txt"),
                     ("test.txt", "../bob/../.././users/test.txt")]
    
    print("\nRunning homograph test...")
    for file1, file2 in homographs:
        assert are_homographs(str(file1), str(file2), cwd)

    print("Running non-homograph test...")
    for file1, file2 in nonhomographs:
        assert not are_homographs(file1, file2, cwd)
    
    print("Success!")

def main():
    menu = True
    while menu:
        choice = str(input("\n1. Run test.\n2. Input two files.\nq. Quit.\nChoice: "))
        if choice == '1':
            test_homograph()
        elif choice == '2':
            user_input()
        elif choice == 'q':
            menu = False

if __name__ == '__main__':
    main()