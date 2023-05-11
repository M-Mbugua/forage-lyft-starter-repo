from tyres.tyres import Tyres


class OctoprimeTyres(Tyres):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear

    def needs_service(self):
        return sum(self.tyre_wear) >= 3.0

