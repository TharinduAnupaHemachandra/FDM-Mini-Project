import numpy as np
import pickle
import streamlit as st


import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
#add_bg_from_local('/app/wp5.jpg')




# loading the saved model
loaded_model = pickle.load(open('/app/models/FD-AdaBoostClassifier.sav', 'rb'))


# creating a function for Prediction

def cancellation_policy(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    cancellation_policy = loaded_model.predict(input_data_reshaped)
    #print(cancellation_policy)

    policy = ''

    if cancellation_policy[0] == 1:
        policy = 'Moderate'
    elif cancellation_policy[0] == 2:
        policy = 'Flexible'
    else:
        policy == 'Strict'

    print(policy)

    #return "Cancellation Policy is" + str(cancellation_policy)
    return policy


# if (predicted_price[0] == 0):
#	return 'The person is not diabetic'
# else:
#	return 'The person is diabetic'

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


def main():
    # giving a title
    # st.title('Cancellation Policy Prediction')
    st.markdown("<h1 style='text-align: center; color: white;'>Cancellation Policy Prediction</h1>",
                unsafe_allow_html=True)

    # getting the input data from the user

    accommodates = st.text_input('Number of Accommodates')

    availability_30 = st.radio('Availability in next 30 days',
                               ('Available', 'Not Available'))

    if availability_30 == 'Available':
        availability_30 = 1
    else:
        availability_30 = 0

    bathrooms = st.text_input('Bathrooms')

    bed_type_Couch = 0
    bed_type_Futon = 0
    bed_type_Pull_out_Sofa = 0
    bed_type_Real_Bed = 0
    bed_type_Airbed = 0

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    bed_type = st.radio(
        "Select the Bed Type",
        ('Real Bed', 'Futon', 'Airbed', 'Couch', 'Pull Out Sofa'))

    # specifying what should be display when the radio button is selected
    if bed_type == 'Real Bed':
        bed_type_Real_Bed = 1
    elif bed_type == 'Futon':
        bed_type_Futon = 1
    elif bed_type == 'Airbed':
        bed_type_Airbed = 1
    elif bed_type == 'Couch':
        bed_type_Couch = 1
    else:
        bed_type_Pull_out_Sofa = 1

    bedrooms = st.text_input('Bedrooms')
    beds = st.text_input('Beds')

    guests_included = st.text_input('Number of guests that can be included')

    instant_bookable_f = 0
    instant_bookable_t = 0

    instant_bookable = st.radio(
        "Select whether this is Instant Bookable",
        ('Yes', 'No'))

    if instant_bookable == 'Yes':
        instant_bookable_t = 1
    else:
        instant_bookable_f = 1

    maximum_nights = st.text_input('maximum_nights')

    property_type_Apartment = 0
    property_type_Bed_Breakfast = 0
    property_type_Boat = 0
    property_type_Bungalow = 0
    property_type_Cabin = 0
    property_type_Camper_RV = 0
    property_type_Chalet = 0
    property_type_Condominium = 0
    property_type_Earth_House = 0
    property_type_House = 0
    property_type_Hut = 0
    property_type_Loft = 0
    property_type_Other = 0
    property_type_Tent = 0
    property_type_Tipi = 0
    property_type_Townhouse = 0
    property_type_Treehouse = 0
    property_type_Villa = 0

    property_type = st.radio(
        'Property Type',
        ('House', 'Camper/RV', 'Bed & Breakfast', 'Apartment', 'Townhouse', 'Condominium', 'Cabin', 'Loft', 'Villa',
         'Boat', 'Bungalow', 'Chalet', 'Earth House', 'Hut', 'Tent', 'Tipi', 'Treehouse', 'Other')
    )

    if property_type == 'House':
        property_type_House = 1
    elif property_type == 'Camper/RV':
        property_type_Camper_RV = 1
    elif property_type == 'Bed & Breakfast':
        property_type_Bed_Breakfast = 1
    elif property_type == 'Apartment':
        property_type_Apartment = 1
    elif property_type == 'Townhouse':
        property_type_Townhouse = 1
    elif property_type == 'Condominium':
        property_type_Condominium = 1
    elif property_type == 'Cabin':
        property_type_Cabin = 1
    elif property_type == 'Loft':
        property_type_Loft = 1
    elif property_type == 'Villa':
        property_type_Villa = 1
    elif property_type == 'Boat':
        property_type_Boat = 1
    elif property_type == 'Bungalow':
        property_type_Bungalow = 1
    elif property_type == 'Chalet':
        property_type_Chalet = 1
    elif property_type == 'Earth House':
        property_type_Earth_House = 1
    elif property_type == 'Hut':
        property_type_Hut = 1
    elif property_type == 'Tent':
        property_type_Tent = 1
    elif property_type == 'Tipi':
        property_type_Tipi = 1
    elif property_type == 'Treehouse':
        property_type_Treehouse = 1
    else:
        property_type_Other = 1

    room_type_Entire_home_apt = 0
    room_type_Private_room = 0
    room_type_Shared_room = 0

    # room_type = st.text_input('room_type')
    room_type = st.selectbox(
        'Room Type',
        ('Private room', 'Entire home/apt', 'Shared room')
    )

    if room_type == 'Private room':
        room_type_Private_room = 1
    elif room_type == 'Entire home/apt':
        room_type_Entire_home_apt = 1
    else:
        room_type_Shared_room = 1

    price = st.text_input('Price')

    # creating a button for Prediction

    # code for Prediction
    cancellation = ''

    if st.button('Predict the Cancellation Policy'):
        cancellation = cancellation_policy(
            [accommodates, availability_30,
             bathrooms, bedrooms, beds,
             guests_included, maximum_nights, bed_type_Airbed, bed_type_Couch,
             bed_type_Futon, bed_type_Pull_out_Sofa, bed_type_Real_Bed,
             instant_bookable_f, instant_bookable_t, property_type_Apartment, property_type_Bed_Breakfast,
             property_type_Boat, property_type_Bungalow,
             property_type_Cabin, property_type_Camper_RV, property_type_Chalet, property_type_Condominium,
             property_type_Earth_House, property_type_House, property_type_Hut, property_type_Loft,
             property_type_Other, property_type_Tent, property_type_Tipi, property_type_Townhouse,
             property_type_Treehouse, property_type_Villa, room_type_Entire_home_apt, room_type_Private_room,
             room_type_Shared_room, price])

    st.success(cancellation)


if __name__ == '__main__':
    main()
