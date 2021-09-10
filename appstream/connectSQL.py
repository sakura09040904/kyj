import streamlit as st
import mysql.connector

@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock":lambda _: None})

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("select * from mypet;") 

for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
