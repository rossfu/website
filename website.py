import streamlit as st

st.write("""# Introducing Ross Fu!!""")
st.write("*Hello World!!!*")
st.write("*Welcome to my website!!!!*")


# Title
st.title('Data Science Showcase')


# Set page config
st.set_page_config(
    page_title="Visually Stunning Website",
    page_icon=":art:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Main title
st.title("Welcome to a Visually Stunning Website")

# Header image
st.image("https://source.unsplash.com/random/800x300", use_column_width=True)

# Subheader
st.subheader("Discover the beauty of data visualization")

# Introduction
st.write(
    "This website is designed to showcase the beauty of data visualization "
    "and the power of storytelling through interactive graphics. Explore "
    "the visualizations below to experience the magic of data."
)

# Spacer
st.write("")

# Section titles
st.markdown("## 1. Stunning Charts")
st.markdown("## 2. Engaging Maps")
st.markdown("## 3. Interactive Dashboards")

# Section 1: Stunning Charts
st.markdown("### 1. Stunning Charts")
st.write(
    "From elegant line plots to vibrant scatter plots, our visualizations are "
    "crafted with precision to convey insights at a glance."
)
# Add your stunning charts here

# Section 2: Engaging Maps
st.markdown("### 2. Engaging Maps")
st.write(
    "Explore the world through captivating maps that bring data to life. "
    "From choropleth maps to interactive markers, the possibilities are endless."
)
# Add your engaging maps here

# Section 3: Interactive Dashboards
st.markdown("### 3. Interactive Dashboards")
st.write(
    "Immerse yourself in our interactive dashboards that allow you to "
    "slice and dice data effortlessly. Customize your view and uncover hidden insights."
)
# Add your interactive dashboards here

# Footer
st.write(
    "Thank you for visiting our visually stunning website! 🎨✨"
    " Stay tuned for more captivating visualizations."
)
