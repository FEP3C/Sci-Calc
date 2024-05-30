class CLIInterface:
    def __init__(self, calculator):
        self.calculator = calculator
        self.running = True

    def start(self):
        print("Welcome to The Scientific Calculator created by Fuzhou No.2 High School Python Creative Coding Club!")
        print("Repo Link: https://github.com/FEP3C/Sci-Calc")
        print("This Program is clearly under Construction. If you want to join us and contribute to our program:")
        print("    * Read our docs in the Docs Folder")
        print("    * Pull a GitHub Request and Create New Branch")
        print("    * Merge with the Source Code in the Github.")
        print("Happy Calculating!")

        while self.running:
            expression = input("Sci-Calc>>> ")
            if expression.lower() == "quit()":
                self.quit()
            else:
                try:
                    result = self.calculator.evaluate(expression)
                    print(f"The Result is: {result}")
                except Exception as e:
                    print(f"Error: {e}")

    def quit(self):
        print("Have a good day!")
        self.running = False

