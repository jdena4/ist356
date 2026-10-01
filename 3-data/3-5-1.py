import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.dataframe(exams)
st.write(list(exams.columns))

st.title("Group by Examples")
group1 = exams.groupby(by=["Letter_Grade"]).agg({"Letter_Grade": "count"})
group1 = group1.rename(columns={"Letter_Grade": "Student_Count"})
st.dataframe(group1)

#Group by section and exam version and average the scores
st.title("Group by Section and Exam Version")
group2 = exams.groupby(by=["Class_Section", "Exam_Version"]).agg({"Student_Score": "mean" , 'Percentage': 'count'})
group2 = group2.rename(columns={"Student_Score": "Average_Score"})
st.dataframe(group2)

st.title("Pivot Table Examples")
pivot1 = exams.pivot_table(index=['Class_Section'],columns=['Exam_Version'],values=['Student_Score'],aggfunc='count')
st.dataframe(pivot1)
#pivot turns rows in columns
#Melt turns columns into rows


st.title("Melt Example")
melt1 = pivot1.reset_index().melt(id_vars=['Class_Section'],
                                   var_name='Exam_Version', 
                                   value_name='Student_Score')





st.dataframe(melt1)