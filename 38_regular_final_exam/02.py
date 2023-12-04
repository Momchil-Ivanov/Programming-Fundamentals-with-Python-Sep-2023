import re

count_of_inputs = int(input())
pattern = r"![A-Z][a-z]{2,}!:\[[A-Za-z]{8,}\]"
patter_brackets = r"\[[A-Za-z]{8,}\]"
pattern_command = r"![A-Z][a-z]{2,}!"
for x in range(0, count_of_inputs):
    current_input = input()
    match = re.fullmatch(pattern, current_input)
    try:
        string_match = str(match.group())
        match_string = re.findall(patter_brackets, string_match)
        final_string = match_string[0]
        final_string = final_string[1:-1]

        match_command = re.findall(pattern_command, string_match)
        final_command = match_command[0]
        final_command = final_command[1:-1]

        final_output = f"{final_command}: "
        for char in final_string:
            char_to_ascii = ord(char)
            final_output += f"{char_to_ascii} "
        final_output = final_output.strip()
        print(final_output)
    except:
        print(f"The message is invalid")
        continue