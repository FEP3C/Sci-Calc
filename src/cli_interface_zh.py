import random
import colorama
from colorama import Fore, Style
import atexit
import os
import readline

class CLIInterface:
    def __init__(self, calculator):
        self.calculator = calculator
        self.color = self.get_color(calculator.settings.get_settings().get('theme', 'white'))
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
║                     科学计算器 (Sci-Calc)                            ║
║                                                                      ║
║          福州二中 Python创意编程社区 2024 版权所有 © 2024            ║
╚══════════════════════════════════════════════════════════════════════╝

📝 GitHub 仓库地址: https://github.com/FEP3C/Sci-Calc

💡 可以计算的功能:
   • 四则计算: +, -, *, /
   • 高级函数: abs(), square(), cube(), sqrt(), factorial(), reciprocal()
   • 三角函数: sin(), cos(), tan()
   • 对数计算: lg(), ln()

 🤝 想要贡献代码吗？
   1. 在 GitHub 仓库中 Fork 项目并阅读 `Docs` 文件夹
   2. 创建新Branch并进行PR
   3. 合并拟定功能到我们的主分支
   4. 等待我们审核并合并代码

输入 'help' 显示指令列表。
输入 'quit()' 退出程序{Style.RESET_ALL}
"""
        print(banner)

    def display_help(self):
        help_text = f"""
{self.color}指令列表:
------------------
1. 四则运算:
   • 加法: a + b
   • 减法: a - b
   • 乘法: a * b
   • 除法: a / b

2. 高级函数:
   • 绝对值函数: abs(x)
   • 平方: square(x)
   • 立方: cube(x)
   • 平方根: sqrt(x)
   • 阶乘: f(x)
   • 倒数: r(x)

3. 三角函数:
   • 正弦函数: sin(x)
   • 余弦函数: cos(x)
   • 正切函数: tan(x)

4. 对数函数:
   • 常见对数 (底数为10): lg(x)
   • 自然对数: ln(x){Style.RESET_ALL}
"""
        print(help_text)

    def start(self):
        self.display_banner()
        histfile = os.path.join(os.path.expanduser("~"), ".sci_calchist")
        try:
            readline.read_history_file(histfile)
            readline.set_history_length(1000)
        except FileNotFoundError:
            pass

        atexit.register(readline.write_history_file, histfile)
        
        while True:
            try:
                expression = input(f"{self.color}Sci-Calc>>> {Style.RESET_ALL}")
            except EOFError:
                break
            if expression.lower() == 'help':
                self.display_help()
                continue
            
            result = self.calculator.evaluate(expression)
            if result == "quit":
                break
            print(f"{self.color}Result: {result}{Style.RESET_ALL}")

        random_messages = [
            "再见! 感谢使用Sci-Calc! 👋",
            "下次见! 祝你算得开心! ✨",
            "拜拜! 记住，数学很有趣! 🌟",
            "再会! 继续保持探索数学的热情! 📚",
            "直到下一次时见, 保持好奇! 🔢"
        ]
        goodbye_message = random.choice(random_messages)
        print(f"\n{self.color}{goodbye_message}{Style.RESET_ALL}")
