import pyalex
from pyalex import Works

from sudabib.constants import DEFAULT_OPEN_ALEX_MAIL


# to turn this into a llm-tool, I need to take inspiration from https://github.com/simonw/llm-tools-sqlite/blob/main/llm_tools_sqlite.py
def get_alex_articles(query: str):
    "Get articles from OpenAlex based on a query in natural language."

    pyalex.config.email = DEFAULT_OPEN_ALEX_MAIL
    works = Works().search(query).sort(cited_by_count="desc").get()
    restricted_keys = [
        "id",
        "title",
        "abstract",
        "publication_year",
        "open_access",
        "cited_by_count",
    ]  # , "authorships"]
    works_restricted = []
    for w in works:
        work_dict = {k: w.get(k, None) for k in restricted_keys}
        works_restricted.append(work_dict)
    return works_restricted


def get_alex_abstract(article_id: str):
    "Get the abstract of an article from OpenAlex based on its ID."
    pyalex.config.email = DEFAULT_OPEN_ALEX_MAIL
    work = Works().get(article_id)
    return work.abstract if work else None
