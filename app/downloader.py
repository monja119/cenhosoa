# table
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image

from app.models import *


def download(model, indication, data_id):
    data = model.objects.get(id=data_id)
    # name of the data
    name = '{}_{}.pdf'.format(indication, data.id)
    # ____________BUILDING PDF FILE___________
    doc = SimpleDocTemplate(name, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    match indication:
        case 'fandaharana':
            content = data.content

            data = [
                ['', content, ''],
                ]

            table = Table(data, 120, 20)

            elements.append(table)

    # building doc
    doc.build(elements)

    return name
