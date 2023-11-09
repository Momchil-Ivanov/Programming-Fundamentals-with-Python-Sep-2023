ban_list = input().split(", ")
current_text = input()

for word in ban_list:
    while word in current_text:
        censor = "*" * len(word)
        current_text = current_text.replace(word,censor)

print(current_text)