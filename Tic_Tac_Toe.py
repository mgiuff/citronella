
def welcome_input():

  player1 = input("Player 1, what's your name?\n")
  print(f"Hello {player1}!\n")

  player2 = input("Player 2, what's your name?\n" )
  print(f"Hello {player2}!\n")
  
  return (player1, player2)

def draw_table(table):
  
  print("\n")
  print(f" -----------------------" )
  print(f"|       |       |       |")
  print(f"|   {table[0]}   |   {table[1]}   |   {table[2]}   |")
  print(f"|       |       |       |")
  print(f" -----------------------" )
  print(f"|       |       |       |")
  print(f"|   {table[3]}   |   {table[4]}   |   {table[5]}   |")
  print(f"|       |       |       |")
  print(f" -----------------------" )
  print(f"|       |       |       |")
  print(f"|   {table[6]}   |   {table[7]}   |   {table[8]}   |")
  print(f"|       |       |       |")
  print(f" -----------------------" )


def make_a_move(player, positions):

  move = input(f"{player}, it's your turn. Choose one out of the available positions: {positions} \n")
  
  if move in range(1,9) and move in positions:
    return int(move)
  else: 
    make_a_move(player, positions)


#  for x in l:
#    if x not in appoggio:
#      appoggio.append(x)
#  return appoggio

#  print(f" Lowercase Letters: {len([letter for letter in s if letter.isupper()])}")


make_a_move("Marco", [1,3,4])
#players = player_input()
