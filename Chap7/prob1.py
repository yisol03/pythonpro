import random

inputDict= {
    1 : " ", 2 : " ", 3 : " ",
    4 : " ", 5 : " ", 6 : " ",
    7 : " ", 8 : " ", 9 : " ",
}

def instructions():
		print("\n\tWelcome to the world's greatest game!")
		print("\tThis will be a showdown between your human brain and my silicon processor.")
		print("\n\n\tYou will make your move known by entering a number, 0 - 8.")
		print("\tThe number will correspond to the board position as illustrated:")
		print("\n\t\t\t\t\t0 | 1 | 2")
		print("\t\t\t\t\t---------")
		print("\t\t\t\t\t3 | 4 | 5")
		print("\t\t\t\t\t---------")
		print("\t\t\t\t\t6 | 7 | 8")
		print("\n\tPrepare yourself, human. The ultimate battle is about to begin.")

def checkDuplicate(position):
    duplicateCheck = False
    if inputDict[position+1] != " ":
        duplicateCheck = True

    return duplicateCheck

def setData(position,value):
    inputDict[position] = value


def printBoard():
    print("{} | {} | {}".format(inputDict[1],inputDict[2],inputDict[3]))
    print("----------")
    print("{} | {} | {}".format(inputDict[4],inputDict[5],inputDict[6]))
    print("----------")
    print("{} | {} | {}".format(inputDict[7],inputDict[8],inputDict[9]))


def confirmVictory(turn):
    if inputDict[1] == turn and inputDict[2]  == turn and inputDict[3] == turn:
        return True
    elif inputDict[1] == turn and inputDict[4]  == turn and inputDict[7] == turn:
        return True
    elif inputDict[1] == turn and inputDict[5]  == turn and inputDict[9] == turn:
        return True
    elif inputDict[4] == turn and inputDict[5]  == turn and inputDict[6] == turn:
        return True
    elif inputDict[7] == turn and inputDict[8]  == turn and inputDict[9] == turn:
        return True
    elif inputDict[2] == turn and inputDict[5]  == turn and inputDict[8] == turn:
        return True
    elif inputDict[7] == turn and inputDict[5]  == turn and inputDict[3] == turn:
        return True
    elif inputDict[3] == turn and inputDict[6]  == turn and inputDict[9] == turn:
        return True
    else:
        return False
        
def isValid(value):
    isValid = True
    if not value.isnumeric():
        print("It's not a number. Please enter it again.")
        isValid = False
    elif -1 > int(value) and int(value) >= 9 :
        print("It is not a number in the range of 0 to 8. Please enter it again.")
        isValid = False
    elif checkDuplicate(int(value)) == True:
        print("Duplicate location. Please enter another number.") 
        isValid = False
    
    return isValid


turn = "O"
count = 0

instructions()
ans = input("Do you require the first move? (y / n): ")
if ans == 'y':
    print("I shall take square number 4")
    setData(5, 'X')
    printBoard()
    
    while count < 10:
        if turn == "O":
            positionO = input("Where will you move? <0 - 8>: ")
            valueO = "O"
            
            if isValid(positionO) == False:
                continue
            
            setData(int(positionO)+1, valueO)
            printBoard()
            count += 1
            isVictory = confirmVictory(turn)
            
            if isVictory == True:
                break
            else:
                turn = "X"
                
        elif turn == "X":
            if count == 2:
                 if inputDict[1] == ' ':
                      if isValid('0') == False:
                           continue
                      setData(1, 'X')
                      print("I shall take square number 0")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[7] == ' ':
                      if isValid('6') == False:
                           continue
                      setData(7, 'X')
                      print("I shall take square number 6")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[3] == ' ':
                      if isValid('2') == False:
                           continue
                      setData(3, 'X')
                      print("I shall take square number 2")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[9] == ' ':
                      if isValid('8') == False:
                           continue
                      setData(9, 'X')
                      print("I shall take square number 8")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                           
            elif count == 4:
                 if inputDict[1] == 'X' and inputDict[9] == " ":
                      if isValid('0') == False:
                           continue
                      setData(9, 'X')
                      print("I shall take square number 8")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[7] == ' ':
                      if isValid('6') == False:
                           continue
                      setData(7, 'X')
                      print("I shall take square number 6")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[3] == ' ':
                      if isValid('2') == False:
                           continue
                      setData(3, 'X')
                      print("I shall take square number 2")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[9] == ' ':
                      if isValid('8') == False:
                           continue
                      setData(9, 'X')
                      print("I shall take square number 8")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
            elif count == 6:
                 if (inputDict[1] == 'X' and inputDict[3] == 'X'):
                      if isValid('1') == False:
                           continue
                      setData(2, 'X')
                      print("I shall take square number 1")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[1] == 'X' and inputDict[7] == 'X'):
                      if isValid('3') == False:
                           continue
                      setData(4, 'X')
                      print("I shall take square number 3")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[7] == 'X' and inputDict[9] == 'X'):
                      if isValid('7') == False:
                           continue
                      setData(8, 'X')
                      print("I shall take square number 7")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[3] == 'X' and inputDict[9] == 'X'):
                      if isValid('5') == False:
                           continue
                      setData(6, 'X')
                      print("I shall take square number 5")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[1] == 'X' and inputDict[9] == " ":
                      if isValid('8') == False:
                           continue
                      setData(9, 'X')
                      print("I shall take square number 8")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[3] == 'X' and inputDict[7] == " ":
                      if isValid('6') == False:
                           continue
                      setData(7, 'X')
                      print("I shall take square number 6")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[7] == 'X' and inputDict[3] == " ":
                      if isValid('2') == False:
                           continue
                      setData(3, 'X')
                      print("I shall take square number 2")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif inputDict[9] == 'X' and inputDict[1] == " ":
                      if isValid('0') == False:
                           continue
                      setData(1, 'X')
                      print("I shall take square number 0")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[1] == 'O' and inputDict[3] == 'O'):
                      if isValid('1') == False:
                           continue
                      setData(2, 'X')
                      print("I shall take square number 1")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[1] == 'O' and inputDict[7] == 'O'):
                      if isValid('3') == False:
                           continue
                      setData(4, 'X')
                      print("I shall take square number 3")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[7] == 'O' and inputDict[9] == 'O'):
                      if isValid('7') == False:
                           continue
                      setData(8, 'X')
                      print("I shall take square number 7")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
                 elif (inputDict[3] == 'X' and inputDict[9] == 'X'):
                      if isValid('5') == False:
                           continue
                      setData(6, 'X')
                      print("I shall take square number 5")
                      isVictory = confirmVictory(turn)
                      if isVictory == True:
                           break
                      else:
                           turn = "O"
            elif count == 8:
                 for i in range(1, 10):
                      if inputDict[i] == " ":
                           if isValid(str(i-1)) == False:
                                continue
                           setData(i, 'X')
                           print("I shall take square number", i)
                           isVictory = confirmVictory(turn)
                 break
            
            printBoard()
            count += 1
            
    if count == 9:
        printBoard()
        print("Draw!")
    else:
        printBoard()
        print(turn ,"won!")
else:
    press = input("Press the enter key to quit.")
    if press == '':
        print("")
