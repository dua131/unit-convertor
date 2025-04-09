import streamlit as st # type: ignore

# App title
st.title("Unit Converter App")

# Unit conversion types
conversion_types = ["Length", "Weight", "Temperature"]

# User selects conversion type
conversion_choice = st.selectbox("Choose conversion type:", conversion_types)

# Length conversion
if conversion_choice == "Length":
    length_units = ["Meter", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("Enter length value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", length_units)
    to_unit = st.selectbox("To unit:", length_units)

    # Conversion dictionary for length
    length_conversion = {
        "Meter": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }

    # Conversion logic
    if st.button("Convert"):
        if from_unit != to_unit:
            result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
            st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.warning("From and To units are the same. No conversion needed.")

# Weight conversion
elif conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("Enter weight value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", weight_units)
    to_unit = st.selectbox("To unit:", weight_units)

    # Conversion dictionary for weight
    weight_conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    # Conversion logic
    if st.button("Convert"):
        if from_unit != to_unit:
            result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
            st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.warning("From and To units are the same. No conversion needed.")

# Temperature conversion
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter temperature value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit:", temperature_units)
    to_unit = st.selectbox("To unit:", temperature_units)

    # Conversion function for temperature
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value

    # Conversion logic for temperature
    if st.button("Convert"):
        if from_unit != to_unit:
            result = convert_temperature(input_value, from_unit, to_unit)
            st.success(f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')
        else:
            st.warning("From and To units are the same. No conversion needed.")