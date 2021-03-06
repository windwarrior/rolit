import pytest, time
from mock import Mock, call, patch

from rolit.server import *

@patch.object(random, 'shuffle', Mock())
class TestServer(object):

    def setup_method(self, method):
        self.server = Server()

        self.mocked_clients = [{ 'socket' : Mock(), 'name' : "Met_TOM_op_de_koffie!", 'supported' : Protocol.CHAT_AND_CHALLENGE },
                               { 'socket' : Mock(), 'name' : "Yorinf",                'supported' : Protocol.CHAT_AND_CHALLENGE },
                               { 'socket' : Mock(), 'name' : "Tegel_14",              'supported' : Protocol.CHAT_ENABLED },
                               { 'socket' : Mock(), 'name' : "Lalala_geld",           'supported' : Protocol.BAREBONE },
                               { 'socket' : Mock(), 'name' : "IEOEDMB",               'supported' : Protocol.CHALLENGE_ENABLED },
                               { 'socket' : Mock(), 'name' : "Inter-Actief",          'supported' : Protocol.CHAT_AND_CHALLENGE }]

        self.clients = []
        for client in self.mocked_clients:
            self.clients.append(self.server.connect(client['socket'], client['name'], client['supported']))

    def start_game_with_two_players(self):
        self.server.create_game(self.clients[0])
        self.server.join_game(self.clients[1], self.clients[0]['name'])
        return self.server.start_game(self.clients[0])

    def start_game_with_three_players(self):
        self.server.create_game(self.clients[0])
        self.server.join_game(self.clients[1], self.clients[0]['name'])
        self.server.join_game(self.clients[2], self.clients[0]['name'])
        return self.server.start_game(self.clients[0])

    def start_game_with_four_players(self):
        self.server.create_game(self.clients[0])
        self.server.join_game(self.clients[1], self.clients[0]['name'])
        self.server.join_game(self.clients[2], self.clients[0]['name'])
        self.server.join_game(self.clients[3], self.clients[0]['name'])
        return self.server.start_game(self.clients[0])
