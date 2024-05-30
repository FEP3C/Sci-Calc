import argparse
from settings import Settings
from cli_interface import CLIInterface
from expressions_parser import ExpressionParser

class Calculator:
    def __init__(self):
        self.settings = Settings()

    def evaluate(self, expression):
        if expression.lower() == "quit()":
            return "quit"
        parser = ExpressionParser(expression)
        return parser.evaluate()

def interactive_fix_settings(calculator):
    settings_info = calculator.settings.display_settings()
    current_settings = calculator.settings.get_settings()
    
    print("Current Settings:")
    for key, value in current_settings.items():
        print(f"{key}: {value} - {settings_info[key]}")

    print("\nEnter the number of the setting you want to change or 'done' to finish:")
    settings_list = list(current_settings.keys())
    for i, setting in enumerate(settings_list, start=1):
        print(f"{i}. {setting} ({settings_info[setting]})")

    settings_to_fix = {}
    while True:
        choice = input("> ")
        if choice.lower() == 'done':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(settings_list):
            key = settings_list[int(choice) - 1]
            new_value = input(f"Enter new value for {key} ({settings_info[key]}): ")
            settings_to_fix[key] = new_value
        else:
            print("Invalid choice. Please enter a number corresponding to the setting or 'done' to finish.")

    calculator.settings.fix_settings(settings_to_fix)
    print("Settings fixed successfully!")

if __name__ == "__main__":
    calculator = Calculator()

    # Argument parser
    parser = argparse.ArgumentParser(description='Scientific Calculator')
    parser.add_argument('--fix-settings', action='store_true', help='Fix settings')
    parser.add_argument('--settings', action='store_true', help='View settings')
    args = parser.parse_args()

    if args.fix_settings:
        interactive_fix_settings(calculator)
    elif args.settings:
        current_settings = calculator.settings.get_settings()
        print("Current Settings:")
        for key, value in current_settings.items():
            print(f"{key}: {value}")
    else:
        # Start calculator
        cli = CLIInterface(calculator)
        cli.start()

