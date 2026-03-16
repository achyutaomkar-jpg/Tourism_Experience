## 🌍 Tourism Experience Analytics System

Tourism Experience Analytics is an end-to-end Machine Learning–based Tourism Intelligence System 
built using Python, Scikit-learn, SQL, and Streamlit.The project analyzes tourism transaction data to understand 
travel behavior, predict visitor preferences, and generate personalized attraction recommendations.The system 
\combines Regression, Classification, and Recommendation models to provide actionable insights 
for tourism platforms and travel agencies.

---


## Using historical user travel data, the system can:

- Predict attraction ratings
- Classify visitor travel modes
- Recommend personalized tourist attractions

---


## 🧠 Project Highlights

- Tourism analytics using real-world style relational datasets
- Regression model to predict attraction ratings
- Classification model to predict visitor travel mode
- Personalized tourist attraction recommendation system
- Exploratory Data Analysis to uncover tourism trends
- Feature engineering from multiple relational datasets
- Interactive Streamlit web application

---


## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- SQL
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

---


## ⚙️ How It Works
## 📊 Data Evaluation & Analysis

The Tourism dataset is loaded and analyzed to understand user travel behavior and attraction popularity.

The dataset consists of multiple relational tables including:

- Transaction Data
- User Data
- City Data
- Attraction Data
- Visit Mode Data
- Country Data
- Region Data
- Continent Data

These datasets are joined and analyzed to create a complete tourism behavior dataset.
---


## 🔍 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to understand patterns in tourism behavior.

Key analyses include:

- User distribution across continents and countries
- Popular tourist attractions by ratings
- Seasonal travel patterns by month and year
- Relationship between travel mode and demographics
- Distribution of attraction ratings
- Identification of tourism hotspots

EDA helps reveal travel trends, visitor behavior, and attraction popularity.

---



## 🔄 Data Preprocessing

Data preprocessing prepares the dataset for machine learning models.

Steps include:

- Handling missing values in transaction and user data
- Textual Preprocessing


Feature Engineering:

- Aggregating User Features and Attraction Features for modeling

- Mapping Season to Month for better Classification

- Aggregating Columns year_trend and season for better Analysis


---


## 🤖 Machine Learning Models

The project implements three types of machine learning tasks.

1️⃣ Regression Model – Attraction Rating Prediction

This model predicts the rating a user may give to a tourist attraction.

Feature Engineering:

- Scaling numerical features for better model performance

- Encoding categorical features like:

- Continent
- Country
- Region
- VisitMode
- AttractionType


Inputs:
- User location (continent, country, city)
- Attraction type
- Visit details (year, month)
- Historical attraction ratings

Output:
- Predicted attraction rating (1–5 scale)

Use Case:
- Identify attractions likely to receive lower ratings
- Improve service quality and user satisfaction
- Suggest attractions that better match user preferences




2️⃣ Classification Model – Visit Mode Prediction

This model predicts how a user is likely to travel. 

Feature Engineering:

- Scaling numerical features for better model performance

- Encoding categorical features like:

- Continent
- Country
- Region
- VisitMode
- AttractionType


Possible Visit Modes:
- Business
- Family
- Couples
- Friends
- Solo

Inputs:
- User demographics
- Attraction characteristics
- Historical visit data
- Travel time (month/year)

Output:
- Predicted visit mode

Use Case:
- Targeted tourism marketing campaigns
- Travel package personalization
- Better resource planning for tourism businesses





3️⃣ Recommendation System – Tourist Attraction Suggestions

A recommendation system suggests tourist attractions based on user preferences.
- Recommendation Approaches
- Collaborative Filtering
- Recommends attractions liked by similar users
- Content-Based Filtering
- Recommends attractions similar to those the user previously visited

Inputs:
- User visit history
- Attraction ratings
- Attraction attributes
- Similar user preferences

Output:
- Ranked list of recommended tourist attractions

---


## 🌐 Streamlit Application

A Streamlit web application is built to make the system interactive.

The application allows users to:
- Enter their location and preferences
- Predict their likely visit mode
- Receive personalized attraction recommendations
- Explore tourism analytics dashboards

The app also displays visual insights such as:
- Popular attractions
- Regional tourism trends
- Visitor behavior patterns

---


## 📁 How to Use This Project (Execution Order)

To reproduce the complete workflow, follow this execution order.

Open the notebooks folder and run the notebooks sequentially.

1️⃣ Run Data_Evaluation.ipynb
- Load all tourism datasets
- Data cleaning
- Handling missing values
- Data merging and feature engineering

Dataset preparation for modeling

Exploratory Data Analysis:
- Visualization of tourism trends
- User demographic analysis
- Attraction popularity insights

2️⃣ Run Regression_Model.ipynb
- Build rating prediction model
- Train regression algorithms

Evaluate model performance using:
- R² Score
- Mean Squared Error
- Mean Absolute Error

3️⃣ Run classification_model.ipynb

Build visit mode Classification_Model

Train algorithms such as:
- Random Forest
- XGBoost

Evaluate using:
- Accuracy
- Precision
- Recall
- F1 Score
  

4️⃣ Run Recommendation_Model.ipynb
- Build collaborative filtering recommendation system
- Create user–item matrix
- Generate personalized attraction recommendations

5️⃣ Run app.py
- Launch the Streamlit web application.
- streamlit run app.py
- The app will allow users to:
- Input travel preferences
- Get visit mode prediction
- Receive attraction recommendations
- Explore tourism insights

---


## 📈 Business Use Cases
## 🧳 Personalized Travel Platforms
- Recommend attractions tailored to user interests
- Improve traveler satisfaction and engagement

---

## 📊 Tourism Trend Analytics

- Identify popular tourist destinations

- Discover emerging tourism hotspots

---


## 🎯 Targeted Marketing

- Predict traveler segments (family, business, couples)

- Promote relevant travel packages


---


## 🔁 Customer Retention

- Deliver personalized travel recommendations

- Increase repeat usage of tourism platforms

---


## 📌 Important Note

- Large datasets may be excluded from GitHub to maintain repository size limits.

- Models can be retrained using the provided notebooks and datasets.

---

## 👨‍💻 Author

Akash Jalapati
