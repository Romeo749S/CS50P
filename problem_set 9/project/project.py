import random
import time


class Jack:
    def __init__(self):
        self._sum_cards = 0
        self._cards = []
        self._current_card = 0
        self._stack = [
            "[2]",
            "[2]",
            "[3]",
            "[3]",
            "[4]",
            "[4]",
            "[5]",
            "[5]",
            "[6]",
            "[6]",
            "[7]",
            "[7]",
            "[8]",
            "[8]",
            "[9]",
            "[9]",
            "[10]",
            "[10]",
            "[J]",
            "[J]",
            "[Q]",
            "[Q]",
            "[K]",
            "[K]",
            "[A]",
            "[A]",
        ]
        self._dict = {
            "[1]": 1,
            "[2]": 2,
            "[3]": 3,
            "[4]": 4,
            "[5]": 5,
            "[6]": 6,
            "[7]": 7,
            "[8]": 8,
            "[9]": 9,
            "[10]": 10,
            "[J]": 10,
            "[Q]": 10,
            "[K]": 10,
            "[A]": 11,
        }

        random.shuffle(self._stack)

    @property
    def sum_cards(self):
        return self._sum_cards

    @property
    def cards(self):
        return self._cards

    @property
    def current_cards(self):
        return self._current_card

    @sum_cards.setter
    def sum_cards(self, card):
        self._sum_cards = card

    def process(self):
        self._current_card = self._stack[-1]
        self._stack.pop()
        return self._current_card

    def waiting(self):
        for _ in range(3):
            print(".")
            time.sleep(1)
        print("done ✅")
        time.sleep(0.5)


# initilizing player and dealer
player = Jack()
dealer = Jack()


def main():
    print("Dealer shuffles cards and takes 2 of them")
    dealer.waiting()
    print("Dealers first card: {}".format(start(dealer)[0]))
    time.sleep(1)
    print("{},{} are your cards\n({}) is your starting points".format(*start(player)))
    time.sleep(1)
    for _ in range(15):
        current_card = dealer.process()
        game = player_ends(current_card)
        time.sleep(1)
        if game == 0:
            dealer_ends()
            print(*dealer.cards, "Are dealers cards")
            print(f"Dealer's total points: ({dealer.sum_cards})")
            if dealer.sum_cards > 21:
                print(f"Dealer's got more that 21\nYou are the WINNER! ")
                break
            elif dealer.sum_cards > player.sum_cards:
                print("You've lost!")
            elif dealer.sum_cards < player.sum_cards:
                print("You are the WINNER!")
            else:
                print("It's a draw!")
            break
        elif game == 1:
            print("You got more than 21 points. You've lost!")
            break
        else:
            print(f"Total points: ({game})")
        time.sleep(1)


def start(n):
    """
    This function starts a game by giving the dealer or the player firt two cards
    and the total points.

    Returns :
    str: First and second random card.
    int: Total points.

    """
    n._cards.append(dealer.process())
    n._cards.append(dealer.process())
    n.sum_cards = card_sum(n.cards, n)
    return n.cards[0], n.cards[1], n.sum_cards


def player_ends(current_card):
    while True:
        print("Do you want to take the next card?(y/n) ", end="")
        vote = input().lower()
        if vote == "y" or vote == "n":
            break
    if vote == "y":
        print(f"{current_card} is you card ")
        player._cards.append(current_card)
        player.sum_cards = card_sum(player.cards, player)
        if player.sum_cards > 21:
            return 1
        return player.sum_cards
    elif vote == "n":
        return 0


def dealer_ends():
    while True:
        current_card = dealer.process()
        if (dealer.sum_cards) < 16:
            dealer.cards.append(current_card)
            print("Dealer picks up a card ")
            time.sleep(1)
            dealer.sum_cards = card_sum(dealer.cards, dealer)
        else:
            return dealer.sum_cards


def card_sum(list1, n):
    sum1 = sum([player._dict[j] for j in list1])
    while True:
        if sum1 > 21 and "[A]" in list1:
            sum1 -= 10
            n.cards.remove(n.cards[n.cards.index("[A]")])
            n.cards.append("[1]")
        else:
            while "[1]" in n.cards:
                n.cards.remove(n.cards[n.cards.index("[1]")])
                n.cards.append("[A]")
            break
    return sum1


if __name__ == "__main__":
    main()
