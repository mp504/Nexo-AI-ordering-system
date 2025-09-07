import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
import os
import base64
from langchain_community.chat_models import ChatOpenAI




api_key = "API key"

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-1106", openai_api_key=api_key)
items_df = pd.read_csv("/path/items.csv")
restaurants_df = pd.read_csv("path/restaurants.csv")



def images_base64():


    # Specify the directory containing your images
    image_directory = "path/item_images"

    # Get a list of image filenames
    image_files = os.listdir(image_directory)

    # Initialize an empty DataFrame
    df = pd.DataFrame(columns=["ImageName", "Base64String"])

    # Iterate through each image file
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        with open(image_path, "rb") as f:
            # Read the image file and encode it as base64
            base64_string = base64.b64encode(f.read()).decode("utf-8")
            # Append the image name and base64 string to the DataFrame
            df = df.append({"ImageName": image_file, "Base64String": base64_string}, ignore_index=True)


    return df

#images_df = images_base64()

  

#initializing openai client
def setup_openai_client(api_key):

 return openai.OpenAI(api_key= api_key)



def create_openai_agent():
  

  agent = create_pandas_dataframe_agent(
    llm,
    [items_df, restaurants_df],
    
    openai_api_key = api_key,
    verbose=False,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    
    )
    
  return agent 



# to transcribe audio to text
def transcribe_audio(client, audio_path):
  with open(audio_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(model = "whisper-1", file = audio_file)

  return transcript.text


#taking the respone from openai
def take_ai_response(client, input_text):
  messages = [{"role": "user", "content":input_text}]
  response = client.chat.completions.create(model = "gpt-3.5-turbo", messages = messages)
  return response.choices[0].message.content











def main():
    # Initialize chat history
    chat_history = []
    #messages = [{"role": "system", "content": "You are an assistant who is helping the user to order through the dataframe that you have, please answer with a list of what the user needs."},
    #                {"role": "user", "content": "{input}"}]


    st.sidebar.title("Assistant")
    st.title("Nexo")
    st.write("Record your voice or write what you want")
    recorded_audio = audio_recorder()
    user_input = st.chat_input("Write what you want", max_chars=600)
    client = setup_openai_client(api_key)
    agent = create_openai_agent()

    # Check if there is recorded audio
    if recorded_audio:
        audio_file = "audio.mp3"
        with open(audio_file, "wb") as f:
            f.write(recorded_audio)

        transcribed_text = transcribe_audio(client, audio_file)
        st.write("Transcribed text: ", transcribed_text)
       
        messages = [{"role": "system", "content": "You are an assistant who is helping the user to order through the dataframe that you have, please answer with a list of what the user needs, also with each item add the restaurant name, list the top 8 matching items.  dont give any information about how many restaurant we have in the dataset, just accept orders."},
                   {"role": "user", "content": transcribed_text}]
        # Append to chat history
       
    elif user_input:
        messages = [{"role": "system", "content": "You are an assistant who is helping the user to order through the dataframe that you have, please answer with a list of what the user needs. also with each item add the restaurant name, list the top 8 matching items. dont give any information about how many restaurant we have in the dataset just accept orders."},
                    {"role": "user", "content": user_input}]
        # Append to chat history
        

   
    # Invoke the agent with the updated messages including history
    response = agent.invoke(messages)
    st.write("Nexo respnse: ", response)
    


if __name__ == "__main__":
    main()
