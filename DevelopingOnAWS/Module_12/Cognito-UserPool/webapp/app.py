import components.authenticate as authenticate
import streamlit as st

# Check authentication when user lands on the home page.
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

# st.session_state

# with st.echo("below"):

st.write(
    """
         Welcome,
         
         This app is an example of how to get User Authentication and page wise authorization in a Streamlit multi-page app using AWS Cognito 🚀! 
         """
)
