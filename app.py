import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

# ✅ Set API key securely
GOOGLE_API_KEY = "your api key"  # 🔴 Replace with your actual API key for security concern i did not mentioned my api key here
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY  # ✅ Store API key in environment

# ✅ Initialize LangChain's Google GenAI Model
llm = GoogleGenerativeAI(model="gemini-1.5-pro")

# ✅ Streamlit UI
st.set_page_config(page_title="AI Travel Planner", layout="centered")
st.title("🌍 AI-Powered Travel Planner")
st.write("Find the best travel options between two locations.")

# ✅ User Inputs
source = st.text_input("Enter source location:")
destination = st.text_input("Enter destination:")

# ✅ Define Prompt with LangChain
prompt_template = PromptTemplate(
    input_variables=["source", "destination"],
    template="""
    You are an AI travel planner. Suggest the best travel options between {source} and {destination}.
    Consider options like flights, trains, buses, and taxis with estimated costs.
    Provide a well-structured response.
    """
)

def get_travel_options(source, destination):
    """Fetch travel options using LangChain's Google GenAI."""
    try:
        prompt = prompt_template.format(source=source, destination=destination)
        response = llm(prompt)
        return response if response else "No travel data available."
    except Exception as e:
        return f"Error fetching travel options: {str(e)}"

# ✅ Button to Generate Travel Options
if st.button("Find Travel Options"):
    if source and destination:
        with st.spinner("Fetching best travel routes..."):
            response = get_travel_options(source, destination)
            st.success("Travel recommendations fetched!")
            st.write(response)
    else:
        st.warning("Please enter both source and destination.")
