from fpdf import FPDF

def main():
    name = input("Name: ").strip()
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(False)
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)
    pdf.image("shirtificate.png", x=50, w=110)
    pdf.set_font("Arial", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(120)
    pdf.cell(0, 10, name, align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
