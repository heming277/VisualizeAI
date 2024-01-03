# VisualizeAI: Language Model Attention Visualization Tool

I created an interactive web application to visualize attention scores from various fill-mask transformer models for language processing. I believe this can give some insight into how these language models work in terms of their attention machanisms. 

The basic underlying logic is that the attention scores from language transformers like Bert uses attention mechanisms in order to understand the context of words in sentences. The attention array is a 3D array with the first level of the array representing the attention heads to explain relationships such as syntactic or semantic relationships, then the second level of the array is the sequence length of the input token, and then the last level is the attention that each token in the input pays to every other token including itself. For each attention head there is a matrix and the value at the i-j location is the attention the ith token gives to the jth token, given this pairwise attention scores, I feel that it is natural to utilize a heatmap to represent this. Higher attention scores between two tokens suggest that the model finds the relationship between those tokens important for understanding the context of the sentence. 

Note--currently the input size limited to 100 words or 600 characters becasue longer inputs take too long for visualizing of all the layers of attention scores for BERT, ALBERT, and RoBERTa, but this may be solved later. 

![Example Image](index.png)
![Example Imagee](analysis.png)

## Features

- **Tech Stack**:Python,Flask,PyTorch,Hugging Face, Numpy, Javascript, Jinja, HTML, CSS, D3.js.

- **Caching**: Used caching mechanisms for processing different transformer models.

- **Transformers and Language Modeling**: 3 transformer models included, you can add more, right now include BERT, ALBERT, and RoBERTa, for analzying text and visualizing attention mechanisms.

- **Interactive Visualizations**: User interactive for visualizing attention scores. 

## Future Improvement

- **Language gneeration and fill-mask**: Add generator models like GPT3 and Claude to see their attention scores as they focus on the input prompts, etc. currently only has fill-mask models. 

- **Large Scale, resource-intensive models and GPU**: May add some large scale systems like BERT large, etc where GPU acceleration may be more appplicable. Or Large scale ETL for datasets like from Wikipedia, etc.

- **Reinforcement Learning and fine tuning**:Future Improvements such as using sentences with masked tokens and then visualize the model's attention as it predicts the masked word(s), etc. 

## Getting Started
1. **Clone**:

git clone https://github.com/heming277/VisualizeAI.git

2. **Set Up**:
- Create a virtual environment:
  ```
  python -m venv venv
  ```
- Activate the virtual environment:
  * On macOS/Linux:
    ```
    source venv/bin/activate
    ```
  * On Windows:
    ```
    venv\Scripts\activate
    ```
- Install the requirements:
  ```
  pip install -r requirements.txt
  ```
3. **Run in Venv**:
  python run.py
  Use on http://127.0.0.1:5000
## Documentation

- **`routes.py`**: Render and send data to templates
- **`model.py`**: For loading the model and doing text and visual prep work 
- **`/templates/index.html`**: Users can select AI models to analyze
- **`/templates/analysis.html`**: The results page
