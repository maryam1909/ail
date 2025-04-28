# Minimax function for perfect computer play
def minimax(stones, is_computer_turn):
    if stones == 0:
        # If no stones left, the player who made the last move wins
        return 1 if not is_computer_turn else -1

    if is_computer_turn:
        best_score = float('-inf')  # Initialize with negative infinity
        for move in range(1, 4):  # Allowed moves: 1, 2, or 3 stones
            if stones - move >= 0:
                score = minimax(stones - move, False)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')  # Initialize with positive infinity
        for move in range(1, 4):
            if stones - move >= 0:
                score = minimax(stones - move, True)
                best_score = min(best_score, score)
        return best_score

def best_move(stones):
    best_score = float('-inf')
    move_choice = 1
    for move in range(1, 4):
        if stones - move >= 0:
            score = minimax(stones - move, False)
            if score > best_score:
                best_score = score
                move_choice = move
    return move_choice

def play_nim_game():
    stones = 10  # starting number of stones
    print("Welcome to Nim Game!")
    print("There are 10 stones. You can remove 1, 2, or 3 stones on your turn.")

    while stones > 0:
        print(f"\nStones remaining: {stones}")
        player_move = int(input("Your move (1, 2, or 3): "))
        if player_move not in [1, 2, 3] or player_move > stones:
            print("Invalid move. Try again.")
            continue
        stones -= player_move

        if stones == 0:
            print("You win!")
            break

        print(f"Stones remaining: {stones}")
        comp_move = best_move(stones)
        print(f"Computer removes {comp_move} stone(s).")
        stones -= comp_move

        if stones == 0:
            print("Computer wins!")
            break

play_nim_game()
