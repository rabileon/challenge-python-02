# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def generate_password():
    longitud = random.randint(8,16)
    password = []

    def generate_list_caracter(longitud,password):
        bCaracter0 = False
        bCaracter1 = False 
        bCaracter2 = False
        bCaracter3 = False
        for idx in range(longitud):
            typeCaracter = random.randint(0,3)
            if typeCaracter == 0 :
                bCaracter0 = True
                password.insert(idx,get_caracter(typeCaracter))
            elif typeCaracter == 1 :
                bCaracter1 = True
                password.insert(idx,get_caracter(typeCaracter))
            elif typeCaracter == 2 :
                bCaracter2 = True
                password.insert(idx,get_caracter(typeCaracter))
            elif typeCaracter == 3 :
                bCaracter3 = True
                password.insert(idx,get_caracter(typeCaracter))
        if not (bCaracter0  and bCaracter1 and bCaracter2 and bCaracter3):
            password.clear()
            generate_list_caracter(longitud,password)
    
    generate_list_caracter(longitud,password)
    password_confirm =  ''.join(password)
    return password_confirm

def get_caracter(typeCaracter):
    if typeCaracter == 0:
        return SYMBOLS[random.randint(0, len(SYMBOLS)-1)]
    elif typeCaracter == 1:
        return string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase )-1)]
    elif  typeCaracter == 2:
        return  string.digits[random.randint(0, len(string.digits)-1)]
    elif typeCaracter == 3:
        return  string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase)-1)]


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
