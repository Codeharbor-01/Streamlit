import streamlit as st

st.title('Electricity Price Calculator')

col1,col2 = st.columns(2)

fN = col1.text_input('First Name',placeholder='John')
lN = col2.text_input('Last Name',placeholder='Doe')

elec_consumption = st.number_input('Electricity Consumption in KWh',min_value=0)

button = st.button(label = 'Calculate')

if button:
    if not (fN and lN and elec_consumption):
        st.error('All fields are mandatory!')
    else:
        if 0<elec_consumption<=20:
            ppu = 4
        elif 21<=elec_consumption<=30:
            ppu = 6.5
        elif 30<=elec_consumption<=50:
            ppu= 10
        elif elec_consumption>50:
            ppu = 12

        total_price = elec_consumption*ppu

        st.header('Calculated Fields')
        df = st.dataframe({
            'First Name':fN,
            'Last Name':lN,
            'Total Electricity consumption':elec_consumption,
            'Total Amount':[total_price]
        })