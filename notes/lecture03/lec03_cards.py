suit = input("Input a card suit: ").lower()
value = input("Input a card value: ").lower()

if (suit == "dimond" or suit == "heart"):
    color = "red"
else:
    color = "black"

if(value =="king" or value == "queen" or value == "jack"):
    is_face_card = True
else:
    is_face_card = False

if (color == "red"):
    if is_face_card:
        print("You choose a red face card")
    else:
        print("Your choose a rede pip card")
else:
    if is_face_card:
        print("Your choose a black card")
    else:
        print("Your choose a black pip card")

