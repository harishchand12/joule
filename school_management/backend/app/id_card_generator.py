from fpdf import FPDF

def generate_id_card(student_name, school_name, student_id):
    """Generates a printable PDF ID card for a student."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=school_name, ln=1, align="C")
    pdf.cell(200, 10, txt="Student ID Card", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Student Name: {student_name}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Student ID: {student_id}", ln=1, align="L")
    pdf.output(f"student_{student_id}_id_card.pdf")
