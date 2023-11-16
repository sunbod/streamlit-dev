import streamlit as st
import base64
import time as ts
from datetime import time as time

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
st.title("Upload Files")
st.markdown("---")
image = st.file_uploader("Please upload an image",["png","jpg"],key="imageUpload")
if image is not None:
    st.image(image)

pdf = st.file_uploader("Please upload your pdf",["pdf"],key="pdfUpload")
if pdf is not None:
    base64_pdf = base64.b64encode(pdf.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display,unsafe_allow_html=True)

mht = st.file_uploader("please upload an mht","mht",key="mhtupload")
if mht is not None:
    bytes_data = mht.getvalue()
    st.write(bytes_data)

def changes():
        print(st.session_state.val)
st.slider("please select a value",value=50,on_change=changes,key="val")


def converter(value):
     m,s,mm = value.split(":")
     t_s = int(m)*60+int(s)+int(mm)/1000
     return t_s


val = st.time_input("Set your time", value=time(0, 0, 0))
if str(val) == "00:00:00":
    st.write("Please sent timer")
else:
    sec = converter(str(val))
    print(sec)
    bar = st.progress(0)
    per = sec/100
    progress_status = st.empty()
    progress_status2 = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1)+"%")
        progress_status2.write()
        ts.sleep(per)