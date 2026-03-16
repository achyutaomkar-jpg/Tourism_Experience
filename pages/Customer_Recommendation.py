# -------------------------------
# Importing Required Libraries
# -------------------------------
import streamlit as st # Imports Streamlit 
# which is used to build the web app UI (buttons, dropdowns, text).
import pandas as pd # Imports Pandas to read and manipulate datasets (CSV files).
import joblib # Used to load saved machine learning models (.pkl files).
import numpy as np # Imports NumPy for numerical operations (used indirectly by ML models).



# -------------------------------
# Visit Mode Mapping
# -------------------------------

#The classifier model outputs numbers (0–3).
#This dictionary converts those numbers into human-readable visit modes.
#Example:
#0 → Solo, 1 → Family, etc.
visit_mode_map = {
    0: "Solo",
    1: "Family",
    2: "Couple",
    3: "Friends"
}



# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Tourism Analytics", # Browser Tab Title
    page_icon="🌍", # icon
    layout="wide"  # Wide Screen
)



# -------------------------------
# App Title
# -------------------------------
st.title("🌍 Tourism Analytics") # Displays the main title of the APP
st.subheader("Personalized Travel Recommendations") # Displays Smaller heading under the title.



#Shows a formatted description explaining:
#What the app does
#Features like ML prediction & recommendations
st.markdown("""
Welcome to **Tourism Analytics**, an intelligent data-driven application 
designed to analyze tourist behavior and provide personalized insights.

### 🔍 What this app offers:
- 📊 Tourism data analysis
- ⭐ Personalized attraction recommendations
- 🧠 ML-based rating prediction 
- 🗺️ Similar attraction discovery
""")

st.markdown("---") # Draws a horizontal line for visual separation.


# -------------------------------
# Load Dataset
# -------------------------------
final_df = pd.read_csv("dataset/cleaned_tourism_data.csv")
# Loads the cleaned tourism dataset from a CSV file into a DataFrame.

# Normalize text columns
for col in ['Country', 'AttractionType', 'Attraction']: # Loops through these text columns.
    final_df[col] = final_df[col].astype(str).str.strip().str.title()
    # For each column: Converts to string, Removes extra spaces, Converts text to Title Case



# -------------------------------
# Load Models
# -------------------------------

# Loads a precomputed similarity matrix used to find similar attractions.
similarity_df = joblib.load("models/similarity_df.pkl") 

# Loads the Linear Regression pipeline that predicts attraction ratings.
rating_model = joblib.load("models/Regressor_Pipeline.pkl")

# Loads the classification pipeline that predicts visit mode.
classify_model = joblib.load("models/Classifier_Pipeline.pkl")



# -------------------------------
# Sidebar Filters
# -------------------------------
st.markdown("### 🌍 Select Country") # Displays a heading in the sidebar.
countries = sorted(final_df['Country'].dropna().unique()) 
# Gets a sorted list of unique countries from the dataset.
selected_country = st.selectbox("Choose a country", countries)
# Creates a dropdown for selecting a country.


st.markdown("### 🎯 Select Attraction Type") # Displays a heading in the sidebar.
# Filters attraction types based on selected country.
filtered_types = sorted(
    final_df[final_df['Country'] == selected_country]['AttractionType']
    .dropna().unique()
)
# Dropdown for attraction type.
selected_type = st.selectbox("Choose attraction type", filtered_types)


st.markdown("### 🧠 Trip Details") # Displays a heading in the sidebar.

# Slider for the expected rating user wants.
avg_rating = st.slider(
    "Expected Attraction Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

# Dropdown to choose season (Summer, Winter, etc.).
season = st.selectbox(
    "Season of Visit",
    sorted(final_df['season'].dropna().unique())
)



st.markdown("---")
# Defines a function to predict visit mode.
def predict_visit_mode(country, attraction_type, avg_rating, season):
    input_df = pd.DataFrame([{ # Creates a one-row DataFrame as model input.
        'Country': country,
        'AttractionType': attraction_type,
        'attraction_avg_rating': avg_rating,
        'season': season
    }])

    # Uses the classifier model to predict visit mode (numeric).
    predicted_mode = classify_model.predict(input_df)[0]
    # Converts numeric output to text (Solo, Family, etc.).
    predicted_visit_mode = visit_mode_map.get(predicted_mode, "Unknown")
    # Returns the Visit Mode
    return predicted_visit_mode



predicted_visit_mode = predict_visit_mode(
    selected_country,
    selected_type,
    avg_rating,
    season
)

# Displays the predicted visit mode in a green success box.
st.success(f"🔮 Predicted Visit Mode: **{predicted_visit_mode}**")

# -------------------------------
# Filter Attractions
# -------------------------------

# Filters the dataset based on Country, AttractionType and Visit Mode
candidate_df = final_df[
    (final_df['Country'] == selected_country) &
    (final_df['AttractionType'] == selected_type) &
    (final_df['VisitMode'] == predicted_visit_mode)
].drop_duplicates(subset=['AttractionId']) # Removes duplicate attractions.



# -------------------------------
# Rating Prediction (PIPELINE SAFE)
# -------------------------------
def predict_user_rating(df): # Function to predict ratings for attractions.
    if df.empty:
        return df

    df = df.copy()

    # Uses the regression model to predict ratings.
    df['PredictedRating'] = rating_model.predict(df)

    return df

# -------------------------------
# Similarity Logic
# -------------------------------
def get_similarity_score(attraction): # Function to get similarity score for an attraction.
    if attraction in similarity_df.index:
        return similarity_df.loc[attraction].mean()
    return 0
# Finds the average similarity score from the similarity matrix.



# -------------------------------
# Apply Recommendation Logic
# -------------------------------

# Displays section heading.
st.markdown("### 🗺️ Recommended Attractions")

if candidate_df.empty:
    st.warning("No attractions found for the selected filters.")
else:
    rated_df = predict_user_rating(candidate_df) # Adds predicted ratings.

    if rated_df.empty:
        st.warning("Not enough data to generate predictions.")
    else:
        # Add similarity score
        rated_df['SimilarityScore'] = rated_df['Attraction'].apply(get_similarity_score)

        # Calculates final recommendation score: 70% rating, 30% similarity
        rated_df['FinalScore'] = (
            0.7 * rated_df['PredictedRating'] +
            0.3 * rated_df['SimilarityScore']
        )
        # Selects top 10 attractions.
        top_recommendations = rated_df.sort_values(
            by='FinalScore',
            ascending=False
        ).head(10)

        st.dataframe( # Displays recommendations in a table.
            top_recommendations[
                ['Attraction', 'PredictedRating', 'SimilarityScore', 'FinalScore']
            ].reset_index(drop=True),
            use_container_width=True
        )

# -------------------------------
# Footer
# -------------------------------

# Shows a footer message.
st.markdown("---")
st.caption("Built with ❤️ using Python, Machine Learning & Streamlit")