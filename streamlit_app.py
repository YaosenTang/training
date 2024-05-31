import streamlit as st

# Initialize session state for phrases if not already set
if 'phrases' not in st.session_state:
    st.session_state.phrases = ["Example phrase 1", "Example phrase 2", "Example phrase 3"]

st.title("Edit and Sort Phrases")

st.write("### Edit your phrases below:")

# Create a text area for each phrase
for i in range(len(st.session_state.phrases)):
    st.session_state.phrases[i] = st.text_input(f"Phrase {i + 1}", value=st.session_state.phrases[i], key=f"phrase_{i}")

# Add a button to sort the phrases
if st.button("Sort Phrases"):
    st.session_state.phrases.sort()
    st.success("Phrases sorted!")

# Display the current list of phrases
st.write("### Current Phrases:")
for phrase in st.session_state.phrases:
    st.write(phrase)
