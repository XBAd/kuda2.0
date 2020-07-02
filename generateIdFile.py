from py2neo import Graph
from pandas import DataFrame

graph = Graph("bolt://localhost:7687/db/schemaKG/", username="neo4j", password="kuda")


with open("./pkubase_entity_id.txt","w") as f:
    data = DataFrame(graph.run("match (n) return id(n),n").data())
    for index,row in data.iterrows():
        f.write('<'+row['n']['name']+'>\t'+str(row['id(n)'])+'\n')

with open("./pkubase_predicate_id.txt","w") as f:
    data = DataFrame(graph.run("match ()-[r]->() return distinct type(r)").data())
    for index, row in data.iterrows():
        f.write('<'+row.to_list()[0]+'>\t'+str(index)+'\n')


with open("./pkubase_type_id.txt", "w") as f:
    data = DataFrame(graph.run("call db.labels()").data())
    for index, row in data.iterrows():
        if index == 0:
            continue
        f.write( '<' + row.to_list()[0] + '>\t'+str(index-1)+'\n')