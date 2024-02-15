def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

def weak_mitigation(username, password):
    return generate_sql_string(username, password)

def strong_mitigation(username, password):
    return generate_sql_string(username, password)

def test_valid(function):

    # test 1
    username = "camlybb123"
    password = "p@ssword"
    expected = "SELECT * FROM users WHERE username = 'camlybb123' AND password = 'p@ssword'"

    result = function(username, password)

    assert expected == result

    # test 2
    username = ""
    password = ""
    expected = "SELECT * FROM users WHERE username = '' AND password = ''"

    result = function(username, password)

    assert expected == result

    # test 3
    username = ""
    password = ""
    expected = "SELECT * FROM users WHERE username = '' AND password = ''"

    result = function(username, password)

    assert expected == result

    # test 4
    username = ""
    password = ""
    expected = "SELECT * FROM users WHERE username = '' AND password = ''"

    result = function(username, password)

    assert expected == result

def test_tautology(function):
    pass

def test_union(function):
    pass

def test_add_state(function):
    pass

def test_comment(function):
    pass


print("validity test running...")
test_valid(generate_sql_string)
test_valid(weak_mitigation)
test_valid(strong_mitigation)
print("validity test passed.")

