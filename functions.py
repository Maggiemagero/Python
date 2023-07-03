def mitmorn():
    print("This is MIT morning class")


mitmorn()
mitmorn()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)


calculate()


def majina(myfirstname, mysecondname, age):
    print('My name is', myfirstname + " " + mysecondname, 'i am', "", age, 'years old')


majina('Maggie', 'Magero', 18)
majina('Maggie', 'Magero', 18)
majina('Maggie', 'Magero', 18)
majina('Maggie', 'Magero', 18)
majina('Maggie', 'Magero', 18)


def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = (2, 5, 6, 3, 5)
result = calculate_average(data)
print("The average is", result)

# create a function that gives you the longest string in a list
