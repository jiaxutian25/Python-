import json
from py2neo import Graph, Node, Relationship

# 连接到 Neo4j 数据库
graph = Graph("http://localhost:7474", auth=("neo4j", "your_password"), name='neo4j')

# 清空数据库
graph.delete_all()

# 从 JSON 文件加载数据
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 创建节点
nodes = {}
for layer in ["nodes_layer1", "nodes_layer2", "nodes_layer3", "nodes_layer4", "nodes_layer5", "nodes_layer6",
              "nodes_layer7", "nodes_layer8"]:
    for node in data.get(layer, []):
        n = Node(node['type'], name=node['label'])
        nodes[node['id']] = n
        graph.create(n)

# 创建关系
for layer in ["edges_layer1_to_layer2", "edges_layer2_to_layer3", "edges_layer3_to_layer4", "edges_layer4_to_layer5",
              "edges_layer5_to_layer6", "edges_layer6_to_layer7", "edges_layer7_to_layer8"]:
    for edge in data.get(layer, []):
        rel = Relationship(nodes[edge['source']], edge['relation'], nodes[edge['target']])
        graph.create(rel)

print("数据已成功导入 Neo4j!")
