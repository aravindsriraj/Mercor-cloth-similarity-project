import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
from io import StringIO
import pickle
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import json
from json import loads, dumps
from flask import Flask, request, jsonify, Response

    

def find_similar_product(new_product,top=10):

    # Load SBERT model
    model_name = 'bert-base-nli-mean-tokens'
    model = SentenceTransformer(model_name)

    # Load Data
    df = pd.read_csv('asos.csv')

    # Load Embeddings
    with open('embeddings.pickle', 'rb') as handle:
        embeddings = pickle.load(handle)
    
    # Encode the new sentence
    new_sentence_embedding = model.encode([new_product], convert_to_tensor=True)

    # Calculate cosine similarity between the new sentence and existing sentences
    similarity_scores = cosine_similarity(new_sentence_embedding, embeddings)

    res = pd.DataFrame({"Products": df['lemmatize_text'],"Similarity":similarity_scores[0],"URL":df['url']})

    return res.sort_values('Similarity',ascending=False).head(top)
  

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        text = request.form.get("text")
        url = request.form.get('url')
        if text is None or text=="":
            return jsonify({"error":"No Input"})
        try:
            # num = np.random.randint(len(df))
            # choice_text = np.random.choice(list(df['lemmatize_text']))
            # choice_url = np.random.choice(list(df['url']))
            
            # data = {'Input Product: ': text,'Input URL': url}
            # return jsonify(data)
            global res_copy
            res_copy = None
            res = find_similar_product(text)
            res_copy = res.copy()
            res_copy['Input Product'] = text
            return Response(res.to_json(orient="index"), mimetype='application/json')
        except Exception as e:
            return jsonify({"error":str(e)})
       
    return Response(res_copy.to_json(orient="index"), mimetype='application/json')
    
if __name__=="__main__":
    app.run(debug=True)
    