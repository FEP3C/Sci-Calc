import json
import os

class Settings:
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.defaults = {
            'version': '1.0',  # Version of the calculator
            'angle_unit': 'degree',  # Angle unit: degree, radian, polar
            'precision': 2,  # Precision of calculations (number of decimal places)
            'theme_color': 'white',  # Theme color: white, green, blue, red
            'decimal_separator': 'dot'  # Decimal separator: dot, comma
        }
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.settings = json.load(file)
        else:
            self.settings = self.defaults

    def save_settings(self):
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def fix_settings(self, settings):
        for key, value in settings.items():
            if key in self.defaults:
                self.settings[key] = value
        self.save_settings()

    def get_settings(self):
        return self.settings

    def display_settings(self):
        settings_info = {
            'version': 'Version of the calculator',
            'angle_unit': 'Angle unit (degree, radian, polar)',
            'precision': 'Precision of calculations (number of decimal places)',
            'theme_color': 'Theme color (white, green, blue, red)',
            'decimal_separator': 'Decimal separator (dot, comma)'
        }
        return settings_info


