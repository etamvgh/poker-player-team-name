import random

class Player:
    VERSION = "Best Python player"

    def betRequest(self, game_state):
        return random.randint(0, game_state['players'][game_state['in_action']]['stack'])

    def showdown(self, game_state):
        pass

