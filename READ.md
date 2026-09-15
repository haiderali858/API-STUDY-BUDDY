 # AI Study Buddy

AI Study Buddy is an AI-powered learning assistant that helps students understand difficult topics in a simple and friendly way.

## Features

- Ask AI about any study topic
- Explain topics in simple English
- Generate quick study notes
- Create practice quizzes with multiple-choice questions
- Get instant AI-generated learning responses

## Technologies Used

- Python
- Flask
- Google Gemini API
- HTML
- CSS
- JavaScript
- Visual Studio Code

## Project Structure

```text
API STUDY BUDDY/
├── app.py
├── test_ai.py
├── templates/
│   └── index.html
├── README.md
└── .venv/
```

## How to Run

1. Install Python.
2. Create and activate a virtual environment.
3. Install the required packages:

```bash
pip install flask google-genai
```

4. Set the `GEMINI_API_KEY` environment variable.
5. Run the application:

```bash
python app.py
```

6. Open this address in your browser:

```text
http://127.0.0.1:5000
```

## How It Works

The student enters a topic and selects an option such as Ask AI, Explain Simply, Make Notes, or Generate Quiz.

The Flask backend sends the request to the Google Gemini API. Gemini generates the response, which is then displayed on the AI Study Buddy website.

## Future Improvements

- Urdu and Roman Urdu explanations
- User login and study history
- Progress tracking
- More quiz types
- Downloadable notes
- Voice-based learning

## Developer

Haider Ali  
BS Software Engineering Student