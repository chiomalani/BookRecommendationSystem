from flask import Flask, request, jsonify

app = Flask(__name__)

# Example function to get recommendations (stub)
def get_book_recommendations(grade_level, student_lexile):
    # In a real deployment, this would query a database or model
    return ["Book A", "Book B", "Book C"]

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get query parameters
    grade_level = int(request.args.get('grade_level'))
    student_lexile = int(request.args.get('student_lexile'))
    
    # Get book recommendations
    recommendations = get_book_recommendations(grade_level, student_lexile)
    
    # Return recommendations as JSON
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
