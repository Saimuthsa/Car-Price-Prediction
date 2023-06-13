import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score , mean_squared_error , mean_absolute_error , mean_squared_log_error
from sklearn.linear_model import LinearRegression

def prediction(data , cw , es , hp  , dwf , ccb):
	X = data.columns[:-1]
	y = data.columns[-1]

	X_train , X_test , y_train , y_test = train_test_split(data[X] , data[y] , test_size = 0.30 , random_state = 42)

	lin_reg = LinearRegression()
	lin_reg.fit(X_train , y_train)
	score_lg = lin_reg.score(X_train , y_train)

	pred = lin_reg.predict([[cw,es,hp,dwf,ccb]]) 
	pred_test = lin_reg.predict(X_test)
	r2 = r2_score(y_test , pred_test)
	rmse = (mean_squared_error(y_test , pred_test))**(1/2)
	mae = mean_absolute_error(y_test , pred_test)
	msle = mean_squared_log_error(y_test,pred_test)

	return pred , score_lg , r2 , rmse , mae , msle


def app(df):
	st.markdown("<p style = color:blue;font-size:40px> This app uses <b> Linear Regression </b> to predict the price of the car based on the inputs </p>" , unsafe_allow_html = True)

	st.subheader("Select Values for Prediction")

	car_width = st.slider("Car Width" , float(np.min(df["carwidth"])) , float(np.max(df["carwidth"])))
	engine_size = st.slider("Engine Size" , float(np.min(df["enginesize"])) , float(np.max(df["enginesize"])))
	hp = st.slider("Horsepower" , float(np.min(df["horsepower"])) , float(np.max(df["horsepower"])))
	dwf = st.radio("Is it a forward drivewheel car?" , ("Yes" , "No"))
	if dwf == "Yes":
		dwf = 1
	else:
		dwf = 0
	car_company_b = st.radio("Was the car manufactured by Buick?" , ("Yes" , "No"))
	if car_company_b == "Yes":
		car_company_b = 1
	else:
		car_company_b = 0

	if st.button("Predict"):
		pred_new ,score , r2 , rmse , mae , msle = prediction(df , car_width , engine_size , hp , dwf , car_company_b) 

		st.success(f"Price of the car = {pred_new}")
		st.info(f"Accuracy = {score}" )
		st.info(f"R squared value = {r2}")
		st.info(f"Root Mean Squared Error = {rmse}")
		st.info(f"Mean Absolute Error = {mae}")
		st.info(f"Mean Squared Log Error = {msle}")





