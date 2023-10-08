def loading_bar(percentages: int):
    times_count = int(percentages / 10)
    loading_bar_list = ["."] * 10
    for x in range(0, times_count):
        loading_bar_list[x] = "%"

    if percentages == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{percentages}% [{''.join(loading_bar_list)}]")
        print("Still loading...")

real_input = int(input())
result = loading_bar(real_input)
result