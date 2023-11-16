import streamlit as st
import pandas as pd

table = pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})
# hidden hamburger and footPage text
st.markdown("""
<style>
.st-emotion-cache-iiif1v
{
    visibility: hidden;
}
.st-emotion-cache-h5rgaw
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
st.title("Hi, I am Streamlit Web App")
st.subheader("Hi! I am your Subheader")
st.header("I am header")
st.text("Hi I am text function and programmers uses me inplace of paragraph")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.latex(r"\begin{pmatrix}a & b \\c & d\end{pmatrix}")
json = {"a": "1,2,3","b":"4,5,6"}
st.json(json)
code = """
print("hello world")
def funct():
    return 0;"""
st.code(code,"python")
st.write("## H2")

# value = "120ms\^-1"
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")

# table is just like a static table
st.table(table)

# data frame provide sort function
st.dataframe(table)

def change():
    print("Changed")
    print(st.session_state.checker)
state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")

if state:
    st.write("Hi")
else:
    pass

radio = st.radio(label="In which Country do you live?", options=["US","UK","Canada"])
print(radio)