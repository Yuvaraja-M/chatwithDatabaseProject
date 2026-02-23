import os
import sqlite3
from pathlib import Path

import streamlit as st
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_openai import AzureChatOpenAI

# ---------------- UI ----------------
st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("LangChain chat with DB")

LOCALDB = "USE_LOCALDB"
radio_opt = ["Use SQLite3 Database - student.db", "Connect to your SQL Database"]
selected_opt = st.sidebar.radio(
    label="Choose the DB you want to chat",
    options=radio_opt,
    index=0
)
os.environ["AZURE_OPENAI_API_KEY"] = "XXXXXXXX"
os.environ["AZURE_OPENAI_ENDPOINT"] = "XXXXXXXX"
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "XXXXXXXX"

# Collect Azure OpenAI config (avoid hardcoding secrets)
api_key = st.sidebar.text_input("Azure OpenAI API key", type="password")
endpoint = st.sidebar.text_input(
    "Azure OpenAI Endpoint",
    value=os.getenv("AZURE_OPENAI_ENDPOINT", "XXXXXX")
)
api_version = st.sidebar.text_input(
    "Azure OpenAI API version",
    value=os.getenv("OPENAI_API_VERSION", "2025-01-01-preview")
)
deployment = st.sidebar.text_input(
    "Azure deployment name",
    value=os.getenv("OPENAI_DEPLOYMENT_NAME", "IBG-GPT4-SI")
)

if not api_key:
    st.info("Please add the Azure API key in the sidebar to start.")

# ---------------- LLM ----------------
llm = AzureChatOpenAI(
    openai_api_version=api_version,
    azure_deployment=deployment,
    temperature=0.2,
    verbose=True,
    streaming=True,
)

# ---------------- DB ----------------
@st.cache_resource(ttl=7200)  # TTL must be integer seconds
def configure_db(use_local: bool = True):
    if use_local:
        dbfilepath = (Path.cwd() / "student.db").absolute()
        st.write(f"Using DB: {dbfilepath}")
        # Correct SQLite URI (no space after 'file:')
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
        engine = create_engine("sqlite:///", creator=creator)
        return SQLDatabase(engine)
    else:
        st.stop()

use_local = (selected_opt == "Use SQLite3 Database - student.db")
db = configure_db(use_local)

# ---------------- Agent ----------------
st.subheader("SQL Agent")
from langchain_community.agent_toolkits import SQLDatabaseToolkit

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

tools = toolkit.get_tools()
for tool in tools:
    print(f"{tool.name}: {tool.description}\n")

system_prompt = """
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most {top_k} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

You MUST double check your query before executing it. If you get an error while
executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
database.

To start you should ALWAYS look at the tables in the database to see what you
can query. Do NOT skip this step.

Then you should query the schema of the most relevant tables.
""".format(
    dialect=db,
    top_k=5,
)
from langchain.agents import create_agent
agent = create_agent(
    llm,
    tools,
    system_prompt=system_prompt,
)
# question = "name the all students out there?"

# for step in agent.stream(
#     {"messages": [{"role": "user", "content": question}]},
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()

if "messages" not in st.session_state:
    st.session_state["messages"] = []
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
if user_query := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)
    
    with st.spinner('Thinking...'):
        response = agent.invoke(
            {"messages": st.session_state.messages}
        )
        msg = response["messages"][-1].content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

