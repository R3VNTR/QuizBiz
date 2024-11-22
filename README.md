# QuizBiz
 QuizBiz is an AI-powered quiz app that creates customizable, interactive quizzes with diverse question types like multiple-choice, true/false, and fill-in-the-blanks. It ensures accuracy with AI validation, offers instant feedback, detailed scoring, and progress tracking, all through a user-friendly interface for dynamic learning and assessment.

# Steps
1. Clone the Repository
    # Clone the project to your local machine:
    git clone https://github.com/R3VNTR/QuizBiz.git


2. Set Up Virtual Environment
    # Create and activate a virtual environment:
    python -m venv quizbiz_env
    # Activate it:
    source venv/bin/activate

3. Install Dependencies
    # Install the required packages from requirements.txt:
    pip install -r requirements.txt

4. Set Up Database
    # Apply migrations to create the database schema:
    python manage.py migrate

5. Create a Superuser
    # Optionally, create an admin user:
    python manage.py createsuperuser

6. Run the Server
    # Start the development server:
    python manage.py runserver

# Visit http://127.0.0.1:8000/ in your browser.


# Key Features of QuizBiz
    AI-Generated Quizzes from URLs.
    Multiple Question Types (Multiple-choice, True/False, Short-answer).
    User Registration & Profile Management.
    Quiz Sharing with the community.