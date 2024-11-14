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


st.write(
    """
         Welcome,
         
         This app is an example of how to get User Authentication and page wise authorization in a Streamlit multi-page app using AWS Cognito 🚀! 
         """
)


if not st.session_state["authenticated"]:
    st.write("you are connected as a guest user")
else:
    st.write("you are connected as " + st.session_state["user_name"])
