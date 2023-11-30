print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

tree_or_rock = input("You see a tree and a rock. Which one do you walk up to. Write rock for rock and tree for tree \n ")

if tree_or_rock == 'rock':
  voice= input("You walk up to the rock and hear a voice behind the rock. Do you go up to it or run. Write voice for voice and run for run \n") 
  if voice == 'voice': 
    print("Yesterday, All my troubles seemed so far away. Now it looks as though they're here to stay. Oh, I believe in yesterday. You've been bamboozled! Sit down and listen to him play his little guitar. GAME OVER!")
  elif voice == 'tree': 
     mining = input("You ran away from the voice. You run as fast as you can. The voice is getting closer. You reach a patch of dirt. Next to it is some mining equipment. Do you mine or not. Write mine for mine and no for no.\n")
    
  if mining == 'mine': 
      print('In the patch of dirt is a treasure chest. You open it up, Daniel appears. Youve won a free webinar to why investing and coding is the way the world turns. Congratulations! GAME OVER!')
  elif mining == 'no': 
    print('Music man catches you. Sit, and listen to john lennon stories that no knows about. You lose, GAME OVER!')
  
elif tree_or_rock == 'tree':
  tree = input("You walk up to the tree. Do you climb it or walk around it. Write climb for climb and walk for walk \n")
  if tree == 'climb':
      cave = input("You climb the tree. Boring. You get down. You walk for a while. You see a cave. Do you walk in? Write yes for yes or no for no \n")
      if cave == 'yes':
        print("you find the treasure chest, open it. I am in it. Daniel. yes me. Congratulations. You win!")
  elif cave == 'no':
      print("You head back to the tree. The tree falls and kills you. Game over!")
  elif tree == 'walk':
      print("Why? Youre looking for a treasure. Could be at the top of the tree. Matter a fact, it is. Well done! GAME OVER!")



