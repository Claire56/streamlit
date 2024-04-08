import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# st.title("NUP Stripe Payments")

st.markdown("<h1 style='text-align: center; color: white;'>NUP Stripe Payments App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: red;'>Select desired visual from left menu</p>", unsafe_allow_html=True)
# Function to generate the DataFrame
def generate_dataframe():
    num_rows = 100
    states = np.random.choice(['Arizona', 'Arkansas', 'California', 'Colorado', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Illinois', 'Kansas',  'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Nevada', 'New Jersey',  'New York','Texas','Virginia', 'Washington'], num_rows)
    totals = np.random.uniform(100, 10000, num_rows)
    payment_counts = np.random.randint(1, 3, num_rows)
    return pd.DataFrame({
        'State': states,
        'Total': totals,
        'Payment_count': payment_counts
    })

# Generate the DataFrame
df = generate_dataframe()

# Streamlit app
# st.header('Select a visualization from the left menu')
# st.write('Select a visualization from the left menu')

# Sidebar for selecting the visualization type
visualization_type = st.sidebar.selectbox('Choose a visualization', ('Bar Chart', 'Pie Chart','All Charts'))

if visualization_type == 'Bar Chart':
    # Bar Chart for 'Total' by 'State'
    st.subheader('Total by State')
    st.bar_chart(df.groupby('State')['Total'].sum())

elif visualization_type == 'Pie Chart':
    # Pie Chart for Proportion of Total per State
    st.subheader('Proportion of Total per State')
    total_per_state = df.groupby('State')['Total'].sum()
    pie_chart_data = total_per_state / total_per_state.sum() * 100
    fig, ax = plt.subplots()
    ax.pie(pie_chart_data, labels=total_per_state.index, autopct='%1.1f%%')
    ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

elif visualization_type == 'All Charts':
    # Bar Chart for 'Total' by 'State'
    st.subheader('Total by State')
    st.bar_chart(df.groupby('State')['Total'].sum())

    # Pie Chart for Proportion of Total per State
    st.subheader('Proportion of Total per State')
    total_per_state = df.groupby('State')['Total'].sum()
    pie_chart_data = total_per_state / total_per_state.sum() * 100
    fig, ax = plt.subplots()
    ax.pie(pie_chart_data, labels=total_per_state.index, autopct='%1.1f%%')
    ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)


    # Line Chart for 'Payment_count' over 'State'
    st.subheader('Registration Payment by State')
    fig, ax = plt.subplots()
    for state in df['State'].unique():
        state_data = df[df['State'] == state]
        ax.plot(state_data['State'], state_data['Total'], label=state)
    ax.set_xlabel('State')
    ax.set_ylabel('Total')
    ax.legend()
    st.pyplot(fig)
