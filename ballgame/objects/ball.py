"""The Ball object."""

from __future__ import annotations

import pygame

from ballgame.vector import Vector


class Ball:
    """A ball."""
    INCREMENT = 4

    def __init__(self, x, y, radius, color=(255, 255, 255)):
        self._center = Vector(x, y)
        self._radius = int(radius)
        self._color = color

        self._destroy_callbacks = []

        self.move_to(x, y)

    @property
    def position(self) -> Vector:
        """Object's position as a vector."""
        return self._center

    @property
    def radius(self) -> int:
        """Radius of the object."""
        return self._radius

    @property
    def rect(self) -> pygame.Rect:
        """The object's bounding box."""
        return pygame.Rect(self._center.x - self._radius,
                           self._center.y - self._radius,
                           self._radius * 2, self._radius * 2)

    def add_destroy_callback(self, callback):
        """Add callbacks to be called when object is destroyed."""
        if not callable(callback):
            raise TypeError('Callback must be callable.')
        self._destroy_callbacks.append(callback)

    def collision(self, other):
        """Collision with other object."""
        if self.radius > other.radius:
            self.grow()
            other.destroy()
        else:
            self.destroy()
            other.grow()

    def copy(self) -> Ball:
        """Builds a copy of this object."""
        return Ball(self._center.x, self._center.y, self._radius, self._color)

    def destroy(self):
        """Destroys the object."""
        while self._destroy_callbacks:
            self._destroy_callbacks.pop()(self)

    def distance(self, other):
        """Distance between the center of two objects."""
        return self.position.distance(other.position)

    def draw(self, surface: pygame.Surface):
        """Draws the object to a surface."""
        pygame.draw.circle(surface, self._color, self._center, self._radius)

    def grow(self):
        """Grows by a fixed amount."""
        self._radius += 2 * Ball.INCREMENT

    def move(self, x, y):
        """Moves object relative to current position."""
        self._center.x += x
        self._center.y += y

    def move_to(self, x, y):
        """Moves object to absolute position."""
        self._center = Vector(x, y)
