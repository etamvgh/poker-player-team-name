import random
import card_query

class Player:
    VERSION = "Best Python player"

    def betRequest(self, game_state):
        rank = 0

        myself = game_state['players'][game_state['in_action']]

        try:
            rank = card_query.query(myself['hole_cards'] + game_state['community_cards'])['rank']
        except Exception as exc:
            rank = 0

        if ((game_state['round'] == 0) and (game_state['current_buy_in'] >= myself['stack'])):
            return 0

        min_to_call = game_state['current_buy_in'] - myself['bet']
        my_money = myself['stack']

        if my_money < min_to_call:
            if (my_money / 2) < myself['bet']:
                return my_money
            return 0

        max_bet = my_money / 9 * (rank +1)
        if max_bet < min_to_call:
            max_bet = min_to_call

        bet = random.randint(0, max_bet)
        if bet < min_to_call:
            bet = min_to_call

        return bet

    def showdown(self, game_state):
        pass

