from template_modifier import result
import pdfkit

pdfkit.from_string(input=result, css='templates/style.css', output_path='generated_pdfs/test.pdf')