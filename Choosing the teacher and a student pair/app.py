from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_certificate(request, student_id, teacher_id):
    # Get student and teacher objects
    student = Student.objects.get(id=student_id)
    teacher = Teacher.objects.get(id=teacher_id)

    # Create a PDF certificate
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Certificate for {student.name}")
    p.drawString(100, 700, f"Teacher: {teacher.name}")
    p.showPage()
    p.save()

    # Rewind the buffer and serve the PDF
    buffer.seek(0)
    response = FileResponse(buffer, as_attachment=True, filename=f'certificate_{student_id}.pdf')
    return response
