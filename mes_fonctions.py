def eratosthene(b):
    liste = [True]*(b+1)
    liste[0],liste[1] = False, False
    for i in range(b+1):
        if liste[i] == True:
            yield i
            for k in range(i**2, b+1, i):
                liste[k] = False

def main():
    print("hello")