import random

print("Welcome to the world of Rock Paper and Scissors!!!! :)")
print("****************************************************")

###required variables
compScore=0
playerScore=0
tieScore=0
possibleHands=["Rock","Paper","Scissors"]

def WhoIsTheWinner(playerHand,ComputerHand):
    if(playerHand=="Rock" and ComputerHand=="Paper"):
        print("Player/User lose.Try again ")
        return "cpu"
    elif(playerHand=="Rock" and ComputerHand=="Scissor"):
        print("Player/User Wins.Yaayyy")
        return "Player"
    elif(playerHand=="Paper" and ComputerHand=="Rock"):
        print("Player/User Wins.Yaayyy")
        return "Player"
    elif(playerHand=="Paper" and ComputerHand=="Scissors"):
        print("Player/User lose.Try again ")
        return "cpu"
    elif(playerHand=="Scissors" and ComputerHand=="Rock"):
        print("Player/User lose.Try again ")
        return "cpu"
    elif(playerHand=="Scissors" and ComputerHand=="Paper"):
        print("Player/User Wins.Yaayyy")
        return "Player"
    else:
        print("Thats a tie !")
        return "Tie"
    
while(playerScore != 3 and compScore != 3):
  ### Validate input
  while True:
    playerHand = input("\nPick a hand. Rock, Paper, or Scissors: ")
    if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
      break
    else:
      print("Invalid input. Try again.")
  
  ### Generate computer pick
  computerHand = random.choice(possibleHands)

  ### Print results
  print("Your hand: ", playerHand)
  print("Cpu hand: ", computerHand)
  result =  WhoIsTheWinner(playerHand, computerHand)
  if(result == "Player"):
    playerScore += 1
  elif(result == "Cpu"):
    compScore += 1
  else:
    tieScore += 1
  print("Your score: ", playerScore, "CPU: ", compScore, "Ties: ", tieScore)

print("Game over! Thank you for playing :)")
        

