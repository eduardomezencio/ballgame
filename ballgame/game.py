"""The game main module."""

from __future__ import annotations

from random import randrange
import sys

import pygame

from ballgame.collision import CollisionWorld
from ballgame.objects.ball import Ball

BLACK = 0, 0, 0
SIZE = WIDTH, HEIGHT = 800, 450


class Game:
    """The game."""
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        self._collision = CollisionWorld()
        self._mouse_pos = WIDTH // 2, HEIGHT // 2
        self._objects = set()
        self._player = None
        self._screen = pygame.display.set_mode(SIZE)
        self._stage = 0
        self._start_stage(self._stage)

    def run(self):
        """Starts the game loop."""
        try:
            while True:
                for event in pygame.event.get():
                    if event.type in (pygame.QUIT, pygame.KEYDOWN):
                        sys.exit()
                    elif event.type == pygame.MOUSEMOTION:
                        self._mouse_pos = tuple(event.pos)
                self._update()
                self._screen.fill(BLACK)
                self._draw()
                pygame.display.flip()
        except SystemExit:
            pass
        finally:
            pygame.quit()

    def _draw(self):
        for obj in self._objects:
            obj.draw(self._screen)

    def _update(self):
        self._player.move_to(*self._mouse_pos)
        for obj_a, obj_b in self._collision.collisions(self._player):
            obj_a.collision(obj_b)
        self._check_conditions()

    def _add_object(self, obj):
        self._objects.add(obj)
        self._collision.add(obj)
        obj.add_destroy_callback(self._remove_object)

    def _remove_object(self, obj):
        self._objects.remove(obj)

    def _clear(self):
        self._collision.clear()
        self._objects.clear()

    def _check_conditions(self):
        if self._player not in self._objects:
            self._lose()
        elif len(self._objects) == 1:
            self._win()

    def _lose(self):
        pygame.quit()
        sys.exit()

    def _win(self):
        self._start_stage(self._stage + 1)

    def _start_stage(self, stage: int):
        self._stage = stage
        self._clear()

        for i in range(stage):
            radius = (2 * i + 5) * Ball.INCREMENT
            ball = Ball(randrange(WIDTH), randrange(HEIGHT), radius)
            while self._any_collision(ball):
                ball.move_to(randrange(WIDTH), randrange(HEIGHT))
            self._add_object(ball)

        ball = Ball(randrange(WIDTH), randrange(HEIGHT), 6 * Ball.INCREMENT)
        while self._any_collision(ball):
            ball.move_to(randrange(WIDTH), randrange(HEIGHT))
        self._add_object(ball)
        self._player = ball

    def _any_collision(self, obj):
        try:
            next(self._collision.collisions(obj))
            return True
        except StopIteration:
            return False


def main():
    """The game main function."""
    game = Game()
    game.run()
