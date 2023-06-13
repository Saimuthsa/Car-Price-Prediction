import streamlit as st 

def app(df):
	st.header("View Data")
	with st.beta_expander("View Dataset"):
		st.table(df)

	st.subheader("Column Descriptions")
	if st.checkbox("Show Summary"):
		st.table(df.describe())

	beta_col1 , beta_col2 , beta_col3 = st.beta_columns(spec = 3)
	with beta_col1:
		if st.checkbox("Display Columns Names:"):
			st.table(df.columns)
	with beta_col2:
		if st.checkbox("View column datatypes:"):
			st.table(df.dtypes)
	with beta_col3:
		if st.checkbox("View column data:"):
			col_name = st.selectbox("Choose column:" , (df.columns))
			st.table(df[col_name])