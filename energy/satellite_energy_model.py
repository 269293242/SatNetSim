from utils import config

class SatelliteEnergyModel:
    """Simplified energy model for LEO satellites with solar charging."""
    def __init__(self, satellite):
        self.satellite = satellite
        self.env = satellite.simulator.env
        self.panel_area = config.SOLAR_PANEL_AREA
        self.panel_efficiency = config.SOLAR_PANEL_EFFICIENCY
        self.battery_capacity = config.BATTERY_CAPACITY
        self.residual_energy = self.battery_capacity
        self.update_interval = 1 * 1e6  # 1s
        self.env.process(self.energy_update())

    def energy_update(self):
        while True:
            harvested = self.panel_area * self.panel_efficiency * config.SOLAR_CONSTANT * (self.update_interval / 1e6)
            self.residual_energy = min(self.battery_capacity, self.residual_energy + harvested)
            self.satellite.residual_energy = self.residual_energy
            yield self.env.timeout(self.update_interval)
