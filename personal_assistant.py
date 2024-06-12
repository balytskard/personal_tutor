import openai
import streamlit as st

openai.api_key = st.secrets['openai']['api_key']


def get_answer(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ],
    )

    return response.choices[0].message['content'].strip()


st.title("Chat with GPT-3.5 Turbo")
user_input = st.text_input("What would you like to know today?")


if user_input:
    with st.spinner("Generating response..."):
        output = get_answer(user_input)
        st.success(output)


if st.button("Clear"):
    st.experimental_rerun()
