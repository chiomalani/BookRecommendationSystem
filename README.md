# Book Recommendation and Engagement System

## Overview

This project is a comprehensive **Book Recommendation and Engagement System** designed to recommend books to students based on their grade level and Lexile score. It includes features for parent engagement by allowing them to log student progress and award badges for reading achievements.

The project utilizes various tools and frameworks, including:
- **Flask** for the main web application (`app.py`).
- **Streamlit** for the booking engine interface.
- **DBeaver** for managing an SQLite3 database.
- **Jupyter Notebook** for data analysis and model evaluation.

---

## Key Features
1. **Book Recommendations**: Students receive personalized book recommendations based on their grade level and Lexile scores.
2. **Parent Engagement**: Parents can log their child's reading activity and award badges when goals are met.
3. **Web Application**: The app is built using Flask to serve recommendations via an API and Streamlit for the booking engine interface.
4. **Data Analysis**: A Jupyter Notebook is used to evaluate and analyze the recommendation model’s performance.
5. **Database**: The project uses an SQLite3 database, managed through DBeaver, to store book data and track student progress.

---

## Tools and Technologies

- **Flask**: A lightweight web framework used to create the API and serve book recommendations via HTTP requests. The `app.py` file handles the core application logic and API routes.

- **Streamlit**: A powerful tool used for creating the booking engine, providing a user-friendly interface for generating book recommendations and logging student progress.

- **SQLite3 Database**: An embedded SQL database used to store book data and student reading logs. It’s managed with DBeaver, a database management tool that provides a GUI for interacting with SQLite.

- **DBeaver**: A database management tool used to create, manage, and query the SQLite3 database for storing book and student data.

- **Jupyter Notebook**: A notebook environment used for data analysis and model evaluation. The notebook provides a step-by-step breakdown of the recommendation engine's performance, based on student reading data.

---

## Project Structure

```plaintext
BookRecommendationSystem/
│
├── README.md                       # Project overview and instructions
├── LICENSE                         # License file (optional)
├── app.py                          # Flask web application
├── book_recommendation_engine.py   # Core recommendation engine code
├── requirements.txt                # List of dependencies
├── data/                           # Folder for storing datasets or database files
│   └── database.db                 # SQLite3 database file (managed with DBeaver)
└── notebooks/                      # Folder for storing Jupyter notebooks
    └── analysis.ipynb              # Jupyter notebook for model evaluation and data analysis

---

## Installation and Setup

### Prerequisites
Before running this project, ensure you have the following installed on your machine:
- **Python 3.8+**
- **pip** (Python's package installer)
- **Anaconda** (recommended for managing the environment)
- **DBeaver** (for SQLite database management)
- **Streamlit** (for the booking engine interface)

### Step 1: Clone the Repository
First, clone the repository from GitHub and navigate to the project folder:
```bash
git clone https://github.com/chiomalani/BookRecommendationSystem.git
cd BookRecommendationSystem


### Step 2: Set Up Virtual Environment (Optional but recommended)
It's recommended to create and activate a virtual environment to manage dependencies:
conda create --name book_rec_env python=3.8
conda activate book_rec_env


### Step 3: Install Dependencies
Install the required dependencies listed in the requirements.txt file:
pip install -r requirements.txt


### Step 4: Set Up the SQLite Database
Use DBeaver to manage the SQLite3 database. The database.db file stores book information, Lexile levels, and student reading logs. Ensure that the database file is located in the data/ directory.


### Step 5: Running the Flask Application
To run the Flask web server and expose the API, use the following command:
python app.py
The application will be accessible at http://127.0.0.1:5000/.


### Step 6: Running the Streamlit Booking Engine
Launch the Streamlit interface, which allows users to generate book recommendations:
streamlit run book_recommendation_engine.py
The Streamlit interface will be accessible via your local server.

---

## Usage

### Flask Web Application (`app.py`)
The Flask app exposes an API that takes the student’s grade level and Lexile score as inputs and returns book recommendations.

**Example API call:**
```bash
GET /recommend?grade_level=5&lexile_score=700


### Streamlit Booking Engine (book_recommendation_engine.py)
The Streamlit app provides a user-friendly interface where students or parents can input grade level, Lexile score, and receive book recommendations.

### Database Management (Using DBeaver)
**DBeaver** is used to manage the database.db SQLite database, which stores all the book data, Lexile levels, and student logs.

### Jupyter Notebook (notebooks/analysis.ipynb)
The Jupyter notebook contains all the code for analyzing the book recommendation engine’s performance, along with evaluating how effective the recommendations are for different grade levels and Lexile scores.

---

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch
3. Commit Changes
   git commit -m 'Add some feature'
4. Push to the Branch   
   git push origin feature-branch
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Contact Information

If you have any questions or need further assistance, feel free to contact the project maintainer at [chiomajessicaa@gmail.com](mailto:chiomajessicaa@gmail.com).


