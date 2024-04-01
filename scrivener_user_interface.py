

# Import Libraries
import streamlit as st
import re
import os
from main.transcribe import TranscribeVideo
from main.transcribe_yt import TranscribeYtVideo
import secrets
from glob import glob


st.set_page_config(layout="wide")

# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)




# # Create a navigation bar
# st.markdown(
#     """
#     <div style="background-color: #f8f9fa; padding: 10px;">
#         <a style="padding: 5px 10px; margin-right: 20px; text-decoration: none; color: black;" href="#home">Home</a>
#         <a style="padding: 5px 10px; margin-right: 20px; text-decoration: none; color: black;" href="#about">About</a>
#         <a style="padding: 5px 10px; margin-right: 20px; text-decoration: none; color: black;" href="#contact">Contact</a>
#     </div>
#     """
#     , unsafe_allow_html=True
# )

# import streamlit as st

# # Define the navigation bar using HTML and CSS
# navigation_bar = """
# <style>
# .nav-link {
#     padding: 5px 10px;
#     margin-right: 20px;
#     text-decoration: none;
#     color: black;
#     transition: background-color 0.3s;
# }
# .nav-link:hover {
#     background-color: #f0f0f0;
# }
# </style>

# <div style="background-color: #f8f9fa; padding: 10px;">
#     <a class="nav-link" href="#home">Home</a>
#     <a class="nav-link" href="#about">About</a>
#     <a class="nav-link" href="#contact">Contact</a>
# </div>
# """

# # Display the navigation bar
# st.markdown(navigation_bar, unsafe_allow_html=True)







# # Add footer to UI
# footer="""<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: black;
# color: white;
# text-align: center;
# }
# </style>
# <div class="footer">

# <p>Contributors: darshan </p>
# </div>
# """
# st.markdown(footer,unsafe_allow_html=True)

# Download the uploaded video file
def save_file(file):
    with open(os.path.join(os.getcwd(), file.name), 'wb') as f:
        f.write(file.getbuffer())
    return 
import streamlit as st
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # Display the image with a smaller width
# st.image("media/logo/logo.gif", width=100, use_column_width=True)

# import streamlit as st
# st.write("<h1>Scriver - video transcript summary </h1>", unsafe_allow_html=True)

import streamlit as st

# Create a two-column layout
col1, col2 = st.columns([1, 4])

# Add the image in the left column
col1.image("media/logo/v1.png", use_column_width=True)

# Add the centered heading in the right column with small font size and custom color
# col2.markdown(
#     "<h2 style='text-align: center; color: #0f3054; font-size: 60px;'>Video Transcript Summarizer</h2>",
#     unsafe_allow_html=True
# )
# Add the centered heading in the right column with custom styling
col2.markdown(
    "<h2 style='text-align: center; color: #5755FE; font-size: 60px; text-decoration: underline;font-family: Aclonica;'>Video Transcript Summarizer</h2>",
    unsafe_allow_html=True
)

# import streamlit as st

# # Display the image on the left side
# st.image("media/logo/v1.png", width=100)

# # Center the heading vertically and horizontally
# st.title("Video Transcript Summarizer")




# # Use custom CSS for styling the heading
# st.markdown(
#     """
#     <style>
#     .centered-heading {
#         font-size: 36px;
#         text-align: center;
#         color: #1f2c56;  /* Custom color */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Display the centered heading
# st.markdown("<h1 class='centered-heading'>Video Transcript Summarizer</h1>", unsafe_allow_html=True)


# Create two columns
col1, col2 = st.columns([2, 5])

# Left column with text
with col1:
    # st.write("<br><br>", unsafe_allow_html=True )
    # st.write("<br><br>", unsafe_allow_html=True )
    st.write("<h3>AI notes & ai knowledge library for better learning</h2>", unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True )
    st.write("<h6> - Youtube summary,  Improve learning efficiency by 10x Get YouTube transcript and use AI to summarize YouTube videos in one click for free online with  YouTube summary tool..</h6>" , unsafe_allow_html=True )
    # st.write("Notegpt - youtube summary, article summary, smart tab, and notes with notegpt ai. improve learning efficiency by 10x")

