from entities.drone import Drone
from mobility.orbital_motion import OrbitalMotion
from energy.satellite_energy_model import SatelliteEnergyModel

class Satellite(Drone):
    """Satellite node using orbital motion and solar energy model."""
    def __init__(self, env, node_id, coords, speed, inbox, simulator):
        super().__init__(env, node_id, coords, speed, inbox, simulator)
        self.mobility_model = OrbitalMotion(self)
        self.energy_model = SatelliteEnergyModel(self)


