'''
The Game Set Up:
    Define a deck of 52 cards
    Define the dealer
    Define the player
        Assign a bank roll to the player


The Game Logic:
    Player places a bet
        Balance the bank roll and make sure there are enough funds
    Serve two cards to the player and face them up
    Serve two cards to the dealer and face one of them up
    If sum of player cards = 21, stop the game and announce the player as the winner

    Player's turn:
        As long as the player hits
            Serve a card to the player
            Calculate the total player_sum
            If player_sum > 21, player busts
                Pay the dealer and balance player's bank roll
                The game is over
            Until the playes stays

    Dealer's turn:
        Show the second card of the dealer
        As long as the dealer_sum < player_sum
            Server a card to the dealer
            Calculate the total sum
            If dealer_sum > 21, dealer busts
                Pay the player and balance the player's bank roll
                The game is over
            Else if dealer_sum > player_sum and delaer_sum <=21
                Pay the dealer  
                Charge the player's bank roll
                The game is over

'''



import random



class Deck(): 
    def __init__(self): 
        self.deck_of_cards = { '1':(1, 'Clubs', 1), '2':(2, 'Clubs', 2), '3':(3, 'Clubs', 3), '4':(4, 'Clubs', 4), '5':(5, 'Clubs', 5), '6':(6, 'Clubs', 6) , '7':(7, 'Clubs', 7), '8':(8, 'Clubs', 8), '9':(9, 'Clubs', 9), '10':(10, 'Clubs', 10), '11':('Jack', 'Clubs', 10), '12':('Queen', 'Clubs', 10) , '13':('King', 'Clubs', 10), '14':(1, 'Spades', 1), '15':(2, 'Spades', 2), '16':(3, 'Spades', 3), '17':(4, 'Spades', 4), '18':(5, 'Spades', 5), '19':(6, 'Spades', 6) , '20':(7, 'Spades', 7), '21':(8, 'Spades', 8), '22':(9, 'Spades', 9), '23':(10, 'Spades', 10), '24':('Jack', 'Spades', 10), '25':('Queen', 'Spades', 10) , '26':('King', 'Spades', 10), '27':(1, 'Hearts', 1), '28':(2, 'Hearts', 2), '29':(3, 'Hearts', 3), '30':(4, 'Hearts', 4), '31':(5, 'Hearts', 5), '32':(6, 'Hearts', 6) , '33':(7, 'Hearts', 7), '34':(8, 'Hearts', 8), '35':(9, 'Hearts', 9), '36':(10, 'Hearts', 10), '37':('Jack', 'Hearts', 10), '38':('Queen', 'Hearts', 10) , '39':('King', 'Hearts', 10), '40':(1, 'Diamonds', 1), '41':(2, 'Diamonds', 2), '42':(3, 'Diamonds', 3), '43':(4, 'Diamonds', 4), '44':(5, 'Diamonds', 5), '45':(6, 'Diamonds', 6) , '46':(7, 'Diamonds', 7), '47':(8, 'Diamonds', 8), '48':(9, 'Diamonds', 9), '49':(10, 'Diamonds', 10), '50':('Jack', 'Diamonds', 10), '51':('Queen', 'Diamonds', 10) , '52':('King', 'Diamonds', 10) }

        
    def reshuffle(self):
        deck.__init__()


    def serve(self):
        if deck.is_finished():
            return 'The deck is served. Reshuffle to fill up the deck.'
        card_number = random.choice(list(self.deck_of_cards.keys()))
        return self.deck_of_cards.pop(card_number)


    def no_of_cards_left(self):
        return len(self.deck_of_cards)


    def is_finished(self):
        return self.no_of_cards_left() == 0


    

class Account(): 
    def __init__(self): 
        self.bank_roll = 0
        self.sum = 0

    
    def set_bank_roll(self, amount):
        self.bank_roll = amount


    def credit_bank_roll(self, amount):
        self.bank_roll += amount
        return self.bank_roll


    def charge_bank_roll(self, amount):
        self.bank_roll -= amount
        return self.bank_roll


    def has_sufficient_balance(self, bet):
        if bet > self.bank_roll:
            print('You do not have sufficient credit in your account')
        return bet <= self.bank_roll


    

