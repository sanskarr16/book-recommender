import streamlit as st
import pickle
import numpy as np
import bz2


# 1. Load Compressed Data
@st.cache_data
def load_data():
    try:
        with bz2.BZ2File('popular.pbz2', 'rb') as f:
            popular_df = pickle.load(f)
        with bz2.BZ2File('pvt.pbz2', 'rb') as f:
            pvt = pickle.load(f)
        with bz2.BZ2File('books.pbz2', 'rb') as f:
            books = pickle.load(f)
        with bz2.BZ2File('Similarity_score.pbz2', 'rb') as f:
            similarity_score = pickle.load(f)
        return popular_df, pvt, books, similarity_score
    except FileNotFoundError:
        st.error("Error: .pbz2 files not found. Please make sure you generated them.")
        return None, None, None, None


popular_df, pvt, books, similarity_score = load_data()

# Stop if data didn't load
if popular_df is None:
    st.stop()

# 2. Sidebar
st.sidebar.title("Book Recommender")
page = st.sidebar.radio("Go to", ["Home", "Recommend"])

# 3. Home Page
if page == "Home":
    st.title("Top 50 Books")
    # Grid layout
    book_names = list(popular_df['Book-Title'].values)
    authors = list(popular_df['Book-Author'].values)
    images = list(popular_df['Image-URL-M'].values)
    votes = list(popular_df['num_ratings'].values)
    ratings = list(popular_df['avg_rating'].values)

    cols = st.columns(4)  # 4 columns
    for i in range(len(book_names)):
        with cols[i % 4]:
            st.image(images[i], use_column_width=True)
            st.caption(f"**{book_names[i]}**")
            st.text(f"{authors[i]}")
            st.text(f"Rating: {round(ratings[i], 2)}")

# 4. Recommend Page
if page == "Recommend":
    st.title("Recommend Books")
    book_list = pvt.index.values
    selected_book = st.selectbox("Select a book", book_list)

    if st.button('Recommend'):
        try:
            index = np.where(pvt.index == selected_book)[0][0]
            similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

            st.write(f"Books similar to **{selected_book}**:")
            rec_cols = st.columns(5)

            for i, col in zip(similar_items, rec_cols):
                temp_df = books[books['Book-Title'] == pvt.index[i[0]]]
                with col:
                    st.image(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0])
                    st.caption(temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0])
        except Exception as e:
            st.error(f"Error: {e}")