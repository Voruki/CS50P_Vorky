from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add header image at specified position and set font for title
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")  # Title
        self.ln(20)  # Add line break after title

def main():
    # Get name input from user and generate shirtificate
    name = input("Name: ")
    generate_shirtificate(name)

def generate_shirtificate(name):
    # Create PDF object, add page, set font and text color
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)  # Set text color to white
    # Add text with name and purpose, align center
    pdf.cell(0, 213, f"{name} took CS50", align="C")
    # Output PDF file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

