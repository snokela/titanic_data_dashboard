import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

####### SIDEBAR #######

st.sidebar.title('Filters')

# Select gender
unique_sex = df['Sex'].unique().tolist()
selected_gender = st.sidebar.selectbox("Select a gender", ['All'] + unique_sex)

# Select travel class
selected_pclass = st.sidebar.multiselect("Select travel class", df['Pclass'].unique(), default=df['Pclass'].unique())

# Filter data based on selections
filtered_df = df[df['Pclass'].isin(selected_pclass)]
if selected_gender != 'All':
  filtered_df = filtered_df[filtered_df['Sex'] == selected_gender]

####### DASHBOARD #######

st.title("🚢 Titanic Data Dashboard")

st.divider()

with st.expander(" **Full Titanic Dataset** (Click to Expand)"):
  st.dataframe(df)

st.divider()

# BAR CHART - Survival rate by travel class
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

# PIE CHART - passenger distribution
st.subheader("Passenger Distribution")
with st.container():
    pclass_counts = filtered_df["Pclass"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(pclass_counts, labels=pclass_counts.index, autopct='%1.1f%%', colors=['gold', 'silver', 'brown'])
    ax2.set_title("Passenger Distribution by Travel Class", fontsize=9)
    st.pyplot(fig2)

st.divider()

# PIVOT TABLE AND BAR CHART - average fares
st.subheader("Average Fare per Travel Class")

with st.container():
  col1, col2 = st.columns(2)

  # Pivot Table - Average Fares by Travel Class
  with col1:
    st.write(f"##### Pivot Table - Average Fare ({selected_gender if selected_gender != 'All' else 'All Genders'})")
    pivot_df = filtered_df.pivot_table(index="Pclass", values="Fare", aggfunc="mean")
    st.dataframe(pivot_df.style.format("{:.2f} €"))  # Formatting fares in euros

  # Bar Chart for Average Fares
  with col2:
    st.write(f"##### Average Fare by Travel Class ({selected_gender if selected_gender != 'All' else 'All Genders'})")
    fig3, ax3 = plt.subplots()
    ax3.bar(pivot_df.index, pivot_df["Fare"], color=['green', 'yellow', 'red'])
    ax3.set_xlabel("Travel Class")
    ax3.set_ylabel("Average Fare (€)")
    ax3.set_title("Average Fare per Travel Class")
    ax3.set_xticks(pivot_df.index)
    st.pyplot(fig3)
