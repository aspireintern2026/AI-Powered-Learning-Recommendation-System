def calculate_mastery(df):
    # Derived feature: mastery_score (Page 3 of PDF)
    df['mastery_score'] = (df['quiz_score'] * 0.7) + ( (1/df['attempts']) * 30)
    
    # Identify knowledge gaps (Page 4 of PDF)
    df['knowledge_gap'] = 100 - df['quiz_score']
    return df