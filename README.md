# ✈️ AI-Powered Travel Planner

**AI-Powered Travel Planner** is a smart itinerary generator that uses AI to help users plan their trips based on destination, budget, and travel duration. Developed by **Pratyush Paradarshi Patra**, this project leverages OpenAI's language model API to build personalized travel experiences quickly and efficiently.

![Python](https://img.shields.io/badge/Built%20With-Python-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![AI](https://img.shields.io/badge/Powered%20By-OpenAI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🧠 Features

- 🗺️ Generates day-wise travel itineraries using AI  
- 🎯 Takes input like location, number of days, and budget  
- 🧠 Uses OpenAI GPT for smart text generation  
- 🖥️ Clean and responsive UI using HTML, CSS, and Bootstrap  
- 🔒 Secure API integration via environment variables

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python, Flask  
- **AI Engine**: OpenAI GPT API  
- **Others**: Git, GitHub, .env config

---
Create .env file and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key
Then run the app:
python app.py
Visit: http://127.0.0.1:5000/

💡 How It Works
User fills in travel destination, budget, and number of days

Flask backend sends prompt to OpenAI GPT API

AI returns a complete, formatted travel plan

UI displays the custom itinerary

🌍 Use Case
This app is perfect for solo travelers, backpackers, or busy professionals who want smart and fast travel suggestions without having to manually search through blogs or travel agents.
## 🚀 How to Run Locally

```bash
git clone https://github.com/pratyush-1235/AI-POWERED-TRAVEL-PLANNER.git
cd AI-POWERED-TRAVEL-PLANNER
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
'''


