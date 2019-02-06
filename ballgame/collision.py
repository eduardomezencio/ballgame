"""Collision detection related funcionality."""
from itertools import combinations


class CollisionWorld:
    """Container and logic for collision detection."""
    def __init__(self):
        self._objects = set()
        self._to_remove = set()
        self._objects_locked = 0

    def add(self, obj):
        """Adds object to world."""
        self._objects.add(obj)
        obj.add_destroy_callback(self.remove)

    def clear(self):
        """Removes all objects from the world."""
        self._objects.clear()

    def check_collision(self, obj_a, obj_b) -> bool:
        """Checks if two objects are in collision."""
        return (obj_a.distance(obj_b) < obj_a.radius + obj_b.radius
                and obj_a not in self._to_remove
                and obj_b not in self._to_remove)

    def collisions(self, obj=None):
        """Iterator for all collisions between pairs of objects."""
        self._objects_locked += 1
        if obj is None:
            yield from ((a, b) for a, b in combinations(self._objects, 2)
                        if self.check_collision(a, b))
        else:
            yield from ((obj, o) for o in self._objects
                        if o is not obj and self.check_collision(obj, o))
        self._objects_locked -= 1
        if not self._objects_locked:
            while self._to_remove:
                self._objects.remove(self._to_remove.pop())

    def remove(self, obj):
        """Remove object from world."""
        if not self._objects_locked:
            self._objects.remove(obj)
        else:
            self._to_remove.add(obj)
