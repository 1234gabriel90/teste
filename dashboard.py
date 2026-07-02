import streamlit as st

from database.supabase import supabase

st.title("Dashboard")

total = supabase.table("funcionarios").select(

    "*",

    count="exact"

).execute()

st.metric(

    "Funcionários",

    total.count

)