import random
import math

class Player:
    VERSION = "Best Python player"

    def betRequest(self, game_state):
        myself = game_state['players'][game_state['in_action']]
        if ((game_state['round'] == 0) and (game_state['current_buy_in'] >= myself['stack'])):
            return 0

        min_to_call = game_state['current_buy_in'] - myself['bet']
        my_money = myself['stack']
        if my_money < min_to_call:
            return math.floor(my_money / 2)
        return random.randint(min_to_call, my_money)

    def showdown(self, game_state):
        pass

