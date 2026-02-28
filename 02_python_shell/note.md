# Python Shell — Why Do We Use It?

The **Python shell** (also called the **REPL** — Read-Eval-Print Loop) is an interactive environment where you type Python code and see the result immediately.

## How to start it

- In the terminal, run: `python` (or `python3` on some systems).
- You’ll see a prompt like `>>>` where you can type code line by line.

## Why we use the Python shell

1. **Try code quickly** — Run a few lines or a small idea without creating or saving a file.
2. **Experiment and explore** — Test built-in functions, operators, or new libraries before putting them in a script.
3. **Debug and inspect** — Run parts of your program, check variable values, and see errors right away.
4. **Learn Python** — See how statements and expressions behave step by step.
5. **Use your own code** — After `import your_module`, you can call your functions and use your variables interactively.

## Useful commands inside the shell

- `import os` — Import the `os` module (paths, environment, etc.).
- `os.getcwd()` — Get the current working directory.
- `import sys` — Import the `sys` module (system-related info).
- `sys.platform` — Get the platform (e.g. `'darwin'`, `'win32'`, `'linux'`).
- `import filename` — Import a Python file (without `.py`); you can then use its functions and variables.

## Summary

The Python shell is for **quick, interactive experimentation** and learning, while script files (`.py`) are for **reusable, saved programs**.
