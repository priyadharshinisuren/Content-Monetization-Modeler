Content Monetization Modeler 🎥💰
A machine learning project that predicts YouTube ad revenue based on video performance metrics and contextual features. This project implements multiple regression models and provides an interactive Streamlit web application for revenue predictions.
🎯 Project Overview Domain: Social Media Analytics Problem Statement: Build a regression model to accurately estimate YouTube ad revenue for individual videos based on performance and contextual features, helping content creators and media companies with revenue forecasting and content strategy optimization.
🛠️ Technologies Used Python Machine Learning: Scikit-learn Data Analysis: Pandas, NumPy Visualization: Matplotlib, Seaborn Web App: Streamlit Model Persistence: Pickle 📊 Dataset Information Name: YouTube Monetization Modeler Dataset Format: CSV Size: ~122,000 rows Source: Synthetic dataset created for learning purposes Target Variable: ad_revenue_usd Features: video_id: Unique identifier date: Upload/report date views, likes, comments: Performance metrics watch_time_minutes, video_length_minutes: Engagement metrics subscribers: Channel subscriber count category, device, country: Contextual information ad_revenue_usd: Revenue generated (target variable)
📁 Project Structure content-monetization-modeler/ │ ├── README.md # Project documentation ├── youtube_ad_revenue_dataset.csv # Dataset ├── content_yt.ipynb # Main Jupyter notebook ├── app_yt.py # Streamlit web application ├── linear_regression_model.pkl # Trained model file └── requirements.txt # Python dependencies 🔬 Methodology
1.	Data Preprocessing Handled ~5% missing values in key columns Removed ~2% duplicate records Encoded categorical variables (category, device, country) Created new feature: engagement_rate = (likes + comments) / views
2.	Exploratory Data Analysis Comprehensive statistical analysis Correlation analysis between features Distribution analysis of target variable
3.	Model Building & Evaluation Tested 5 different regression models:
Lasso Regression KNeighborsRegressor Linear Regression DecisionTreeRegressor RandomForestRegressor
4.	Model Selection RandomForestRegressor was selected as the best model based on:
Train R2 Score: 0.9924545043936243 Test R2 Score: 0.9494890074148347
Built-in feature selection capability Good generalization performance
💻 Streamlit App Features The interactive web application includes:
Input Fields:
Numeric inputs :'likes', 'comments', 'watch_time_minutes', 'video_length_minutes', 'engagement_rate', 'views', 'subscribers'
Real-time Predictions:
Instant ad revenue predictions based on user inputs Professional UI with clear result display
📈 Key Insights Strong Predictive Power: All models achieved greater then 95% R² score, indicating excellent predictive capability
🎯 Skills Demonstrated Machine Learning: Regression modeling, model comparison Data Science: EDA, feature engineering, data cleaning, statistical analysis Programming: Python, Pandas, Scikit-learn, data visualization Web Development: Streamlit app development

