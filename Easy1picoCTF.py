from string import ascii_uppercase as letters

key =           "SOLVECRYPTO"
encryptedFlag = "UFJKXQZQUNB"

alphabet = []
for i in letters:
    alphabet.append(i)

solvedFlag = []

for v,k in zip(encryptedFlag, key):
    sol = alphabet[alphabet.index(v)-alphabet.index(k)]
    solvedFlag.append(sol)
    print(alphabet.index(v)-alphabet.index(k))

print("picoCTF{" + ''.join(solvedFlag) + "}")



