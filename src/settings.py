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
            "angle_unit": "Angle unit (degree, radian, polar)",
            "precision": "Number of decimal places",
            "theme": "Theme color (white, green, blue, red)",
            "decimal_separator": "Decimal separator (comma, dot)"
        }

    @staticmethod
    def settings_filter():
        return {
            "angle_unit": lambda x: x in ["degree", "radian", "polar"],
            "precision": str.isdigit,
            "theme": lambda x: x in ["red", "blue", "green", "white"],
            "decimal_separator": lambda x: x in ["comma", "dot"]
        }

    @staticmethod
    def default_settings():
        return {
            "version": "1.0.0",
            "angle_unit": "degree",
            "precision": "2",
            "theme": "white",
            "decimal_separator": "."
        }
