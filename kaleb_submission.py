
'''
injection planning 

take 2 strings from user (username and password)

show raw unfiltered atttack

have 2 functions (weak and strong filtering)
func1: weak blacklists certain characters (return string)
func2: strong whitelists certain characters (return string)
'''

def take_info():
    username = input("please input a username")
    password = input("please input a password")
    return username,password

def weak_injection(user_entry):

    for character in user_entry:
        if character == '':
            user_entry.pop(character)

def strong_injection(user_entry):
    character_white_list = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                  'r','s','t','u','v','w','x','y','z',' ']
    character_number_list = ['1','2','3','4','5','6','7','8','9','0']

    for character in user_entry:
        character = character.lower()
        if (character not in character_white_list and character not in character_number_list):
            return "invalid character in submission"
        else:
            pass
        


def test_cases():
    