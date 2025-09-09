import cohere
from flask import Flask, render_template, request
import secrets
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Set a secret key for CSRF protection

# Replace with your free Cohere API key (get one at https://dashboard.cohere.com/)
COHERE_API_KEY = os.getenv('API')

@app.route('/', methods=['GET', 'POST'])
def home():
    output = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        co = cohere.Client(COHERE_API_KEY)
        response = co.chat(
            model='command-nightly',         # Use the latest free model
            message=user_input,
            max_tokens=300,
            temperature=0.7
        )
        output = response.text
    return render_template('home.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
