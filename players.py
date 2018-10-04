import random


class Champion:

    def __init__(self, name, strength, endurance, agility):
        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        self.base_health = 500 + (50 * endurance)
        self.current_health = self.base_health
        self.base_stamina = 300 + (25 * endurance)
        self.current_stamina = self.base_stamina

    def print_full_stats(self):
        print("Champion " + self.name)
        print("Str: {0}  -- End: {1}  -- Agi: {2}".format(self.strength, self.endurance, self.agility))
        print('Health: {0}   Stamina: {1}'.format(self.current_health, self.current_stamina))
        print("")

    def refresh_display(self):
        """
        Refresh the stats for the Player by outputting to terminal
        """
        print('---'*20)
        print("Champion " + self.name)
        print('Health: {0}   Stamina: {1}'.format(round(self.current_health,2),
                                                  round(self.current_stamina,2)))

    def lose_health(self, damage):
        """
        Deal damage to champion's health
        :param damage: integer amount
        """
        if damage > self.current_health:
            self.current_health = 0
        else:
            self.current_health -= damage

    def lose_stamina(self, loss):
        """
        Champion lost stamina from use of ability
        :param loss: integer amount
        """
        if loss > self.current_stamina:
            self.current_stamina = 0
        else:
            self.current_stamina -= loss

    def got_hit(self, damage):
        """
        Champion was struck by opponent and health will be decreased. Will add more functionality later.
        :param damage: Integer amount to decrease health by
        """
        self.lose_health(damage)
        print(self.name + " was damaged for " + str(round(damage, 2)) + ' hp.')
        # later will implement stumbling

    def got_blocked(self, damage, exertion):
        """
        Champion's attack was blocked by opponent. Stamina and Health will decrease.
        :param damage: Integer amount to decrease health by
        :param exertion: Integer amount to decrease stamina by
        """
        self.lose_health(damage)
        self.lose_stamina(exertion)
        print(self.name + " was damaged for " + str(round(damage, 2)) + ' hp.')
        print(self.name + " was drained of " + str(round(exertion, 2)) + ' stamina.')
        # later will implement stumbling

    def was_evaded(self, exertion):
        """
        Champion's attack was evaded by opponent's dodge. Stamina will decrease
        :param exertion: Integer amount to decrease stamina by
        """
        self.lose_stamina(exertion)
        print(self.name + " was drained of " + str(round(exertion, 2)) + ' stamina.')

    def heal(self):
        """
        Heal Champion for random amount of missing health
        """
        self.current_health += int((self.base_health - self.current_health) * random.random())

    def rest(self):
        """
        Replenish Champion's stamina
        """
        rejuvenate = (self.base_stamina - self.current_stamina) * random.uniform(0.75, 1.0)
        self.current_stamina += int(rejuvenate)

    def is_dead(self):
        if self.current_health == 0:
            return True
        else:
            return False


class Player(Champion):

    def next_action(self):
        """
        Asks Player what action they would like to perform next
        :return: Action(string), Value(float)
        """
        self.refresh_display()
        action_prompt = "What is your next action: Attack('A'), Shield('S'), or Dodge('D'): "
        player_decision = input(action_prompt)

        stamina_percent = self.current_stamina / self.base_stamina

        while True:
            if player_decision == 'A':
                attack_value = self.strength * stamina_percent
                self.lose_stamina(10)
                return 'Attack', attack_value
            elif player_decision == 'S':
                defense_value = self.endurance * stamina_percent
                self.lose_stamina(5)
                return 'Shield', defense_value
            elif player_decision == 'D':
                dodge_value = self.agility * stamina_percent
                self.lose_stamina(3)
                return 'Dodge', dodge_value
            else:
                player_decision = input("Incorrect Action. Please try again: ")


class Opponent(Champion):

    def next_action(self):
        """
        AI must decide what move to perform next
        :return: Action(string), Value(float)
        """
        # create probability list
        ai_actions = ['Attack', 'Shield', 'Dodge']
        ai_probabilities = [1.0, 0.80, 1.0]

        random_choice = random.random()
        print('random choice: ' + str(random_choice))

        stamina_percent = self.current_stamina / self.base_stamina

        if random_choice < ai_probabilities[0]:
            attack_value = self.strength * stamina_percent
            self.lose_stamina(10)
            return 'Attack', attack_value
        elif random_choice < ai_probabilities[1]:
            defense_value = self.endurance * stamina_percent
            self.lose_stamina(5)
            return 'Shield', defense_value
        else:
            dodge_value = self.agility * stamina_percent
            self.lose_stamina(3)
            return 'Dodge', dodge_value
