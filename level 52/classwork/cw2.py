def whose_move(last_player, win):
    if win:
        return last_player
    if last_player == "black":
        return "white"
    else:
        return "black"
        