# import os
# import streamlit as st
# import pandas as pd
# import numpy as np
# import warnings
# from langchain.agents.agent_types import AgentType
# from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
# from langchain_openai import ChatOpenAI

# os.environ['OPENAI_API_KEY'] = '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'

# def create_langchain_agent():
#     df = pd.read_csv(".dist/Anime_list.csv")
#     agent = create_pandas_dataframe_agent(
#         ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
#         df,
#         verbose=False,
#         agent_type=AgentType.OPENAI_FUNCTIONS,
#         agent_executor_kwargs={"handle_parsing_errors": True}
#     )
#     return agent

# def func_langchain(agent, query):
#     result = agent.run(query)
#     return result

# def chatbot_call(dataset):
#     warnings.filterwarnings("ignore")

#     st.title("Research Assistant")

#     # Load Langchain agent
#     langchain_agent = create_langchain_agent()

#     # Upload dataset
#     uploaded_file = dataset
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         langchain_agent = create_pandas_dataframe_agent(
#             ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
#             df,
#             verbose=False,
#             agent_type=AgentType.OPENAI_FUNCTIONS,
#             agent_executor_kwargs={"handle_parsing_errors": True}
#         )

#     # User input for the query
#     query = st.text_input("Enter a query:")

#     # Execute Langchain function on button click
#     if st.button("Submit"):
#         result = func_langchain(langchain_agent, query)
#         st.text("Result:")
#         st.write(result)


import os
import streamlit as st
import pandas as pd
import warnings
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent 
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = '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'

def create_langchain_agent(df):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        df,
        verbose=False,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )
    return agent

def func_langchain(agent, query):
    result = agent.run(query)
    return result

def suggest_questions(agent):
    suggested_questions = agent.run("Suggest 5 analytical questions regarding this dataset")
    return suggested_questions.split("\n")

def chatbot_call(dataset):
    warnings.filterwarnings("ignore")

    st.title("Research Assistant")

    uploaded_file = dataset
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        langchain_agent = create_langchain_agent(df)
    
        suggested_questions = suggest_questions(langchain_agent)

        st.write("Suggested questions:")
        for question in suggested_questions:
            if question:
                if st.button(question):
                    result = func_langchain(langchain_agent, question)
                    st.text("Result:")
                    st.success(result)  # Display result in a success box

        query = st.text_input("Enter a query:")

        if st.button("Submit"):
            result = func_langchain(langchain_agent, query)
            st.text("Result:")
            st.success(result)  # Display result in a success box

if __name__ == "__main__":
    chatbot_call()