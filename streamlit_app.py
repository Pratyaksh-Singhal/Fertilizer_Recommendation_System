import streamlit as st

# Title of the web app
st.title('Fertilizer Recomendation System')

# First dropdown menu
option1 = st.selectbox(
    'Select Location',
    ('AJMER','ALWAR','BANSWARA','BARAN',' BARMER','BHARATPUR','BHILWARA','BIKANER','BUNDI','CHITTORGARH','CHURU','DAUSA','DHOLPUR','DUNGARPUR','GANGANAGAR','HANUMANGARH',
'JAIPUR','JAISALMER','JALORE','JHALAWAR','JHUNJHUNU','JODHPUR','KARAULI','KOTA','NAGAUR','PALI','PRATAPGARH','RAJSAMAND','S.MADHOPUR','SIKAR','SIROHI','TONK','UDAIPUR')
)

# Second dropdown menu
option2 = st.selectbox(
    'Select Season',
    ('KHARIF','RABI')
)

# Input boxes
input2 = st.text_input('Nitrogen (N) ', '')
input3 = st.text_input('Phosphorus (P)', '')
input4 = st.text_input('Potassium (K)', '')

# Button to submit inputs
submit_button = st.button('Predict')

# Display inputs on submit
if submit_button:
    st.write('Option 1 selected:', option1)
    st.write('Option 2 selected:', option2)
    st.write('Input 2:', input2)
    st.write('Input 3:', input3)
    st.write('Input 4:', input4)

