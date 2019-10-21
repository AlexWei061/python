
"""
Description:
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :]
"""

""""
def is_eye(c):
    if c == ":":
        return True
    elif c == ";":
        return True
    else:
        return False

def is_nose(c):
    if c == "~":
        return True
    elif c == "-":
        return True
    else:
        return False

def is_face(c):
    if c == ")":
        return True
    elif c == "D":
        return True
    else:
        return False


def is_smile_face(s):
    if len(s) == 2:
        if is_eye(s[0]) and is_face(s[1]):
            return True

    elif len(s) == 3:
        if is_eye(s[0]) and is_nose(s[1]) and is_face(s[2]):
            return True
    return False


def count_smileys(arr):
    snum = 0
    for sface in arr:
        if is_smile_face(sface):
            snum = snum+1
    return snum # the number of valid smiley faces in array/list

smile_faces = [':(',':~)',';~D',':)']
print(count_smileys(smile_faces))

num = 9
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    list = []
    x = 1
    while (num/x > 1):
        x = x+1
        print(x)
        if num % x == 0:
            return False
    return True
print(is_prime(num))
"""
"""
import copy
hamming_num_list = []
num = 19
def is_hamming_num (num):
    prime_num_list = []
    i = 2
    while num != 1:
        if num % i == 0:
            num = num / i
            prime_num_list.append(i)
        else:
            i = i + 1
    tmp_list = copy.deepcopy(prime_num_list)
    for tmp in tmp_list:
        if tmp in [2,3,5]:
            del prime_num_list[0]
    if len(prime_num_list) == 0:
        return True
    else:
        return False
def hamming(n):
    hamming_num = 0
    k = 1
    h = 1
    while k <= n:
        if is_hamming_num(h):
            k = k+1
            hamming_num = h
        h = h+1
    return hamming_num
print(hamming(num))
"""

#def yield_hamming():
#    hammings = [1]
#    max_hamming = 1
#
#    while True:
#        hammings.append()
#        yield max_hamming
def hamming(n):
    hamming = [1]
    while len(hamming) <= n:
        for num in hamming:
            if num*2 in hamming:
                hamming.append(num*2)
            elif num*3 in hamming:
                hamming.append(num*3)
            elif num*5 in hamming:
                hamming.append(num*5)
    return hamming[len(hamming)-1]
#print(hamming)
#print(hamming(2))

import collections
import copy
import bisect
all_hammings = [1]
seed_hammings = [1] #only include hamming for next iteration
reverse_hammings_dict = collections.OrderedDict()  # all hamming numbers
reverse_hammings_dict[1] = 1  # hamming value is 1, is the first hamming number
hammings_list = [1]
count = 1

def hamming_gj(n):
    global all_hammings
    global seed_hammings
    global hammings_dict
    global reverse_hammings_dict
    global count
    while count <= n:
        next_seeds = []
        for num in seed_hammings:
            for factor in [2,3,4,5]:
                next_test_hamming = num * factor
                if next_test_hamming not in hammings_list:
                    count = count + 1
                    next_seeds.append(next_test_hamming)
                    reverse_hammings_dict[next_test_hamming] = count
                    bisect.insort(hammings_list, next_test_hamming)
        seed_hammings = next_seeds.copy()

    return hammings_list[n]

print(hamming_gj(8))


