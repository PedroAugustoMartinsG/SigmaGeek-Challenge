from math import sqrt

"""
To ensure pi decimals are correct, I downloaded digital pi's files from archive.org instead of generating them on my own,
and I found the first palindromic prime of 21 digits.
The complexity of this solution is O(n).
"""


def findFirstPalindromicPrime(arr):
    i, j, count = 0, 0, 0
    while (i+20 <= len(arr)-2):
        while (count < 10 and i+20 <= len(arr)-2):
            j = i+20-count*2
            if (arr[i] == arr[j]):
                count = count+1
            else:
                count = 0
            i += 1
        if (isPrime(arr[i-10:j+10])):
            print("Palindromic Prime:")
            print(f'i: {i}')
            print(f'arr[i]: {arr[i]}')
            print(f'j: {j}')
            print(f'arr[j]: {arr[j]}')
            print(arr[i-10:j+10])
            print(f'{i-9}--{j+10}')
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
    else:
        return False


round = 0
fileName = "nBillion.txt" 
with open(fileName) as f:
    dataA = f.read(1_000_000)
    while True:
        findFirstPalindromicPrime(dataA)
        round += 1
        dataA = dataA[1_000_000-20:] + f.read(1_000_000-20)
        if (round % 100):
            print(f'{round} million was verified')
        if not dataA:
            break


