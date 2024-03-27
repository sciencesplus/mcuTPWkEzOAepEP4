import pandas as pd
import numpy as np
import pickle
import streamlit as st

#clf_file = open('knn_5.pkl', 'rb')
clf_file = open('Customer-happy-clf.pkl', 'rb')
classifier = pickle.load(clf_file)

def Happy_Customer_prediction(X5,X1):
#def Happy_Customer_prediction(X1,X2,X3,X4,X5,X6):
    '''Predict Customer satisfaction based on features values'''
    
    prediction = classifier.predict([[X5,X1]])
    #prediction = classifier.predict([[X1,X2,X3,X4,X5,X6]])
    print(prediction)
    
    return "The predicted value is" + str(prediction)

def main():
    st.title("Customer Satisfaction Prediction App")
    X1 = st.number_input("X1",1, 5)
    #X2 = st.number_input("X2",1, 5)
    #X3 = st.number_input("X3",1, 5)
    #X4 = st.number_input("X4",1, 5)
    X5 = st.number_input("X5",1, 5)
    #X6 = st.number_input("X6",0, 5)
    
    result= ""
    
    if st.button("Predict"):
        result = Happy_Customer_prediction(X5,X1)
        #result = Happy_Customer_prediction(X1,X2,X3,X4,X5,X6)
        if result == 0:
            st.success("The customer sentiment prediction is: Unhappy Customer")
        else:
            st.success("The customer sentiment prediction is: hjhjhjhjh")
    
    

        
if __name__=='__main__':
    main()