my_dict = {'Nastya':1999, 'Stepa':2012, 'Tanya':2011}
print(my_dict)
print('Existing value:', my_dict['Stepa'])
print('Not existing value:', my_dict.get('Sofiya'))
my_dict.update({'Sasha':2004,
                'Vovka':2012})
a = my_dict.pop('Sasha')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print (' ')
my_set = {'Sasha', 'Tanya', 1, 2, 3, 2, 3, 1, 3.14}
print('Set:', my_set)
my_set.add((7, 8, 9))
my_set.add(10)
my_set.discard(1)
print('Modified set:', my_set)
