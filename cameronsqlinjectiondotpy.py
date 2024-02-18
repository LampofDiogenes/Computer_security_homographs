'''
W06 Lab: Path SQL Injection Mitigation
Team members: Cameron Lybbert, Gage Smith, Vinnicius Castro, Kaleb Bradford

injection planning 
'''
def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

def weak_mitigation(username, password):
    # setup
    mitigated_username = ''
    mitigated_password = ''

    # if we find a blocked character in the username or password, 
    # stop adding the charaters to the mitigated version
    for character in username:
        if character == "'" or character == ';' or character == '-':
            break
        else:
            mitigated_username += character
    
    for character in password:
        if character == "'" or character == ';' or character == '-':
            break
        else:
            mitigated_password += character

    # return a generated string with the mitigated username and password.
    return generate_sql_string(mitigated_username, mitigated_password)

def strong_mitigation(username, password):
    
    # setup
    allow_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                  'r','s','t','u','v','w','x','y','z',' ', '!', '@', '#', '$', '%','^','&','*', ',', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    mitigated_username = ''
    mitigated_password = ''
    
    # If the character is not in the allow list, stop adding character to the mitigated version.
    for character in username:
        if character.lower() not in allow_list:
            break
        else:
            mitigated_username += character

    for character in password:
        if character.lower() not in allow_list:
            break
        else:
            mitigated_password += character

    # return a string generated with the mitigated username and password.
    return generate_sql_string(mitigated_username, mitigated_password)

def test_valid(function):

    # tests
    test_cases = [
    ("camlybb123","p@ssword"),
    ("test1", "iamhere"),
    ("test2", "mydogsname"),
    ("test3", "mycatsname")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_tautology(function):
    # tests
    test_cases = [
    ("camlybb123","p@ssword' OR 'x' == 'x"),
    ("test1", "' OR 1=1'"),
    ("test2", "' AND 1=1'"),
    ("test3' OR 1=1'", "nothing")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_union(function):
    # tests
    test_cases = [
    ("camlybb123","p@ssword' UNION SELECT * FROM customers '"),
    ("test1", "' UNION SELECT * FROM users '"),
    ("test2", "' UNION SELECT username FROM users-- "),
    ("test3", "'UNION SELECT password FROM users--")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_add_state(function):
    # tests
    test_cases = [
    ("camlybb123","p@ssword'; INSERT INTO users (username, password) VALUES 'Bob', '1234"),
    ("test1", "fireball'; DELETE FROM users WHERE username = 'Root"),
    ("test1", "tequila'; INSERT INTO users (username, password) VALUES 'Bob', '1234"),
    ("test3", "ba,nananana'; DROP TABLE users--")]
    
    for username, password in test_cases:
        print(function(username, password))

def test_comment(function):
    # tests
    test_cases = [
    ("Root';--","nothing"),
    ("';--", "nothing"),
    ("test3';--", "paswword"),
    ("nothing' OR 1=1;--", "none")]
    
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

