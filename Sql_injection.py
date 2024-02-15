"""
W06 Lab:  SQL Injection Mitigation
Team members: Cameron Lybbert, Gage Smith, Vinnicius Castro, Kaleb Bradford
"""

def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

def weak_mitigation(username, password):
    # do weak mitigation
    return generate_sql_string(username, password)

def strong_mitigation(username, password):
    # do strong mitigation
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
    ("camlybb123","p@ssword"),
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
    ("camlybb123","p@ssword"),
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

