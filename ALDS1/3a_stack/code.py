
class Stack:
  def __init__(self, max_size):
    self.list = []
    self.top = -1
    self.max_size = max_size
  
  def is_empty(self):
    return self.top == -1

  def is_full(self):
    return self.top == self.max_size - 1

  def push(self, value):
    if(self.is_full()):
      raise Exception("the stack is full")

    self.list.append(value)
    self.top += 1

  def pop(self):
    if(self.is_empty()):
      raise Exception("the stack is empty")

    value = self.list.pop()
    self.top -= 1

    return value

  def peek(self):
    return self.list[self.top]

expression = input().split()


stack = Stack(100)

for value in expression:
  if(value == "+"):
    b = stack.pop()
    a = stack.pop()

    stack.push(a + b)

  elif(value == "-"):
    b = stack.pop()
    a = stack.pop()

    stack.push(a - b)

  elif(value == "*"):
    b = stack.pop()
    a = stack.pop()

    stack.push(a * b)

  else:
    stack.push(int(value))

print(stack.peek())
