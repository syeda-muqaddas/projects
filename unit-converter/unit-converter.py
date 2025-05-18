import streamlit as st  # Import Streamlit for creating the web-based UI


# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g., temperature conversion), call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined


  # Streamlit UI setup
   # Centered title using Markdown and HTML
st.markdown("<h1 style='text-align: center;'>🔄 Simple Unit Converter</h1>", unsafe_allow_html=True) # set tittle for the web app
  # User input: numerical value to convert
     # Bold text using **
value = st.number_input("**Enter value:**", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "**Convert from:**", ["meters", "kilometers", "grams", "kilograms"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("**Convert to:**", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
# Custom styling using Streamlit's built-in features
st.markdown("""
    <style>
    .stButton>button {
        color: black;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 15px;
        border-radius: 5px;
        border: yes;
        cursor: pointer;
        transition: transform 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color:lightblue;
        transform: scale(1.1); /* Slightly enlarges button */
    }
    </style>
""", unsafe_allow_html=True)

# Button with enhanced UI
if st.button("🚀**Convert**"):
    with st.spinner("Converting..."):
        result = convert_units(value, unit_from, unit_to)  # Call your function
        st.success(f"✅ Converted Value: {result}")  # Display result