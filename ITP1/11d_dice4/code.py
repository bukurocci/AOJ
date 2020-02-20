n = int(input())
dices = []

class Dice:
  def __init__(self, faces):
    self.faces = faces

  def roll(self, ops):
    faces = self.faces

    for opDir in ops:
      if(opDir == 'N'):
        faces = [faces[1], faces[5], faces[2], faces[3], faces[0], faces[4]]
      elif(opDir == 'S'):
        faces = [faces[4], faces[0], faces[2], faces[3], faces[5], faces[1]]
      elif(opDir == 'E'):
        faces = [faces[3], faces[1], faces[0], faces[5], faces[4], faces[2]]
      elif(opDir == 'W'):
        faces = [faces[2], faces[1], faces[5], faces[0], faces[4], faces[3]]

    self.faces = faces

  def matches(self, dice):
    ops_pattern = ["S", "", "WS", "ES", "SS", "N"]
    clone = self.clone()

    ops_index = clone.faces.index(dice.faces[1]) if dice.faces[1] in clone.faces else -1

    if(ops_index == -1):
      return False

    clone.roll(ops_pattern[ops_index])

    if(clone.faces == dice.faces):
      return True
    
    for op in "WWW":
      clone.roll(op)

      if(clone.faces == dice.faces):
        return True

    return False

  def clone(self):
    return Dice(self.faces[:])


result = "Yes"

for i in range(n):
  faces = list(map(int, input().split()))
  dice = Dice(faces)

  if(i != 0):
    for d in dices:
      if dice.matches(d):
        result = "No"
        break

  dices.append(dice)

print(result)