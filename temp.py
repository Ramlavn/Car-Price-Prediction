import streamlit as st
import pandas as pd
import datetime
import pickle
from sklearn.ensemble import GradientBoostingRegressor as gbr

def main():
    author_name = "Your Name"  # Replace "Your Name" with your actual name
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    html_temp = """
    <div style="text-align:left;">
        <p style="font-size: 14px; color: ##888888;">Author: Ramlavan</p>
        <p style="font-size: 14px; color: #8888888;">Date: """ + current_date + """</p>
    </div>
    <div style="background-color:#6495ED;padding:10px">
        <h2 style="color:white;text-align:center;">Car Price Prediction</h2>
    </div>
    <br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    path_to_file = r'car_price_predictor.pkl'  # Update this line with the correct path
    
    # Load the trained model
    with open(path_to_file, 'rb') as f:
        model = pickle.load(f)

    st.markdown("###### Are you planning to sell your car!?\n###### So let's try evaluating the price.")
    
    st.write('')
    st.write('')
    
    p1 = st.number_input("Ex-Showroom price of the car (In Lakhs)", 2.5, 25.0, step=1.0)
    p2 = st.number_input("Distance completed by the car (In Kms)", 100, 500000, step=100)
    
    s1 = st.selectbox("Fuel type of the car?", ('Petrol', 'Diesel', 'CNG'))
    
    if s1 == 'Petrol':
        p3 = 0
    elif s1 == 'Diesel':
        p3 = 1
    elif s1 == 'CNG':
        p3 = 2
        
    s2 = st.selectbox("Dealer or Individual", ('Dealer', 'Individual'))
    
    if s2 == 'Dealer':
        p4 = 0
    elif s2 == 'Individual':
        p4 = 1
        
    s3 = st.selectbox("Transmission Type?", ('Manual', 'Automatic'))
    
    if s3 == 'Manual':
        p5 = 0
    elif s3 == 'Automatic':
        p5 = 1
        
    p6 = st.slider("No. of owners the car previously had?", 0, 3)
    
    years = st.number_input("Car Purchase year?", 1990, datetime.datetime.now().year)
    p7 = datetime.datetime.now().year - years
    
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'age': p7
    }, index=[0])
    
    if st.button('Predict'):
        try:
            pred = model.predict(data_new)
            st.success('You can sell your car for {:.2f} lakhs'.format(pred[0]))
        except Exception as e:
            st.error(f"Error making prediction: {e}")

if __name__ == '__main__':  
    main()
