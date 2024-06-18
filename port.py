import streamlit as st
from PIL import Image
#from streamlit_extras.app_logo import add_logo
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Portfolio",
    page_icon=":rocket:",
    #layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a portfolio webite!"
    }
)
logo_url = "Pic.png"
st.sidebar.image(logo_url)

with st.sidebar:
    selected = st.sidebar.option_menu("", ["Introduction", "Skills", "Projects", "Achievements", "Get in Touch"], 
        icons=[], menu_icon="cast", default_index=0)
    selected


if selected == "Introduction":
    st.title("Introduction")
    st.text("")
    st.image("Rectangle 88.png")
    #st.markdown("""---""")
    st.text("")
    st.write("Hey!")


    col1, col2 = st.columns(2)

    with col1:
        st.title("I'm Damini Sharma")
        st.write('UI | UX DESIGNER  :sunglasses:')
        st.text("")

        st.write("I'm searching for some worthwhile experience right now to hone my design abilities. Like to work with and assist communities, I also have a collaborative mentality. I'll use every effort to accomplish my goals. Learning new skills is what I'm most interested in doing, especially UI/UX Design.") 
        st.text("")
    with col2:
        st.image("Group 71.png")

    st.text("")

    def generate_pdf_content():
    # Replace this function with your code that generates the PDF content.
    # You can use any library (e.g., ReportLab, FPDF) to generate the PDF.
    # For the sake of this example, we'll just create a simple PDF content.
                content = "Download My Resume."
                return content
    def main():

    # Create a download button
                    pdf_content = generate_pdf_content()

# Assuming you have a PDF file named "example.pdf"
    file_path = "Damini-Resume.pdf"

# Read the PDF file and get its content as bytes
    with open(file_path, "rb") as file:
                pdf_content = file.read()

# Provide the file name and content to st.file_download()
    st.download_button("Download Resume", pdf_content, mime="application/pdf")

#SKILL
if selected == "Skills":
    st.title("Skills")
    st.text("")
    st.image("Rectangle 88.png")
    st.text("")
    st.text("")
    col1, col2 = st.columns(2)

    with col1:
        st.image("lappy.png")

    with col2:
        st.text("")
        st.text("")
        st.text("")
        st.markdown(
        """
        - Tools : 
        """
          )
        st.write("Figma  |  CANVA  |  InDesign  ")

        st.markdown(
        """
        - Languages :
        """
        )
        st.write("HTML |  CSS  |  PYTHON(Streamlit)  ")

        st.markdown(
        """
        - Soft Skills : 
        """
          )
        st.write("Communication  |  Problem Solving  |  Creative Thinking  |  Leadership")

#Projects
if selected == "Projects":
    st.title("Projects")
    st.text("")
    st.image("Rectangle 88.png")
    st.text("")

#Project 1
    st.header("Reczee")
    col1, col2 = st.columns(2)

    with col1:
        st.image("Illustration - Frame.jpg")

        st.markdown(
        """
        -  All stakeholders in the hiring process, including talent acquisition, interview panels, and organization administrators, benefit from the end-to-end recruiting platform RECZEE.
        -  Led a design project in reczee to meet the goals of the project through my designs.
        -  Successfully managed multiple projects simultaneously.meeting tight deadlines.
        -  Created innovative designs that effectively communicated the brand’s message to target audiences.
        """
          )
    with col2:
        st.image("Frame 9.jpg")
        st.image("ppt.jpg")


#Project 2
    st.markdown("""---""")
    st.header("OrFresh")
    col1, col2 = st.columns(2)
    with col1:
        st.image("OrF (1).jpg")
        st.image("OrF (2).jpg")

    with col2:
        st.image("OrF (3).jpg")

        st.markdown(
        """
        -  All stakeholders in the hiring process, including talent acquisition, interview panels, and organization administrators, benefit from the end-to-end recruiting platform RECZEE.
        -  Led a design project in reczee to meet the goals of the project through my designs.
        -  Successfully managed multiple projects simultaneously.meeting tight deadlines.
        -  Created innovative designs that effectively communicated the brand’s message to target audiences.
        """
          )
    
#Project 3
    st.markdown("""---""")
    st.header("Event Maker")
    col1, col2 = st.columns(2)

    with col1:
        st.image("Eve1 (3).jpg")

        st.markdown(
        """
        -  All stakeholders in the hiring process, including talent acquisition, interview panels, and organization administrators, benefit from the end-to-end recruiting platform RECZEE.
        -  Led a design project in reczee to meet the goals of the project through my designs.
        -  Successfully managed multiple projects simultaneously.meeting tight deadlines.
        -  Created innovative designs that effectively communicated the brand’s message to target audiences.
        """
          )
    with col2:
        st.image("Eve1 (1).jpg")
        st.image("Eve1 (2).jpg")


#Achievements
if selected == "Achievements":
    st.title("Achievements")
    st.text("")
    st.image("Rectangle 88.png")
    st.text("")
    st.text("")

    st.markdown(
        """
        -  Certified the GOOGLE UX Design Certificate through Coursera in 2022. 
        """
          )
    st.write("My comprehension of Google's research methodology and search engine design process has greatly improved thanks to the Google UX Design Certificate. How original and creative thinking should be applied to tackle the issue. ")

    st.markdown(
        """
        -  Certified the UI/UX Design Certificate through Coursera in 2020. 
        """
          )
    st.write("The greatest course is the one offered by California University and Coursera. My comprehension of the design process, starting from the foundations and extending to the entire platform or application's development, has been much enhanced by the tutors.")

    st.markdown(
        """
        -  HTML/CSS Certified through Coursera in 2023 
        """
          )
    st.write("The best course is the one offered by Coursera. With their excellent examples that go beyond the fundamentals and show how the entire platform or application is being created and constructed, the tutors have really aided me in learning how the web is designed utilizing simple text-based html and CSS code.")


#Get in touch
if selected == "Get in Touch":
    st.title("Get in Touch")
    st.text("")
    st.image("Rectangle 88.png")
    st.text("")
    st.text("")

    col1, col2 = st.columns(2)

    with col1:
        st.image("emoji.png")

    with col2:
        st.markdown(
        """
        -  Email ID
        """
          )
        st.write("daminisharma9704@gmail.com")
        st.markdown(
        """
        -  Phone No.
        """
          )
        st.write("+91 9372347616")

        st.text("")
    
        st.markdown(
        """
        -  Follow me on :
        """
          )
        st.write("[LinkedIn](https://www.linkedin.com/in/daminisharma29/)")
        st.write("[Behance](https://www.behance.net/daminisharma2905)")
        st.write("[Instagram](https://www.instagram.com/_damini_designer/)")
    st.text("")
    
