# %%
import llm

from sudabib.constants import DEFAULT_LOCAL_MODEL, DEFAULT_MODEL, DEFAULT_OPEN_ALEX_MAIL
from sudabib.llm_tools_alex import get_alex_abstract_from_id, get_alex_articles
from pyalex import Works
import pyalex

# %%
pyalex.config.email = DEFAULT_OPEN_ALEX_MAIL
# works = get_alex_articles("health around retirement age")
query = "effects of retirement age on healthcare"
works = Works().search(query).get()
w0 = works[0]
print(w0.keys())
print(w0["abstract"])
get_alex_abstract_from_id(w0["id"])
# %%

question = "What is the impact of retirement age on health? Search open alex abstracts by extending this question and return the most relevant articles."

model = llm.get_model(DEFAULT_MODEL)
chain_response = model.chain(question, tools=[get_alex_articles, get_alex_abstract_from_id], after_call=print)
for chunk in chain_response:
    print(chunk, end="", flush=True)
# %%
