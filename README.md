Of course. Here is a complete README.md file that you can copy and paste for your project.

-----

# PromptGen

`prompt-gen` is a command-line interface (CLI) tool that uses the Google Gemini API to transform raw ideas & context into perfectly structured, high-quality prompts.

It acts as an intelligent co-pilot for your prompt engineering workflow, saving you time by automatically generating and formatting prompts for complex tasks.

## Features

  * **AI-Powered Refinement**: Leverages a "meta-prompt" to ask Gemini to act as an expert prompt engineer, turning your simple context into a detailed prompt.
  * **Clipboard Integration**: Automatically copies the final, AI-generated prompt to your system's clipboard for immediate use.
  * **Secure API Key Handling**: Uses a `.env` file to securely manage your Google Gemini API key, keeping it out of your code.
  * **Easy Installation**: Can be installed as a global command using standard Python packaging tools.

-----

## Installation

Follow these steps to get `prompt-crafter` up and running.

### Prerequisites

  * Python 3.8+
  * Git

### 1\. Clone the Repository

First, clone the project from its source repository to your local machine.

```bash
git clone <your-repository-url>
cd prompt-crafter_project
```

### 2\. Set Up Your Gemini API Key

This tool requires a Google Gemini API key to function.

1.  Get your free API key from **[Google AI Studio](https://aistudio.google.com/app/apikey)**.

2.  In the project directory, create a `.env` file to store your key securely. Replace `your_api_key_here` with the key you just obtained.

    ```bash
    # Create the file
    touch .env

    # Add your key to the file
    echo 'GEMINI_API_KEY="your_api_key_here"' > .env
    ```

### 3\. Install the Package

Install the tool and its dependencies using `pip`. The `-e` flag installs it in "editable" mode, so any changes you make to `prompt-gen.py` will be immediately effective.

```bash
pip install -e .
```

The `prompt-gen` command is now globally available in your terminal.

-----

## Usage

To use the tool, simply call the `prompt-gen` command with the `-c` or `--context` option, followed by your raw idea in quotes.

### Example

Let's say you need to debug a slow database query. Instead of writing a detailed prompt manually, you can just provide the basic idea:

```bash
prompt-gen -c "my sql query to fetch user orders is too slow. it uses a few joins. need to figure out why and how to fix it."
```

The tool will display the following messages as it works:

```
🧠 Contacting Gemini to refine your prompt...
✅ AI-refined prompt copied to clipboard!

--- Generated Prompt ---

**Role:** SQL Performance Analyst

---
**Context:**
my sql query to fetch user orders is too slow. it uses a few joins. need to figure out why and how to fix it.
Here is the relevant code:
```

[PASTE CODE HERE]

```

---
**Task:**
You are a Gemini agent. Please perform the following task: Analyze the provided SQL query that is experiencing performance issues. Identify potential bottlenecks such as inefficient joins, missing indexes, or suboptimal query structure. Provide a detailed explanation of the problems found and suggest an optimized version of the query.
```

The complete, refined prompt is now on your clipboard, ready to be pasted into any LLM interface.

-----

## License

This project is licensed under the MIT License.