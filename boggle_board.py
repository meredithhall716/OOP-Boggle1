import random

class BoggleBoard:
  
  def __init__(self, word1=None, word2=None, word3=None, word4=None):
    self.word1 = word1
    self.word2 = word2
    self.word3 = word3
    self.word4 = word4

    if (self.word1 == None):
      print("____")
      print("____")
      print("____")
      print("____")

  def shake(self):
    
    dice = {
      1:['R ', 'I ', 'F ', 'O ', 'B ', 'X '],
      2:['I ', 'F ', 'E ', 'H ', 'E ', 'Y '],
      3:['D ', 'E ', 'N ', 'O ', 'W ', 'S '],
      4:['U ', 'T ', 'O ', 'K ', 'N ', 'D '],
      5:['H ', 'M ', 'S ', 'R ', 'A ', 'O '],
      6:['L ', 'U ', 'P ', 'E ', 'T ', 'S '],
      7:['A ', 'C ', 'I ', 'T ', 'O ', 'A '],
      8:['Y ', 'L ', 'G ', 'K ', 'U ', 'E '],
      9:['Qu', 'B ', 'M ', 'J ', 'O ', 'A '],
      10:['E ', 'H ', 'I ', 'S ', 'P ', 'N '],
      11:['V ', 'E ', 'T ', 'I ', 'G ', 'N '],
      12:['B ', 'A ', 'L ', 'I ', 'Y ', 'T '],
      13:['E ', 'Z ', 'A ', 'V ', 'N ', 'D '],
      14:['R ', 'A ', 'L ', 'E ', 'S ', 'C '],
      15:['U ', 'W ', 'I ', 'L ', 'R ', 'G '],
      16:['P ', 'A ', 'C ', 'E ', 'M ', 'D ']
    }
    
    choose_from = []
    counter = 0
    for i in dice:
      choose_from.append(dice[i][random.randint(0,5)])
      if counter < 3:
        print(choose_from[-1], end = " ")
        counter += 1
      
      else:  
        print(choose_from[-1])
        counter=0
    

game = BoggleBoard()

game.shake()




