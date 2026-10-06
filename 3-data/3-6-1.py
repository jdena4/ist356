import streamlit as st
import pandas as pd
import datetime
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls"

#load the Roster data
roster = pd.read_csv(f"{base}/roster.csv")

#load in the Poll Data
weeks = 4
polls = []
start_date = datetime.date(2024, 1, 8)
class_span = datetime.timedelta(days=7)
for week in range(weeks):
    current_date = start_date + (week * class_span)
    poll_file = f"{base}/poll-responses-{current_date}.csv"
    poll_data = pd.read_csv(poll_file)
    polls.append(poll_data)

polls_appended = pd.concat(polls)

# get a count of poll responses by student and week
polls_pivot = polls_appended.pivot_table(index="student_id", columns = "poll_date" , values="answer", aggfunc="count", fill_value=0)
st.dataframe(polls_pivot)


