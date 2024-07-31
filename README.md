# Sci-Calc

Sci-Calc 是一款用 Python 编写的功能强大的命令行科学计算器。 它支持从基本算术到高级函数和三角函数等多种数学运算。

## 目录

- [功能](#功能)
- [安装](#安装)
- [使用方法](#使用方法)
- [文件结构](#文件结构)
- [贡献](#贡献)
- [许可证](#许可证)

## 功能

Sci-Calc 提供以下功能：

- **基本操作：**
  - 加法运算
  - 减法
  - 乘法
  - 除法

- 高级运算：**
  - 绝对值
  - 平方、立方
  - 平方根、立方根
  - 阶乘
  - 倒数

- 三角函数：**
  - 正弦
  - 余弦
  - 正切

- 对数函数：**
  - 对数（基数 10）
  - 自然对数（以 e 为底）

## 安装

请按照以下步骤安装和设置 Sci-Calc：

1. **克隆版本库：**

   ```bash
   git clone https://github.com/FEP3C/Sci-Calc.git
   ```

2. **导航到项目目录：**

   ```bash
   cd sci-calc
   ```

3. **创建并激活虚拟环境（可选，但推荐）：**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate # 在 Windows 上使用 `venv\Scripts\activate` 。
   ```

4. **安装所需的依赖项：**

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

要开始使用 Sci-Calc，请运行命令行界面：

```bash
python src/sci_calc.py
```

然后，你可以直接在终端输入数学表达式。 下面是一些示例：

- 基本算术：`2 + 3`、`5 - 2`、`4 * 3`、`8 / 2
- 绝对值： `abs(-5)`
- 幂和根： `square(4)`, `cube(3)`, `sqrt(16)`, `cube_root(27)`
- 阶乘： 阶乘(5)
- 倒数: `reciprocal(4)`
- 三角函数： sin(30)`，cos(60)`，tan(45)
- 对数： `log(100)`, `log10(100)`, `ln(2)`

## 文件结构

项目结构如下

```
sci-calc/
│
├── bin/
│ └─── （可执行脚本，如果有的话）
│
├── docs/
│ └─── （文档文件）
│
├── src/
│ ├── sci_calc.py
│ ├─── expressions_parser.py
├─── 基本操作.py
├─── 高级操作.py
│ ├──cli_interface.py
│ └─── settings.py
│
├── .gitignore
├── LICENSE
└── README.md
```

- **src/sci_calc.py:** 集成所有功能的主模块。
- **src/expressions_parser.py:** 解析和评估数学表达式。
- **src/basic_operations.py:** 包含基本算术运算函数。
- **src/advanced_operations.py:** 包含高级数学运算函数。
- **src/cli_interface.py:** 命令行界面逻辑。
- **src/settings.py:** 项目的配置设置。

## 贡献

我们欢迎为 Sci-Calc 投稿！ 要投稿，请按照以下步骤操作：

1. 分叉仓库。
2. 创建一个新分支（`git checkout -b feature-branch`）。
3. 进行更改。
4. 提交改动（`git commit -m 'Add some feature'`）。
5. 推送到分支（`git push origin feature-branch`）。
6. 打开拉取请求。

请确保你的代码遵循项目的编码标准并包含适当的测试。

## 许可证

Sci-Calc 采用 MIT 许可。 更多信息请参见 [LICENSE](LICENSE) 文件。

---

感谢您使用 Sci-Calc！ 如果您有任何问题或需要进一步帮助，请随时在 [GitHub 代码库](https://github.com/FEP3C/Sci-Calc) 上提交问题。 祝您计算愉快！

