from typing import Dict
import numpy as np
import random
from tdw.controller import Controller

class ObjectInfo:
    """
    Based on ObjectPosition from &tdw_physics
    """

    def __init__(self, position: Dict[str, float], radius: float, id: int):
        """
        :param position: The position of the object.
        :param radius: The maximum radius swept by the object's bounds.
        :param id: The object id
        """

        self.position = position
        self.radius = radius
        self.id = id

 
def get_random_avatar_position(radius_min: float, radius_max: float, y_min: float, y_max: float,
                                center: Dict[str, float], angle_min: float = 0,
                                angle_max: float = 360) -> Dict[str, float]:
        """
        The same as get_random_avatar_position from &tdw_physics
        :param radius_min: The minimum distance from the center.
        :param radius_max: The maximum distance from the center.
        :param y_min: The minimum y positional coordinate.
        :param y_max: The maximum y positional coordinate.
        :param center: The centerpoint.
        :param angle_min: The minimum angle of rotation around the centerpoint.
        :param angle_max: The maximum angle of rotation around the centerpoint.

        :return: A random position for the avatar around a centerpoint.
        """

        a_r = random.uniform(radius_min, radius_max)
        a_x = center["x"] + a_r
        a_z = center["z"] + a_r
        theta = np.radians(random.uniform(angle_min, angle_max))
        a_x = np.cos(theta) * (a_x - center["x"]) - np.sin(theta) * (a_z - center["z"]) + center["x"]
        a_y = random.uniform(y_min, y_max)
        a_z = np.sin(theta) * (a_x - center["x"]) + np.cos(theta) * (a_z - center["z"]) + center["z"]

        return {"x": a_x, "y": a_y, "z": a_z}