from setup import setup, Executable
executables = [Executable("calc.py")]

setup(
    name = "calculator",
    version = "1.0",
    description = "simple calculator",
    executables = executables
)