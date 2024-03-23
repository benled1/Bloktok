import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_TOKEN"))

def write_text_to_speech(content: str, post_id: str) -> str:
    file_path = f'{post_id}.mp3'
    try:
        with open(file_path, 'x') as file:
            pass 

        response = openai_client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=content
        )
        response.stream_to_file(f'{post_id}.mp3')

    except FileExistsError:
        return "File already exists"
        

    return file_path

