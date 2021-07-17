from fpdf import FPDF

title = 'Vinte Mil Léguas Submarinas'

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)

        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)

        self.set_draw_color(230, 230, 0)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)

        self.set_line_width(1)

        self.cell(w, 9, title,1 ,1, 'C', 1)

        self.ln(10)

    def footer(self):
        self.set_y(-15)

        self.set_font('Arial', 'I', 8)

        self.set_text_color(128)

        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Arial', '', 12)

        self.set_fill_color(200, 220, 255)

        self.cell(0, 6, 'Capítulo %s : %s' % (num, label), 0, 1, 'L', 1)

        self.ln(4)

    def chapter_body(self, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')

        self.set_font('Times', '', 12)

        self.multi_cell(0, 5, txt)

        self.ln()

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)



pdf = PDF('P', 'mm', 'A4')

pdf.set_title(title)
pdf.set_author('Júlio Verne')

pdf.set_subject('Livro')
pdf.set_keywords('vinte submarinas julio verne')

pdf.print_chapter(1, 'Capítulo 1', '20k_c1.txt')
pdf.print_chapter(2, 'Capítulo 2', '20k_c2.txt')
pdf = PDF('P', 'mm', 'A4')
pdf.output('vinte_mil_leguas.pdf', 'F').encode('latin-1')































