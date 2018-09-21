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
            return my_money

        max_bet = my_money / 8
        if max_bet < min_to_call:
            max_bet = min_to_call

        bet = random.randint(0, max_bet)
        if bet < min_to_call:
            bet = min_to_call

        return bet

    def showdown(self, game_state):
        pass

