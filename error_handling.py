# The try block lets you test a block of code for errors.
try:
    print(8/0)

# The except block lets you handle the error.
except :
    print('oopsies! you cant do thhaatt!')

# you can use the else keyword to define a block of code to be executed if no errors were raised:
else:
    print('it worked!')

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
finally:
    print('first attempt')


# this one does not work cus the error we excepted doesn't happen and it will rasie an error
# try :
#     n = m
# except TypeError :
#     print('meow')

# this one works
try :
    n = m
except NameError :
    print('meow')  


# if we have more than one except we have to specify all the except blocks errors but the last one 
try : 
    n == 9
except SyntaxError:
    print(1)
except NameError:
    print(2)
except : # the last ones error can be specify or not
    print(3)


try :
    meo = 4 + '3'
except TypeError : 
    print(TypeError) # prints the class of the error

try :
    meo = 4 + '3'
except TypeError as TP: 
    print(TP) # prints info about the ocuring error

try :
    d = input('inter a number : ') # if user inters a letter the error will be TypeError and if they enter zero it will be ZeroDivisionError
    print(d/2)
except (TypeError, ZeroDivisionError) as meows :
    print(meows)

# if there is more than one exception the order is important
class B(Exception):

    pass


class C(B):

    pass


class D(C):

    pass


for cls in [B, C, D]:

    try:

        raise cls()

    except D:

        print("D")

    except C:

        print("C")

    except B:

        print("B")


# error rasing
def electricity_consumption(last_reading, current_reading):

    if last_reading < 0 or current_reading < 0:

        raise ValueError('Negative readings')

    units = current_reading - last_reading

    if units < 0:

        raise ValueError('Negative consumption')
    
 #electricity_consumption( 67, 66)

