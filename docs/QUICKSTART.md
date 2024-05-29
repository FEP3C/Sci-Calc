# Sci-Calc Quickstart Guide

Welcome to Sci-Calc! This guide will help you get started with using Sci-Calc, a command-line scientific calculator written in Python. Sci-Calc supports a wide range of mathematical operations, including basic arithmetic, advanced functions, and trigonometry.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/FEP3C/sci-calc.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd sci-calc
   ```

3. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the Sci-Calc command-line interface, run the following command:

```bash
python src/cli_interface.py
```

You can now enter mathematical expressions directly into the terminal. Here are some examples of what you can do:

- Basic arithmetic: `2 + 3`, `5 - 2`, `4 * 3`, `8 / 2`
- Absolute value: `abs(-5)`
- Powers and roots: `square(4)`, `cube(3)`, `sqrt(16)`, `cbrt(27)`
- Factorial: `factorial(5)`
- Reciprocal: `reciprocal(4)`
- Trigonometric functions: `sin(30)`, `cos(60)`, `tan(45)`
- Logarithms: `log(100)`, `log10(100)`, `ln(2)`

## Features

Sci-Calc supports a variety of mathematical operations:

- **Basic Operations:**
  - Addition, Subtraction, Multiplication, Division

- **Advanced Operations:**
  - Absolute Value
  - Square, Cube
  - Square Root, Cube Root
  - Factorial
  - Reciprocal

- **Trigonometric Functions:**
  - Sine, Cosine, Tangent

- **Logarithmic Functions:**
  - Logarithm (base 10)
  - Natural Logarithm (base e)

## File Structure

The project structure is organized as follows:

```
sci-calc/
│
├── bin/
│   └── (Executable scripts, if any)
│
├── docs/
│   └── (Documentation files)
│
├── src/
│   ├── sci_calc.py
│   ├── expressions_parser.py
│   ├── basic_operations.py
│   ├── advanced_operations.py
│   ├── cli_interface.py
│   └── settings.py
│
├── .gitignore
├── LICENSE
└── README.md
```

- **src/sci_calc.py:** Main module that integrates all functionalities.
- **src/expressions_parser.py:** Parses and evaluates mathematical expressions.
- **src/basic_operations.py:** Contains functions for basic arithmetic operations.
- **src/advanced_operations.py:** Contains functions for advanced mathematical operations.
- **src/cli_interface.py:** Command-line interface logic.
- **src/settings.py:** Configuration settings for the project.

## Contributing

We welcome contributions to Sci-Calc! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

## License

Sci-Calc is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more information.

---

Thank you for using Sci-Calc! If you have any questions or need further assistance, feel free to open an issue on the [GitHub repository](https://github.com/your-username/sci-calc). Happy calculating!
