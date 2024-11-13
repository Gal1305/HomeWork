calls = 0
def count_calls ():
    global calls
    calls += 1

def string_info (string):
    string_0 = str(string)
    function_result = (len(string_0), string_0.upper(), string_0.lower())
    count_calls()
    return function_result

def is_contains (string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for q in range(len(list_to_search)):
        if str(list_to_search[q]).lower() == string:
            result = True
            break
        else: result = False
        continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)