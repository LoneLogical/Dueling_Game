from players import *
from duel import *

user = Player('Lothar', 4, 3, 3)
ai = Opponent('Brute', 4, 3, 3)

first_duel = Duel(user, ai)

first_duel.commence()
first_duel.mainloop()
