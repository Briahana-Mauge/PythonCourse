# Machine Learning is a subset of artificial intelligence

# Steps for a ML project
'''
1. Import the Data
2. Clean the Data (removing the duplicates or irrelavant info)
3. Split the Data into 2 sets: Training (input [70-80% of data]) and Testing (output [20-30% of data])
4. Create a Model
5. Train the Model
6. Make Predictions
7. Evaluate and Improve
'''

# Libraries and Tools to use
'''
LIBRARIES
1. Numpy - provides multidimensional arrays
2. Pandas - provides a dataframe. dataframe is a 2d data structure that is like a spreadsheet
3. MatPlotLib - 2D plotting library that can help create graphs and plots
4. Scikit-Learn - provides common algorithms used in ML projects

TOOLS
1. Jupyter - the enviornment where ML projects should be done. VSCode cant handle it
 put this command in the terminal and it will open up a jupyter notebook for you online
 "jupyter notebook"
2. Kaggle.com
'''

# PANDAS
'''
pd.read_csv('file_name) - returns the spreadsheet
pd.shape - return a 2d array (# of records, # of columns)
pd.describe() - returns basic info about each column and the dataset (all cells with numerical values)
pd.values - returns a 2D array with all row information about each game as a row[] in the outside array
pd.drop() - it will drop whatever you specify and pass as an argument. ex: .drop(columns=['genre'])
    # doesnt modify the orginal dataset, it create a new one without the infomation you want
    # Used to get the input dataset and i represented by 'X'
pd.read_csv(file)['column'] - returns all the values in that column
    # doesnt modify the orginal dataset, it create a new one without the infomation you want
    # Used to get the output dataset and i represented by 'y'
'''

# Scikit-Learn
'''
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3) - take the args input, output and size of train sample
    # returns a touple with 4 variables with random data from the set
accuracy_score(y_test, predictions) - returns a score for how the accurate the model algo is between 0 & 1
'''