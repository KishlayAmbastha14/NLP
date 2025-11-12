import streamlit as st
import joblib

model = joblib.load("spam_model.pkl")

st.markdown("""

    <h1 style='color: #A72C43;'>Spam Classifier Project</h1>

""",unsafe_allow_html=True)

st.markdown("""
    <style>
    .stTextArea textarea {
        color: white;           /* Navy Blue text */
        font-size: 22px;          /* Slightly smaller for readability */
        background-color: black; /* Very light blue background */
        border-radius: 8px;       /* Rounded corners */
        padding: 10px;            /* Inner spacing */
    }
    </style>
""", unsafe_allow_html=True)



input_text = st.text_area("Enter the email/message",height=250)

if st.button("Check is Spam/Not Spam"):
  if input_text.strip() == "":
    st.warning("Plese enter the text")

  else:
    # vectorized_input = tfidf.transform([input_text])
    # prediction = model.predict(vectorized_input)
    prediction = model.predict([input_text])

    if prediction[0] == 1:
      st.error("This is SPAM")
    else:
      st.success("This is NOT SPAM")