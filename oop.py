SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

def create_deck():
    cards = []
    for suit in SUITS:
        for ranks in RANKS:
            cards.append(suit,ranks)
    return cards

def main():
    test = create_deck()

    print(test)




if __name__ == "__main__":
    main()