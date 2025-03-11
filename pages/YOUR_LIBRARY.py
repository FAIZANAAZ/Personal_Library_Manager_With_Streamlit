import streamlit as st
from library_manager import display_books, display_statistics

# ✅ Ensure books list is initialized
if "books" not in st.session_state:
    st.session_state.books = []

st.title("Library Page 📚")
display_books()  # ✅ Books show karega

st.title("BOOK DATA 📊")
display_statistics()  # ✅ Statistics show karega
