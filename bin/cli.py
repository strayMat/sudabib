#! /usr/bin/env python
import logging

import click
import llm

from sudabib.constants import DEFAULT_MODEL, LOG_LEVEL
from sudabib.llm_tools_alex import get_alex_abstract_from_id, get_alex_articles

logging.basicConfig(
    level=logging.getLevelName(LOG_LEVEL),
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
)


@click.group()
@click.version_option(package_name="sudabib")
def cli():
    pass


@cli.command()
def main() -> None:
    """sudabib Main entrypoint"""
    click.secho("Welcome to sudabib!", fg="green")


@cli.command()
@click.option("--question", "-q", required=True, help="The research question to explore")
@click.option("--model", "-m", default=DEFAULT_MODEL, help="LLM model to use")
@click.option("--verbose", "-v", is_flag=True, help="Show tool calls")
def search(question: str, model: str, verbose: bool) -> None:
    """Search OpenAlex articles using AI tools to answer research questions.

    QUESTION: The research question to explore using OpenAlex database
    """
    system_promt = "To answer the question, search OpenAlex abstracts with tools by extending this question and return the most relevant articles."
    prompt = system_promt + question
    try:
        llm_model = llm.get_model(model)

        chain_response = llm_model.chain(
            prompt, tools=[get_alex_articles, get_alex_abstract_from_id], after_call=print if verbose else None
        )

        for chunk in chain_response:
            print(chunk, end="", flush=True)
        print()  # Add final newline

    except Exception as e:
        click.secho(f"Error: {e}", fg="red", err=True)
        raise click.Abort()


if __name__ == "__main__":
    cli()
