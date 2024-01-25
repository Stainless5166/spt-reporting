from weasyprint import HTML, CSS

html = HTML('output.html')
css = CSS(filename='style_report.css')
html.write_pdf('report.pdf', stylesheets=[css])
