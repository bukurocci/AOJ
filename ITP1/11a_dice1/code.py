class Dice:
  def __init__(self, sides):
    self.__sides = sides

  def roll(self, opDir):
    old = self.__sides

    if(opDir == 'N'):
      self.__sides = [old[1], old[5], old[2], old[3], old[0], old[4]]
    elif(opDir == 'S'):
      self.__sides = [old[4], old[0], old[2], old[3], old[5], old[1]]
    elif(opDir == 'E'):
      self.__sides = [old[3], old[1], old[0], old[5], old[4], old[2]]
    elif(opDir == 'W'):
      self.__sides = [old[2], old[1], old[5], old[0], old[4], old[3]]

  def getTop(self):
    return self.__sides[0]

  def getRight(self):
    return self.__sides[2]

sides = list(map(int, input().split()))
ops = input()

dice = Dice(sides)

for op in ops:
  dice.roll(op)

print(dice.getTop())