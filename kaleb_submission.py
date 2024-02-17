
'''
injection planning 

take 2 strings from user (username and password)

show raw unfiltered atttack

have 2 functions (weak and strong filtering)
func1: weak blacklists certain characters (return string)
func2: strong whitelists certain characters (return string)
'''

def weak_mitigation(username, password):
    for character in username:
        if character == '':
            username.pop(character)
    for character in password:
        if character == '':
            password.pop(character)
    return generate_sql_string(username, password)



# THIS IS THE IMPORTANT PART RIGHT UNDERNEATH HERE


def strong_mitigation(username, password):
    
    # normally you would want all info in a database for ease of developer use. to make this function practical 
    # in a professional setting, this would demand that we have a function that queries from the database to be
    # stored in the python file directly. this prevents any sql attack, but may open other attacks 
    # targetting the python file directly

    user_info = {
    "camlybb123":"p@ssword",
    "test1": "fireball",
    "test2": "tequila",
    "test3": "ba,nananana"
    }
    if user_info[username] == password:
        return "access granted"
    else:
        return "access denied"
    

# END OF IMPORTANT PART
    

def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
def test_valid(function):

    # tests
    test_cases = [
    ("camlybb123","p@ssword"),
    ("test1", "fireball"),
    ("test1", "tequila"),
    ("test3", "ba,nananana")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_tautology(function):
    # tests
    test_cases = [
    ("camlybb123","p@ssword' OR 'x' == 'x"),
    (" ", " "),
    (" ", " "),
    (" ", " ")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_union(function):
    # tests
    test_cases = [
    ("camlybb123","p@ssword"),
    (" ", " "),
    (" ", " "),
    (" ", " ")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_add_state(function):
    # tests
    test_cases = [
    ("camlybb123","p@ssword"),
    (" ", " "),
    (" ", " "),
    (" ", " ")]
    
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


funcitons = [test_valid, test_tautology, test_comment, test_union, test_add_state]
for item in funcitons:
    print("\n")
    print(str(item.__name__), "- no mitigation")
    item(generate_sql_string)
    print(str(item.__name__), "- weak mitigation")
    item(weak_mitigation)
    print(str(item.__name__), "- strong mitigation")
    item(strong_mitigation)

