import json
import re

def replace_placeholders(template, data):
    placeholders = re.findall(r"{{(.*?)}}", template)
    for placeholder in placeholders:
        value = data.get(placeholder, f"{{{{{placeholder}}}}}")
        template = template.replace(f"{{{{{placeholder}}}}}", value)
    return template

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('template.html', 'r') as template_file:
    template = template_file.read()

html = replace_placeholders(template, data)

with open('output.html', 'w') as output_file:
    output_file.write(html)

print("HTML generato con successo: output.html")
