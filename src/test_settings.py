import json
import os
from settings import Settings


def setup_module():
    # Create a default settings file for testing
    default_settings = {
        "version": "1.0.0",
        "angle_unit": "degree",
        "precision": 2,
        "theme": "white",
        "decimal_separator": "."
    }
    with open("settings.json", "w") as f:
        json.dump(default_settings, f, indent=4)


def teardown_module():
    # Remove the settings file after testing
    os.remove("settings.json")


def test_settings_load():
    settings = Settings()
    assert settings.config['version'] == "1.0.0"
    assert settings.config['angle_unit'] == "degree"
    assert settings.config['precision'] == 2
    assert settings.config['theme'] == "white"
    assert settings.config['decimal_separator'] == "."


def test_fix_settings():
    settings = Settings()
    new_settings = {
        "precision": 3,
        "theme": "green"
    }
    settings.fix_settings(new_settings)
    assert settings.config['precision'] == 3
    assert settings.config['theme'] == "green"

    # Reload settings to ensure changes are persistent
    settings.load_settings()
    assert settings.config['precision'] == 3
    assert settings.config['theme'] == "green"
