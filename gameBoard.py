import pandas as pd

class GameBoard:
    
    def __init__(self, size):

      #Game size is size x size. size > 2. 
      self.size = size 
      
      #Use dataFrame to simulate the game board. Initialize all elements as 'null' 
      self.boardElements = pd.DataFrame(index=range(self.size),columns=range(self.size))
      self.boardElements.fillna('null')
  
    def save(self):
      self.boardElements.tostring()

    def reset(self):
    
    



