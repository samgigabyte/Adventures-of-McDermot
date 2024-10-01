def play_game():
    options = ["checkmicrowave", "checkbin", "inventory", "checkcoffeemachine"]
    inventory = ["mop"]
    puzzles = 0
    print("You are Carl McDermot, a janitor, but not just any janitor. You take your job very seriously. Cleaning is not just a task for you—it’s a mission  \nYou believe that cleanliness is the foundation of order, and order is the foundation of civilization. Without people like you, everything would descend into chaos. The fate of the workplace, nay, the world, depends on you. GOOO!! ")
    print("You enter the breakroom. The coffee machine gurgles ominously, spilling drops of liquid onto the counter, creating a sticky moat around itself. \nCrumbs from donuts and sandwiches litter the floor. A peculiar smell wafts from the microwave, and as you approach it, you realize:\nsomeone has left their lunch to fester for days.But there’s something more. An urgent note on the fridge door catches your eye. It reads:Carl, somethings not right. The mess... its spreading. Beware of the trash bin in the corner. \nClean it if you dare.The note is unsigned.")
    while True and puzzles == 0:
            print("You can do the following options", options)
            move = input("Enter your move: ")
            if move == "checkmicrowave" and "checkmicrowave" in options:
                print("You slowly creak the microwave door opens, a  steaming curry with round chicken balls and strange rice is in a papertray, still warm from the earlier heating by a student")
                while True:
                      takeitcurry = input("Take it? Y/N: ")
                      if takeitcurry == "Y":
                          print("You take the toxic curry and hold it in your palm, as far away from your nose as possible")
                          inventory.append("curry")
                          options.remove("checkmicrowave")
                          break
                      elif takeitcurry == "N":
                          print("You back away from the pungent microwave")
                          break
                      else:
                          print("Not a valid input")
            if move == ("inventory"):
                print("Your inventory has:", inventory)
            if move == "checkcoffeemachine" and "checkcoffeemachine" in options:
                print("The sticky machine is dripping a deep brown liquid")
                while True:
                    brewcuppa = input("Brew a coffee? Y/N: ")
                    if brewcuppa == "Y":
                        print("You press a button and a piping hot paper cup of molten coffee flows out.")
                        inventory.append("coffee")
                        options.remove("checkcoffeemachine")
                        break
                    elif brewcuppa == "N":
                        print("You unstick your shoes from the coffee mess on the floor and move away from the machine")
                        break
                    else:
                        print("Not a valid move")
            if move == "checkbin" and "checkbin" in options:
                print("A blonde haired woman pushes the lid of the bin open, she shouts \"He's some cheek opening my bin dunty!\n Go way dis is my bin ked\" ")
                print("You are taken aback by this woman guarding the bin, you wield your mop like a sword")
                while True:
                    attackdunty = input("Approach the woman? Y/N:")
                    
                    if attackdunty == "Y" and "curry" in inventory and "coffee" in inventory:
                        print("You sprint towards the bin, holding your collection of hot food, you dump the mixture of molten coffee and pungent curry into the bin \n You hear a screech followed quickly by \"You rat!\". You quickly dispose of the bin by tossing it through a nearby open window")
                        print("You walk out of the room delighted you resolved the situation ready to tackle the next challenge")
                        puzzles = 1
                        break
                    elif attackdunty == "Y":
                        print("You sprint at the bin and the woman delivers a strong right jab, she exclaims \"BOXING\" and you retreat")
                        print("Maybe you should search the rest of the room for some items")
                        break
                    elif attackdunty == "N":
                        ("You step away from the lady")
                        break
                    else:
                        print("Not a valid input")
                    
                
                    
play_game()