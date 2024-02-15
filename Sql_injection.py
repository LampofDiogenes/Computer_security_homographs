"""
W06 Lab:  SQL Injection Mitigation
Team members: Cameron Lybbert, Gage Smith, Vinnicius Castro, Kaleb Bradford
"""

'''
W06 Lab: Path SQL Injection Mitigation
Team members: Cameron Lybbert, Gage Smith, Vinnicius Castro, Kaleb Bradford

injection planning 
'''
def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

def weak_mitigation(username, password):
    for character in username:
        if character == '':
            username.pop(character)
    for character in password:
        if character == '':
            password.pop(character)
    return generate_sql_string(username, password)

def strong_mitigation(username, password):
    character_white_list = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                  'r','s','t','u','v','w','x','y','z',' ']
    character_number_list = ['1','2','3','4','5','6','7','8','9','0']

    for character in username:
        if (character not in character_white_list and character not in character_number_list):
            return "invalid character in submission"
        else:
            pass

    for character in password:
        if (character not in character_white_list and character not in character_number_list):
            return "invalid character in submission"
        else:
            pass

    return generate_sql_string(username, password)

def test_valid(function):

    # tests
    test_cases = [
    ("camlybb123","p@ssword"),
    (" ", " "),
    (" ", " "),
    (" ", " ")]
    
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

