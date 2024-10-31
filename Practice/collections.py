# import random
# random.randint(1,10)
# random.randrange(4)
# random.random()
#
# from random import choice as c
# print(c([1, 2, 3, 4, 5]))
# print(random.randint(1, 10))
# print(random.randrange(4))

# from collections import Counter
# #
# # l = [1, 1, 2, 3, 3, 4, 4, 5, 5]
# # Counter(l)
# #
# # print(Counter(l))
# #
# string: str = "aweosakjdsaldwjdwq"
# Counter(string)
# s = 'this is such a nice nice nice thing that is nice!'
# c = Counter(s.split())
#
# print(c)

# from collections import defaultdict
#
# counts = defaultdict(int)
# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
#
# for word in words:
#     counts[word] += 1
#     print(counts)

# from collections import defaultdict
#
# d = defaultdict(list)
# d['fruits'].append('apple')
# d['fruits'].append('orange')
#
# print(d)

# from collections import OrderedDict
#
# # d = {}
# # d['one'] = 1
# # d['two'] = 2
# # d['three'] = 3
# # d['four'] = 4
# #
# # for k,v in d.items():
# #     print(k,v)
#
# od = OrderedDict()
# od['one'] = 1
# od['two'] = 2
# od['three'] = 3
# od['four'] = 4
#
# for k,v in od.items():
#     print(k,v)

from collections import namedtuple

t = [1, 2, 3]
t[1] = 2

Person = namedtuple('Person', 'first_name last_name fav_color')
elie = Person('Elie', 'Schoppik', 'purple')
print(elie.fav_color)