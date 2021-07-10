from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('Arial', '', 16)
pdf.cell(60, 20, 'Curso de Python', 0, 1, 'L')

pdf.set_font('Times', 'I', 12)
pdf.cell(190, 20, 'Curso de SQL', 1, 1, 'C', False)
#pdf.cell(190, 20, 'Curso de Python', 1, 1, 'C', True)

pdf.set_font('Times', 'B', 12)
pdf.cell(0, 20, 'Curso de HTML5', 1, 1, 'R', False)

pdf.output('exemplo.pdf', 'F')
