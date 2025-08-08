Prompt Gen 🤖
prompt-gen is a command-line interface (CLI) tool that uses the power of the Google Gemini API to transform your raw ideas into perfectly structured, high-quality prompts.

It acts as an intelligent co-pilot for your prompt engineering workflow, saving you time by automatically generating and formatting prompts for complex tasks.

Features
AI-Powered Refinement: Leverages a "meta-prompt" to ask Gemini to act as an expert prompt engineer, turning your simple context into a detailed prompt.

Flexible Input: Provide context via command-line arguments, files, or by piping directly from standard input.

Model Selection: Easily choose your desired Gemini model using simple aliases (e.g., pro2.5, flash1.5).

Clipboard Integration: Automatically copies the final, AI-generated prompt to your system's clipboard for immediate use.

Secure API Key Handling: Uses a .env file to securely manage your Google Gemini API key.

Installation
Follow these steps to get prompt-gen up and running.

Prerequisites
Python 3.8+

An active Conda environment

1. Clone the Repository
First, clone the project from its source repository to your local machine.

git clone <your-repository-url>
cd PromptGen

2. Set Up Your Gemini API Key
This tool requires a Google Gemini API key to function.

Get your free API key from Google AI Studio.

In the project directory, create a .env file to store your key securely. Replace your_api_key_here with the key you just obtained.

echo 'GEMINI_API_KEY="your_api_key_here"' > .env

3. Install the Package
Install the tool and its dependencies into your active Conda environment using pip. The -e flag installs it in "editable" mode, so any changes you make to the script will be immediately effective.

pip install -e .

The prompt-gen command is now globally available in your terminal.

Usage
prompt-gen is designed to be flexible. You can provide your context in three different ways.

Method 1: Command-Line Argument (for short text)
Use the -c or --context flag for simple, single-line context.

prompt-gen -c "my python function to calculate fibonacci is slow"

Method 2: From a File (Recommended for code)
For multi-line text or code snippets, save your context to a file (e.g., my_code.py) and use the -f or --file flag.

prompt-gen -f my_code.py

Method 3: Using a Pipe / Standard Input
You can also pipe content directly into the command. This is a powerful way to integrate prompt-gen into other command-line workflows.

Piping from a file:

cat my_code.py | prompt-gen

Pasting directly into the terminal (using a "here document" instigated by << followed by some delimiter): 

prompt-gen <<EOF
> Paste your multi-line
> code or text directly
> into the terminal.
> EOF

Selecting a Model
Use the -m or --model flag to specify which Gemini model to use. If you don't provide one, it will default to gemini-2.5-pro

Available aliases: pro2.5, flash2.5, flash-lite2.5, pro2.0, flash2.0, flash-lite2.0