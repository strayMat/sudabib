# %%
import llm

from sudabib.constants import DEFAULT_LOCAL_MODEL, DEFAULT_MODEL
from sudabib.llm_tools_alex import get_alex_abstract, get_alex_articles

# %%
# works = get_alex_articles("health around retirement age")

# w0 = works[0]
# print(w0.keys())
# print(w0["abstract"])
# %%

question = "What is the impact of retirement age on health? Search open alex abstracts by extending this question and return the most relevant articles."

model = llm.get_model(DEFAULT_MODEL)
chain_response = model.chain(question, tools=[get_alex_articles, get_alex_abstract], after_call=print)
for chunk in chain_response:
    print(chunk, end="", flush=True)
# %%
