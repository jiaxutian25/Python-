import json

# 文件路径
file_path = 'path/data.json'

# 读取 JSON 数据
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 修正所有层的 ID
new_id = 1
for key in sorted(data.keys()):
    for node in data[key]:
        node['id'] = new_id
        new_id += 1

with open(file_path, 'w', encoding='utf-8') as file:
    file.write("{\n")
    for key, value in data.items():
        file.write(f'"{key}": [\n')
        # 每个节点对象用两个空格缩进
        entries = ',\n'.join('  ' + json.dumps(node, ensure_ascii=False) for node in value)
        file.write(entries)
        file.write("\n]")
        if key != list(data.keys())[-1]:
            file.write(",\n")
    file.write("\n}\n")

print("OK")

