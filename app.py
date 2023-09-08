import streamlit as st
import time
import random

# Create a Streamlit web application
st.title("MEDTRAX - Smart Ambulance Routing and Navigation System")

# Select user role (Ambulance Driver or Traffic Police)
user_role = st.sidebar.radio("Select User Role", ("Ambulance Driver", "Traffic Police"))

# Define user credentials (replace with your actual authentication logic)
user_credentials = {
    "Ambulance Driver": {"username": "driver123", "password": "password1"},
    "Traffic Police": {"username": "police456", "password": "password2"},
}

# Initialize user input fields
st.subheader(f"{user_role} Login")  # Label for Ambulance Login or Police Login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Create a login button
if st.button("Log In"):
    if user_credentials.get(user_role, {}).get("username") == username and user_credentials.get(user_role, {}).get("password") == password:
        st.success(f"Welcome Back, {user_role}!")  # Welcome Back message
        st.session_state.user_authenticated = True  # Set user authentication status
    else:
        st.error("Invalid credentials. Please try again.")

# Check user authentication status and user role
if hasattr(st.session_state, "user_authenticated") and st.session_state.user_authenticated:
    if user_role == "Ambulance Driver":
        # Ambulance Driver Interface
        # Location toggle button
        location_toggle = st.checkbox("Toggle Location")

        # Severity selection (radio buttons)
        st.subheader("Select Severity")
        severity = st.radio("Severity:", ("Life-Threatening", "Emergency", "Urgent"))

        # Hospital name input field
        hospital_name = st.text_input("Hospital Name")

        # Submit button
        if st.button("Submit"):
            if location_toggle:
                st.success("Location is ON")
            else:
                st.warning("Location is OFF")

            st.success(f"Severity: {severity}")
            st.success(f"Hospital Name: {hospital_name}")

    elif user_role == "Traffic Police":
        # Traffic Police Interface with Ambulance Tracking
        st.subheader("Ambulance Tracking")
        
        # Simulate ambulance tracking with random coordinates (replace with actual tracking data)
        ambulance_latitude = random.uniform(12.9, 13.1)
        ambulance_longitude = random.uniform(77.5, 77.7)

        # Display ambulance location
        st.write(f"Ambulance Location: Latitude {ambulance_latitude}, Longitude {ambulance_longitude}")
        
        # Simulate real-time updates every 10 seconds
        while True:
            time.sleep(10)
            ambulance_latitude += random.uniform(-0.001, 0.001)
            ambulance_longitude += random.uniform(-0.001, 0.001)
            st.write(f"Ambulance Location: Latitude {ambulance_latitude}, Longitude {ambulance_longitude}")

# Run the Streamlit web app
if __name__ == "__main__":
    st.sidebar.title("Navigation")
    st.sidebar.info("Go to 'Streamlit Dev' or use 'streamlit run medtrax_web_app.py' in your terminal to launch this app.")

