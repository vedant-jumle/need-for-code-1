import tensorflow as tf
from tensorflow import keras
from itertools import product
import pandas as pd
import numpy as np

exclusion = [
    'hours working per day',
    'logical quotient rating',
    'hackathons',
    'coding skills rating',
    'public speaking points']
items_1 = [
    'Acedamic percentage in Operating Systems', 
    'percentage in Algorithms',
    'Percentage in Programming Concepts',
    'Percentage in Software Engineering', 
    'Percentage in Computer Networks',
    'Percentage in Electronics Subjects',
    'Percentage in Computer Architecture', 
    'Percentage in Mathematics',
    'Percentage in Communication skills']
items_2 = [
    'can work long time before system?',
    'self-learning capability?', 
    'Extra-courses did',
    'Management or Technical', 
    'Salary/work', 
    'hard/smart worker', 
    'worked in teams ever?', 
    'Introvert', 
    'Job/Higher Studies?']
items_3 = [
    'certifications',
    'workshops',
    'reading and writing skills',
    'memory capability score',
    'Interested subjects',
    'interested career area',
    'Type of company want to settle in?']

# convert all the lists above to have lower case strings
exclusion = [i.lower() for i in exclusion]
items_1 = [item.lower() for item in items_1]
items_2 = [item.lower() for item in items_2]
items_3 = [item.lower() for item in items_3]

labels = ['Database Developer',
 'Portal Administrator',
 'Systems Security Administrator',
 'Business Systems Analyst',
 'Software Systems Engineer',
 'Business Intelligence Analyst',
 'CRM Technical Developer',
 'Mobile Applications Developer',
 'UX Designer',
 'Quality Assurance Associate',
 'Web Developer',
 'Information Security Analyst',
 'CRM Business Analyst',
 'Technical Support',
 'Project Manager',
 'Information Technology Manager',
 'Programmer Analyst',
 'Design & UX',
 'Solutions Architect',
 'Systems Analyst',
 'Network Security Administrator',
 'Data Architect',
 'Software Developer',
 'E-Commerce Analyst',
 'Technical Services/Help Desk/Tech Support',
 'Information Technology Auditor',
 'Database Manager',
 'Applications Developer',
 'Database Administrator',
 'Network Engineer',
 'Software Engineer',
 'Technical Engineer',
 'Network Security Engineer',
 'Software Quality Assurance (QA) / Testing']

class CareerAdvisor:
    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)
        self.df = pd.read_csv("./dataset/career_pred.csv")

    def predict(self, data):
        return self.model.predict(data)

    def predict_label(self, data):
        return labels[np.argmax(self.predict(data))]

    def get_top(self, data, n):
        return data.argsort()[-n:][::-1]

    def permutate(self, x):
        keys = ["certifications", "workshops", "interested subjects", "interested career area", "type of company want to settle in?"]
        permuations = product(*[x[key] for key in keys])

        data = []
        for perm in permuations:
            temp = {}

            for col in x.keys():
                if col in keys:
                    temp[col] = perm[keys.index(col)]
                else:
                    temp[col] = x[col]

            data.append(temp)

        return data

    
    def preprocess(self, data):
        input_labels = []
        for item in data:
            input_labels.append(self.convert_to_x(item))
        
        return input_labels
        

    def convert_to_x(self, row):
        labels = []

        for col in row.keys():
            if col in items_1:
                labels.append(row[col]/100)
            elif col in items_2:
                labels.append(0 if row[col] == "no" else 1)
            elif col in items_3:
                uniques = self.df[col].unique().tolist()
                labels.append(uniques.index(row[col]))
            elif col in exclusion:
                labels.append(row[col])

        return labels


    def process(self, x, top=5):
        x = self.permutate(x)
        x = self.preprocess(x)
        x = np.array(x)
        outputs = self.predict(x)

        list_of_careers = []
        # get the top 5 output labels for each input and append to list_of_careers
        for i in range(len(x)):
            top_5 = self.get_top(outputs[i], top)
            for j in top_5:
                list_of_careers.append(labels[j])

        # return the list of unique careers
        return list(set(list_of_careers))