import wget

import string

import os.path
from os import path


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = plaintext.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

numbers = []
flag = ""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Hi, today I will solve a problem for you')  # Press Ctrl+F8 to toggle the breakpoint.
    if not path.exists("ciphertext"):
        url = input("Enter the url for the file : ")
        filename = wget.download(url)

f = open("ciphertext", "r")

cipheredFlag = f.read()

message = cipheredFlag[8:]
message = message[:-1]
print(message + "is the original key")

flag = caesar(message, 4)
finalAnswer = "picoCTF{" + flag + "}"

print(finalAnswer)
'''
for l in flagWoPico:
    number = ord(l) - 96
    numbers.append(number)

print(numbers)
for i in range(-100, 100):
    for number in numbers:
        number -= i
        flag += chr(number + 96)
    print(flag)
    flag=''
'''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
