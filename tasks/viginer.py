#! /usr/bin/env python3 


def get_string_and_key(message_string, message_key):
    input_string = input(message_string)
    input_key = input(message_key)

    return input_string, input_key

def generate_key(user_string, key):
    key = list(key)
    if len(user_string) == len(key):
        return(key)
    else:
        for i in range(len(user_string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     

def cipher_text(user_string, key):
    cipher_text = []
    for i in range(len(user_string)):
        x = (ord(user_string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     

def original_text(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))
     

if __name__ == "__main__":
    message_string = 'Enter string -> '
    message_key = 'Enter key -> '

    user_string, keyword = get_string_and_key(message_string, message_key)

    key = generate_key(user_string, keyword)
    cipher_text = cipher_text(user_string, key)
    print("Cipher text -> ", cipher_text)
    
    print(f"Original/Decrypted Text -> {original_text(cipher_text, key)}")