import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

####### SIDEBAR #######

st.sidebar.title('Filters')

# Select sex
unique_sex = df['Sex'].unique().tolist()
selected_sex = st.sidebar.selectbox("Select a sex", ['All'] + unique_sex)

# Select travel class
selected_pclass = st.sidebar.multiselect("Select travel class", df['Pclass'].unique(), default=df['Pclass'].unique())

# Filter data based on selections
filtered_df = df[df['Pclass'].isin(selected_pclass)]
if selected_sex != 'All':
  filtered_df = filtered_df[filtered_df['Sex'] == selected_sex]

####### DASHBOARD #######

st.title("🚢 Titanic Data Dashboard")
df
st.divider()

# BAR CHART - Survival Rate by Travel Class
st.subheader("Survival Rate by Travel Class")
survival_rates = filtered_df.groupby("Pclass")["Survived"].mean() * 100

with st.container():
    fig, ax = plt.subplots()
    ax.bar(survival_rates.index, survival_rates, color=['blue', 'orange', 'green'])
    ax.set_xlabel("Travel Class")
    ax.set_ylabel("Survival Rate (%)")
    ax.set_title("Survival Rate by Travel Class")
    ax.set_xticks(survival_rates.index)
    st.pyplot(fig)

st.divider()

# Pie chart and Pivot table on the same row
st.subheader("Passenger Distribution")
with st.container():
    pclass_counts = filtered_df["Pclass"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(pclass_counts, labels=pclass_counts.index, autopct='%1.1f%%', colors=['gold', 'silver', 'brown'])
    ax2.set_title("Passenger Distribution by Travel Class", fontsize=9)
    st.pyplot(fig2)

st.divider()

