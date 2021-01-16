from datetime import datetime
from core.settings import common


# should be install xhtml2pdf and docxtpl

def render_to_pdf(template, name, data=None):
    from django.template.loader import get_template
    from io import BytesIO
    from xhtml2pdf import pisa

    if data is None:
        data = {}
    data.update({
        'font_path': f'{common.STATIC_PATH}/DejaVuSansCondensed.ttf'
    })
    template = get_template(f'{template}.html')
    html = template.render(data)
    destination = f'{common.MEDIA_ROOT}/exports/'
    filename = f'{name.replace(" ", "-")}-{str(datetime.now().timestamp()).replace(".", "")}'
    file = open(f'{destination}{filename}.pdf', 'w+b')
    pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=file, encoding='UTF-8')
    file.close()
    return f'{common.MEDIA_URL}exports/{filename}.pdf'


def render_docx(template, name, data):
    from docxtpl import DocxTemplate

    docx_template = DocxTemplate(f'{common.STATIC_PATH}/{template}.docx')
    docx_template.render(data)
    docx_template.save(f'{name}.docx')