# Right column with image
with col2:
    st.image("media/working_animation/scrivener_working.gif", width=1000, use_column_width=True)

#-----------------------------------------------------------------------------------------------------------------------------





# # Display Radio options
# input_format = st.radio('Choose your input format', ['Youtube Link', 'Upload a Video'])

import streamlit as st

# Display Radio options with larger size using Markdown
st.markdown("### Choose your input format")
input_format = st.radio('', ['Youtube Link', 'Upload a Video'])

if input_format == 'Youtube Link':
    st.markdown("<h1 style='font-size: 20px;'>Youtube Link</h1>", unsafe_allow_html=True)
elif input_format == 'Upload a Video':
    st.markdown("<h1 style='font-size: 20px;'>Upload a Video</h1>", unsafe_allow_html=True)



# If user provides a Youtube Link
if input_format=='Youtube Link':
    # Text input box 
    youtube_link = st.text_input('Enter Youtube Link')
    # Check if its a valid youtube link
    if re.findall('(www\.youtube\.com\/watch\?v=)',youtube_link):
        st.video(youtube_link)
        # Make a progress bar
        progress_bar = st.progress(0)
        # Decorative material
        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        progress_bar.progress(10)
        
        # Wait till we run the summarization
        with st.spinner(progress_lines+' . . .'):
            progress_bar.progress(25)
            # Call TranscribeYtVideo class 
            transcribe_video = TranscribeYtVideo(youtube_link)
            progress_bar.progress(40)
            # Get summary
            summary = transcribe_video.transcribe_yt_video()
            progress_bar.progress(80)
        # Complete progress bar to 100
        progress_bar.progress(100)
        # Display Summary
        st.header('Summary')
        st.write(summary)
        
    
    # If user inputs an invalid Youtube link
    elif youtube_link!='':
        st.error('Please enter a valid Youtube Link!')

# If user uploads a local video    
elif input_format=='Upload a Video':
    # Browse button for uploading .mp4 files
    file = st.file_uploader('Upload a video',type=['mp4'],accept_multiple_files=False)
    if file is not None:
        st.video(file)
        # Make a progress bar
        progress_bar = st.progress(0)
        progress_bar.progress(10)
        # Decorative material
        progress_lines = secrets.choice(['Hired Shakespeare to summarize your video', 'Taking advice from Charles Dickens to help you',
                                        'Shakespeare is completing the assignment', 'Do not worry, Mark Twain is on it',
                                        'Robert Frost is taking the right road to summarize your video'])
        # Wait till we run the summarization
        with st.spinner(progress_lines+' . . .'):
            progress_bar.progress(25)
            # Download the uploaded video file
            save_file(file)
            progress_bar.progress(40)
            # Call TranscribeVideo class 
            transcribe_video = TranscribeVideo()
            progress_bar.progress(60)
            # Get summary
            summary = transcribe_video.transcribe_video(os.path.join(os.getcwd(), file.name))
        # Complete progress bar to 100
        progress_bar.progress(100)
        # Display Summary
        st.header('Summary')
        st.write(summary)
    else:
        for name in glob('*.mp4'):
            os.remove(name)

    st.write("<br><br>", unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    import streamlit as st
st.markdown("<h6>Caution: AI-generated summaries may vary in accuracy and completeness.</h6>", unsafe_allow_html=True)






# Display text in h1 tag centered using HTML and CSS
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <h2>How to Summarize YouTube Videos?</h2>
    </div>
    """,
    unsafe_allow_html=True
)
# # Display text in h2 tag
# st.write("<h6>You can easily summarize the youtube videos use SCRIVENER with just 3 simple steps</h6>", unsafe_allow_html=True)

import streamlit as st

# Add padding and styling for the boxes
st.markdown(
    """
    <style>
    .highlight:hover {
        transform: scale(1.05);
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);
    }
    .highlight {
        padding: 20px;
        margin: 10px;
        border-radius: 10px;
        transition: all 0.3s ease;
        background-color: #f0f0f0;
        border: 2px solid #ccc;
        box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1);
        height: 200px; /* Adjust the height as needed */
    }
    .highlight:hover {
        background-color: #97E7E1;
        border-color: #d20062;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the three horizontal boxes
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        "<div class='highlight'><h3>Step 1: Get Video URL</h3><p>Get and copy video URL from YouTube.com.</p></div>",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        "<div class='highlight'><h3>Step 2: Paste Video URL</h3><p>Paste URL into the field above and hit 'Generate Summary' button.</p></div>",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        "<div class='highlight'><h3>Step 3: Generate Summary</h3><p>You can get YouTube transcripts and summary with AI.</p></div>",
        unsafe_allow_html=True,
    )
