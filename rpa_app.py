import streamlit as st
from modules.rpa import scraper, desktop_bot, ocr_engine
import os

# Set page configuration FIRST — must be before any other Streamlit calls
st.set_page_config(page_title="PyAutomate RPA Panel", layout="centered")

# Streamlit content starts here
st.title("PyAutomate AI - RPA Control Panel")
st.markdown("Run automation tasks directly from this interface.")


'''Sidebar dropdown for showcasing future features:
- Lets the user explore what's coming in the roadmap
- Displays a description when a feature is selected'''

# Sidebar: Future Features
st.sidebar.title("Future Features")
future_features = st.sidebar.selectbox(
    "Explore what's coming next:",
    [
        "AI Decision Making (Gemini Integration)",
        "PDF and Excel Data Extraction",
        "Workflow Builder",
        "Cloud Deployment",
        "Dashboard and Reporting",
        "Slack/Email Notifications"
    ]
)

st.sidebar.info(f"Selected: {future_features}")

'''Main Section: Book Scraper
- Button to start web scraping from books.toscrape.com
- Saves the data to a CSV
- Shows a download button so user can get the file directly'''

# Section: Book Scraper
if st.button("Run Book Scraper"):
    data = scraper.scrape_books()
    scraper.save_to_csv(data)
    st.success(f"Scraped and saved {len(data)} books to books.csv")

    with open("books.csv", "rb") as file:
        st.download_button(
            label="Download books.csv",
            data=file,
            file_name="books.csv",
            mime="text/csv"
        )

# Section: Desktop Automation
if st.button("Run Desktop Automation"):
    desktop_bot.open_application("notepad.exe")
    desktop_bot.type_text("Automated by PyAutomate AI")
    st.success("Notepad opened and text typed")

# Section: OCR Engine
st.markdown("### Upload Image for OCR")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image_path = "temp_uploaded_image.png"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    text = ocr_engine.extract_text_from_image(image_path)
    st.text_area("OCR Extracted Text", text, height=200)
