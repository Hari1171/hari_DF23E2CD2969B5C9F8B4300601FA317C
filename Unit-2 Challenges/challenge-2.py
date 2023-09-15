#creating a player class
class player:
    def play(self):
        print("The player is playing cricket.")
#creating a batsman class
class batsman(player):
    def play(self):
        print("The batsman is batting.")
#creating a bowler class
class bowler(player):
    def play(self):
        print("The bowler is bowling>")

 #creating object for batsman & bowler class
        
Bman = batsman()
Bowler = bowler()

#method calling
Bman.play()
Bowler.play()