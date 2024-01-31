from weasyprint import HTML, CSS

html = HTML("output.html")
css = CSS(filename="styles/style_report.css")
html.write_pdf("report.pdf", stylesheets=[css])
