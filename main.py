import streamlit as st 
import pandas as pd

st.title("Prompt-driven data analysis with PandasAI")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    # new code below...
    prompt = st.text_area("Enter your prompt:")

    # Generate output
    if st.button("Generate"):
        if prompt:
            st.write("Generating response...")
        else:
            st.warning("Please enter a prompt.")


from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

# create an LLM by instantiating OpenAI object, and passing API token
#llm = OpenAI(api_token="sk-YOUR_KEY_HERE")
model_name = "gpt-3.5-turbo"
# model_name = "gpt-4"
llm = OpenAI(model_name=model_name, openai_api_key = st.secrets["openai_api_key"], streaming=True)

# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(3))
        prompt = st.text_area("Enter your prompt:")

    # Generate output
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")
