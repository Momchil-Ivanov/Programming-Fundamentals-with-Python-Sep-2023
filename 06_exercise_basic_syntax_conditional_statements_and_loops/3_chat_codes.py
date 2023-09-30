count_of_messages = int(input())

for x in range (0, count_of_messages):

    current_message_num = int(input())
    current_message = str()


    if current_message_num == 88:
        current_message = "Hello"
    elif current_message_num == 86:
        current_message = "How are you?"
    elif current_message_num < 88:
        current_message = "GREAT!"
    elif current_message_num > 88:
        current_message = "Bye."

    print(current_message)