# def difference (a,b):
#     return a-b
# print(difference(2,2))
# print(difference(0,2))
from unittest import removeResult


# def print_day(number):
#     days_of_week = {
#         1: "Sunday",
#         2: "Monday",
#         3: "Tuesday",
#         4: "Wednesday",
#         5: "Thursday",
#         6: "Friday",
#         7: "Saturday"
#     }
#     return days_of_week.get(number, None)
# print(print_day(1))
# print(print_day(41))

# def last_element (list):
#     if len(list) == 0:
#         return None
#     return list[-1]
# print(last_element([1,2,3,4]))
# print(last_element([]))

# def number_compare(a,b):
#     if a > b:
#         return "First is greater"
#     elif a < b:
#         return "Second is greater"
#     else:
#         return "Numbers are equal"
# print(number_compare(4,1))
# print(number_compare(1,4))
# print(number_compare(3,3))

# def single_letter_count (word,letter):
#     word = word.lower()
#     letter = letter.lower()
#     return word.count(letter)
# print(single_letter_count('amazing','A'))
#
# def multiple_letter_count (word,):
#     letter_count = {}
#     for letter in word:
#         if letter in letter_count:
#             letter_count[letter] += 1
#         else:
#             letter_count[letter] = 1
#     return letter_count
# print(multiple_letter_count("hello"))
# print(multiple_letter_count("person"))

# def list_manipulation(lst, command, location, value=None):
#     if command == "remove":
#         if location == "end":
#             return lst.pop()
#         elif location == "beginning":
#             return lst.pop(0)
#     elif command == "add":
#         if location == "beginning":
#             lst.insert(0, value)
#             return lst
#         elif location == "end":
#             lst.append(value)
#             return lst
# print(list_manipulation([1,2,3], "remove", "end"))
# print(list_manipulation([1,2,3], "remove", "beginning"))
# print(list_manipulation([1,2,3], "add", "beginning", 20))
# print(list_manipulation([1,2,3], "add", "end", 30))

# def is_palindrome (word):
#     word = word.lower()
#     return word == word[::-1]
# print(is_palindrome('testing'))
# print(is_palindrome('tacocat'))
# print(is_palindrome('hannah'))
# print(is_palindrome('robert'))
#
# def frequency(list,search_term):
#     return list.count(search_term)
# print(frequency([1,2,3,4,4,4], 4))
# print(frequency([True, False, True, True], False))

# def flip_case (string, letter):
#     result =""
#     for char in string:
#         if char.lower() == letter.lower():
#             if char.islower():
#                 result += char.upper()
#             else:
#                 result += char.lower()
#         else:
#             result += char
#     return result
# print(flip_case("Hardy har har", "h"))

# def multiply_even_numbers(numbers):
#     product = 1
#     has_even = False
#     for num in numbers:
#         if num % 2 == 0:
#             product *= num
#             has_even = True
#     return product if has_even else 0
# # print(multiply_even_numbers([2,3,4,5,6]))

# def mode(number):
#     frequency = {}
#
#     for num in number:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
#     most_frequent = max(frequency, key=frequency.get)
#     return most_frequent
# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))

# def capitalize(string):
#     return string.capitalize()
#
# print(capitalize("tim"))
#
# def compact (lst):
#     return [item for item in lst if item]
#
# print (compact([0,1,2,"",[], False, {}, None, "All done"]))

# def partition (lst, callback):
#     true_list = []
#     false_list = []
#     for i in range(len(lst)):
#         if callback(lst[i]):
#             true_list.append(lst[i])
#             callback(lst[i])
#         else:
#             false_list.append(lst[i])
#     return [true_list, false_list]
#
# def is_even(num):
#     return num % 2 == 0
# print(partition([1,2,3,4], is_even))

# def intersection(two_d_list):
#     if not two_d_list:
#         return []
#     common_values = set(two_d_list[0])
#     for sublist in two_d_list[1:]:
#         common_values.intersection_update(sublist)
#     return list(common_values)
#
#
# print(intersection([[1, 2, 3], [2, 3, 4]]))

# def once(func):
#     def wrapper(*args, **kwargs):
#         if not hasattr(wrapper, 'has_run'):
#             wrapper.has_run = True
#             return func(*args, **kwargs)
#         return None
#     return wrapper
#
# def add(a,b):
#     return a + b
# one_addition = once(add)
#
# print(one_addition(2,2))
# # print(one_addition(2,2))
# # print(one_addition(12,2400))
#
# def sequence_sum(begin_number, end_number, step):
#     if begin_number > end_number:
#         return 0
#
#     total_sum = 0
#     for i in range(begin_number, end_number + 1, step):
#         total_sum += i
#
#     return total_sum
#
# print(sequence_sum(2, 2, 2))

# def count_smileys(arr):
#     count = 0
#
#     for face in arr:
#         if len (face) == 2 and face [0] in [";",":"] and face [1] in [")","D"]:
#             count += 1
#         if len (face) == 3 and face [0] in [";",":"] and face [1] in ["-","~"] and face [2] in [")","D"]:
#             count += 1
#     return count
#
# arr = [":)", ";-D", ":~)", ":>"]
# print(count_smileys(arr))

def sentence_count(paragraph):
    count = 0
    for i in paragraph:
        if i in ['.','?',"!"]:
            count += 1
    return count