import random

board = [' ' for _ in range(10)]

player_score = 0
ai_score = 0
draw =0 
def draw_board():
    print('-------------')
    print('|', board[1], '|', board[2], '|', board[3], '|')
    print('-------------')
    print('|', board[4], '|', board[5], '|', board[6], '|')
    print('-------------')
    print('|', board[7], '|', board[8], '|', board[9], '|')
    print('-------------')

def make_move(player, position, playerRef):
    while board[position] != ' ':
      if player == playerRef:
        print("Position is taken, please retype")
        player_move = input("Enter a position for 'X' (1-9): ")
        while player_move.isnumeric() == False and int(player_move) not in range[1:9]:
          print("Invalid input, please retype the input")
          player_move = input("Enter a position for 'X' (1-9): ")
        position = int(player_move)
      else:
        position = ai_move()
    board[position] = player
def available_moves():
    moves = []
    for i in range(len(board)-1):
        if board[i+1] == ' ':
            moves.append(i+1)
    return moves

def check_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

player, ai = 'X', 'O'

def tic(moves):
  return random.choice(moves)

def tac(moves, rand = True):
  for move in moves:
      board_copy = board.copy()
      board_copy[move] = ai
      if check_winner(board_copy, ai):
        return move
  for move in moves:
      board_copy = board.copy()
      board_copy[move] = player
      if check_winner(board_copy, player):
        return move
  if rand:
    return tic(moves)
  else:
    return -1

def toe(moves):
  winCheck = tac(moves,False)
  if winCheck != -1:
    return tac(moves)

  if len(moves) == 9:
    return random.choice([1,3,7,9])
  if 1 in moves and 3 in moves and 7 in moves and 9 in moves:
    return random.choice([1,3,7,9])
  if 5 in moves and len(moves) == 8:
    return 5

  cornerMoves = []
  for move in [1,3,7,9]:
    if move in moves:
      cornerMoves.append(move)
  sideMoves = []
  for move in [2,4,6,8]:
    if move in moves:
      sideMoves.append(move)
  if len(cornerMoves) == 2 and len(moves) != 7:
    return random.choice(sideMoves)
  if len(cornerMoves) > 0:
    return random.choice(cornerMoves)

  return tic(moves)
    
difficulty = 0

def ai_move():
  moves = available_moves()
  if difficulty == 1:
    move = tic(moves)
  elif difficulty == 2:
    move = tac(moves)
  elif difficulty == 3:
    move = toe(moves)
  return move
    
def reset_board():
    global board
    board = [' '] * 10

def set_player():
  if bool(random.getrandbits(1)):
    ai_position = ai_move()  
    make_move('X', ai_position, 'O')
    return 'O','X'
  return 'X','O'

while difficulty == 0:
  diff = input("Enter difficulty level (Options: Easy, Medium, Hard): ")
  if diff.lower() == "easy":
    difficulty = 1
  elif diff.lower() == "medium":
    difficulty = 2
  elif diff.lower() == "hard":
    difficulty = 3
  else:
    print("You must select either Easy, Medium, or Hard difficulty.")
player, ai = set_player()
while True:
    draw_board()
    player_move = int(input("Enter a position for '{}' (1-9): ".format(player)))
    while player_move not in range(1,10):
      print("Invalid input, please retype the input")
      player_move = int(input("Enter a position for '{}' (1-9): ".format(player)))
    make_move(player, player_move, player)
    if check_winner(board, player):
        draw_board()
        print('You win!')
        player_score += 1
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            break
        else:
            reset_board()
            player, ai = set_player()
            continue
    elif len(available_moves()) == 0:
        draw_board()
        print('Tie!')
        draw +=1
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            break
        else:
            reset_board()
            player, ai = set_player()
            continue
    ai_position = ai_move()  
    make_move(ai, ai_position, player)
    if check_winner(board, ai):
        draw_board()
        print('AI wins!')
        ai_score += 1
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            break
        else:
            reset_board()
            player, ai = set_player()
            continue  
    elif len(available_moves()) == 0:
        draw_board()
        print('Tie!')
        draw +=1
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            break
        else:
            reset_board()
            player, ai = set_player()
            continue
print("Player's score is:",player_score)
print("AI's score is:",ai_score)
print("Tie:",draw)

    