from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the Hugging Face summarization pipeline for English
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        # Perform summarization
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
