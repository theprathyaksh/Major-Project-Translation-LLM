from datasets import load_dataset
# importing the libraries
import streamlit as st
import os
import openai
# Entere your openAI key here
openai.api_key = "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"

# Define the list of available languages
languages = [
    "English",
    "Hindi",
    "French",
    "Telugu",
    "Albanian",
    "Bengali",
    "Bhojpuri",
    # Add more languages as needed, if you want
    ]
    
# creating a function.

def translate_text(text, source_language, target_language):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt = (
    f"Translate the following text from {source_language} "
    f"to {target_language}:\n{text}"
),

        max_tokens=100,
        n=1,
        stop=None,
        temperature=0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    translation = response.choices[0].text.strip().split("\n")[0]
    return translation

# Streamlit web app
def main():
    st.title("Translate My Text")

    # Input text
    text = st.text_area("Enter the text to translate")

    # Source language dropdown to select the languages
    source_language = st.selectbox("Select source language", languages)

    # Target language dropdown to select the languages
    target_language = st.selectbox("Select target language", languages)

    # Translate button to translate
    if st.button("Translate"):
        translation = translate_text(text, source_language, target_language)
       
        st.markdown(f'<p style="color: blue; font-size: 25px;">{translation}</p>', unsafe_allow_html=True)



if __name__ == '__main__':
    main()
