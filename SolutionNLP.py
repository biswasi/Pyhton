import wikipedia as wp 
import re
import requests
import spacy
import spacy_transformers
from spacy import displacy
from spacy.matcher import Matcher
import networkx as nx
from pyvis.network import Network

wp.set_lang("en")

# Obtain and store the data
title = "New York"
data = wp.page(title).content

# View the data
print(data)
data = data.lower().replace('\n' ,"")

# Remove the last part of the text, certain punctuation marks, headings, as well as any text within the parentheses
data = re.sub('== see also ==.*|[@#:&\\"]|===.*?===|==.*?==|\\(.*?\\)', '', data)

# View the data
print(data)
# Load a language model
nlp = spacy.load('en_core_web_lg')
doc=nlp(data)

# Display the entities in the doc
displacy.render(doc,style="ent",jupyter=True)
# Add the coreference resolution component in the pipeline
nlp.add_pipe('coreferee')

# Pass the data to the language model 
doc = nlp(data)

# Print resolved coreferences, if any
doc._.coref_chains.print()

resolved_data = ""
for token in doc:
    resolved_coref = doc._.coref_chains.resolve(token)
    if resolved_coref:
        resolved_data += " " + " and ".join(r.text for r in resolved_coref)
    elif token.dep_ == "punct":
        resolved_data += token.text
    else:
        resolved_data += " " + token.text
print(resolved_data)


def extract_relationship(sentence):
    doc = nlp(sentence)
    
    first, last = None, None
    
    for chunk in doc.noun_chunks:
        if not first:
            first = chunk
        else:
            last = chunk

    if first and last:
        return (first.text.strip(), last.text.strip(), str(doc[first.end:last.start]).strip())
    
    return (None, None, None)


# Create a Network object
graph_doc = nlp(resolved_data)

# Create an empty graph
nx_graph = nx.DiGraph()

for sent in enumerate(graph_doc.sents) :
    if len(sent[1]) > 3:
        (a, b, c) = extract_relationship(str(sent[1]))

        # Add nodes and edges to graph
        if a and b:
            nx_graph.add_node(a, size = 5)
            nx_graph.add_node(b, size = 5)
            nx_graph.add_edge(a, b, weight=1, title=print_five_words(c), arrows="to")

g = Network(notebook=True, cdn_resources='in_line')
g.from_nx(nx_graph)
g.save_graph("example.html")    


print(nx_graph.edges(['manhattan']))