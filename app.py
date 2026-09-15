from flask import Flask, render_template, request
from google import genai
import markdown

app = Flask(__name__)

client = genai.Client()


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        action = request.form.get("action", "ask")

        if not topic:
            response = "Please enter a topic first."

        else:
            if action == "ask":
                instruction = "Explain this topic clearly for a university student."

            elif action == "simple":
                instruction = "Explain this topic in very simple English with an easy real-life example."

            elif action == "notes":
                instruction = "Create short, clear revision notes with headings and bullet points."

            elif action == "quiz":
                instruction = (
                    "Create 5 multiple-choice questions about this topic. "
                    "Give four options for each question and show the correct answers at the end."
                )

            else:
                instruction = "Explain this topic clearly."

            prompt = f"""
You are AI Study Buddy, a helpful educational assistant.

Topic: {topic}

Task: {instruction}

Use simple English and make the answer easy to understand.
"""

            try:
                result = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                response =markdown.markdown(result.text)


            except Exception as error:
                response = "AI connection error. Please check your internet or API key."

 
    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)