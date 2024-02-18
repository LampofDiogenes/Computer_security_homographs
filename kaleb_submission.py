
'''
injection planning 

take 2 strings from user (username and password)

show raw unfiltered atttack

have 2 functions (weak and strong filtering)
func1: weak blacklists certain characters (return string)
func2: strong whitelists certain characters (return string)
'''

def weak_mitigation(input_str1, input_str2):
    # find any ' in the string, and then delete it
    input1 = input_str1.replace("'", "")
    input2 = input_str2.replace("'", "")
    sanitized_input = generate_sql_string(input1, input2)
    return sanitized_input


def strong_mitigation(username, password):
    
    # normally you would want all info in a database for ease of developer use. to make this function practical 
    # in a professional setting, this would demand that we have a function that queries from the database to be
    # stored in the python file directly. this prevents any sql attack, but may open other attacks 
    # targetting the python file directly


    # summary: make a python database (just for passwords) and only give information if 
    # the data matches the python database. should entirely ignore sql problems
    user_info = {
    "camlybb123":"p@ssword",
    "test1": "fireball",
    "test2": "tequila",
    "test3": "ba,nananana"
    }
    try: 
        if user_info[username] == password:
            return generate_sql_string(username, password)
        else:
            return "access denied"
    except KeyError:
        return "the username or password is incorrect"


test_cases = [
("camlybb123","p@ssword"),
("test1", "fireball"),
("test1", "tequila"),
("test3", "ba,nananana")]
    

def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
def test_valid(function):

    # tests
    
    
    for username, password in test_cases:
        print(function(username, password))

def test_tautology(function):
    # tests
    
    
    for username, password in test_cases:
        print(function(username, password))

def test_union(function):
    # tests
   
    
    for username, password in test_cases:
        print(function(username, password))

def test_add_state(function):
    # tests
    
    
    for username, password in test_cases:
        print(function(username, password))

def test_comment(function):
    # tests
    test_cases = [
    ("Root';--","nothing"),
    (" ", " "),
    (" ", " "),
    (" ", " ")]
    
    for username, password in test_cases:
        print(function(username, password))


functions = [test_valid, test_tautology, test_comment, test_union, test_add_state]
for item in functions:
    print("\n")
    print(str(item.__name__), "- no mitigation")
    item(generate_sql_string)
    print(str(item.__name__), "- weak mitigation")
    item(weak_mitigation)
    print(str(item.__name__), "- strong mitigation")
    item(strong_mitigation)

