# Nexo: Voice & Text Food Ordering Assistant 🍔🎤

An AI-powered assistant that helps users discover food items and restaurants by querying CSV datasets. Supports **voice** and **text input** to generate a curated list of dishes with restaurant details.

---

## Core Features ✨

### **Voice & Text Input**
- 🎤 Record orders via microphone (uses `audio_recorder_streamlit`).
- 📝 Type requests directly into the chat interface.
- 🔄 Voice recordings are transcribed using OpenAI’s Whisper model.

### **AI-Powered Analysis**
- 🤖 Uses **GPT-3.5 Turbo** and LangChain’s `pandas_dataframe_agent`.
- 📊 Queries two CSV datasets:
  - `items.csv`: Food menu items (e.g., dish names, prices).
  - `restaurants.csv`: Restaurant details (e.g., names, locations).

### **Dynamic Responses**
- 📋 Lists **top 8 matching items** per request.
- 🏠 Includes restaurant names for each dish.
- 🚫 Avoids disclosing internal dataset details (e.g., restaurant count).

---

## Technical Components ⚙️

### **Backend**
- OpenAI API for text generation (`gpt-3.5-turbo`) and speech-to-text (`whisper-1`).
- LangChain agents to interact with CSV data.
- Base64 image encoding (optional, commented out in code).

### **Frontend**
- Streamlit-based UI with a sidebar and main interaction panel.

---

## Use Case Example 💬
*User says*: *"Find me vegetarian sushi near downtown"*  
*Nexo responds*:  
1. Vegetarian Sushi Roll - Sushi Palace  
2. Avocado Maki - Tokyo Grill  
3. ... *(top 8 results)*  


---

## Setup & Usage 🚀

1. **Replace Placeholders**:
   - Add your OpenAI API key (replace `sk-proj-...` in the code).
   - Update CSV paths to your dataset locations.

2. **Run Locally**:
   ```bash
   streamlit run app.py
   ```
## Notes ⚠️

- 🔒 **Avoid exposing API keys in code** — Use `.env` files for production.  
- 📂 **Ensure CSVs have columns** matching the code’s expectations (e.g., `item_name`, `restaurant_id`).  
   
## Author
Mansour Alhamami


