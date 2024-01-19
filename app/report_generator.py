from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

some_data = [
    {'name': 'John Doe', 'age': 42},
    {'name': 'Jane Doe', 'age': 43},
    {'name': 'Santa Claus', 'age': 1000}
]

# Load templates from the templates directory
env = Environment(loader=FileSystemLoader('templates'))

# Load an HTML template
template = env.get_template('report_template.html')

# Fill the template with data
filled_template = template.render(data=some_data)

# Convert the filled template to HTML
html = HTML(string=filled_template)

# Load a CSS file
css = CSS(filename='styles.css')

# Convert the HTML to PDF
html.write_pdf('output.pdf', stylesheets=[css])
