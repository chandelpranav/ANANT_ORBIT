from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import numpy as np

styles = getSampleStyleSheet()

doc = SimpleDocTemplate("Planet_Report.pdf")

story = []

story.append(Paragraph("<b>AI ENABLED EXOPLANET DETECTION REPORT</b>", styles["Title"]))
story.append(Paragraph("<br/>", styles["Normal"]))

# Target
story.append(Paragraph("<b>Target Star:</b> TOI-700", styles["Heading2"]))

# Prediction
story.append(Paragraph("<b>Prediction:</b> Planet Detected", styles["Heading2"]))

# Confidence
confidence = 98.6
story.append(Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["Heading2"]))

# Estimated Radius
planet_radius = 1.21
story.append(
    Paragraph(
        f"<b>Estimated Planet Radius:</b> {planet_radius:.2f} Earth Radius",
        styles["Heading2"],
    )
)

# Period
period = 18.12
story.append(
    Paragraph(
        f"<b>Orbital Period:</b> {period:.2f} Days",
        styles["Heading2"],
    )
)

# Transit Depth
depth = 0.0021
story.append(
    Paragraph(
        f"<b>Transit Depth:</b> {depth}",
        styles["Heading2"],
    )
)

story.append(Paragraph("<br/>", styles["Normal"]))

story.append(
    Paragraph(
        "<b>Workflow Used</b>",
        styles["Heading1"],
    )
)

workflow = """
NASA TESS Data<br/>
↓<br/>
Preprocessing<br/>
↓<br/>
Noise Removal<br/>
↓<br/>
Feature Extraction<br/>
↓<br/>
CNN Prediction<br/>
↓<br/>
Planet Detection
"""

story.append(Paragraph(workflow, styles["BodyText"]))

story.append(Paragraph("<br/>", styles["Normal"]))

story.append(
    Paragraph(
        "<b>Technologies Used</b>",
        styles["Heading1"],
    )
)

tech = """
• Python<br/>
• PyTorch<br/>
• Lightkurve<br/>
• NumPy<br/>
• Astropy<br/>
• Matplotlib
"""

story.append(Paragraph(tech, styles["BodyText"]))

doc.build(story)

print("=" * 40)
print("Planet_Report.pdf Generated Successfully")
print("=" * 40)