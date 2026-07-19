import streamlit as st
from dashboard.admin import show_admin
from dashboard.home import show_home
from dashboard.upload import show_upload
from dashboard.chatbot import show_chatbot
from dashboard.summarizer import show_summary
from dashboard.compare import show_compare
from dashboard.analytics import show_analytics
from dashboard.settings import show_settings

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

pages = {
    "🏠 Home": show_home,
    "📄 Upload": show_upload,
    "💬 Chat": show_chatbot,
    "📝 Summary": show_summary,
    "📚 Compare": show_compare,
    "📊 Analytics": show_analytics,
    "⚙ Settings": show_settings,
    "🛠 Admin":show_admin
}

choice = st.sidebar.radio(
    "Navigation",
    list(pages.keys())
)

pages[choice]()