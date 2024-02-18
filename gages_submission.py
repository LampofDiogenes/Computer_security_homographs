def weak_mitigation(input_str):
    sanitized_input = input_str.replace("'", "")
    return sanitized_input

# Test weak mitigation function
def test_weak_mitigation():
    test_input = "user1'; DROP TABLE users; --"
    sanitized_input = weak_mitigation(test_input)
    print(sanitized_input)

test_weak_mitigation()