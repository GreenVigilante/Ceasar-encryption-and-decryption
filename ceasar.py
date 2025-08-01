import string

tobe = input("Encrypt or Decrypt: ")
shift = int(input("Enter Number of shifts: "))
tobe = tobe.lower()

if tobe == "encrypt":
    text = str(input("Enter to be encrypted: "))
    alph ="abcdefghijklmnopqrstuvwxyz"
    shifted = alph[shift:]+alph[:shift]
    table = str.maketrans(alph, shifted)
    encrypt = text.translate(table)
    print(encrypt)
elif tobe == "decrypt":
    text = str(input("Enter to be decrypted: "))
    alph ="abcdefghijklmnopqrstuvwxyz"
    shifted = alph[shift:]+alph[:shift]
    table = str.maketrans(shifted, alph)
    decrypt = text.translate(table)
    print(decrypt)

else:
    print("Invalid Input")

