import json


class Settings:
    def __init__(self):
        self.config = self.load_settings()

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return self.default_settings()

    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.config, f, indent=4)

    def fix_settings(self, new_settings):
        self.config.update(new_settings)
        self.save_settings()

    def get_settings(self):
        return self.config

    @staticmethod
    def display_settings():
        return {
            "version": "The version number of the calculator",
            "angle_unit": "Angle unit (degree, radian, polar)",
            "precision": "Number of decimal places",
            "theme": "Theme color (white, green, blue, red)",
            "decimal_separator": "Decimal separator (comma, dot)"
        }

    @staticmethod
    def default_settings():
        return {
            "version": "1.0.0",
            "angle_unit": "degree",
            "precision": 2,
            "theme": "white",
            "decimal_separator": "."
        }
