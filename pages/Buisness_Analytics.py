# -------------------------------
# Importing Required Libraries
# -------------------------------
import streamlit as st # Imports Streamlit 
# which is used to build the web app UI (buttons, dropdowns, text).
import pandas as pd # Imports Pandas to read and manipulate datasets (CSV files).
import joblib # Used to load saved machine learning models (.pkl files).
import numpy as np # Imports NumPy for numerical operations (used indirectly by ML models).



# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Tourism Analytics", # Browser Tab Title
    page_icon="📊", # icon
    layout="wide"  # Wide Screen
)


# -------------------------------
# App Title
# -------------------------------
st.title("📊 Tourism Analytics") # Displays the main title of the APP
st.subheader("Business Intelligence Dashboard") # Displays Smaller heading under the title.




# Shows a formatted description explaining:
# What the dashboard does
# Business-focused analytics & predictive insights

st.markdown("""
Welcome to the **Tourism Business Intelligence Dashboard**, a data-driven analytics 
platform designed for travel agencies, tourism operators, and decision-makers 
to understand customer behavior and optimize strategic planning.

### 📊 What this dashboard offers:
- 📈 Seasonal demand and tourism trend analysis
- 👥 Visit mode distribution insights (Solo, Family, Couple, Friends)
- ⭐ Attraction performance and rating analytics
- 🧠 Predictive modeling for customer rating behavior
- 💼 Data-backed insights for package design and revenue growth

This module transforms tourism data into actionable business intelligence 
to support smarter operational and marketing decisions.
""")


st.markdown("---") # Draws a horizontal line for visual separation.


# -------------------------------
# Load Dataset
# -------------------------------
final_df = pd.read_csv("dataset/cleaned_tourism_data.csv")
# Loads the cleaned tourism dataset from a CSV file into a DataFrame.


# -------------------------------
# Calculating Profits
# -------------------------------
# Profit Score = Rating * Popularity
final_df["ProfitScore"] = (
    final_df["attraction_avg_rating"] *
    final_df["attraction_popularity"]
)


# Calculating average profit score for each season and attraction type
profit_analysis = (
    final_df.groupby(["season", "AttractionType"])["ProfitScore"]
    .mean()
    .reset_index()
)


# Creating a dropdown showing each unique season
selected_season = st.selectbox(
    "Select Season",
    sorted(final_df["season"].unique())
)

# Applying the profit analysis to each season and sorting (descending) based on profit score
season_data = profit_analysis[
    profit_analysis["season"] == selected_season
].sort_values(by="ProfitScore", ascending=False)

# Applying the season_data to every attraction type to depict the bar chart based on profit score
st.bar_chart(
    season_data.set_index("AttractionType")["ProfitScore"]
)


st.markdown("---") # Draws a horizontal line for visual separation.

# Counting the number of users travelling in each visit mode (Family, Solo, Couple etc)
visit_mode_counts = final_df["VisitMode"].value_counts()

# Converting the count into percentage
visit_mode_percentage = (
    final_df["VisitMode"]
    .value_counts(normalize=True) * 100
)

# Title for the Bar Chart Visualising the percentage of customers in each Visit Mode
st.subheader("👥 Visit Mode Distribution")

st.bar_chart(visit_mode_percentage)


st.markdown("---") # Draws a horizontal line for visual separation.

# Selecting the Input Features
features = ['VisitMode', 'season', 'Country', 'AttractionType']

# Loading the Regression Pipeline
rating_model = joblib.load("models/Regressor_Pipeline.pkl")

# Storing the predictions in a new column "PredictedRating" for the input features
final_df["PredictedRating"] = rating_model.predict(
    final_df[features]
)


# Sorting the attraction type based on average predicted rating in descending order
avg_predicted_rating = (
    final_df.groupby("AttractionType")["PredictedRating"]
    .mean()
    .reset_index()
    .sort_values(by="PredictedRating", ascending=False)
)


# Title for the bar chart 
st.subheader("⭐ Average Predicted Rating by Attraction Type")

# Setting the bar chart
st.bar_chart(
    avg_predicted_rating.set_index("AttractionType")
)


# Selecting the attraction type with the highest average predicted rating
top_type = avg_predicted_rating.iloc[0]

# Depicting the attraction type and it's average rating
st.metric(
    label="Top Performing Attraction Type (Predicted)",
    value=f"{top_type['AttractionType']} ({top_type['PredictedRating']:.2f})"
)

