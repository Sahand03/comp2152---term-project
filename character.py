class Character:
    def __init__(self, combat_strength, health_points):
        self.__combat_strength = combat_strength
        self.__health_points = health_points

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self.__combat_strength = max(0, min(6, value))

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        self.__health_points = max(0, value)

    def __del__(self):
        print(f"{self.__class__.__name__} object destroyed.")
