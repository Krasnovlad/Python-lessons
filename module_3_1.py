calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    count_ = len(string)
    str_inf = (count_, string.upper(),string.lower())
    return str_inf

def is_contains(string, list_to_search):
    count_calls()
    list_to_search = list(list_to_search)
    string = str(string.lower())
    for i in range(len(list_to_search)):
        if str(list_to_search[i].lower()) == string.lower():
            res = True
            break
        else:
            res = False
            continue
    return res

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)