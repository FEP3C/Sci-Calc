import colorama
from colorama import Fore, Style

class CLIInterface:
    def __init__(self, calculator):
        self.calculator = calculator
        self.color = self.get_color(calculator.settings.get_settings().get('theme_color', 'white'))
        colorama.init()

    def get_color(self, color_name):
        colors = {
            'white': Fore.WHITE,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'red': Fore.RED
        }
        return colors.get(color_name, Fore.WHITE)

    def start(self):
        print(f"{self.color}Welcome to The Scientific Calculator created from Fuzhou No.2 High School Python Creative Coding Club!")
        print("Repo Link: https://github.com/FEP3C/Sci-Calc")
        print("This Program is clearly under Construction. If you want to join us and contribute for our program:")
        print("    * Read our docs in the Docs Folder")
        print("    * Pull a GitHub Request and Create New Branch")
        print("    * Merge with the Source Code in the Github.")
        print("Happy Calculating! Type 'quit()' to exit.")
        print(Style.RESET_ALL)
        
        while True:
            expression = input(f"{self.color}Sci-Calc>>> {Style.RESET_ALL}")
            result = self.calculator.evaluate(expression)
            if result == "quit":
                break
            print(f"The Result is: {result}")
        
        print(f"{self.color}Have a good day!{Style.RESET_ALL}")

