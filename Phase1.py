from math import sqrt

"""
To ensure pi decimals are correct, I downloaded one (1) million digital pi from www.angio.net/pi/digits.html instead of generating them on my own,
and I found the first palindromic prime of nine (9) digits, which is 318272813.
The first occurrence of 318272813 was discovered in pi's decimal position 129079 (to 129087).
The complexity of this solution is O(n).
"""


def findFirstPalindromicPrime(arr):
    i, j, count = 0, 0, 0
    while (i+8 < len(arr)):
        while (count < 4 and i+8 < len(arr)):
            j = i+8-count*2
            if (arr[i] == arr[j]):
                count = count+1
            else:
                count = 0
            i = i+1
        if (isPrime(arr[i-4:j+4])):
            #print("First Palindromic Prime:")
            print(arr[i-4:j+4])
            # print(f'{i-3}--{j+4}')
            break
        count = 0


def isPrime(arr):
    n = int("".join(arr))
    prime_flag = 0
    if (n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    return False


with open("pi_dec_1m.txt", "r") as file:
    arr = file.read()

findFirstPalindromicPrime(arr)
