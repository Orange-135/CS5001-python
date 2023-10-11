class Person:
   """
   A class representing a person
   """
   def __init__(self, name, age):
      """
      Constuct a Person object
      """
      self.name = name
      self.age = age
      self.friends = []

   def introduce_self(self):
      """
      Prints out a self introduction
      """
      print(f"Hi, I am {self.name} and I am {self.age} years old.")
      if (len(self.friends) > 0):
         self.introduce_friends()
      else:
         print("I prefer to work alone.")

   def befriend(self, new_friend):
      """
      Add friend to friends list
      """
      print(f"{self.name} befriends {new_friend.name}")
      new_friend.befriend(self)
      self.friends.append(new_friend)

   def introduce_friends(self):
      """
      Prints out friends
      """
      print("My friends are:")
      for friend in self.friends:
         print(f"\t{friend.name}")