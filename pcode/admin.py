"""Admin dashboard to view the results"""

import pandas as pd
import streamlit as st

from pcode.validation import check_password


def login_screen():
    """Asks for password."""
    st.title("Admin Login")
    password = st.text_input(
        "Enter admin password",
        type="password"
    )

    if st.button("Log In"):
        try:
            stored_password = st.secrets["ADMIN_PASSWORD_HASH"]
        except Exception:
            st.error("Admin password is not configured")
            return

        if check_password(password, stored_password):
            st.session_state.admin_logged_in = True
            st.rerun()
        else:
            st.error("Incorrect password")


def dashboard(attempts):
    """Show all attempts and lets them get downloaded"""
    st.title("Admin Dashboard")

    if len(attempts) == 0:
        st.write("No quiz results found")
        return

    results = pd.DataFrame(attempts)

    st.write("Total Attempts: " + str(len(results)))
    st.dataframe(results)

    csv_file = results.to_csv(index=False)

    st.download_button(
        "Download Results",
        csv_file,
                "quiz_results.csv",
        "text/csv"
    )