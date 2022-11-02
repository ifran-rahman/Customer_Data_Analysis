from flask import Flask
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)
dataset = pd.read_csv('scaled_trainset.csv')
regressor = joblib.load("xgb_reg.sav")

def process_inputs(dataset, customer_since, category,	gender,	age,	region,	state,	price,	discount_percentage):
   #Creating StandardScaler Object
    scaler = preprocessing.StandardScaler() 
   
    data = [[customer_since, category,	gender,	age,	region,	state,	price,	discount_percentage]]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['customer_since', 'category',	'gender',	'age',	'region',	'state',	'price',	'discount_percentage'])

    encoder = LabelEncoder()
    cat_features = ['category', 'gender', 'region', 'state']

    for cat_feature in cat_features:
       df[cat_feature] = encoder.fit_transform(df[cat_feature])

    #Creating StandardScaler Object
    scaler = preprocessing.StandardScaler() 
    dataset = scaler.fit_transform(dataset)

    df = scaler.transform(df) 
    
    
    return df

def predict_revenue(customer_since, category,	gender, age, region, state, price, discount_percentage):
   dataset = pd.read_csv('scaled_trainset.csv')
   x = process_inputs(dataset,customer_since, category,	gender, age, region, state, price, discount_percentage)

   regressor = joblib.load("xgb_reg.sav")
   prediction = regressor.predict(x)
      
   return prediction

def main():
   #  st.title("Revenue prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Revenue prediction</h2>
    </div>
    """
  
    st.markdown(html_temp,unsafe_allow_html=True)
    customer_since = st.text_input("Customer Since (days)", "")
    age = st.text_input("Age","")
    
    genders = dataset['Gender'].drop_duplicates()
    genders = genders.to_list()
    gender = st.selectbox('Select state', genders)

    price = st.text_input("Price","")

    states = dataset['State'].drop_duplicates()
    states = states.to_list()
    state = st.selectbox('Select state', states)

    Regions = dataset['Region'].drop_duplicates()
    Regions = Regions.to_list()
    region = st.selectbox('Select region', Regions)    

    categories = dataset['category'].drop_duplicates()
    categories = categories.to_list()
    category = st.selectbox('Select category', categories)
    
    discount_percentage =  st.text_input("Discount percentage","")
    
    


    result=""
    if st.button("Predict"):
        result=predict_revenue(customer_since, category,	gender, age, region, state, price, discount_percentage)
        result = result[0]
    st.success('Estimated revenue {}'.format(result))
    if st.button("About"):
        st.text("Lets Laarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
   main()