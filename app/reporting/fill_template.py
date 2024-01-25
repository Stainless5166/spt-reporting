from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template_report.html")

data = {
    "title": "My Report Title",
    "content": "This is the content of my report",
    "users": [{
        "id": "12",
        "first_name": "John",
        "last_name": "Doe",
        "email": "",
        "phone": ""
    }]
}

output = template.render(data)

with open("output.html", "w") as f:
    f.write(output)
