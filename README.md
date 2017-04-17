# gunosy.task1

# This is a repository containing files for task 1.
# In task 1 we aim to create an application that
# returns the categories of articles give their urls.
# 
# task1_b3 is the newset branch (2017/4/17 present)
#
# How to use
# In task1_2/task1_2_venv there are primary files and directories for this application
#
# To test naive Bayes performance, change directory in to polls/naivebayes
# Then run 'python predict.nb.py trained.nb.pkl item_gunosy_9.csv'
# This will return 'category name, its test number, the number of correct'
#
# Naive Bayes is trained using train.nb.py with naiveBayes.py module.
# To train, run 'python train.nb.py item_gunosy_7.csv'
# This will generate 'trained.nb.pkl' that stores a trained model.
#
# item_gunosy_N.csv includes category number and title
# 
# In 'polls/' directory models.py loads 'naivebayes/naiveBayes.py' module
# 127.0.1:8000/ shows two links 'What's up?' and 'Find a category?'
# Choose the latter
# Then views.py contains functions 'find' and 'input'
# The former shows the entrance page (find.html) where input form is present
# If someone inputs URL there and submit it, page moves to output page (outpu.html) using 'input' function
# Currently 'output' function does not work 
#
# To run server please be task1_2_venv and run 'python manage.py runserver'
#
