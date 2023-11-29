import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path
from PIL import Image



# --- PATH SETTINGS ---
current_dir =  Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
cv_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profilepic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Saoirse Burke"
NAME = "Saoirse Burke"
DESCRIPTION = "Business Analytics Graduate from Cork looking for new opportunities"
EMAIL = "saoirse_burke@hotmail.com"
LINKEDIN = "https://www.linkedin.com/in/saoirse-burke/"
SOCIAL_MEDIA = {
    ".": ".",
    ".": ".",
    ".": ".",
    ".": ".",
}

st.set_page_config(page_title=PAGE_TITLE, layout="wide")

# --- LOAD CSS, PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(cv_file, "+rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=cv_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️ Email", EMAIL)
    st.write("🤝 Connect with me on Linkedin!", LINKEDIN)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


 # --- EDUCATION ---
    st.write("#")
    st.subheader("EDUCATION")
    st.write(
        """
        - ► Work in Wind 2023: Green Tech Skillnet - September 2023 - October 2023
        - ► MSc in Business Analytics: University of Limerick First Class Honours (3.52/4 QCA) - September 2022 – August 2023
        - ► Bachelor of Commerce: University College Cork – First Class Honours (1.1) – September 2017 – May 2021
        - ► Leaving Certificate: Mount Mercy College, Cork – 478/625 points – September 2011 – May 2017
        """
        )

    # --- SKILLS ---
    st.write("#")
    st.subheader("SKILLS")
    st.write(
        """
        - ► Programming: Python (matplotlib, networkx, numpy, pandas, pgmpy, scikit_learn, scipy, seaborn, streamlit), SQL (MySQL), R 
        - ► Data Visualisation: Excel, Tableau
        - ► Office 365: PowerPoint, Excel, Word, Outlook, SharePoint
        - ► Analytical, presentation, organisation and communication skills
        """
        )
    
    # --- WORK HISTORY ---
    st.write("#")
    st.subheader("WORK HISTORY")
    st.write("---")

    # --- JOB 1 ---
    st.write("**Munster Technological University - MTU Cork School of Music, Union Quay, Ballintemple, Co. Cork – Exam Invigilator**")
    st.write("**November 2023 - Present**")
    st.write(
        """
        - ► Key Duties include: Distribution of examination material
        - ► Recording attendance
        - ► Ensuring that all examination material is collected, recorded on the attendance list and returned to the Examinations Office
        """)

    # --- JOB 2 ---
    st.write("**TK Maxx - The Cornmarket, 39 Cornmarket St, Centre, Co. Cork – Sales Associate**")
    st.write("**September 2021 - July 2022**")
    st.write(
        """
        - ► Maintained the shop floor and fitting rooms to a high standard
        - ► Assisted customers with their queries
        - ► Conducted point-of-sale transacIons as cashier
        """)
    
    # --- JOB 3 ---
    st.write("**JD Sports - Mahon Point Shopping Centre, Mahon Point, Co. Cork – Sales Assistant**")
    st.write("**June 2021 - September 2021**")
    st.write(
        """
        - ► Maintained the shop floor and performed full clothing standards at close of day
        - ► Other responsibilities included answering customer queries, performing price checks, updating prices, and preparing sale stock
        """)
    
    # --- JOB 4 ---
    st.write("**Accenture - 1 Grand Canal Square, Grand Canal Dock, Co. Dublin (Remote Working) – Technology Consulting Intern**")
    st.write("**March 2020 - August 2020**")
    st.write(
        """
        - ► Performed analysis of skills and specialisations of employees
        - ► Exported detailed reports from HR insights Dashboard to Excel for analysis
        - ► Presented HR findings to business leads
        - ► Briefly worked in Resources in CommunicaIons role for a leading utility service provider
        """)
    
    # --- JOB 5 ---
    st.write("**Student Centre - Áras Na Mac Léinn, UCC, College Road, Co. Cork – Student Staff**")
    st.write("**August 2019 - October 2019**")
    st.write("""
            - ► Conducted transactions via point-of-sale system
            - ► Performed stock taking
            - ► Liaised with other retail departments
             """)
    
