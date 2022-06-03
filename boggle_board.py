from random import randrange, sample

class BoggleBoard:
  grid = []

  def __init__(self):
    self.board = f"""
    ____
    ____
    ____
    ____

    """
  
  def shake(self) -> str:
    alphabet = ('AAEEGN', 'ELRTTY', 'AOOTTW', 'ABBJOO', 'EHRTVW', 'CIMOTU', 'DISTTY', 'EIOSST', 'DELRVY', 'ACHOPS', 'HIMNQU', 'EEINSU', 'EEGHNW', 'AFFKPS', 'HLNNRZ', 'DEILRX')
    rolls = []

    for i in range(16):
      rolls.append(randrange(1,6))
    
    for i in range(0, len(rolls)):
      for j in range(0, len(alphabet)):
        if i == j:
          if(alphabet[j][rolls[i]] == 'Q'):
            BoggleBoard.grid.append('Qu')
          else:
            BoggleBoard.grid.append(alphabet[j][rolls[i]]+' ')

    BoggleBoard.grid = sample(BoggleBoard.grid, len(BoggleBoard.grid))
    
    self.board = f"""
    {BoggleBoard.grid[0]} {BoggleBoard.grid[1]} {BoggleBoard.grid[2]} {BoggleBoard.grid[3]}
    {BoggleBoard.grid[4]} {BoggleBoard.grid[5]} {BoggleBoard.grid[6]} {BoggleBoard.grid[7]}
    {BoggleBoard.grid[8]} {BoggleBoard.grid[9]} {BoggleBoard.grid[10]} {BoggleBoard.grid[11]}
    {BoggleBoard.grid[12]} {BoggleBoard.grid[13]} {BoggleBoard.grid[14]} {BoggleBoard.grid[15]}
    """

    return self.board

  # def include_word(self, word) -> str:
  #   for i in word:
  #     for j in range(len(BoggleBoard.grid)):
  #       if(i == BoggleBoard.grid[j]):
  #         BoggleBoard.search(j, i)

  # @staticmethod
  # def search(index, char):
  #     BoggleBoard.up(index, char)

  # @staticmethod
  # def up(index, char):
  #   if(index > 3):
  #     if(BoggleBoard.grid[index-4] == char):
  #       BoggleBoard.search(index-4, BoggleBoard.grid[index-4])
  #     else:
  #       BoggleBoard.down(index, char)
  #   else:
  #     return BoggleBoard.down(index, char)
  
  # @staticmethod
  # def down(index, char):
  #   if(index < 12):
  #     if(BoggleBoard.grid[index+4] == char):
  #       BoggleBoard.search(index+4, BoggleBoard.grid[index+4])
  #     else:
  #       BoggleBoard.forward(index, char)
  #   else:
  #     return BoggleBoard.forward(index, char)

  # @staticmethod
  # def forward(index, char):
  #   if(index != 3 and index != 7 and index != 11 and index != 15):
  #     if(BoggleBoard.grid[index+1] == char):
  #       BoggleBoard.search(index+1, BoggleBoard.grid[index+1])
  #     else:
  #       BoggleBoard.backward(index, char)
  #   else:
  #     return BoggleBoard.backward(index, char)

  # @staticmethod
  # def backward(index, char):
  #   if(index%4 != 0):
  #     if(BoggleBoard.grid[index-1] == char):
  #       BoggleBoard.search(index-1, BoggleBoard.grid[index-1])
  #   else:
  #     return False

boggle = BoggleBoard()
print(boggle.shake())
# print(boggle.board)


# Movement logic
# up = (4,5,6,7,8,9,10,11,12,13,14,15) == index > 3 -> -4
# down = (0,1,2,3,4,5,6,7,8,9,10,11) == index < 12 -> +4
# forward = (0,1,2,4,5,6,8,9,10,12,13,14) == index != 3 or 7 or 11 or 15 -> +1
# back = (1,2,3,5,6,7,9,10,11,13,14,15) == index%4 != 0 -> -1

# Steps:
# 1) search grid for the first letter of the word
# 2) if that letter does not exist in the grid, return false
# 3) if that letter does exist in the grid, save its index, then search up, down, left, and right for the second letter in the word
# 4) if the second letter isn't found, search the rest of the grid for the first letter
# 5) if the first letter isn't in the rest of the grid, return false
# 6) if the first letter is still in the grid, repeat step 3
# 7) if the second letter is found, update the current index, then search around that index
# 8) repeat these steps until either the word is found, or the word does not exit in the grid