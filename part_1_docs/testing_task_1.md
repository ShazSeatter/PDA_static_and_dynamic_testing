### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# no properties have been defined - not a class

  def check_for_ace(self, card):
    # needs to be == to check for equality
    if card.value = 1:
      return True
    # missing : after else to indicate new block of code
    else
      return False
   
# dif does not define a function. In python it should be def highest_card()
  dif highest_card(self, card1 card2):
  # should have indentations. Right now block of code is same line as where the function starts 
  # should write self.car1.value
  if card1.value > card2.value:
    # wrong variable name
    return card
  else:
    return card2
  


def cards_total(self, cards):
  # starting value/total hasn't been defined 
  total
  for card in cards:
    total += card.value
  # return on this level will exit the loop and not continue adding all the values
  # total needs to be converted into a string for the concatentation to work 
    return "You have a total of" + total

```
