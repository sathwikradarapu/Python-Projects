import tkinter as tk
from tkinter import messagebox

class TicTacToe:
  def __init__(self):
    self.current_player="X"
    self.board=[["","",""],["","",""],["","",""]]
    self.window=tk.Tk()
    self.window.title("Tic Tac Toe")

    self.buttonsGrid=[]
    for i in range(3):
      row=[]
      for j in range(3):
        button=tk.Button(self.window,text="",height=15,width=30,command=lambda i=i,j=j:self.make_move(i,j))
        button.grid(row=i,column=j)
        row.append(button)
      self.buttonsGrid.append(row)
    
  def run(self):
    self.window.mainloop()
  
  def make_move(self,row,col):
    if self.board[row][col]=="":
      self.board[row][col]=self.current_player
      self.buttonsGrid[row][col].config(text=self.current_player)
      if self.check_winner(self.current_player):
        messagebox.showinfo("GAME OVER","WINNER IS "+str(self.current_player))
        self.window.quit()
      elif self.is_draw():
        messagebox.showinfo("GAME OVER","IT'S A DRAW")
        self.window.quit()
      if self.current_player=='X':
        self.current_player="O"
      else:
        self.current_player="X"
  
  def check_winner(self,player):
    for i in range(3):
      if player==(self.board[i][0])==(self.board[i][1])==(self.board[i][2]):
        return True
      if player==(self.board[0][i])==(self.board[1][i])==(self.board[2][i]):
        return True
    if player==(self.board[0][0])==(self.board[1][1])==(self.board[2][2]):
      return True
    if player==(self.board[0][2])==(self.board[1][1])==(self.board[2][0]):
      return True
    return False
  
  def is_draw(self):
    for row in self.board:
      if "" in row:
        return False
    return True

game=TicTacToe()
game.run()