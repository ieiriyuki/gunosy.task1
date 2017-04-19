# gunosy.task1

This is a repository containing files for task 1.
In task 1 we aim to create an application that
returns the categories of articles give their urls.

task1_b3 is the newset branch (2017/4/18 present)

* How to use
In task1_2_venv there are primary files and directories for this application

* Validate naive Bayes
To test naive Bayes performance, change directory in to polls/naivebayes
Then run 'python predict.nb.py storedmodel.pkl testdata.csv'
This will return the matrix of true and called categories.
Each row shows true models and each column shows called categories
         エンタメ スポーツ ... <- call
エンタメ a        b
スポーツ c        d
...
true

* How to train
Naive Bayes is trained using train.nb.py with naiveBayes.py module.
naiveBayes.py contains naiveBayes class to analyze words, store data, construct model, and do prediction
To train, run 'python train.nb.py traindata.csv storedmodel.pkl'
You can choose other name of *.pkl file that stores trained model

traindata.csv and testdata.csv include category numbers 1..8 and article titles

* Http and server settings
In 'polls/' directory models.py loads 'naivebayes/nbModel.py' module and naiveBayes class
127.0.1:8000/ shows two links 'What's up?' and 'Find a category?'
Choose the latter
Then views.py contains functions 'find' and 'input'
The former shows the entrance page (find.html) where input form is present
If someone inputs URL there and submit it, page moves to output page (outpu.html) using 'input' function
Currently 'output' function does not work 

To run server please move into 'task1_2_venv' and run 'python manage.py runserver'

* Web crawl and scrape
Web crawling and scraping is done using files in 'gunosynews' directory
Do 'scrapy crawl gunosy' at 'gunosynews' directory so as to crawl and scrape
'https://gunosy.com/categories/"number"' is crawled and scraped to obtain category number and article title
The code to crawl and scrape is written in 'gunosynews/spider/gunosy.py'
