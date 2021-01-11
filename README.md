# iTA
A Digital Teaching Assistant

We have designed and implemented a question-answering chatbot, dubbed iTA (intelligent Teaching Assistant), which can answer detailed questions by effectively identifying the most relevant answers in “long” text sources (documents or textbooks). The iTA answers questions by implementing a two-stage procedure. First, the topmost relevant paragraphs are identified in the selected text source using a retrieval-based approach and compute the scores for the retrieved paragraphs. Second, using a generative model, we extract the relevant content from the top-ranked paragraph to generate the answer. We will present and demonstrate iTA.

We have used [The Foundations of Data Science](https://www.inferentialthinking.com/chapters/intro.html) as a long text source. We stored in
```
data/dataset.txt
```

We have adopted and adapted Simple and Effective Multi-Paragraph Reading Comprehension.
```
cd ./document-qa
```
Follow the readme to setup https://github.com/allenai/document-qa

Once the setup is done! Use
```
python ~/main.py /path/to/model/directory /path/to/long document/directory
```
Open your localhost:8080 to interact with the application.
