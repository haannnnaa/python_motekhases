dic = {
    2 : 6 ,
    'meow' : True,
    (7) : 'jntsws',
    'nana' : 6,
    345 : [1,2,3]
      }
print(dic)

# creating a dictionary
a = dict(name= 'hana', age= 20, j23 = (4,4)) #keys type will be string
print(a)

# creating a dictionary
info = dict([('name', 'hana'), ('age', 19), (3, 4)])
print(info)

# creating a dictionary
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 
myDict = dict(zip(keys, values)) 
print(myDict)

# creating a dictionary
dic=dict.fromkeys(range(5), True)
print(dic)

# calling a keys value
print(info['age'])

# updating a keys value
r = info['age'] = 20
print(r)

# adding a new key : value
info['car'] = '206'

# deleting a key : value
del info[3]
print(info)

# clearing the dictionary
car = {'mvm' : 4, "pride" : 1}
car.clear()

# deleting the whole dictionary
meow = {'moeeeeeeewwwww' : 'wwksnmsjlnwa'}
del meow

# get method
d = {'a': 10, 'b': 20, 'c': 30}

print(d.get('b'))
print(d.get('z'))
print(d.get('z', -1))
print(d.get('a', 110))

print(d)

#method items 
d = {'a': 10, 'b': 20, 'c': 30}

print(list(d.items()))
print(list(d.items())[1][0])
print(list(d.items())[1][1])

# key method 
d = {'a': 10, 'b': 20, 'c': 30}

print(d)

print(list(d.keys()))

#value method
d = {'a': 10, 'b': 20, 'c': 30}
print(d)
print(list(d.values()))

#pop method
d = {'a': 10, 'b': 20, 'c': 30}

print(d.pop('b'))
print(d.pop('a', 111111))
print(d.pop('z', -1))
print(d)

#popitem method
d = {'a': 10, 'b': 20, 'c': 30}
print(d.popitem())
print(d)

#update method
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)


d3 = {'a': 10, 'b': 20, 'c': 30}
d3.update([('b', 200), ('d', 400)])
print(d3)


d4 = {'a': 10, 'b': 20, 'c': 30}
d4.update(b=200, d=400)
print(d4)

# copy method
original = {1: 'geeks', 2: 'for'}

new = original.copy()

new.clear()

print('new: ', new)

print('original: ', original)

# setdefault method
print(d4.setdefault(55555))
print(d4)
