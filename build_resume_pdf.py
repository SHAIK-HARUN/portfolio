import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Paths
source_img = r"C:\Users\User\.gemini\antigravity\brain\baf0e5a0-9ec9-4d43-9cba-099167254d6f\media__1791397984426.jpg"
assets_img_dir = r"d:\PORTFOLIO\assets\images"
assets_pdf_dir = r"d:\PORTFOLIO\assets\pdf"

os.makedirs(assets_img_dir, exist_ok=True)
os.makedirs(assets_pdf_dir, exist_ok=True)

target_resume_img = os.path.join(assets_img_dir, "resume.jpg")
target_pdf_file = os.path.join(assets_pdf_dir, "Shaik_Harun_Resume.pdf")

# 1. Save updated image
img = Image.open(source_img)
img.convert("RGB").save(target_resume_img, "JPEG", quality=95)

# 2. Build 1-Page ATS Vector PDF
doc = SimpleDocTemplate(
    target_pdf_file,
    pagesize=letter,
    leftMargin=0.35 * inch,
    rightMargin=0.35 * inch,
    topMargin=0.3 * inch,
    bottomMargin=0.3 * inch
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    'DocName',
    parent=styles['Heading1'],
    fontName='Times-Bold',
    fontSize=18,
    leading=20,
    alignment=1,
    textColor=colors.black,
    spaceAfter=2
)

contact_style = ParagraphStyle(
    'DocContact',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=8.8,
    leading=10.8,
    alignment=1,
    textColor=colors.black,
    spaceAfter=4
)

section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=10.5,
    leading=11.5,
    textColor=colors.black,
    spaceBefore=2,
    spaceAfter=1
)

body_style = ParagraphStyle(
    'DocBody',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=8.8,
    leading=10.6,
    textColor=colors.black,
    spaceAfter=1.5
)

bullet_style = ParagraphStyle(
    'DocBullet',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=8.6,
    leading=10.4,
    textColor=colors.black,
    leftIndent=10,
    firstLineIndent=-6,
    spaceAfter=1.5
)

story = []

def add_hr():
    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.black, spaceBefore=1, spaceAfter=2))

# Header
story.append(Paragraph("Shaik Harun", name_style))
story.append(Paragraph("Bangalore &nbsp;|&nbsp; shaikharun811@gmail.com &nbsp;|&nbsp; +91 9182257621 &nbsp;|&nbsp; <a href='https://shaikharun1.netlify.app' color='black'><u>shaikharun1.netlify.app</u></a> &nbsp;|&nbsp; <a href='https://linkedin.com/in/shaik-harun-developer/' color='black'><u>linkedin.com/in/shaik-harun-developer/</u></a><br/><a href='https://github.com/SHAIK-HARUN' color='black'><u>github.com/SHAIK-HARUN</u></a>", contact_style))

# Objective
story.append(Paragraph("Objective", section_title_style))
add_hr()
story.append(Paragraph("B.Tech Computer Science graduate with expertise in Python, Django, REST APIs, SQL, and Data Analysis (Pandas, NumPy, Matplotlib), experienced in building full-stack web applications and cloud-based solutions. Passionate about Software/Python Developer, Data Analytics, and solving real-world problems using DSA, OOP, and scalable system design.", body_style))

# Technical Skills
story.append(Paragraph("Technical Skills", section_title_style))
add_hr()
skills_text = """
<b>Programming Languages:</b> Python<br/>
<b>Frontend:</b> HTML5 | CSS3 | JavaScript | React<br/>
<b>Frameworks:</b> Django | Rest APIs<br/>
<b>Data Analysis:</b> Pandas | NumPy | Matplotlib | Excel<br/>
<b>Databases:</b> MySQL | SQLite<br/>
<b>Core Cs:</b> Data Structure Algorithms | OOPs | DBMS | System Design | CI / CD<br/>
<b>Cloud:</b> Cloud Computing (NPTEL Certified) | AWS(EC2)<br/>
<b>Emerging Tech:</b> AI / ML | Generative AI | RAG | LLMs | Prompt Engineering(Vibe Coding) | Antigravity | Git/GitHub
"""
story.append(Paragraph(skills_text, body_style))

