immutable_var = (1, 2, 'a', 'b')
print ('Immutable tuple:', immutable_var)
mutable_list = [1, 2, 'a', 'b']
print('mutable_list', mutable_list) # эта строка лишняя (по заданию), для большей наглядности что список изменяется
mutable_list.append('Modified')
print('mutable_list', mutable_list)