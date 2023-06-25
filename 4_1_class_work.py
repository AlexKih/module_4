## решение задачи за O(N**2)  цикл в цикле

# def strcounter(s):
#     counter = 0
#     for lit in s:
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter += 1
#         print(lit, counter)
#
# strcounter('abcd')
# в этом коде counter находится не на своем месте поэтому не считаются буквы, а перечисляются

# def strcounter(s):
#     for lit in s:
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter += 1
#         print(lit, counter)
#
# strcounter('aaabccd')
# в этом коде counter находится в правильном месте и считает кол-во каждой из букв

## решение задачи за O(N*M) где М <= N
# s = ('aaabbcdd')
# print(list(s))
# print(set(s))

# def strcounter(s):
#     for lit in set(s):
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter += 1
#         print(lit, counter)
#
# strcounter('aaabccdd')

## решение задачи за O(N+N) --> O(2N)  --> O(N)

# def strcounter(s):
#     lits_counter = {}
#     for lit in s:
#         lits_counter[lit] = lits_counter.get(lit, 0) + 1
#     for lit, counter in lits_counter.items():
#         print(lit, counter)
#
# strcounter('aaaabbcccddddd')

def palindrome(s):
    return s[::-1] == s

while True:
    s = input ('введите слово')
    print(palindrome(s))