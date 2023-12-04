number_of_pieces = int(input())
pieces_dict = {}

for x in range(0, number_of_pieces):
    piece_info = input().split("|")
    current_piece = {'composer': {piece_info[1]}, 'key': {piece_info[2]}}
    pieces_dict[piece_info[0]] = current_piece

command = input()

while command != "Stop":
    command_to_list = command.split("|")
    current_command = command_to_list[0]
    piece = command_to_list[1]

    if current_command == "Add":
        composer = command_to_list[2]
        key = command_to_list[3]

        if piece in pieces_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = {'composer':{composer}, 'key':{key}}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif current_command == "Remove":
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_command == "ChangeKey":
        new_key = command_to_list[2]
        if piece in pieces_dict.keys():
            pieces_dict[piece]['key'] = "  " + new_key + "  "
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for each_piece in pieces_dict.keys():
    print(f"{each_piece} -> Composer: {str(pieces_dict[each_piece]['composer'])[2:-2]}, Key: {str(pieces_dict[each_piece]['key'])[2:-2]}")