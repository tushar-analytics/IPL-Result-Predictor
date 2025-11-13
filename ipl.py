import streamlit as st
import pickle
import pandas as pd

# ------------------------ SETUP ------------------------
st.set_page_config(
    page_title="🏏 IPL Win Predictor",
    page_icon="🏆",
    layout="centered",
)

# Apply custom CSS for background and headings
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #1e3c72, #2a5298);
        color: white;
    }
    .stApp {
        background-color: #0f2027;
        background-image: linear-gradient(315deg, #2c5364 0%, #203a43 74%);
    }
    .big-font {
        font-size: 32px !important;
        font-weight: bold;
        color: #FFD700;
    }
    .small-font {
        font-size: 18px !important;
        color: #E0E0E0;
    }
    .result {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------ DATA ------------------------
cities = ['Hyderabad', 'Rajkot', 'Bengaluru', 'Mumbai', 'Indore', 'Kolkata',
       'Bangalore', 'Delhi', 'Chandigarh', 'Kanpur', 'Chennai', 'Jaipur',
       'Pune', 'Visakhapatnam', 'Abu Dhabi',
       'Dubai International Cricket Stadium', 'Sharjah Cricket Stadium',
       'Ahmedabad', 'Sharjah', 'Dubai', 'Navi Mumbai', 'Lucknow',
       'Guwahati', 'Dharamsala', 'Mohali', 'New Chandigarh', 'Cape Town',
       'Port Elizabeth', 'Durban', 'Centurion', 'East London',
       'Johannesburg', 'Kimberley', 'Bloemfontein', 'Cuttack', 'Nagpur',
       'Raipur', 'Ranchi']

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans',
 'Royal Challengers Bengaluru']

# Load trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# ------------------------ HEADER ------------------------
st.markdown("<h1 class='big-font' style='text-align:center;'>🏏 IPL WIN PROBABILITY PREDICTOR 🏆</h1>", unsafe_allow_html=True)
st.markdown("<p class='small-font' style='text-align:center;'>Predict the winning chances of your favorite team in real-time!</p>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------ INPUTS ------------------------
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the Bowling Team', sorted(teams))

selected_city = st.selectbox('Select Match City', sorted(cities))
target = st.number_input('🎯 Target Runs', min_value=0, step=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('🏏 Current Score', min_value=0, step=1)
with col4:
    overs = st.number_input('⏱ Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('❌ Wickets Fallen', min_value=0, max_value=10, step=1)

# ------------------------ PREDICTION ------------------------
if st.button('🔥 Predict Winning Probability'):
    if overs == 0 or target == 0:
        st.warning("Please enter valid target and overs before predicting.")
    else:
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'target_runs': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # ------------------------ RESULT DISPLAY ------------------------
        st.markdown("---")
        st.subheader("📊 Winning Probabilities")

        colA, colB = st.columns(2)
        with colA:
            st.markdown(f"<div class='result'>{batting_team}<br><span style='color:#00FF7F;'>{round(win*100)}%</span></div>", unsafe_allow_html=True)
        with colB:
            st.markdown(f"<div class='result'>{bowling_team}<br><span style='color:#FF4B4B;'>{round(loss*100)}%</span></div>", unsafe_allow_html=True)

        st.markdown("---")
        if win > loss:
            st.success(f"🏆 {batting_team} are currently in control of the game!")
        else:
            st.error(f"⚡ {bowling_team} are dominating right now!")

st.markdown("<br><p style='text-align:center;color:#bbb;'>Made with ❤️ by Tushar | Powered by Streamlit</p>", unsafe_allow_html=True)