st.write("<br><br>", unsafe_allow_html=True)



#--------------------------------------------------------------------------------------------------------------------------
# Display text in h1 tag centered using HTML and CSS
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <h2>How to Summarize Videos stored In Devices?</h2>
    </div>
    """,
    unsafe_allow_html=True
)
# # Display text in h2 tag
# st.write("<h6>You can easily summarize the youtube videos use SCRIVENER with just 3 simple steps</h6>", unsafe_allow_html=True)

import streamlit as st

# Add padding and styling for the boxes
st.markdown(
    """
    <style>
    .highlight:hover {
        transform: scale(1.05);
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);
    }
    .highlight {
        padding: 20px;
        margin: 10px;
        border-radius: 10px;
        transition: all 0.3s ease;
        background-color: #f0f0f0;
        border: 2px solid #ccc;
        box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1);
        height: 200px; /* Adjust the height as needed */
    }
    .highlight:hover {
        background-color: #97E7E1;
        border-color: #d20062;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the three horizontal boxes
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        "<div class='highlight'><h3>Step 1: Get Video URL</h3><p>Get and copy video URL from YouTube.com.</p></div>",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        "<div class='highlight'><h3>Step 2: Upload Video </h3><p>Upload Video OR Drag and Drop into the field above and hit 'Generate Summary' button.</p></div>",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        "<div class='highlight'><h3>Step 3: Generate Summary</h3><p>You can get summary with AI.</p></div>",
        unsafe_allow_html=True,
    )
st.write("<br><br>", unsafe_allow_html=True)
#-------------------------------------------------------------------------------------------------------------------------------

# # Display Image
# st.image("media/working_animation/scrivener_working.gif")


# # Add a big header for FAQ section
# st.title("Frequently Asked Questions")

# faq_data = [
#     {
#         "question": "What is the YouTube video summarizer generator used for?",
#         "answer": "It is an online tool that can automatically generate text summaries of YouTube videos."
#     },
#     {
#         "question": "Is the quality of the generated summaries good?",
#         "answer": "It can capture the main ideas of the video, but will not perfectly transcribe the entire video word-for-word. The summary quality depends on the video content."
#     },
#     {
#         "question": "Do you need to pay to use this tool?",
#         "answer": "No payment is needed. This YouTube video summarizer tool is completely free to use."
#     },
#     {
#         "question": "What kinds of videos can I use it to summarize?",
#         "answer": "It works best for 10-60 minute long explanatory videos, such as educational or speech-style videos."
#     },
#     {
#         "question": "Does it support summarization for other languages?",
#         "answer": "Currently, it mainly supports English language videos. Support for other languages may be added in the future."
#     }
# ]

# # Custom CSS to change the expander box color when expanded
# expander_style = """
# <style>
# [data-testid="stSidebar"] .sidebar-content { background-color: #FF9800; }
# </style>
# """
# st.markdown(expander_style, unsafe_allow_html=True)

# with st.expander(f"{faq_data[0]['question']}"):
#     st.write(faq_data[0]['answer'])

# for faq in faq_data[1:]:
#     with st.expander(f"{faq['question']}"):
#         st.write(faq['answer'])

# import streamlit as st

# # Display text in h1 tag centered using HTML and CSS
# st.markdown(
#     """
#     <div style="display: flex; justify-content: center;">
#         <h2>How to Summarize YouTube Videos?</h2>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


#------------------------------------------------------------------------------------------------------------------------------
# import streamlit as st

# # Create two columns
# col1, col2 = st.columns([2, 5])

