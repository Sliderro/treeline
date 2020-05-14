from treeline.engine.engine import Engine
from treeline.engine.camera import Camera
from treeline.model.board import Board
from treeline.model.player import Player
from treeline.model.resource import Resources
from treeline.model.game import Game


if __name__ == '__main__':
    engine = Engine()
    camera = Camera((0, 0), fov=32)
    engine.set_camera(camera)
    engine.register_for_keys(camera)

    board = Board("./resources/maps/map1.csv")
    player = Player(Resources())
    game = Game(board, player)
    for actor in game.get_all_actors():
        engine.add_actor(actor)

    engine.start()
