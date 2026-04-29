#1

class StackList:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return len(self.stack) == 0
  
  def push(self, url):
    self.stack.append(url)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
        return "Stack is empty"
    return self.stack[-1]

  def size(self):
    return len(self.stack)

s = StackList()

s.push("google")
s.push("youtube")
s.push("github")

print("Stack:", s.stack)
print("Pop:", s.pop())
print("Setelah pop:", s.stack)
print("Peek:", s.peek())
print("Is Empty:", s.isEmpty())
print("Size:", s.size())

#2

class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.count = 0

  def isEmpty(self):
    return self.top is None

  def push(self, url):
    new_node = Node(url)
    new_node.next = self.top
    self.top = new_node
    self.count += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.top
    self.top = self.top.next
    self.count -= 1
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.top.url

  def size(self):
    return self.count

  def printStack(self):
    current = self.top
    while current:
      print(current.url, end=" -> ")
      current = current.next
    print("None")
s = Stack()

s.push("google")
s.push("youtube")
s.push("github")

print("Pop:", s.pop())
print("Peek:", s.peek())
print("Is Empty:", s.isEmpty())
print("Size:", s.size())