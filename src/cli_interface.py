import random
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

    def display_banner(self):
        banner = f"""
{self.color}╔══════════════════════════════════════════════════════════════════════╗
║                     Scientific Calculator (Sci-Calc)                 ║
║                                                                      ║
║          Fuzhou No.2 High School Python Creative Coding Club         ║
╚══════════════════════════════════════════════════════════════════════╝

📝 GitHub Repository: https://github.com/FEP3C/Sci-Calc

💡 Available Operations:
   • Basic: +, -, *, /
   • Advanced: abs(), square(), cube(), sqrt(), factorial()
   • Trigonometric: sin(), cos(), tan()
   • Logarithmic: log(), ln()

🤝 Want to Contribute?
   1. Read our documentation in the Docs folder
   2. Create a new branch and submit a Pull Request
   3. Merge your changes with our source code

Type 'help' for command list
Type 'quit()' to exit{Style.RESET_ALL}
"""
        print(banner)

    def display_help(self):
        help_text = f"""
{self.color}Available Commands:
------------------
1. Basic Operations:
   • Addition: a + b
   • Subtraction: a - b
   • Multiplication: a * b
   • Division: a / b

2. Advanced Functions:
   • Absolute Value: abs(x)
   • Square: square(x)
   • Cube: cube(x)
   • Square Root: sqrt(x)
   • Factorial: factorial(x)

3. Trigonometric Functions:
   • Sine: sin(x)
   • Cosine: cos(x)
   • Tangent: tan(x)

4. Logarithmic Functions:
   • Common Log (base 10): log(x)
   • Natural Log: ln(x){Style.RESET_ALL}
"""
        print(help_text)

    def start(self):
        self.display_banner()
        
        while True:
            expression = input(f"{self.color}Sci-Calc>>> {Style.RESET_ALL}")
            if expression.lower() == 'help':
                self.display_help()
                continue
            
            result = self.calculator.evaluate(expression)
            if result == "quit":
                break
            print(f"{self.color}Result: {result}{Style.RESET_ALL}")

        random_messages = [
            "Farewell! Thanks for using Sci-Calc! 👋",
            "See you next time! Happy calculating! ✨",
            "Goodbye! Remember, math is fun! 🌟",
            "Take care! Keep exploring mathematics! 📚",
            "Until next time, stay curious! 🔢"
        ]
        goodbye_message = random.choice(random_messages)
        print(f"\n{self.color}{goodbye_message}{Style.RESET_ALL}")
