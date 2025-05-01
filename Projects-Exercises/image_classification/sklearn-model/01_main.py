import os

import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
# prepare data

input_dir = 'C:/Users/angel/OneDrive/Escritorio/TRAIN-MODELS-ML/Train-Flowers-ML'
categories=['daisy','dandelion','rose','sunflower','tulip']

data=[]
labels=[]

# Confirm if the directory exists
if not os.path.isdir(input_dir):
    raise FileNotFoundError (f'El directorio {input_dir} no existe')
else:
    print(f' El directorio {input_dir} existe :D')


for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        print(f'Processing the image: {file}')
        img_path = os.path.join(input_dir,category, file)
        img = imread(img_path)
        img = resize(img,(15,15))
        data.append(img.flatten()) # make data a array
        labels.append(category_idx)
        # resize
# os.listdir return a list of the names of the entries in a directory.
# os.path.join is useful to concatenate various parts of a file path in a way that is independent of the operating system.
# imread is a function used to reading image files in python
# resize is a function used to change the size of an image
#flatten() transforms an array of arrays into a single array

print(f'This take a long time :D but the data is ready')
dta = np.asarray(data)
labels = np.asarray(labels)


# train / test split

x_train, x_test,y_train, y_test= train_test_split(data,labels,test_size=0.1, stratify=labels, shuffle=True)
# convention in machine learning: x_train, y_train, y_test and x_test
# This line of code is splitting some labels into two parts, called y_train and y_test.
#and splitting some labels into two parts, called y_train and y_test.
#The text_size =.2 means that 20% of the data will be put in the x_test and y_test groups,
#  while the remaining 80$ of the data will be put in the x_train and y_train groups
# The shuffle=True part means that the data will be mixed up randomly before splitting
# Like shuffling a deck of cards. the stratify=labels part ensures that both
# groups have the same proportion of different types of labels as the original data
# the x_train and x_test groups have a smilar proportion of different labels, so its fair and representative.


#Train classifier

model = SVC()
parameters=[{'gamma':[0.01,0.001,0.0001],'C':[1,10,100,1000]}]
grid_search = GridSearchCV(model, parameters)
grid_search.fit(x_train,y_train)

# SVC or Support Vector Classification is a class in the scikit-learn library that implements the SVM algorithm for classification tasks.
# GridSearchCV is a function in scikit-learn used for hyperparameter values to find the optimal combination that maximizes model performance.This process is crucial because a model's performance is significantly influenced by the choice of hyperparameters,
#GridSearchCV.fit in scikit-learn exhaustively searches for the best combination of hyperparameter values for a given model. It trains the model on all possible combinations specifie


# This code is about training a machien learning model to classify things.
# The model is like a special kind of robot that learns from examples.
# The next part, params, is like a list of options for the model to try out
# It includes different values for 'gamma' and 'C'
# Think of these as settings that the model can adjust to kae better predictions.
# Then comes grid_search. It s like a helper that helps the model find the best combination of settings from the options in params. It tries different combinations of settings and compares how well the model performs with each combination
# the code is saying to the model, Hey chabom intenta con differentes combinacion de ajuste de parametros  y usa grid_search para encontrarr los mejores para la exactitudes de las predicciones


# Test Performance

# get the best of all the different image classifiers
best_estimator = grid_search.best_estimator_
y_prediction = best_estimator.predict(x_test)

#in sklearn.model_selection.GridSearchCV, best_estimator_ refers to the estimator (model) that was found to perform the best during the grid search process.
#is a method in scikit-learn used to make predictions on new, unseen data after hyperparameter tuning. GridSearchCV

score = accuracy_score(y_prediction,y_test)

print(f'The accuracy score is:{format(str(score*100))}%')

data = {'classifier':best_estimator}
with open('model.pkl', 'wb') as file:
    pickle.dump(data,file)
    print('I am here')
