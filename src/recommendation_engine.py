def get_recommendation(student_id, df):
    student_data = df[df['student_id'] == student_id].iloc[-1]
    
    if student_data['quiz_score'] < 60:
        return f"Practice {student_data['topic']}", "Intermediate Problem Set"
    else:
        return "Advance to Next Module", "Advanced Theory Video"