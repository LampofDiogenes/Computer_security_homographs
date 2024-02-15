def generate_sql_string(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

def weak_mitigation(username, password):
    # do weak mitigation
    return generate_sql_string(username, password)

def strong_mitigation(username, password):
    # do strong mitigation
    return generate_sql_string(username, password)

def test_valid(function):

    # test 1
    username = "camlybb123"
    password = "p@ssword"

    print(function(username, password))

    # test 2
    username = ""
    password = ""

    print(function(username, password))


    # test 3
    username = ""
    password = ""

    print(function(username, password))


    # test 4
    username = ""
    password = ""

    print(function(username, password))


def test_tautology(function):
    pass

def test_union(function):
    pass

def test_add_state(function):
    pass

def test_comment(function):
    pass


print("Test valid - no mitigation")
test_valid(generate_sql_string)
print("Test valid - weak mitigation")
test_valid(weak_mitigation)
print("Test valid - strong mitigation")
test_valid(strong_mitigation)

