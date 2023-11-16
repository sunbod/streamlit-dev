import streamlit as st


# hidden hamburger and footPage text
st.markdown("""
<style>
.st-emotion-cache-czk5ss
{
    visibility: hidden;
}
.st-emotion-cache-h5rgaw
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>User Registration</h1>",unsafe_allow_html=True)
# form = st.form("Form 1")
# form.text_input("First Name")
# form.form_submit_button("提交")

with st.form("Form 2",clear_on_submit=True):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last  Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_status = st.form_submit_button("Submit")
    if s_status:
        if f_name == "" or l_name == "":
            st.warning("Please fill above fields")
        else:
            st.success("Submitted Successfully")