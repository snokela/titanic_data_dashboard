import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

# dataframe
df

####### SIDEBAR #######

st.sidebar.title('Filters')
st.sidebar.info("ℹ️ **Tip:** Uncheck 'Show full dataset' to enable filters.")

# show full dataset
show_full_df =  st.sidebar.checkbox('Show full dataset', value=True)

# select age range
# min_age = df["Age"].min()
# max_age = df["Age"].max()
#avg_year = df["Age"].mean()  -> 29,699 -> (25-30)

# selected_age = st.sidebar.slider("Select age range", float(min_age), float(max_age), (float(25) - float(30)))

unique_sex = df['Sex'].unique().tolist()
selected_sex = st.sidebar.selectbox("Select a sex", ['All'] + unique_sex)

selected_pclass = st.sidebar.multiselect("Select travel class", df['Pclass'].unique(), default=df['Pclass'].unique())

# Filter data based on selections
filtered_df = df
if not show_full_df:
    filtered_df = filtered_df[df['Pclass'].isin(selected_pclass)]
    if selected_sex != 'All':
        filtered_df = filtered_df[filtered_df['Sex'] == selected_sex]