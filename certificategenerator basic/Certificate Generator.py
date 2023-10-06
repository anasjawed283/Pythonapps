from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch

# Create a function to generate the certificate
def generate_certificate(pdf_filename, recipient_name, course_name, academic_year, organization_name, owner_signature_image, stamp_image):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Create a stylesheet for the certificate text
    certificate_style = ParagraphStyle(
        'CertificateStyle',
        fontSize=12,
        leading=15,
        alignment=1,  # Center alignment
    )

    # Create the content for the certificate
    story = []

    # Certificate border
    #story.append(Image("border.png", width=letter[0], height=letter[1]))

    # Add organization logo in the upper right corner
    org_logo = Image("logo.jpg", width=1.5 * inch, height=1.5 * inch)
    org_logo.hAlign = 'RIGHT'
    story.append(org_logo)

    # Add organization name in the upper middle
    story.append(Spacer(1, 0.25 * inch))
    org_name_text = f"<b>{organization_name}</b>"
    org_name_paragraph = Paragraph(org_name_text, certificate_style)
    org_name_paragraph.alignment = 1  # Center alignment
    story.append(org_name_paragraph)

    # Add recipient name, course name, and academic year
    story.append(Spacer(1, 0.5 * inch))
    certificate_text = f"This is to certify that user <b>{recipient_name}</b> has successfully completed the <b>{course_name}</b> course within the academic year <b>{academic_year}</b>."
    certificate_paragraph = Paragraph(certificate_text, certificate_style)
    story.append(certificate_paragraph)

    # Add owner's signature in the lower right corner
    owner_signature = Image(owner_signature_image, width=2 * inch, height=0.5 * inch)
    owner_signature.hAlign = 'RIGHT'
    story.append(owner_signature)

    # Add stamp in the lower left corner
    stamp = Image(stamp_image, width=1.5 * inch, height=1.5 * inch)
    stamp.hAlign = 'LEFT'
    story.append(stamp)

    doc.build(story)

# Specify the certificate details and file paths
recipient_name = "John Doe"
course_name = "Python Programming"
academic_year = "2023"
organization_name = "Your Organization"
owner_signature_image = "sign.png"
stamp_image = "stamp.png"
pdf_filename = "certificate.pdf"

# Generate and save the certificate
generate_certificate(pdf_filename, recipient_name, course_name, academic_year, organization_name, owner_signature_image, stamp_image)
print(f"Certificate saved as '{pdf_filename}'")
