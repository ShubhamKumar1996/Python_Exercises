# Program to test whether given character is vowel or not.
# Program to check whether number is present in list or not.

def check_vowel(ch):
    if ch in "aeiou":
        print("%c is vowel" % ch)
    else:
        print("%c is consonant" % ch)


def check_num_presence(num_list, target):
    if target in num_list:
        print("%d is found" % target)
    else:
        print("%d is not found" % target)


check_vowel("a")
check_vowel("w")

check_num_presence([1,3,5,7,9], 7)
check_num_presence([1,3,5,7,9], 4)