from deck import Deck


def main():
    deck1 = Deck("mini")  # Just a few cards
    deck2 = Deck("mini")
    # deck1 = Deck()
    # deck2 = Deck()

    card1 = deck1.deal_one()
    card2 = deck2.deal_one()

    print(card1)
    print(card2)
    print(repr(card1))
    print(repr(card2))

    if card1 == card2:
        print(card1, "and", card2, "are equal")
    else:
        print(card1, "and", card2, "are not equal")
        if (card1 > card2):
            print(card1, "beats", card2)
        elif (card2 > card1):
            print(card2, "beats", card1)

    print(repr(card1))
    print(card1.__class__.__name__)##Card

    # I'd like to keep counts of identical cards I see
    cards_dict = {}

    if card1 in cards_dict:
        cards_dict[card1] += 1
    else:
        cards_dict[card1] = 1

    if card2 in cards_dict:
        cards_dict[card2] += 1
    else:
        cards_dict[card2] = 1

    print(cards_dict)

    print(hash(card1))
    print(card1.__hash__())##一样

    print(str(card1))
    print(card1.__str__())##一样

    print(repr(card1))
    print(card1.__repr__())##一样

    print(list(cards_dict.keys())[0])


main()
