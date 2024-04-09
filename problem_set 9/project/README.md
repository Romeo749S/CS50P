# Black Jack 
    #### Video Demo:  <https://youtu.be/Alkt-qQXT2o
    #### Description:
    I've implemented BlackJac game in python.

    Rules :

    In this game you have to take cards and try to get as many 
    points as you can, but you shouln't get more than 21 ,
    because if you do -- you are going to loose.
    Dealer does the same thing. Wins the one that has more 
    points than another.

    How to play :

    1. Wait until dealer shuffles the cards and takes 2 of them,
    you are going to see only the first card.
    2. You are going to recieve 2 cards as well, and you can see 
    their label and your total points.
    3. After that you are going to be asked if you want to take
    the next card . Try not to get more than 21 , because you
    are going to loose.
    4. After you are done taking cards dealer are going to do
    the same thing. 
    5. The results. You are going to see wether you won or not
    and why.

    The code :

    - First of all I initiliaze player and dealer
    player = Jack()
    dealer = Jack() 

    - Class Jack() initiliazes the cards that are being played
    with, cards than were picked and total points. It controls
    the whole process of the game.

    ---I've implemented 4 functions :

    - start(n): returns first 2 cards which get saved to 
    n._cards and total points of "n" which get saved to 
    n.sum_cards

    - player_ends(current_card): prompts player if he wants to
    take a card and if the answer is positive - the card is
    gonna be saved to player._cards and total points to
    player.sum_cards

    - dealer_ends(): The function begins with an infinite loop. 
    It will break out of this loop only when the dealer's total 
    points exceed 16.
        Within the loop, the dealer continuously draws cards 
    from the deck until their total points exceed 16. 
    This is a common rule in Blackjack: the dealer must keep 
    drawing cards until they have a total of 17 or more.
        The function returns the total points of the dealer's 
    hand after the drawing process is complete
    
    
    card_sum(list1, n): list1: This parameter represents the 
    list of cards in the player's or dealer's hand.
        This parameter represents the player or dealer object 
    for which the calculation is being performed.
    sum1 is initialized to calculate the total sum of the card 
    values in the hand.
        If the sum of the cards is over 21 (indicating a potential 
    bust), and an Ace ([A]) is present in thehand, the function 
    checks for the presence of Ace.
        If an Ace is found and removing its value of 11 would bring 
    the total below or equal to 21, it subtracts 10 from the total sum, 
    effectively converting the Ace value from 11 to 1.
        If there's no Ace in the hand or adjusting the Ace value doesn't 
    help prevent a bust, it proceeds to the next step.
        If there's any [1] (which represents a converted Ace value) 
    in the hand, it replaces it with [A].
    This step ensures consistency in the representation of Ace values 
    in the hand.
        The function returns the final total sum of the card values 
    after considering the values of Aces.

    main(): It starts with printing a message indicating that the 
    dealer is shuffling cards and taking two of them. Then, it calls
    the waiting() method, which simulates a waiting period by printing
    dots for 3 seconds. After the wait, it prints the dealer's first card.
        Within a loop that iterates 15 times (a hardcoded limit for 
    demonstration purposes),the dealer draws a card using the process()
    method. Then, it calls theplayer_ends() function to prompt the player
    whether they want to draw another card or not.
        Depending on the player's decision, the function either draws 
    a new card for the player or ends the player's turn. If the player's
    total points exceed 21, the game ends, indicating that the player 
    has lost.
    After each action by the player, the function prints the total points
    accumulated by the player.
        If the game continues without the player exceeding 21 points, it 
    proceeds to the dealer's turn. The dealer continues drawing cards
    until they have a total of 17 or higher.
        Once the dealer's turn ends, the function compares the total points 
    of the player and the dealer. Depending on the outcome, it prints a
    message indicating whether the player has won, lost, or the game ended 
    in a draw.











    
    