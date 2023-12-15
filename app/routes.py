# routes.py
from flask import render_template, request, flash, session
from app import app
from .model import analyze_text

@app.route('/', methods=['GET', 'POST'])
def index():
    text = session.get('text', '')  
    return render_template('index.html', text=text)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.form['text']
        session['text'] = text
        model_name = request.form['model']
        result = analyze_text(text, model_name)
        attentions = result.get('attentions')
        tokens = result.get('tokens')
        return render_template('analysis.html', attentions=attentions, tokens=tokens, model_name=model_name)
    except Exception as e:
        flash(str(e))
        return render_template('index.html')