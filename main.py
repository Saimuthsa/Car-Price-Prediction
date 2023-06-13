#S 2.1
import pandas as pd
import streamlit as st 

st.set_page_config(page_title = "Car Price Prediction" , page_icon = "random" , layout = "centered" , initial_sidebar_state = "auto")

#S 3.1
words_dict = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "eight": 8, "twelve": 12}
def num_map(series):
    return series.map(words_dict)
@st.cache()
def load_data():
	# Reading the dataset
    cars_df = pd.read_csv("car-prices.csv")
    # Extract the name of the manufactures from the car names and display the first 25 cars to verify whether names are extracted successfully.
    car_companies = pd.Series([car.split(" ")[0] for car in cars_df['CarName']], index = cars_df.index)
    # Create a new column named 'car_company'. It should store the company names of a the cars.
    cars_df['car_company'] = car_companies
    # Replace the misspelled 'car_company' names with their correct names.
    cars_df.loc[(cars_df['car_company'] == "vw") | (cars_df['car_company'] == "vokswagen"), 'car_company'] = 'volkswagen'
    cars_df.loc[cars_df['car_company'] == "porcshce", 'car_company'] = 'porsche'
    cars_df.loc[cars_df['car_company'] == "toyouta", 'car_company'] = 'toyota'
    cars_df.loc[cars_df['car_company'] == "Nissan", 'car_company'] = 'nissan'
    cars_df.loc[cars_df['car_company'] == "maxda", 'car_company'] = 'mazda'
    cars_df.drop(columns= ['CarName'], axis = 1, inplace = True)
    cars_numeric_df = cars_df.select_dtypes(include = ['int64', 'float64']) 
    cars_numeric_df.drop(columns = ['car_ID'], axis = 1, inplace = True)
    # Map the values of the 'doornumber' and 'cylindernumber' columns to their corresponding numeric values.
    cars_df[['cylindernumber', 'doornumber']] = cars_df[['cylindernumber', 'doornumber']].apply(num_map, axis = 1)
    # Create dummy variables for the 'carbody' columns.
    car_body_dummies = pd.get_dummies(cars_df['carbody'], dtype = int)
    # Create dummy variables for the 'carbody' columns with 1 column less.
    car_body_new_dummies = pd.get_dummies(cars_df['carbody'], drop_first = True, dtype = int)
    # Create a DataFrame containing all the non-numeric type features.
    cars_categorical_df = cars_df.select_dtypes(include = ['object'])
    #Get dummy variables for all the categorical type columns using the dummy coding process.
    cars_dummies_df = pd.get_dummies(cars_categorical_df, drop_first = True, dtype = int)
    #  Drop the categorical type columns from the 'cars_df' DataFrame.
    cars_df.drop(list(cars_categorical_df.columns), axis = 1, inplace = True)
    # Concatenate the 'cars_df' and 'cars_dummies_df' DataFrames.
    cars_df = pd.concat([cars_df, cars_dummies_df], axis = 1)
    #  Drop the 'car_ID' column
    cars_df.drop('car_ID', axis = 1, inplace = True)
    final_columns = ['carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price']

    return cars_df[final_columns]
df = load_data()

#S 4.1
import home
import data
import plots
import predict

modules_dict = {"Home":home , "View data":data , "Visualize data":plots , "Prediction":predict}
st.sidebar.title("Navigation")
user_input = st.sidebar.radio("Go to:" , modules_dict.keys())
if user_input == "Home":
	modules_dict[user_input].app()
else:
	modules_dict[user_input].app(df)

