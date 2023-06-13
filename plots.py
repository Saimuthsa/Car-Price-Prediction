import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(df):
	st.header("Visualise Data")
	st.set_option("deprecation.showPyplotGlobalUse" , False)

	user_choice = st.multiselect("Select Type Of Plot:" , ("Scatterplot" , "Boxplot" , "Histogram" , "Correlation Heatmap"))

	if "Scatterplot" in user_choice:
		scatter_features = st.multiselect("Choose Features for Scatterplot:" , ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price'))

		for i in range(len(scatter_features)):
			st.subheader(f"Scatter plot for {scatter_features[i]} and price")

			plt.figure(figsize = (20,5))
			sns.scatterplot(df[scatter_features[i]] , df["price"])
			st.pyplot()

	if "Boxplot" in user_choice:
		box_features = st.multiselect("Choose Features for Boxplot:" , ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price'))

		for i in range(len(box_features)):
			st.subheader(f"Boxplot for {box_features[i]} ")

			plt.figure(figsize = (20,5))
			sns.boxplot(df[box_features[i]])
			st.pyplot()

	if "Histogram" in user_choice:
		hist_features = st.multiselect("Choose Features for Histogram:" , ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price'))

		for i in range(len(hist_features)):
			st.subheader(f"Histogram for {hist_features[i]} ")

			plt.figure(figsize = (20,5))
			plt.hist(df[hist_features[i]] , bins = "sturges")
			st.pyplot()

	if "Correlation Heatmap" in user_choice:
		st.subheader("Correlation Heatmap")

		plt.figure(figsize = (10,10))
		sns.heatmap(df.corr() , annot = True)
		st.pyplot()


