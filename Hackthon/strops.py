def getspan(s, ss):
    start = s.find(ss)
    end = start + len(ss)
    print(start, end)
    start1 = s.find(ss, end)
    end1 = start1 + len(ss)
    print(start1, end1)
s = input("Enter a word to be searched: ")
ss = input(f"Enter a substring to be searched in {s}: ")
getspan(s,ss)
print("-"* 80)

# ----------------------------------------------
def reverseWords(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    print(reverse)
s = input("Enter a word to be reversed: ")
reverseWords(s)
print("-"* 80)

# ----------------------------------------------
def removePunctuation(s):
    a = ""
    for i in s:
        if(i.isalpha() or i.isdigit() or i==" "):
            a = a+i
    return a
s = input("Enter a sentence with puctuation: ")
print(removePunctuation(s))
print("-"*80)

# ----------------------------------------------
def countWords(s):
    word = s.split()
    print(len(word))
s = input("Enter a word to get the count of the word: ")
countWords(s)
print("-"*80)
# ----------------------------------------------
def charecterMap(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
s = input("Enter a sentence to get the count of each character: ")
charecterMap(s)
print("-"*80)
# ----------------------------------------------


def makeTitle(s):
    titled = s.title()
    print(titled)
s = input("Enter a sentence to make it to a title: ")
makeTitle(s)
print("-"*80)
# ----------------------------------------------
def normalizeSpaces(s):
    a = s.split()
    # print(a)
    b = " ".join(a)
    print(b)
s = input("Enter a sentence to normalize spaces: ")
normalizeSpaces(s)
print("-"*80)
# ----------------------------------------------
def transform(s):
    swapped = s.swapcase()
    reverse = ""
    for char in swapped:
        reverse = char + reverse
    print(reverse)
s=input("Enter a string for transforming: ")
transform(s)
print('-'*80)
# ---------------------------------------------- 
import random
def permuntations(s):
    s1 = list(s)
    factorial = 1
    mn=[]
    for i in range(1, len(s1)+1):
        factorial *= i
    # print(factorial)
    for i in range(1, factorial+1):
        # empty_list = []
        random.shuffle(s1)
        a = "".join(s1)
        # print(a)
        while True:
            if a not in mn:
                mn.append(a)
                break
            else:
                random.shuffle(s1)
                a = "".join(s1)

    return mn
s =input("Enter a string to get the different possible permutations of it: ")
print(permuntations(s))
print('-'*80)
# ----------------------------------------------