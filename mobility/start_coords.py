import random
import math
from utils import config


def get_random_start_point_3d(sim_seed):
    start_position = []
    for i in range(config.NUMBER_OF_DRONES):
        random.seed(sim_seed + i)
        position_x = random.uniform(1, config.MAP_LENGTH - 1)
        position_y = random.uniform(1, config.MAP_WIDTH - 1)
        position_z = random.uniform(1, config.MAP_HEIGHT - 1)

        start_position.append(tuple([position_x, position_y, position_z]))

    return start_position


def get_orbit_start_point(sim_seed):
    start_position = []
    radius = config.EARTH_RADIUS + config.SATELLITE_ALTITUDE
    for i in range(config.NUMBER_OF_DRONES):
        angle = 2 * math.pi * i / config.NUMBER_OF_DRONES
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = 0
        start_position.append((x, y, z))
    return start_position
