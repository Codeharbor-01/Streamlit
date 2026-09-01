import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Data Quality Checker')
st.write('We check and provide data quality of your input file')

col1,col2,col3 = st.columns(3)

file_path = col1.file_uploader('Upload a file')
file_type = col2.pills('Choose your file type',['Excel','CSV'])

if file_type == 'CSV':
    sep = col3.radio('Choose your seperator : ',['\\t',',','|'],horizontal=True)
if file_path:
    if file_type == 'Excel':
        df = pd.read_excel(file_path)
    elif file_type == 'CSV':
        df = pd.read_csv(file_path,sep=sep)
    st.write("**Sample Data**")
    st.dataframe(df)
    st.write("**Data Types :**")
    st.dataframe(df.dtypes)

    st.write('Missing Data : ')
    # fig,ax = plt.subplots()
    # missing_data = df.isna().sum()
    # plt.plot(missing_data)
    # missing_only = missing_data[missing_data>0]
    # missing_data.plot(kind='bar')
    # st.pyplot(fig)

    #Create a drop down to choose chart type
    #Create another drop down to choose x-axis
    #Create another drop down to choose y-axis
    #Make the plot according to inputs from above three widgets

    st.title('Dynamic Charts')
    column_names = df.columns.to_list()
    
    chart_type = st.selectbox('Choose chart type you want to view :',['line','bar','scatter'])

    col_1,col_2 = st.columns(2)
    X_col = col_1.selectbox('Choose X axis:',column_names)
    Y_col = col_2.selectbox('Choose Y axis:',column_names)

    fig,ax = plt.subplots()
    if chart_type == 'line':
        sns.lineplot(data=df,x=X_col,y=Y_col)
    elif chart_type =='bar':
        sns.barplot(data=df,x = X_col,y = Y_col)
    elif chart_type =='scatter':
        sns.scatterplot(data=df,x = X_col,y = Y_col)
    plt.tight_layout()
    st.pyplot(fig)