# Training & Internships
story.append(Paragraph("Training & Internships", section_title_style))
add_hr()
story.append(Paragraph("<b>Python Full Stack Training</b>, <i>Pentagon Space</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; May 2024 – Dec 2024", body_style))
story.append(Paragraph("• Completed 300+ hour full-stack program in Python, Django, JavaScript, and REST APIs; used NumPy and Pandas to clean, analyze, and visualize 5+ datasets in Matplotlib and Excel.", bullet_style))

story.append(Paragraph("<b>AWS Cloud Intern</b>, <i>BrainOvision Solutions Pvt. Ltd</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jan 2023 – Apr 2023", body_style))
story.append(Paragraph("• Gained knowledge on the basics of cloud infrastructure, deployment, and resource management through hands-on practice.", bullet_style))

story.append(Paragraph("<b>J.P. Morgan Chase and Co. Software Engineering Virtual Internship via Forage</b>", body_style))
story.append(Paragraph("• Gained hands-on experience with stock price data, data visualization, including an open-source contribution.", bullet_style))

# Projects
story.append(Paragraph("Projects", section_title_style))
add_hr()
story.append(Paragraph("<b>CareConnect: Hospital Appointment Booking & Scheduling System</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href='https://bookingsys.netlify.app/' color='black'><u>bookingsys.netlify.app/</u></a>", body_style))
story.append(Paragraph("• Full-stack booking platform built with Python, Django (REST Framework), SQLite, and JavaScript.", bullet_style))
story.append(Paragraph("• Implemented 3+ REST API endpoints for appointment scheduling, supporting 50+ patients and 10+ providers.", bullet_style))
story.append(Paragraph("• Built a custom scheduling engine that cut manual conflicts by 90% via real-time availability checks.", bullet_style))

story.append(Paragraph("<b>PyPractice: Wasm-Powered Python Compiler</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href='https://practicecompiler.netlify.app/' color='black'><u>practicecompiler.netlify.app/</u></a>", body_style))
story.append(Paragraph("• Created a serverless, browser-based Python compiler and complexity analyzer using Prompt Engineering (Vibe Coding) at Antigravity.", bullet_style))
story.append(Paragraph("• Built client-side Python execution in WebAssembly (Pyodide) with real-time memory and Big-O spectrum tracking.", bullet_style))
story.append(Paragraph("• Designed a glassmorphic React workspace featuring dynamic console inputs and debounced auto-saving.", bullet_style))
story.append(Paragraph("&nbsp;&nbsp; <b>Skills:</b> React | Vite | WebAssembly | Python AST | Vibe Coding", bullet_style))

# Education
story.append(Paragraph("Education", section_title_style))
add_hr()
story.append(Paragraph("<b>Bachelor of Technology in Computer Science Engineering. | CGPA: 7.4</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Oct 2020 – May 2024", body_style))
story.append(Paragraph("Annamacharya Institute of Technology and Sciences, Kadapa", body_style))

story.append(Paragraph("<b>Intermediate. | CGPA: 8.6</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sept 2018 – Mar 2020", body_style))
story.append(Paragraph("Narayana Junior College", body_style))

story.append(Paragraph("<b>Secondary Education. | CGPA: 8.8</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jan 2017 – Feb 2018", body_style))
story.append(Paragraph("Sarada High School", body_style))

# Certificates
story.append(Paragraph("Certificates", section_title_style))
add_hr()
story.append(Paragraph("Python for Data Science, IBM Cognitive Class | Flipkart | HackerRank | Simplilearn | Cloud Computing", body_style))

# Continuous Learning & Soft Skills
story.append(Paragraph("CONTINUOUS LEARNING & SOFT SKILLS", section_title_style))
add_hr()
story.append(Paragraph("Consistently practicing Data Structures & Algorithms, exploring advanced Python concepts, and building communication skills, while applying leadership and time management skills gained through academic project work.", body_style))

doc.build(story)
print("1-Page ATS Vector PDF successfully generated!")
