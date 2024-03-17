import math
#errors in python
# we have 2 types of errors in python :
# 1 syntax errors
# 2 logica errors (all the errors that are not related to syntax error)
#1# type error -> using a wrong type of value 

# print(len(123))
"""or"""
# print("23" + 88)
"""or"""
# x = "meow"
# x() #calling a noncallable object
"""or"""
# def sum(num1, num2):
#     print(num1 + num2)
# sum(1, "3") # giving a wrong argument to a function
"""or"""
# def fullname(firstName, lastName):
#     full = firstName + lastName
#     print(full)
# fullname('ali', 'meow', '2')

#2# syntax error -> not folowing the syntax rules

# print('hi'
"""or"""
# if y - 2 :
#     print(e)
# else :
#     r = 2 # using 'else' without 'if'
"""or"""
# try :
#     f = 2 + 3 # using 'try' withot 'except' or 'finally'

#3# name error -> using a varibale that does not exist or a module that has not been imported

# num1 = random.randrange(1,10) # using a module that has not been imported
"""or"""
# print(x)

#4# value error -> right type wrong value (often in mathematic codes)

# math.sqrt(-10) # this function accept int (the type is correct) but the value is not right for this function (wrong value)
"""or"""
# s = int('meow')
"""or"""
# furit = ['apple', 'orange', 'watermelon']
# furit1, furit2 = furit

#5# key error -> using a key that doesn't exist

# dic = {'meow' : 1, 'purr' : 2}
# print(dic['moo'])

#6# index error -> using an index that does not exist (happens to any object that have index like str, list, tuple...)

# momo = [1, 2, 3, 4]
# print(momo[4])

#7# attribute error -> using a wrong attribute or spelling it wrong

# dic = {}
# dic.append(1) # appent is not a dictionary's attribute

#8# zero division error -> divide a number by 0
# a=20
# b=0
# print(a/b)

#9# import error -> mistakes in importing

#10# indentation error -> 

# if 3 > 2 :
# print(1)
