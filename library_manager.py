import streamlit as st
import pandas as pd



# Session state for storing books
if "books" not in st.session_state:
    st.session_state.books = []
def display_books():
    if st.session_state.books:
        df = pd.DataFrame(st.session_state.books)
        st.write(df)
    else:
        st.write("No books available yet.")
def add_book(title, author, publication, genre, read):
    if title and author and publication and genre:
        # Check if the book title already exists
        existing_books = [book["Title"].lower() for book in st.session_state.books]
        
        if title.lower() in existing_books:
            st.error("This book is already in your library!")
        else:
            new_book = {
                "Title": title,
                "Author": author,
                "Publication": publication,
                "Genre": genre,
                "Read": "Yes" if read else "No"
            }
            st.session_state.books.append(new_book)
            st.success("Book added successfully!")
    else:
        st.error("Please fill all the fields")

def display_statistics():
    if st.session_state.books:
        total_books = len(st.session_state.books)
        total_books_read = len(list(filter(lambda book: book["Read"] == "Yes", st.session_state.books)))

        # Calculate percentage (avoid division by zero)
        percentage_read = (total_books_read / total_books * 100) if total_books > 0 else 0

        st.write(f"Total Books: {total_books}")
        st.write(f"Total Books Read: {total_books_read} ({percentage_read:.2f}%)")
    else:
        st.write("No data available yet.")
   
def remove_book(title):
        book_to_remove = next((book for book in st.session_state.books if book["Title"] == title), None)
        
        if st.button("Remove Book"): 
            if book_to_remove:
                    st.session_state.books.remove(book_to_remove)
                    st.success("Book removed successfully!")
            else:
                    st.error("Book not found!")
                

def search_book(title=None,author=None):
       
       if title != None: 
        book_to_search = list(filter(lambda book: book["Title"].lower() == title, st.session_state.books))  
       elif author != None:
        book_to_search = list(filter(lambda book: book["Author"].lower() == author, st.session_state.books))

       if st.button("Search"):
         if book_to_search:
            st.write("Book found!")
            st.write(pd.DataFrame(book_to_search))  # ✅ Sirf milne wali book show karega
         else:
            st.error("Book not found!")
      
               

                

st.title("Welcome to your Personal Library Manager!")
st.write("This is a simple web application that allows you to manage your personal library.")

def logic():
    options = st.selectbox("What would you like to do?", [
        "CLICK HERE", "Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics", "Exit"
    ])

    if options == "Add a book":
        title = st.text_input("Enter the title of the book")
        author = st.text_input("Enter the author of the book")
        publication = st.text_input("Enter the publication of the book")
        genre = st.text_input("Enter the genre of the book")
        read = st.checkbox("Have you read the book?")

        if st.button("ADD BOOK"):
            add_book(title, author, publication, genre, read)
            

    elif options == "Display all books":
        display_books()
        
    elif options == "Remove a book":
        
        user_title = st.selectbox("Select a book to remove", [book["Title"] for book in st.session_state.books],)
        remove_book(user_title)
        
    elif options == "Search for a book":
        selection = st.selectbox("Search by", ["Title", "Author"])
        
        user_title = None
        user_author = None

        if selection == "Title":
            user_title = st.text_input("Enter the title of the book you want to search for")
        elif selection == "Author":
            user_author = st.text_input("Enter the author of the book you want to search for")

   
        if user_title:
            search_book(title=user_title, author=user_author)
            user_author = None
        elif user_author:
            search_book(title=user_title, author=user_author)
            user_title = None
        else:
            st.error("Please enter a value to search!")
    
    elif options == "Display statistics":
        display_statistics()            

       
       
       
    elif options == "Exit":
        st.write("Goodbye!")
        st.stop()
        
        
        
            

logic()

