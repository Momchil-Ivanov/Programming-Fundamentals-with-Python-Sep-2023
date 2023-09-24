victim = str(input())
mutagen = str(input())
list_victim = list(victim)
list_mutagen = list(mutagen)

for x in range (0, len(victim)):
    if victim[x] != mutagen[x]:
        list_victim[x] = list_mutagen[x]
        print("".join(list_victim))