class Players(Account): 
    def __init__(self): 
        self.sum = 0 
        self.hand = []
        self.bank_roll = 0
        
        
    def set_bank_roll(self, amount):
        self.bank_roll = amount
        
        
    def credit_bank_roll(self, amount):
        self.bank_roll += amount
        return self.bank_roll


    def charge_bank_roll(self, amount):
        self.bank_roll -= amount
        return self.bank_roll


    def has_sufficient_balance(self, bet):
        return bet <= self.bank_roll


    def hit(self, deck):
        card = deck.serve()
        self.hand.append(card)
        return self.hand


    def sum_of_cards(self, deck):
        self.sum = 0
        if deck.is_finished(): 
            return 'The deck is served. Reshuffle to fill up the deck.'

        for item in self.hand:
            if int(item[2]) == 1 and self.sum <= 10:
                self.sum += 11
            else:
                self.sum += int(item[2])
        return self.sum




class Dealer(): 
    def __init__(self): 
        self.sum = 0 
        self.hand = []


    def hit(self, deck):
        card = deck.serve()
        self.hand.append(card) 
        return self.hand


    def sum_of_cards(self, deck):
        self.sum = 0
        if deck.is_finished(): 
            return 'The deck is served. Reshuffle to fill up the deck.'

        for item in self.hand:
            if int(item[2]) == 1 and self.sum <= 10:
                self.sum += 11
            else:
                self.sum += int(item[2])
        return self.sum


    def play(self, player, deck, bet):
        '''
        Dealer's turn: As long as the dealer_sum < player_sum
            Serve a card to the dealer
            Calculate the total dealer_sum
        '''
        while self.sum < player.sum:
            self.hit(deck)
            self.sum_of_cards(deck)
        return self.sum

    
    
deck = Deck() 
player = Players() 
dealer = Dealer()

# Set an account credit for the player
player.set_bank_roll(100)


# Player places a bet
while True: 
    try: 
        bet = int(input('Place a bet: ')) 
    except ValueError: 
        print('You did not type in a number') 
        continue 
    else: 
        break

# Check the bank roll and make sure there are enough funds
if player.has_sufficient_balance(bet):
    # Serve two cards to the dealer and face one of them up, keep the second face down
    a = dealer.hit(deck)[-1][:2]
    print('\nDealer 1st card: ', a)
    b = dealer.hit(deck)[-1][:2]
    print('Dealer next card: ', '_____Hidden____')

    # Serve two cards to the player and face both of them up
    print('\nPlayer 1st card: ', player.hit(deck)[-1][:2])
    print('Player next card: ', player.hit(deck)[-1][:2], ' Total player hand: ', player.sum_of_cards(deck))
    # print('Player total hand: ', player.sum_of_cards(deck))

    # If sum of player's first two cards is 21, stop the game and announce the player as the winner
    if player.sum_of_cards(deck) == 21:
        print("\nThe player won! Player's hand is: ", player.sum_of_cards(deck))
        player.credit_bank_roll(bet)
        print('Player new account balance is: ', player.bank_roll)
    else:
        # As long as the player hits, serve a card and calculate the total hand
        while True:
            hit = input('hit? (Y/N)').upper()
            if hit == 'N':
                break
            elif hit =='Y':
                print('Player next card: ', player.hit(deck)[-1][:2], ' Total player hand: ', player.sum_of_cards(deck))

                # If total hand > 21, player busts
                if player.sum_of_cards(deck) > 21:
                    print('Player is BUST')

                    # Pay the dealer and balance player's bank roll
                    player.charge_bank_roll(bet)
                    print('Player new account balance is: ', player.bank_roll)
                    break
            else:
                print('Type in Y or N: ')
else: 
    print('You do not have sufficient credit in your account')

    
if hit == 'N': 
    print('\nDealers turn') 
    print('Dealer 1st card: ', a) 
    print('Dealer next card: ', b, ' Total dealer hand: ', dealer.sum_of_cards(deck))

    x = dealer.play(player, deck, bet)
    print('\nDealer total hand is: ', x)

    if x > 21:
        print('Dealer lost')
        player.credit_bank_roll(bet)
        print('Player new account balance is: ', player.bank_roll)
    else:
        print('Dealer won')
        player.charge_bank_roll(bet)
        print('Player new account balance is: ', player.bank_roll)
    


