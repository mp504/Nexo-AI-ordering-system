# Create project structure
mkdir OrderSystem
cd OrderSystem
mkdir data
mkdir item_images

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install streamlit openai pandas langchain audio_recorder_streamlit langchain-experimental

# Create necessary files
echo "# Nexo - AI-Powered Food Ordering Assistant

## Overview
Intelligent food ordering system using voice commands and text chat with AI-powered recommendations.

## Features
- Voice ordering with real-time transcription
- Text-based chatbot interface  
- Smart menu recommendations
- Restaurant suggestions
- Image support for menu items

## Tech Stack
- **Frontend**: Streamlit
- **AI/ML**: 
  - OpenAI GPT-3.5
  - LangChain
  - RAG (Retrieval Augmented Generation)
- **Data**: 
  - Pandas
  - CSV storage
- **Audio**: audio_recorder_streamlit

## Installation
\`\`\`bash
pip install streamlit openai pandas langchain audio_recorder_streamlit
\`\`\`

## Configuration
1. Add OpenAI API key to environment:
\`\`\`bash
export OPENAI_API_KEY=\"your-api-key\"
\`\`\`

2. Prepare data files:
- items.csv
- restaurants.csv 
- item_images/

## Usage
\`\`\`bash
streamlit run project.py
\`\`\`

## Project Structure
\`\`\`
├── project.py
├── data/
│   ├── items.csv
│   └── restaurants.csv
└── item_images/
\`\`\`

## How It Works
1. Loads restaurant and menu data
2. Accepts voice/text input
3. Processes using LangChain + OpenAI
4. Returns recommendations and responses
5. Displays relevant menu images

## License
MIT

## Author
Mansour Alhamami" > README.md

# Create sample CSV files
echo "item_id,name,price,description,category,restaurant_id
1,Pizza,10.99,Delicious pizza,Italian,1
2,Burger,8.99,Juicy burger,American,2" > data/items.csv

echo "restaurant_id,name,cuisine,rating,location
1,Italian Place,Italian,4.5,Downtown
2,Burger Joint,American,4.2,Uptown" > data/restaurants.csv

# Set environment variable for OpenAI API key
setx OPENAI_API_KEY "your-api-key"

# Create .gitignore
echo "venv/
__pycache__/
.env
*.pyc
.DS_Store" > .gitignore

# Initialize git repository
git init
git add .
git commit -m "Initial commit"

echo "Project setup complete. Remember to:"
echo "1. Add your actual OpenAI API key"
echo "2. Add your menu item images to item_images/"
echo "3. Update CSV files with your actual data"
