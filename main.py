import pandas as pd
import streamlit as st
import seaborn as sns
import pickle
import numpy as np
import matplotlib.pyplot as plt

from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Prediction'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
if selected== "Home": 
    st.header("Content Monetization Modeler")
    st.markdown(
    "<h2 style='text-decoration: underline;'>Exploratory Data Analysis (EDA)</h2>", unsafe_allow_html=True)


    df = pd.read_csv("C:/Users/priya/OneDrive/Desktop/datascience/content/cleaned_dataset.csv")
    
    ############################
    st.title("Target variable")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(df['ad_revenue_usd'], bins=50, kde=True, ax=ax)
    ax.set_title("Distribution of Ad Revenue (USD)")
    st.pyplot(fig)
    
##########################
    st.title(" Univariate analysis")
    numeric_feartures=['views','likes','comments','watch_time_minutes',
           'video_length_minutes','subscribers','ad_revenue_usd','engagement_rate']
    col_choice = st.selectbox("Choose a column to plot:", numeric_feartures)

    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(df[col_choice], bins=50, kde=True, ax=ax)
    ax.set_title(f"Distribution of {col_choice}")
    st.pyplot(fig)
 
    ###################
    st.title("Multivariate analysis")
    corr = df[['views','likes','comments','watch_time_minutes',
           'video_length_minutes','subscribers','ad_revenue_usd','engagement_rate']].corr()

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)

    st.pyplot(fig)
    ########################
    st.title("Which content categories drive more engagement")
    grouped = df.groupby('category')[['views','likes','comments']].mean()

    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    ax.set_ylabel("Average Engagement")
    ax.set_title("Engagement by Content Category")
    st.pyplot(fig)
    #############
    st.title("Mean Watch Time by Device")
    grouped = df.groupby('device')['watch_time_minutes'].mean()

    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    ax.set_ylabel("Average Watch Time (minutes)")
    ax.set_title("Mean Watch Time by Device")
    st.pyplot(fig)
    ################
    st.title("Ad Revenue by Country")
    grouped = df.groupby('country')['ad_revenue_usd'].sum().sort_values()

    fig, ax = plt.subplots()
    grouped.plot(kind='barh', ax=ax, color='skyblue')
    ax.set_xlabel("Total Ad Revenue (USD)")
    ax.set_title("Ad Revenue by Country")
    st.pyplot(fig)
    
    ####################
    st.title("Device Distribution")
    fig, ax = plt.subplots()
    df['device'].value_counts().plot(kind='pie', autopct='%1.2f%%', ax=ax)  
    ax.set_title("Device Distribution")
    st.pyplot(fig)
    
else:
    st.title("Predictions")

# Load model
    with open("RandomForestRegressor_model.pkl", "rb") as f:
        model = pickle.load(f)

# Input fields
        col1, col2 = st.columns(2)
        with col1:
            views = st.number_input("Views:", value=0.0)
            likes = st.number_input("Likes:", value=0.0)
            comments = st.number_input("Comments:", value=0.0)
            watch_time_minutes = st.number_input("Watch time (min):", value=0.0)
        with col2:
             video_length_minutes = st.number_input("Video length (min):", value=0.0)
             subscribers = st.number_input("Subscribers:", value=0.0)
             engagement_rate = st.number_input("Engagement rate:", value=0.0)

# Collect features into DataFrame with correct schema
        data = {
             "views": [views],
            "likes": [likes],
             "comments": [comments],
                "watch_time_minutes": [watch_time_minutes],
                "video_length_minutes": [video_length_minutes],
                "subscribers": [subscribers],
                "engagement_rate": [engagement_rate]
                    }
        input_data = pd.DataFrame(data)

# Predict button
    if st.button("PREDICT"):
        prediction = model.predict(input_data)
        st.success(f"Predicted Ad Revenue: $ {prediction[0]:.2f}")


     

    

        



    








