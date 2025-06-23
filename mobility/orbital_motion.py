import math
import numpy as np
from utils import config

class OrbitalMotion:
    """Simple circular orbital motion model for LEO satellites."""
    def __init__(self, satellite):
        self.satellite = satellite
        self.env = satellite.simulator.env
        self.altitude = config.SATELLITE_ALTITUDE
        self.earth_radius = config.EARTH_RADIUS
        self.orbit_radius = self.earth_radius + self.altitude
        # Calculate angular velocity using Kepler's third law
        self.angular_velocity = math.sqrt(config.MU_EARTH / self.orbit_radius ** 3)
        self.phase = 2 * math.pi * satellite.identifier / satellite.simulator.n_drones
        self.update_interval = 0.1 * 1e6  # 0.1s
        self.env.process(self.update_position())

    def update_position(self):
        while True:
            t = self.env.now / 1e6  # convert to seconds
            angle = self.angular_velocity * t + self.phase
            x = self.orbit_radius * math.cos(angle)
            y = self.orbit_radius * math.sin(angle)
            z = 0
            self.satellite.coords = [x, y, z]
            yield self.env.timeout(self.update_interval)
