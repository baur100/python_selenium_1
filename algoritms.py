# # Создайте range из положительных четных чисел от 15 до 27 с шагом 3 - выведите его на экран
#
# start, end = 15, 27
# for num in range(start, end, 3):
#     if num % 2 == 0:
#         print(num)


#
#
# list_1 = [12,34,25,76,34,89,97,45,33,99]
# print(max(list_1))
# print(min(list_1))
# i = sum(list_1)
# print(i)

#
# Выведите на экран все индексы где в массиве хранится 10
# list_1 = [10, 15, 10, 6, 23, 10, 16]
# list_2 = []
# for i in range(len(list_1)):
#     if list_1[i] == 10:
#         list_2.append(i)
#
# print(list_2)

#
# def prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# for num in range(1, 21):
#     print(num, prime(num))
#
# word1 = "bad credit"
# word2 = "debit card"
#
#
# def anagram(w1, w2):
#     if len(w1) != len(w2):
#         return False
#     list1 = sorted(w1)
#     list2 = sorted(w2)
#     for i in range(len(w1)):
#         if list1[i] != list2[i]:
#             return False
#     return True
#
#
# print(anagram(word1, word2))
#
#
# def c_to_f(temp):
#     return 9 / 5 * temp + 32
#
#
# print(c_to_f(25))
#
#
# def f_to_c(temp):
#     return (temp - 32) * 5/9
# print(f_to_c(77))


# def fizz_buzz(i):
#     if i % 3 == 0 and i % 5 == 0:
#         return "fizzbuzz"
#     if i % 3 == 0:
#         return "fizz"
#     if i % 5 == 0:
#         return "Buzz"
#
#
# for i in range(1, 21):
#     print(i, fizz_buzz(i))

#
#
#

# for i in range(21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif i % 3 == 0:
#         print("fizz")
#         continue
#     elif i % 5 == 0:
#         print("buzz")
#         continue
#     print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
from pip._vendor.msgpack.fallback import xrange

word1 = "bad credit"
word2 = "debit card"









# For an array of integers/characters, length unknown, write an algorithm to store them backwards by using the same array.
# Note: You must build an algorithm and not just use built-in string reversing functionality.
# https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python


# def prime(num):


# a = [1, 2, 3, 4]
# a = a[::-1]
# print(a)
#
# l = list(range(10))
# l = l[::-1]
# print(l)


# def isPalindrome(s):
#     return s == s[::-1]
#
#
# # Driver code
# s = "kayak"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")

def palindrome(n):
    return n == n[::-1]

print(palindrome("kayak"))

# print ('mississipi'.count('s'))
#
# def palindrone_sentence(sentence):
#     string = ''
#     for x in sentence:
#         if x.isalnum():
#             string += x
#
#     return string[::-1].casefold() == string.casefold()
#
# print(palindrone_sentence("Mr. Owl ate my metal worm"))


# def fibonachi(n):
#     if 0 <= n <= 1:
#         return n
#     n_minus1, n_minus2 = 1, 0
#     result = None
#     for i in range (n - 1):
#         result = n_minus2 + n_minus1
#         n_minus2 = n_minus1
#         n_minus1 = result
#
#     return result
#
# for i in range(12):
#     print(i,fibonachi(i))



