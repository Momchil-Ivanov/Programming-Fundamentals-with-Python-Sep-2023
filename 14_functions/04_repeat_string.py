repeat_string = lambda string_input, times: str(string_input) * int(times)

string_tested = str(input())
times_tested = int(input())

result = repeat_string(string_tested, times_tested)
print(result)