import helpers


def calculate_numbers(a, b, fn):
    if fn == 'add':
        return add(a, b)
    elif fn == 'subtract':
        return subtract(a, b)


calculate_numbers(1, 4, 'add')
