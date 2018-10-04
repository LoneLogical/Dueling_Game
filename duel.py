import random


class Duel:

    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def commence(self):
        # let player know what they are up against
        self.player.print_full_stats()
        self.opponent.print_full_stats()

    def player_victory(self):
        print("PLAYER VICTORY")

    def game_over(self):
        print("GAME OVER")

    def mainloop(self):
        """
        Function that loops to keep champions fighting until someone is defeated.
        :return: True if player wins and false if player loses
        """
        while not self.player.is_dead() and not self.opponent.is_dead():
            # At the moment, players and opponent are oblivious to other's current action
            self.player.refresh_display()
            self.opponent.refresh_display()

            player_action, player_value = self.player.next_action()
            oppo_action, oppo_value = self.opponent.next_action()

            print('*****')
            print(player_action + ' -- ' + str(player_value))
            print(oppo_action + ' -- ' + str(oppo_value))

            if player_action == 'Attack':
                if oppo_action == 'Attack':
                    if player_value > oppo_value:
                        self.opponent.got_hit(25 * random.random() * player_value)
                    else:
                        self.player.got_hit(25 * random.random() * oppo_value)
                elif oppo_action == 'Shield':
                    if player_value * random.uniform(0.5, 1.0) > oppo_value:
                        self.opponent.got_hit(25 * random.random() * player_value)
                    else:
                        self.player.got_blocked(10 * random.random() * oppo_value, 10 * random.random() * player_value)
                else:
                    if player_value * random.uniform(0.3, 0.8) > oppo_value:
                        self.opponent.got_hit(25 * random.random() * player_value)
                    else:
                        self.player.was_evaded(10 * random.random() * player_value)

            elif player_action == 'Shield':
                if oppo_action == 'Attack':
                    if oppo_value * random.uniform(0.5, 1.0) > player_value:
                        self.player.got_hit(25 * random.random() * oppo_value)
                    else:
                        self.opponent.got_blocked(10 * random.random() * player_value, 10 * random.random() * oppo_value)
                elif oppo_action == 'Shield':
                    if player_value > oppo_value:
                        self.opponent.got_blocked(10 * random.random() * player_value, 10 * random.random() * oppo_value)
                    else:
                        self.player.got_blocked(10 * random.random() * oppo_value, 10 * random.random() * player_value)
                else:
                    if player_value * random.uniform(0.3, 0.8) > oppo_value:
                        self.opponent.got_blocked(10 * random.random() * player_value, 10 * random.random() * oppo_value)
                    else:
                        self.player.was_evaded(10 * random.random() * player_value)

            else:
                if oppo_action == 'Attack':
                    if oppo_value * random.uniform(0.3, 0.8) > player_value:
                        self.player.got_hit(25 * random.random() * oppo_value)
                    else:
                        self.opponent.was_evaded(10 * random.random() * oppo_value)
                elif oppo_action == 'Shield':
                    if oppo_value * random.uniform(0.3, 0.8) > player_value:
                        self.player.got_blocked(10 * random.random() * oppo_value, 10 * random.random() * player_value)
                    else:
                        self.opponent.was_evaded(10 * random.random() * oppo_value)
                else:
                    self.player.was_evaded(0)
                    self.opponent.was_evaded(0)


        # broke out of while loop so someone died

        if self.player.is_dead():
            self.game_over()
        else:
            self.player_victory()


    """
    def first_move(self):
        player_value = self.player.dodge() * random.uniform(0.5, 1.0)
        opponent_value = self.opponent.dodge() * random.uniform(0.5,1.0)

        if player_value > opponent_value:
            return self.player, self.opponent
        else:
            return self.opponent, self.player
    """