import random

class Player():
  # Creates player
  def __init__(self,num,deck):
    self.hand = [self.give_card(deck),self.give_card(deck)]
    self.num = num + 1
  def __repr__(self):
    selfstr = "Player " + str(self.num) + " has: "
    for card in self.hand:
      selfstr += card + " "
    return selfstr
  # Gives a card
  def give_card(self,deck):
    card_index = random.randint(0,len(deck.cards)-1)
    return deck.cards.pop(card_index)
  # Player's action on their turn
  def action(self,deck):
    stand = False
    while stand == False:
      action = input("Player {num}, will you hit (h) or stand (s)?\n".format(num=self.num))
      if action == "h":
        self.hand.append(self.give_card(deck))
        print(self)
        if self.total() > 21:
          print("Bust!")
          break
      elif action == "s":
        stand = True
      else:
        print("Please enter a valid action")
  # Dealer stands on 17
  def dealer_action(self,deck):
    self.dealer_print()
    while self.total() < 17:
      self.hand.append(self.give_card(deck))
      self.dealer_print()
  def dealer_print(self):
    selfstr = "Dealer has: "
    for card in self.hand:
      selfstr += card + " "
    print(selfstr)
  # Counts the player's total
  def total(self):
    total = 0
    tens = ['10H','10D','10C','10S','JH','JD','JC','JS','QH','QD','QC','QS','KH','KD','KC','KS']
    aces = ['AH','AD','AC','AS']
    for card in self.hand:
      if card in aces:
        total += 11
      elif card in tens:
        total += 10
      else:
        total += int(card[0])
    if total > 21 and (self.hand[0] in aces or self.hand[1] in aces):
      total -= 10
    return total

class Deck():
  def __init__(self):
    self.cards = self.new_deck()
  def __repr__(self):
    print(len(self.cards))
    selfstr = "Deck includes: "
    for card in self.cards:
      selfstr += card + " "
    return selfstr
  # Shuffles a new deck
  def new_deck(self):
    deck_of_cards = ['2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']
    unshuffled = deck_of_cards + deck_of_cards + deck_of_cards + deck_of_cards
    shuffled = []
    for i in range(0,208):
      card_index = random.randint(0,len(unshuffled)-1)
      shuffled.append(unshuffled.pop(card_index))
    return shuffled

continues = True
deck = Deck()

while continues == True:
  # Creates players
  num_players = int(input("How many people are playing?\n"))
  players = []
  for i in range(0,num_players):
    new_player = Player(i,deck)
    players.append(new_player)
    print(new_player)
  dealer = Player(69,deck)
  print("Dealer has: X {card}".format(card=dealer.hand[1]))

  for player in players:
    player.action(deck)
  dealer.dealer_action(deck)

  for player in players:
    if player.total() > 21:
      print("Player {num} busted".format(num=player.num))
    elif dealer.total() > 21:
      print("Player {num} wins! Dealer busts".format(num=player.num))
    elif player.total() == 21 and len(player.hand) == 2:
      print("Congrats! Player {num} has a blackjack".format(num=player.num))
    elif player.total() > dealer.total():
      print("Player {num} wins!".format(num=player.num))
    elif player.total() == dealer.total():
      print("Player {num} pushes".format(num = player.num))
    elif player.total() < dealer.total():
      print("Player {num} loses".format(num=player.num))
    else:
      print("I'm confused bruh! You broke the program")

  if input("Play again? (y/n)\n") == "y":
    continues = True
  else:
    continues = False

  if len(deck.cards) < 26:
    deck = Deck()