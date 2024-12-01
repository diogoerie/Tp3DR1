
palavra = "para"

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    return False

print(palindromo(palavra))
