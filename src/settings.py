import json
import logging

class Settings:
    def __init__(self):
        self.config = self.load_settings()

    def load_settings(self) -> dict:
        try:
            with open("settings.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"加载设置失败: {e}")
            return self.default_settings()

    def save_settings(self) -> None:
        try:
            with open("settings.json", "w") as f:
                json.dump(self.config, f, indent=4)
        except IOError as e:
            logging.error(f"保存设置失败: {e}")

    def fix_settings(self, new_settings) -> None:
        if self.validate_settings(new_settings):
            self.config.update(new_settings)
            self.save_settings()
        else:
            logging.warning("新的设置无效，不会更新。")

    def validate_settings(self, new_settings) -> bool:
        filters = self.settings_filter()
        for key, value in new_settings.items():
            if key in filters:
                if not filters[key](value):
                    logging.warning(f"设置项 {key} 的值 {value} 无效。")
                    return False
        return True

    def get_settings(self) -> dict:
        return self.config

    @staticmethod
    def display_settings() -> dict:
        return {
            "angle_unit": "Angle unit (degree, radian, polar)",
            "precision": "Number of decimal places",
            "theme": "Theme color (white, green, blue, red)",
            "decimal_separator": "Decimal separator (comma, dot)"
        }

    @staticmethod
    def settings_filter() -> dict:
        return {
            "angle_unit": lambda x: x in ["degree", "radian", "polar"],
            "precision": str.isdigit,
            "theme": lambda x: x in ["red", "blue", "green", "white"],
            "decimal_separator": lambda x: x in ["comma", "dot"]
        }

    @staticmethod
    def default_settings() -> dict:
        return {
            "version": "1.0.0",
            "angle_unit": "degree",
            "precision": "2",
            "theme": "white",
            "decimal_separator": "."
        }
