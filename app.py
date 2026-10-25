import streamlit as st
from engine import run_inference_engine
st.title("Rule-Based Movie Recommendation System")
st.markdown("**RTC Dhangawadi 2026-27 - AI Mini-Project**")
st.sidebar.header("User Preference Profile")
g=st.sidebar.selectbox("Genre",["Sci-Fi","Mystery","Comedy"])
m=st.sidebar.selectbox("Mood",["Thought-Provoking","Exciting","Lighthearted"])
p=st.sidebar.selectbox("Pace",["Fast","Slow","Moderate"])
t=st.sidebar.selectbox("Type",["Movie","TV Show"])
if st.sidebar.button("Run Inference Engine"):
    res=run_inference_engine(t,g,m,p)
    if not res: st.warning("No match found")
    for i,r in enumerate(res,1):
        with st.expander(f"{i}. {r['title']} | Score:{r['score']} Rating:{r['rating']}"):
            st.write(f"Genre: {r['genre']}")
            for tr in r["trace"]: st.success(tr)
else:
    st.info("Sidebar se select karke Run button dabao")