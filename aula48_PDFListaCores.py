from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

convidados = [['Ana Braga', '(11) 65878756666', 2, 'A'],
              ['Ana Br',    '(11) 65873984765', 1, 'B'],
              ['Ana Bra',   '(11) 65878764773', 4, 'C'],
              ['Ana Brag',  '(11) 65871452334', 3, 'B'],
              ['Ana Brvvb', '(11) 65877689286', 5, 'A']]

pdf.set_font('Arial', 'B', 16)

pdf.set_draw_color(255, 111, 105)
pdf.set_fill_color(255, 111, 105)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 20, 'Convidados Jantar Beneficente', 1, 1, 'C', 1)

pdf.set_draw_color(255, 204, 92)
pdf.set_fill_color(255, 204, 92)
pdf.set_text_color(0, 0, 0)
subtitulo = f'{"Nome":<35}     {"Telefone":<20}    {"Qtd":<3}    Setor'
pdf.set_font('courier', 'B', 12)
pdf.cell(0, 20, subtitulo, 0, 1)

pdf.set_font('courier', '', 12)

i=0
for convidado in convidados:
    nome = convidado[0]
    telefone = convidado[1]
    pessoas = convidado[2]
    setor = convidado[3]

    if i:
        pdf.set_text_color(200, 0, 0)
        i = 0
    else:
        pdf.set_text_color(50, 50, 50)
        i = 1

    pdf.cell(0, 10, f'{nome:<35}     {telefone:<20}     {pessoas:^3}     {setor:<1}', 0, 1)


pdf.output('convidados.pdf', 'F')