import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

# Function to check and award badges based on books read
def check_and_award_badge(student_id):
    try:
        conn = sqlite3.connect("C:/APS Book Database/Apsbdb")
        cursor = conn.cursor()

        # Query to count books read by the student in the current week
        query = f"""
        SELECT COUNT(*) AS BooksRead 
        FROM StudentReadingLog 
        WHERE StudentID = {student_id}
        AND DateCompleted BETWEEN date('now', 'weekday 0', '-6 days') AND date('now', 'weekday 0', '+1 day')
        """
        cursor.execute(query)
        books_read = cursor.fetchone()[0]

        st.write(f"Books read this week by Student ID {student_id}: {books_read}")

        # Determine the message based on the number of books read
        if books_read < 3:
            books_left = 3 - books_read
            message = f"You're on a streak! Only {books_left} more book(s) to go to meet the weekly goal of 3!"
        elif books_read == 3:
            message = "Congratulations! You've hit your weekly reading goal!"
        else:
            message = f"Wow! You're a reading rockstar! You've read {books_read} books this week!"

        # Check if the student has already been awarded a badge for this week
        query_check_badge = f"""
        SELECT * FROM ParentBadges 
        WHERE StudentID = {student_id} 
        AND BadgeName = 'Weekly Reading Badge' 
        AND AwardedDate BETWEEN date('now', 'weekday 0', '-6 days') AND date('now', 'weekday 0', '+1 day')
        """
        cursor.execute(query_check_badge)
        badge_awarded = cursor.fetchone()

        if books_read >= 3 and not badge_awarded:
            # Award the badge to the student/parent
            query_award_badge = f"""
            INSERT INTO ParentBadges (StudentID, BadgeName, AwardedDate)
            VALUES ({student_id}, 'Weekly Reading Badge', date('now'))
            """
            cursor.execute(query_award_badge)
            conn.commit()

            # Add to the message if the badge was awarded
            message += "\nA badge has been awarded for your engagement this week!"

        conn.close()
    
    except Exception as e:
        # Return error message if any
        return f"An error occurred while checking badges: {str(e)}"
    
    # Return the motivational message
    return message

# Function to get recommendations based on grade and segment
def get_segment_recommendations(grade_level, segment):
    grade_lexile_ranges = {
        3: {
            'Beginning Learner': (200, 400),
            'Developing Learner': (401, 500),
            'Proficient Learner': (501, 650),
            'Distinguished Learner': (651, 760)
        },
        4: {
            'Beginning Learner': (300, 500),
            'Developing Learner': (501, 600),
            'Proficient Learner': (601, 740),
            'Distinguished Learner': (741, 850)
        },
        
       5: {
        'Beginning Learner': (400, 600),
        'Developing Learner': (601, 700),
        'Proficient Learner': (701, 830),
        'Distinguished Learner': (831, 940)
    },
    6: {
        'Beginning Learner': (500, 700),
        'Developing Learner': (701, 800),
        'Proficient Learner': (801, 925),
        'Distinguished Learner': (926, 1070)
    },
    7: {
        'Beginning Learner': (600, 800),
        'Developing Learner': (801, 900),
        'Proficient Learner': (901, 970),
        'Distinguished Learner': (971, 1120)
    },
    8: {
        'Beginning Learner': (700, 900),
        'Developing Learner': (901, 1000),
        'Proficient Learner': (1001, 1010),
        'Distinguished Learner': (1011, 1180)
    }
        
    }
    
    # Get Lexile range based on segment
    lexile_range = grade_lexile_ranges[grade_level][segment]
    min_lexile, max_lexile = lexile_range

    # Connect to the SQLite database
    conn = sqlite3.connect("C:/APS Book Database/Apsbdb")
    query = f"""
    SELECT BookID, BookTitle, LexileLevel, Author
    FROM BookRecommendations
    WHERE GradeLevel = {grade_level}
    AND LexileLevel BETWEEN {min_lexile} AND {max_lexile}
    """
    recommendations = pd.read_sql_query(query, conn)
    conn.close()
    return recommendations

# Function to log completed books for a student
def log_completed_books(student_id, completed_books):
    conn = sqlite3.connect("C:/APS Book Database/Apsbdb")
    cursor = conn.cursor()
    
    # Insert each completed book into StudentReadingLog
    for book_id in completed_books:
        query = f"""
        INSERT INTO StudentReadingLog (StudentID, BookID, DateCompleted)
        VALUES ({student_id}, {book_id}, DATE('now'))
        """
        cursor.execute(query)
    
    conn.commit()
    conn.close()

# Initialize session state for completed books and recommendations if not present
if 'completed_books' not in st.session_state:
    st.session_state['completed_books'] = []
if 'recommendations' not in st.session_state:
    st.session_state['recommendations'] = None

# Streamlit interface
st.title('Book Recommendation Engine')

# Input for Student ID (could be retrieved dynamically if connected to user system)
student_id = st.text_input("Enter Student ID")
st.write(f"Student ID entered: {student_id}")  # Debugging line

# Select grade level
grade = st.selectbox('Select Grade', [3, 4, 5, 6, 7, 8])

# Select learner segment
segment = st.selectbox('Select Learner Segment', 
                      ['Beginning Learner', 'Developing Learner', 'Proficient Learner', 'Distinguished Learner'])

# Button to get recommendations
if st.button('Get Recommendations'):
    st.session_state['recommendations'] = get_segment_recommendations(grade, segment)

# Display recommendations if available
if st.session_state['recommendations'] is not None:
    st.write(f"Recommended Books for {segment} Learners in Grade {grade}:")
    
    # Multi-select widget with pre-filled session state selections
    selected_books = st.multiselect(
        "Select Completed Books", 
        options=st.session_state['recommendations']['BookID'], 
        default=st.session_state['completed_books'],  # Persist selections
        format_func=lambda x: st.session_state['recommendations'][st.session_state['recommendations']['BookID'] == x]['BookTitle'].values[0]
    )
    
    st.write(f"Books selected: {selected_books}")  # Debugging line

    # Button to log completed books
    if st.button("Log Completed Books"):
        if student_id and selected_books:
            log_completed_books(student_id, selected_books)
            st.success("Completed books logged successfully!")
            
            # Check and award badge
            result_message = check_and_award_badge(student_id)
            if result_message:  # Ensure a message is returned
                st.success(result_message)
            else:
                st.error("No message was returned from the badge function.")
            
            st.session_state['completed_books'] = []  # Reset after logging
        else:
            st.error("Please enter a valid Student ID and select at least one book.")
