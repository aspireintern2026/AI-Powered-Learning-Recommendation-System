import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="EduSmart Recommendation System", layout="wide")

st.title("🎯 Student Learning Recommendation Dashboard")
st.markdown("---")

# Sidebar for Student Input
with st.sidebar:
    st.header("👤 Student Profile")
    student_id = st.text_input("Student ID", value="S101")
    current_topic = st.selectbox("Current Topic", 
                                ["Variables", "Loops", "Arrays", "Recursion", "Sorting Algorithms"])
    
    st.header("📊 Performance Stats")
    quiz_score = st.slider("Last Quiz Score (%)", 0, 100, 45)
    time_spent = st.number_input("Time Spent (minutes)", min_value=1, value=60)
    attempts = st.number_input("Number of Attempts", min_value=1, value=3)

# Logic as per Day 4/6 of the PDF
def generate_recommendation(score, topic):
    # Base logic mentioned in Page 6: "If score < 60 -> recommend practice"
    if score < 60:
        rec_topic = f"{topic} Practice"
        resource = f"Intermediate {topic} Problem Set"
        status = "⚠️ Needs Reinforcement"
        color = "red"
    else:
        # Simplified Logic for progression
        topics = ["Variables", "Loops", "Arrays", "Recursion", "Sorting Algorithms"]
        idx = topics.index(topic)
        next_topic = topics[idx + 1] if idx + 1 < len(topics) else "Advanced Concepts"
        rec_topic = next_topic
        resource = f"Introduction to {next_topic} Masterclass"
        status = "✅ Concept Mastered"
        color = "green"
    
    return rec_topic, resource, status, color

# Action Button
if st.button("Generate AI Recommendation"):
    rec_topic, resource, status, color = generate_recommendation(quiz_score, current_topic)
    
    # Display Results in Layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Performance Summary")
        st.metric(label="Topic Mastery Status", value=status)
        
        # Simulated Feature Engineering (Day 4)
        progress_data = {
            "Metric": ["Knowledge Gap Index", "Learning Progress Rate", "Mastery Score"],
            "Value": [round(100-quiz_score, 2), f"{quiz_score/attempts}%", quiz_score]
        }
        st.table(pd.DataFrame(progress_data))

    with col2:
        st.subheader("Personalized Path")
        st.success(f"**Recommended Next Topic:** {rec_topic}")
        st.info(f"**Suggested Resource:** {resource}")
        
        # Visualization (Day 3)
        st.markdown("**Performance Trend**")
        chart_data = pd.DataFrame(
            np.random.randn(5, 1),
            columns=['Score History']
        )
        st.line_chart(chart_data)

st.markdown("---")
st.caption("Powered by Aspire Code AI - Recommendation Engine Model v1.0")