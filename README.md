# 📚 Book Recommender System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://book-recommender-bysanskar.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)

A Machine Learning-powered web application that suggests books based on user interests. This system utilizes both **Popularity-Based** and **Collaborative Filtering** techniques to provide accurate recommendations.

**🌟 Live Demo:** [Click here to view the App](https://book-recommender-bysanskar.streamlit.app/)

---

## 📖 Overview

Finding the next book to read can be overwhelming given the millions of titles available. This project analyzes a massive dataset of books, users, and ratings to build an intelligent recommendation engine.

The system offers two modes of recommendation:
1.  **Top 50 Books:** A curated list of the highest-rated books (Popularity Based).
2.  **Personalized Recommendations:** Input a book you like, and the system suggests similar books based on user voting patterns (Collaborative Filtering).

---

## 🛠️ Tech Stack

* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Cosine Similarity)
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Community Cloud

---

## 📊 Dataset & Preprocessing

The project uses the **Book-Crossing Dataset**, consisting of three files:
* `Books.csv`: ISBN, Title, Author, Year, Publisher, Image URLs.
* `Users.csv`: User ID, Location, Age.
* `Ratings.csv`: User ID, ISBN, Book Rating.

### Data Analysis Steps (from Jupyter Notebook):
1.  **Cleaning:** Handled missing values, incorrect data types (Year of Publication), and duplicate entries.
2.  **EDA:** Visualized user age distribution, top authors, top publishers, and rating statistics.
3.  **Filtering:**
    * To ensure statistical significance, only users with **>200 ratings** were considered "experienced users."
    * Only books with **>50 ratings** were kept to remove obscure titles.

---

## 🧠 Algorithms Used

### 1. Popularity Based Filtering
This approach calculates the average rating of books but weighs it against the total number of ratings to avoid bias (e.g., a book with one 5-star rating vs. a book with one thousand 4.8-star ratings).
* **Criteria:** Books with at least 250 votes.
* **Result:** The top 50 books sorted by average rating.

### 2. Collaborative Filtering (Item-Based)
This method looks for similarities between items (books) based on user ratings.
* **Matrix Construction:** Created a Pivot Table where:
    * Index = Book Title
    * Columns = User IDs
    * Values = Ratings
* **Similarity Metric:** Used **Cosine Similarity** to calculate the distance between vectors (books).
* **Outcome:** When a user searches for a book, the model finds the 5 nearest vectors (most similar books) in the multi-dimensional space.

---

## 🚀 How to Run Locally

If you want to run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sanskarr16/book-recommender.git](https://github.com/sanskarr16/book-recommender.git)
    cd book-recommender
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit App:**
    ```bash
    streamlit run stremlit_app.py
    ```

4.  Open your browser and go to `http://localhost:8501`.

---

## 📂 Project Structure
