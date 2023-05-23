# Mercor Clothing Similarity Project

**Objective:**

- The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites.

- Deployment on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.

**Outline:**

- We will collect the data from ASOS company by web scraping

**ASOS is a well-known British fashion and beauty retailer that operates and ships globally to 195+ countries. Founded in the year 2000 in London, ASOS offers their own label, known as ASOS Design, as well as more than 850 other brands, similar to an outlet retailer.**

- Save the data as a excel format
- Perform Text pre-processing
- Implement Feature Extraction techniques like word2vec and Sentence Transformers.
- Compute the Cosine similarity to find Top-N similar products

**Contents:**

- web_scraping.ipynb: Web Scraping and Data Collection
- feature_extraction_similarity.ipynb: Feature Extraction and Cosine Similarity
- main.py: A Simple Flask application which accepts the input as a request and predicts the similar products along with the similarity score
- test.py: A program which selects random product from the dataset and gives as input to the main.py.


**Steps to Run:**

- Open terminal and run **python main.py**.
- Copy the local host **http://127.0.0.1:5000/** to the test.py
- open another terminal and run **python test.py**

**Screenshots:**
- main.py
![image](https://github.com/aravindsriraj/Mercor-cloth-similarity-project/assets/60252521/81d3217a-77ee-4da5-813d-d9854839b1c5)

- test.py
![image](https://github.com/aravindsriraj/Mercor-cloth-similarity-project/assets/60252521/6f65b8c1-c76a-4452-8524-ca2a9d60dc8e)

- Output in localhost
![image](https://github.com/aravindsriraj/Mercor-cloth-similarity-project/assets/60252521/e8b76b1a-6093-4bc1-ad5c-324b96b0c296)

**Steps for Deployment**
1. Write App (Flask, Tensorflow)
- Implement the app in **main.py**

2. Setup Google Cloud
- Create new project
- Activate Cloud Run API and Cloud Build API

3. Install and init Google Cloud SDK
https://cloud.google.com/sdk/docs/install

4. Dockerfile, requirements.txt, .dockerignore
https://cloud.google.com/run/docs/quickstarts#containerizing

5. Cloud build & deploy
> gcloud builds submit --tag gcr.io/<project_id>/<function_name>

> gcloud run deploy --image gcr.io/<project_id>/<function_name> --platform managed

6. Test
- Test the code with test.py

**Google cloud run app** - https://getsimilarity-ujmy7r6rkq-uc.a.run.app

