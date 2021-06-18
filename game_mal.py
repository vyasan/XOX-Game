# --------- ഗ്ലോബൽ  വേരിയബിൾ -----------
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]  # ബോർഡ് ഡാറ്റ
game_still_going = True
winner = None
current_player = "X"  # X ആണ് നിലവിലെ കളിക്കാരൻ


# ------------- fns ---------------
def play_game():  # XOX ഗെയിം ആരംഭിക്കുന്നു
    display_board()  # ആദ്യ ഗെയിം ബോർഡ് കാണിക്കുന്നതിന്
    while game_still_going:  # നിർത്തുന്നതുവരെ ഗെയിം ലൂപ്പ് ചെയ്യുക (winner അല്ലെങ്കിൽ tie)
        handle_turn(current_player)  # അടുത്ത കളിക്കാരന് അവസരം കൈമാറുന്നു
        check_if_game_over()
        flip_player()  # മറ്റ് കളിക്കാരന് അവസരം കൈമാറുന്നു
    if winner == "X" or winner == "O":  # ഗെയിം പൂർത്തിയായി & print winner അല്ലെങ്കിൽ tie
        print(winner + " ജയിച്ചു.")
    elif winner is None:
        print(" ടൈ.")


def display_board():  # സ്‌ക്രീനിൽ ഗെയിം ബോർഡ് പ്രദർശിപ്പിക്കുക
    print("\n")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | " + "      | 7 | 8 | 9 | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | " + "      | 4 | 5 | 6 | ")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | " + "      | 1 | 2 | 3 | ")
    print("\n")


def handle_turn(player):  # അടുത്ത കളിക്കാരനായി അവസരം കൈമാറുന്നു
    print(player + "'S ഊഴം.")  # അടുത്ത കളിക്കാരന്റെ അവസരം
    position = input("1നും 9നും ഇടയിലെ ഒരു ലൊക്കേഷൻ തെരഞ്ഞെടുക്കുക: ")  # input നൽകുന്നത് ഉറപ്പുവരുത്തുക
    valid = False
    while not valid:  # input valid അണെന്ന് പരിശോധിക്കുക
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("1നും 9നും ഇടയിലെ ഒരു ലൊക്കേഷൻ തെരഞ്ഞെടുക്കുക: ")
        position = int(position) - 1  # ബോർഡ് പട്ടികയിൽ ശരിയായ സ്ഥാനം (position)
        if board[position] == "-":  # ബോർഡിലെ vacancy ഉറപ്പാക്കുക
            valid = True
        else:
            print("ഒരിക്കൽ ഉപയോഗിച്ച ലൊക്കേഷൻ പിന്നെയും ഉപയോഗിക്കരുത് .")
    board[position] = player
    display_board()  # ഗെയിം ബോർഡ് പ്രദർശിപ്പിക്കുക


def check_if_game_over():  # ഗെയിം അവസാനിച്ചോ പ്രവർത്തിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക
    check_for_winner()
    check_for_tie()


def check_for_winner():  # ആരെങ്കിലും വിജയിച്ചിട്ടുണ്ടോയെന്ന് പരിശോധിക്കുക
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():  # row പരിശോധിക്കുക
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"   # ഏതെങ്കിലും വരികൾക്ക് എല്ലാ മൂല്യങ്ങളും തുല്യമാണോയെന്ന് പരിശോധിക്കുക
    if row_1 or row_2 or row_3:   # വരികളൊന്നും പൊരുത്തപ്പെടുന്നില്ലെങ്കിൽ, ഒരു win ഉണ്ടെന്ന് flag ചെയ്യുക
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:  # return None
        return None


def check_columns():  # column പരിശോധിക്കുക
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"    # ഏതെങ്കിലും നിരകൾക്ക് എല്ലാ മൂല്യങ്ങളും തുല്യമാണോയെന്ന് പരിശോധിക്കുക
    if column_1 or column_2 or column_3:  # വരികളൊന്നും പൊരുത്തപ്പെടുന്നില്ലെങ്കിൽ, ഒരു win ഉണ്ടെന്ന് flag ചെയ്യുക
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None  # return None


def check_diagonals():  # diagonals പരിശോധിക്കുക
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"    # ഏതെങ്കിലും rows എല്ലാ മൂല്യങ്ങളും തുല്യമാണോയെന്ന് പരിശോധിക്കുക
    if diagonal_1 or diagonal_2:  # വരികളൊന്നും പൊരുത്തപ്പെടുന്നില്ലെങ്കിൽ, ഒരു win ഉണ്ടെന്ന് flag ചെയ്യുക
        game_still_going = False
    if diagonal_1:  # return winner
        return board[0]
    elif diagonal_2:
        return board[2]
    else:  # return None
        return None


def check_for_tie():  # ഒരു tie ഉണ്ടോയെന്ന് പരിശോധിക്കുക
    global game_still_going
    if "-" not in board:  # if ബോർഡ് നിറഞ്ഞിട്ടുണ്ടെങ്കിൽ
        game_still_going = False
        return True
    else:  # else ടൈ ഇല്ല
        return False


def flip_player():  # നിലവിലെ പ്ലെയറിനെ X ൽ നിന്ന് O ലേക്ക് അല്ലെങ്കിൽ O ലേക്ക് X ലേക്ക് മാറ്റുക
    global current_player
    if current_player == "X":  # current player == X ആണെങ്കിൽ, അത് O ആക്കുക
        current_player = "O"
    elif current_player == "O":  # current player == O ആണെങ്കിൽ, അത് X ആക്കുക
        current_player = "X"


# ------------ execution തുടങ്ങുന്നു -------------
play_game()  # XOX ഗെയിം കളി തുടങ്ങുന്നു