# # Left column with text
# with col1:
#     st.write("<br><br>", unsafe_allow_html=True )
#     st.write("<h3>AI notes & ai knowledge library for better learning</h2>", unsafe_allow_html=True)
#     st.write("<br><br>", unsafe_allow_html=True )
#     st.write("<h6>Notegpt - youtube summary, article summary, smart tab, and notes with notegpt ai. improve learning efficiency by 10x.</h6>" , unsafe_allow_html=True )
#     st.write("Notegpt - youtube summary, article summary, smart tab, and notes with notegpt ai. improve learning efficiency by 10x")

# # Right column with image
# with col2:
#     st.image("media/working_animation/scrivener_working.gif", width=1000, use_column_width=True)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Add a big header for the FAQ section
st.title("Frequently Asked Questions")

# Define the FAQ data
faq_data = [
    {
        "question": "What is the YouTube video summarizer generator used for?",
        "answer": "It is an online tool that can automatically generate text summaries of YouTube videos."
    },
    {
        "question": "Is the quality of the generated summaries good?",
        "answer": "It can capture the main ideas of the video, but will not perfectly transcribe the entire video word-for-word. The summary quality depends on the video content."
    },
    {
        "question": "Do you need to pay to use this tool?",
        "answer": "No payment is needed. This YouTube video summarizer tool is completely free to use."
    },
    {
        "question": "What kinds of videos can I use it to summarize?",
        "answer": "It works best for 10-60 minute long explanatory videos, such as educational or speech-style videos."
    },
    {
        "question": "Does it support summarization for other languages?",
        "answer": "Currently, it mainly supports English language videos. Support for other languages may be added in the future."
    }
]

# Create collapsible expanders for each question and answer pair
for pair in faq_data:
    with st.expander(pair["question"]):
        st.write(pair["answer"])



#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Display text in h1 tag centered using HTML and CSS
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <h2> Team member</h2>
    </div>
    """,
    unsafe_allow_html=True
)

#-----------------------------------------------------------------------------------------------------------------------------

# import streamlit as st

# # Define team member data
# team_members = [
#     {"name": "Darshan Chotalia", "image_path": "media/team/meme1.jpeg"},
#     {"name": "Amey Sonawane", "image_path": "media/team/meme2.jpeg"},
#     {"name": "Sahil Satam", "image_path": "media/team/meme3.jpeg"}
# ]

# # Create a horizontal layout
# col1, col2, col3 = st.columns(3)

# # Center the container horizontally
# st.markdown("<style> .team-container {display: flex; justify-content: center;} </style>", unsafe_allow_html=True)


# # Container for team members
# st.markdown("<div class='team-container'>", unsafe_allow_html=True)

# # Box 1
# with col1:
#     st.image(team_members[0]['image_path'], width=290)
#     st.write(team_members[0]['name'])

# # Box 2
# with col2:
#     st.image(team_members[1]['image_path'], width=290)
#     st.write(team_members[1]['name'])

# # Box 3
# with col3:
#     st.image(team_members[2]['image_path'], width=290)
#     st.write(team_members[2]['name'])

# # Close container
# st.markdown("</div>", unsafe_allow_html=True)



import streamlit as st

# Define team member data
team_members = [
    {"name": "Sahil Satam", "image_path": "media/team/meme3.png"},
    {"name": "Amey Sonawane", "image_path": "media/team/meme2.png"},
    {"name": "Darshan chotalia ", "image_path": "media/team/meme1.png"}
]

# Create a horizontal layout with 4 columns
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

# Center the container horizontally
st.markdown("<style> .team-container {display: flex; justify-content: center;} </style>", unsafe_allow_html=True)

# Container for team members
st.markdown("<div class='team-container'>", unsafe_allow_html=True)

# Box 1
with col1:
    # Write "TEAM MEMBER" with h2, bold, and underline styles
    st.markdown("<h2 style='text-decoration: underline;'>TEAM MEMBER</h2>", unsafe_allow_html=True)

# Box 2
with col2:
    st.image(team_members[0]['image_path'], width=290)
    st.write(team_members[0]['name'])

# Box 3
with col3:
    st.image(team_members[1]['image_path'], width=290)
    st.write(team_members[1]['name'])

# Box 4
with col4:
    st.image(team_members[2]['image_path'], width=290)
    st.write(team_members[2]['name'])

# Close container
st.markdown("</div>", unsafe_allow_html=True)


