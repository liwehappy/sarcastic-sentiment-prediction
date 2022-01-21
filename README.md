# Sarcastic-Headline-Prediction
A basic example to specifically predict sarcastic news headlines with traditional machine models and ensembling technique.

This repo accompanies the blog post from my blog post [here](https://liwehappy.github.io/metastability/jupyter/text%20analytics/machine%20learning/ensembling/2021/11/25/Sarcasm-Detection.html)

## Features
* Text Analysis including word counts, most frequent words, wordcloud
* Build text preprocessing pipeline with bag of n-grams representation, nltk's casual_tokenizer, classifiers.
* Ensemble text preprocessing piepeline and multiple classifiers.

## How to use it and basic deployment

### Quick prototyping
If you want to directly play with it, the model had been deployede to [here](https://sarcasticheadlineprediction.herokuapp.com/) using heroku.
Caution: This model was trained with sarcastic news headline, other sarcastic text such as from tweets or conversation might suffer from low predictive accuracy.

## Possible improvement
Although this basic model may not be a state-of-art model, it is actually could be a quick and dirty baseline  for most of text classification problems in the beginning. Depends on the problem at hand, we could still gradually improve this model with more sophisticated text preprocessing method or other state-of-art model.