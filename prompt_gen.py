# prompt_gen.py

import os
import sys
from typing import Optional

import google.generativeai as genai
import pyperclip
import typer
from dotenv import load_dotenv
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing_extensions import Annotated

# --- Configuration ---
load_dotenv()
app = typer.Typer()

# --- Model Mapping ---
# Maps short aliases to full Gemini model names.
MODEL_MAP = {
    "pro2.5": "gemini-2.5-pro",
    "flash2.5": "gemini-2.5-flash",
    "flash-lite2.5": "gemini-2.5-flash-light",
    "pro2": "gemini-2.0-pro",
    "flash2": "gemini-2.0-flash",
    "flash-lite2": "gemini-2.0-flash-lite",
}
DEFAULT_MODEL_ALIAS = "pro2.5"
DEFAULT_MODEL_NAME = MODEL_MAP[DEFAULT_MODEL_ALIAS]


# --- The "Meta-Prompt" ---
META_PROMPT_TEMPLATE = """
You are an expert prompt engineer. Your task is to take a user's raw context and transform it into a detailed, effective, and well-structured prompt for another LLM agent.

Here is the user's raw context to analyze:
---
{raw_context}
---

**Rules:**
1.  Analyze the user's context to infer the most likely role they need the agent to take (e.g., "Python Developer," "Code Reviewer," "Computational Chemist").
2.  Analyze the context to create a concise but comprehensive task description.
3.  Format the final output *exactly* as follows, replacing the bracketed placeholders with the role and task description you inferred.
4.  A **critical requirement** is that you do not replicate any code that you were provided as context, instead providing a placeholder where you wish for it to be included.

**Role:** 
[INSERT INFERRED ROLE HERE]

---
**Context:**
[INSERT CONTEXT HERE]
---
**Task:**
[INSERT TASK DESCRIPTION HERE]
"""


@app.command()
def main(
    context_arg: Annotated[
        Optional[str],
        typer.Option(
            "--context",
            "-c",
            help="Your raw idea or context for the prompt (for short, single-line input).",
        ),
    ] = None,
    file_path: Annotated[
        Optional[typer.FileText],
        typer.Option(
            "--file",
            "-f",
            help="Path to a file containing the context.",
        ),
    ] = None,
    model_alias: Annotated[
        str,
        typer.Option(
            "--model",
            "-m",
            help=f"Model alias to use. Options: {', '.join(MODEL_MAP.keys())}.",
        ),
    ] = DEFAULT_MODEL_ALIAS,
):
    """
    Uses Gemini to refine a raw context into a polished, structured prompt.
    Context can be provided via -c, -f, or standard input.
    """
    raw_context = ""
    if context_arg:
        raw_context = context_arg
    elif file_path:
        raw_context = file_path.read()
    # Check if data is being piped into stdin
    elif not sys.stdin.isatty():
        raw_context = sys.stdin.read()
    else:
        typer.secho(
            "Error: No context provided. Please provide context using -c, -f, or by piping from stdin.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        typer.secho(
            "Error: GEMINI_API_KEY not found in environment variables or .env file.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    genai.configure(api_key=api_key)

    # Get the full model name from the alias, falling back to the default if invalid.
    full_model_name = MODEL_MAP.get(model_alias, DEFAULT_MODEL_NAME)

    try:
        model = genai.GenerativeModel(full_model_name)
        final_meta_prompt = META_PROMPT_TEMPLATE.format(raw_context=raw_context)
        polished_prompt = ""

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(
                description=f"🧠 Contacting {full_model_name}...", total=None
            )
            response = model.generate_content(final_meta_prompt)
            polished_prompt = response.text

        pyperclip.copy(polished_prompt)
        typer.secho("✅ AI-refined prompt copied to clipboard!", fg=typer.colors.GREEN)
        typer.echo("\n--- Generated Prompt ---\n")
        typer.echo(polished_prompt)

    except Exception as e:
        typer.secho(
            f"An error occurred while contacting the Gemini API: {e}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
