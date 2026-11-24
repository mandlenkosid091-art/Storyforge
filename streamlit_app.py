import streamlit as st

st.title("📖 StoryForge")
st.write("Create your own story!")

topic = st.text_input("What should your story be about?")

if st.button("Generate Story"):
    if not topic:
        topic = "a magical adventure"

    st.subheader("Your Story")
    st.write("Once upon a time, there was " + topic + ".")
    st.write("It was a wonderful day full of surprises.")
    st.write("And they all lived happily ever after. The End!")
