import streamlit as st

st.subheader("**Excel Dashboard Looking at Bike Sales**")
st.markdown("---")

# OneDrive embed code
onedrive_embed_code = '<iframe src="https://onedrive.live.com/embed?resid=E58CB34B19BFAEB6%2112073&authkey=!AE1qKv16rKrGJrw&em=2" width="800" height="600" frameborder="0" scrolling="no"></iframe>'

# Display the iframe using Streamlit
st.markdown(onedrive_embed_code, unsafe_allow_html=True)