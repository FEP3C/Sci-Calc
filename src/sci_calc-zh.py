import argparse
from settings import Settings
from cli_interface_zh import CLIInterface
from basic_operations import BasicOperations
from advanced_operations import AdvancedOperations


class Calculator:
    def __init__(self):
        self.settings = Settings()

    @staticmethod
    def evaluate(expression):
        if expression.lower() == "quit()":
            return "quit"
        parser = ExpressionParser(expression)
        return parser.evaluate()


class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, self.get_operations())
            return result
        except Exception as e:
            return str(e)

    @staticmethod
    def get_operations():
        return {
            "add": BasicOperations.add,
            "subtract": BasicOperations.subtract,
            "multiply": BasicOperations.multiply,
            "divide": BasicOperations.divide,
            "square": AdvancedOperations.square,
            "cube": AdvancedOperations.cube,
            "sqrt": AdvancedOperations.sqrt,
            "cube_root": AdvancedOperations.cube_root,
            "sin": AdvancedOperations.sin,
            "cos": AdvancedOperations.cos,
            "tan": AdvancedOperations.tan,
            "ln": AdvancedOperations.ln,
            "log10": AdvancedOperations.lg,
            "lg": AdvancedOperations.lg,
            "log_base": AdvancedOperations.log,
            "reciprocal": AdvancedOperations.reciprocal,
            "abs": AdvancedOperations.abs,
            "factorial": AdvancedOperations.factorial,
            "math": __import__('math')  # Import the math module for additional operations
        }


def interactive_fix_settings(calculator):
    settings_info = calculator.settings.display_settings()
    current_settings = calculator.settings.get_settings()
    settings_filter = calculator.settings.settings_filter()

    print("Current Settings:")
    for key in settings_info.keys():
        print(f"{key}: {current_settings[key]} - {settings_info[key]}")

    print("\nEnter the number of the setting you want to change or 'done' to finish:")
    settings_list = list(settings_info.keys())
    for i, setting in enumerate(settings_list, start=1):
        print(f"{i}. {setting} ({settings_info[setting]})")

    settings_to_fix = {}
    while True:
        try:
            choice = input("> ")
        except EOFError:
            print()
            break
        if choice.lower() == 'done':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(settings_list):
            key = settings_list[int(choice) - 1]
            new_value = input(f"Enter new value for {key} ({settings_info[key]}): ")
            if not settings_filter[key](new_value):
                print(f"Invalid value. Please enter a valid value for {key} ({settings_info[key]})")
                continue
            settings_to_fix[key] = new_value
        elif choice.lower() in ('list', 'help'):
            settings_list = list(settings_info.keys())
            for i, setting in enumerate(settings_list, start=1):
                print(f"{i}. {setting} ({settings_info[setting]})")
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
