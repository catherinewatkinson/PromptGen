# setup.py

from setuptools import setup

setup(
    # The name of the package that you install with pip
    name="prompt-gen",
    version="1.1.0",  # Updated version to reflect changes
    # The list of Python modules to include. This must match the filename.
    py_modules=["prompt_gen"],  # Looks for prompt_gen.py
    install_requires=[
        "typer[all]",
        "pyperclip",
        "google-generativeai",
        "python-dotenv",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            # This line creates the command 'prompt-gen'
            # and links it to the 'app' object in your 'prompt_gen.py' file.
            "prompt-gen = prompt_gen:app",
        ],
    },
)
