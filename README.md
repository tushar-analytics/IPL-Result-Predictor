# 🏏 IPL Win Probability Predictor

### 🎯 Predict the winning chances of IPL teams in real-time using machine learning!

---

## 📘 Overview

This project predicts the **win probability** of an IPL team during a live match based on the current game situation (runs, overs, wickets, venue, etc.).

It combines **data analysis**, **feature engineering**, and a **machine learning model (Logistic Regression)**, wrapped in a beautiful **Streamlit web app**.

---

## 🧩 Dataset Details

- **Source:** [Cricsheet.org](https://cricsheet.org/)
- **Format:** JSON files (each representing one IPL match)
- **Data Extracted:**
  - `matches` data — match metadata (teams, city, season, toss info, result)
  - `deliveries` data — ball-by-ball information for every innings

### 🧠 Data Processing Steps
1. Combined all JSON files into structured **Pandas DataFrames**
2. Merged **matches** and **deliveries** datasets
3. Extracted meaningful fields:
   - Batting team, Bowling team
   - Venue, Season, City
   - Runs scored, Wickets fallen, Overs completed
   - Target runs (for 2nd innings)
4. Cleaned and preprocessed:
   - Removed miscounted overs
   - Handled wide/no-ball logic
   - Filled missing values logically (balls_left, city, etc.)

---

## 📊 Exploratory Data Analysis (EDA)

EDA was done using **Matplotlib** and **Pandas groupby (Split–Apply–Combine)**.

### 📈 Key Observations

- 🏟️ **Number of matches** was highest in **2008 and 2009**, then dropped.  
  In the past 3 years, the **average matches per season ≈ 75**.

- 🟡 **Mumbai Indians (MI)** and **Chennai Super Kings (CSK)** have the **most wins**, showing consistent dominance.

- 🎯 **Toss Decision Trends:**
  - Most teams choose **fielding first** even after winning the toss because:
    - Chasing is considered easier (teams know the exact target)
    - Due factor (dew) affects bowling in 2nd innings
    - In T20s, batting second allows controlled aggression

- 💥 **Powerplay Performances:**
  - **Royal Challengers Bengaluru (RCB)** often start strong — they have the **best powerplay run rate** among all teams.

- 🚀 **Death Overs (last 3 overs):**
  - **CSK** and **MI** are the most **volatile & explosive** teams, with the **highest number of sixes** in the final overs.

---

## ⚙️ Model Development

### 🧹 Data Preprocessing
- Cleaned and structured the merged dataset  
- Used **OneHotEncoder** for categorical columns (teams, city, etc.)  
- Normalized numeric columns (`runs_left`, `balls_left`, `crr`, `rrr`, etc.)  
- Built a **Pipeline** for seamless transformation + model training

### 🤖 Model Used
- **Logistic Regression** (binary classification)
- Predicts the **probability of winning** for the batting team

---

## 🧮 Features Used for Prediction

| Feature | Description |
|----------|-------------|
| `batting_team` | Current batting team |
| `bowling_team` | Current bowling team |
| `city` | Match city |
| `runs_left` | Runs remaining to win |
| `balls_left` | Balls remaining |
| `wickets_left` | Remaining wickets |
| `target_runs` | Total target for chase |
| `crr` | Current Run Rate |
| `rrr` | Required Run Rate |

---

## 💻 Tools & Libraries Used

| Category | Tools |
|-----------|--------|
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib |
| **Modeling** | Scikit-learn (Logistic Regression, OneHotEncoder, Pipeline) |
| **Web App** | Streamlit |
| **Development** | PyCharm, Jupyter Notebook |
| **Data Source** | Cricsheet JSONs |

---

## 🌐 Web App (Streamlit UI)

The Streamlit interface allows users to:
- Select batting & bowling teams
- Input current score, overs, and wickets
- Choose city and match target
- Get **live win probability** instantly

### ✨ Features
- Dynamic team colors & logos  
- Gradient UI theme  
- Probability cards with visual comparison  
- Real-time prediction using trained model  

---

## 🚀 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/IPL-Win-Predictor.git
   cd IPL-Win-Predictor

2. **Install Dependencies**
   pip install -r requirements.txt
   
3. **Run the streamlit app**
   streamlit run app.py

--

## 🏆 Results
1. Model achieves ~80% accuracy on unseen match data
2. Predictions align closely with real-life IPL trends
3. Demonstrates end-to-end data engineering → modeling → deployment

--

## ❤️ Acknowledgements
- Data: Cricsheet.org
- Libraries: Streamlit, Scikit-learn, Pandas, Matplotlib
- Developer: Tushar Chaudhary

--

## 📫 Contact
- 📧 chaudharytushar017@gmail.com
- 💼 LinkedIn Profile = https://www.linkedin.com/in/tusharchaudhary017

