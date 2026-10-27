class TrafficManager:

    def __init__(self):
        self.vehicles = {
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }

        self.signal = {
            1: "RED",
            2: "RED",
            3: "RED",
            4: "RED"
        }

    def update_vehicles(self, road, vehicles):
        self.vehicles[road] = vehicles

    def get_status(self):
        return {
            "vehicles": self.vehicles,
            "signal": self.signal
        }

    def select_signal(self):
        # Find road with maximum traffic
        road = max(self.vehicles, key=self.vehicles.get)

        # Make all signals RED
        for r in self.signal:
            self.signal[r] = "RED"

        # Give GREEN signal to highest traffic road
        self.signal[road] = "GREEN"

        return {
            "message": "Automatic signal selected",
            "green_road": road,
            "signal": self.signal
        }

    def emergency_priority(self, road):
        # Make all signals RED
        for r in self.signal:
            self.signal[r] = "RED"

        # Emergency road gets GREEN
        self.signal[road] = "GREEN"

        return {
            "message": "Emergency priority activated",
            "emergency_road": road,
            "signal": self.signal
        }
