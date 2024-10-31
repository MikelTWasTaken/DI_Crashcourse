# Functions
# https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8

# def hello_func():
#     print('Hello Function.')
#
# hello_func()
# hello_func()
# hello_func()
# hello_func()

#DRY - DON'T REPEAT YOURSELF

# def hello_func(greeting, name ='You'):
#     return '{}, {}.'.format(greeting, name)
#
# # print(hello_func().lower())
# # print(hello_func().upper())
# print(hello_func('Hi', 'John'))

# print(len('Test'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Art']
info = [name:'John', age: 22]

student_info(*courses, **info)