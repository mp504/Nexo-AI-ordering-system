
## Overview
Nexo is an AI-powered food ordering assistant that lets users search restaurant menus via voice or text input. Built with Streamlit, it analyzes CSV datasets (items.csv and restaurants.csv) using OpenAI's GPT-3.5 Turbo and LangChain to recommend top food matches with their respective restaurants. Perfect for quick, voice-enabled food discovery!
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
```bash
pip install streamlit openai pandas langchain audio_recorder_streamlit
```

## Configuration
1. Add OpenAI API key to environment:
```bash
export OPENAI_API_KEY=\"your-api-key\"
```

2. Prepare data files:
- items.csv
- restaurants.csv 
- item_images/

## Usage
```bash
streamlit run project.py
```

## Project Structure
```
├── project.py
├── data/
│   ├── items.csv
│   └── restaurants.csv
└── item_images/
```

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


