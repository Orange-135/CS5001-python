class Card:
     """
     A playing card
     """

     def _init_(self, suit, value):
          """
          Construct a card
          """
          self.suit = suit
          self.value = value
     
     def num_value(self):
          """
          Return the card's numerical value
          """
          ACE_VALUE = 11
          FACE_CARD_VALUE = 10 
          if self.value == 'ace':
               return ACE_VALUE
          elif (self.vaule == 'jack' or
                self.value == 'queen' or
                self.value == 'king'):
               return FACE_CARD_VALUE
          else:
               return int(self.value)