import random

class Player:
    VERSION = "Best Python player"

    def betRequest(self, game_state):
        min_to_call = game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet']
        my_money = game_state['players'][game_state['in_action']]['stack']
        if my_money < min_to_call:
            return my_money
        return random.randint(min_to_call, my_money)

    def showdown(self, game_state):
        pass

