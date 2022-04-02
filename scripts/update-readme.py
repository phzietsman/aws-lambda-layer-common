from asyncore import read
import json
import jinja2

variables = {}

with open("./versions.json", "r") as f:
    variables = json.load(f)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "README.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(variables)

with open("./README.md", "w") as f:
    f.write(outputText)