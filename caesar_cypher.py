# simple implementation of caesar cypher
a=ord('a')
alphabet = [chr(i) for i in range(a,a+26)]

def print_menu():
    print("\n\n\n")
    print("------ CAESAR CYPHER ------")
    print("e - Encrypt")
    print("d - Decrypt")
    print("q - Quit")

def encrypt(word, shift):
    encrypt = []
    for letter in word:
        encrypt.append(ord(letter) + shift % 26)
    encrypted_list = [chr(i) for i in encrypt]
    encrypted_word = "".join(encrypted_list)
    return encrypted_word

def decrypt(word, shift):
    decrypt = []
    for letter in word:
        decrypt.append(ord(letter) - shift % 26)
    decrypted_list = [chr(i) for i in decrypt]
    decrypted_word = "".join(decrypted_list)
    return decrypted_word

print("hello >> 6")

enc = encrypt("hello", 6)
dec = decrypt(enc, 6)

print(enc)
print(dec)

option = ""
while option != "q":
    print_menu()
    option = input("Option: ")
    
    if option == "e":
        word = input("Word: ")
        shift  = int(input("Shift: "))
        encrypted = encrypt(word, shift)
        print(f"Result: {encrypted}")

    if option == "d":
        mistery = input("Mistery: ")
        shift  = int(input("Shift: "))
        decrypted = decrypt(mistery, shift)
        print(f"Word: {decrypted}")

