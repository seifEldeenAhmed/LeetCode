import string
def is_anagram (str1,str2):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for char in str1:
        d[char]+=1

    for char in str2:
        d[char]-=1

    for i in d.values():
        if i:
            return False

    return True

print(is_anagram('race','de'))

#_______________________________________


# solution without importing

def is_anagram2 (str1,str2):
    chars=[0]*26
    for char in str1:
        chars[ord(char)-ord("a")]+=1

    for char in str2:
        chars[ord(char)-ord("a")]-=1

    for i in chars:
        if i:
            return False

    return True

print(is_anagram2('racecar','carrace'))