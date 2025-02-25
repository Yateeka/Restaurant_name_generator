import streamlit as st
import lang_chain_helper  # Ensure this is your helper script file

# Streamlit App Title
st.title("Restaurant Name Generator")

# Sidebar for Cuisine Selection
cusine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Lebanese", "Australian")
)

# Generate Name and Menu when a Cuisine is Selected
if cusine:
    # Call the helper function
    response = lang_chain_helper.generate_restaurant_name_items(cusine)

    # Display Restaurant Name
    restaurant_name = response.get("restaurant_name")
    st.header(restaurant_name.strip())

    # Display Menu Items
    menu_items = response.get("menu", "").strip().split("\n")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(f"- {item.strip()}")
