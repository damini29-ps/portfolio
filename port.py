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
    selected = option_menu("", ["Introduction", "Skills", "Projects", "Achievements", "Get in Touch"], 
        icons=[], menu_icon="cast", default_index=0)
    selected


if selected == "Introduction":
    st.title("Introduction")
    st.text("")
    st.image("Rectangle 88.png")
    #st.markdown("""---""")
    st.text("")
    st.title("Hey!")


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
    file_path = "UI-Resume.pdf"

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
        st.write("FIGMA  |  CANVA   |   ADOBE XD  ")

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
    st.header("Paw Paradise")
    col1, col2 = st.columns(2)
    with col1:
        st.image("Paw_1.webp")
        st.image("Paw_2.webp")

    with col2:
        st.image("Paw_3.webp")

        st.markdown(
        """
        -  As the UI/UX designer for Paw Paradise, a veterinary services platform focused on providing compassionate care for pets, I was responsible for crafting a user-friendly, emotionally engaging digital experience tailored for pet owners seeking reliable veterinary assistance. 
        -  Conducted user research through surveys and interviews with pet owners to understand their needs, expectations, and pain points related to online vet consultations and appointment bookings. 
        -  Designed a clean, pet-friendly interface using soft, calming colors and playful design elements to create a comforting experience. Incorporated icons and illustrations of pets for added emotional connection.
        -  Designed a seamless booking system that allowed users to easily schedule appointments with vets, access pet care services, and receive timely reminders.
        -  [Paw Paradise Website Project](https://www.figma.com/design/sVXSLIGWNolLYqpgED73gy/Projects?node-id=102-8&p=f&t=2gELSzvVL8AXCQA0-0)
        """
          ) 

    
#Project 2
    st.markdown("""---""")
    st.header("Reczee")
    col1, col2 = st.columns(2)

    with col1:
        st.image("Realme 10.png")

        st.markdown(
        """
        -  All stakeholders in the hiring process, including talent acquisition, interview panels, and organization administrators, benefit from the end-to-end recruiting platform RECZEE.
        -  Led a design project in reczee to meet the goals of the project through my designs.
        -  Successfully managed multiple projects simultaneously.meeting tight deadlines.
        -  Created innovative designs that effectively communicated the brand’s message to target audiences.
        -  [Reczee Website Project](/)
        """
          )

    with col2:
        st.image("Desktop - 7.jpg")
        st.image("Frame 38.jpg")
        
        st.image("Group 177.png")


#Project 3
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
        -  OrFresh is a website that assists people who are diet-conscious and require something green and leafy to maintain a healthy diet. 
        -  The platform provides clean and user-friendly visuals to keep users interested with the site. 
        -  Trust OrFresh's process and services. I designed this website with simplicity in mind. 
        -  Transitions are designed to keep the user engaged as a visually appealing component of the design process.
        -  [OrFresh Website Project](https://www.figma.com/proto/VzzHlGV01ofzAePG3cdTY3/Untitled?node-id=102-263&starting-point-node-id=102%3A263)
        """
          )
    
#Project 4
    st.markdown("""---""")
    st.header("Event Maker")
    col1, col2 = st.columns(2)

    with col1:
        st.image("Eve1 (3).jpg")

        st.markdown(
        """
        -  Event Maker is a website that offers complete party services and event management programs. 
        -  Event maker is created in such a manner that the visitor will not be bored while visiting our website, and the look and feel conveys everything about the party mode. 
        -  I've kept in mind that feel is more crucial for this site because it caters to the "All cool party planner guys vibe" crowd. 
        -  [Event Maker Website Project](https://www.figma.com/proto/spfWzWreCGYog1aKo01qGb/NewPortfoio?node-id=229-189&starting-point-node-id=229%3A189)
        """
          )

    with col2:
        st.image("Property 1.png")
        st.image("MacBook.png")



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
        -  Introduction to Social Media Marketing in 2024 
        """
          )
    st.write("The best course available on Coursera. Starting from the foundations and continuing through the development of the entire platform or application, the tutors greatly improved my understanding of the design process and making them visible to others, as well as the fundamental strategy of how to present the designs and your product and services to others via social media platforms. By their superb illustrations that transcend the basics and demonstrate the development and construction of the full platform or application.")


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
    
    
