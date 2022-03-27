# Input handling
with open('input.txt') as fin:
  numbers, *boards = fin.read().split('\n\n')
  numbers = [int(i) for i in numbers.strip().split(',')]
  allBoards = [[[int(col) for col in row.split()]for row in board.split('\n')] for board in boards]


# Place an 'x' if a number in the board is called
def mark_spot(number, board):
  for row in board:
    for i in range(0, len(row)):
      if row[i] == number:
        row[i] = 'x'


# Check if winner has been found
def check_for_winner(board):
  winner = False

  # Check for row winner
  for row in board:
      winner = all(elem in ['x'] for elem in row)
      
      if winner:
          return winner
  
  # Check for column winner
  for i in range(0, 5):
      winner = all(elem in ['x'] for elem in [row[i] for row in board])

      if winner:
          return winner

  # Return false if no winner found
  return winner


# Sum the rest of the board spots
def sum_board(board):
  sum = 0
  for row in board:
    for num in row:
      if num != 'x':
        sum += num

  return sum


# Part 1
def part1():
  boards = allBoards
  for number in numbers:
    for board in boards:
      mark_spot(number, board)

      if check_for_winner(board):
        return sum_board(board) * number
              
        

# Part 2:
def part2():
  boards = allBoards
  allNums = numbers
  
  winnerFound = False
  while not winnerFound:
    number = allNums[0]
    allNums = allNums[1:]

    for board in boards:
      mark_spot(number, board)

    index = 0
    while index < len(boards):
      if check_for_winner(boards[index]):
        if len(boards) > 1:
          boards.pop(index)
        else:
          winnerFound = True
          return sum_board(boards[index]) * number
      else:
        index += 1
    




print("Answer to part 1: ", part1())
print("Answer to part 2: ", part2())
