from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple

class VentasReport():
   
    def run(self):
        query = "SELECT * FROM sucursal "
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        
        #print(rows)

        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        resultado = [nt_result(*row) for row in rows]
        #print(resultado)
       
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        p = canvas.Canvas(response)
        initY = 400
        for res in resultado:
            initY = initY - 10
            print(res)
            print(res.id)
            p.drawString(1, initY, res.id)
            p.drawString(400, initY, res.nombre)

        p.showPage()
        p.save()
        return response
       
        



