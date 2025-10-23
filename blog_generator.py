from google import genai
from google.genai import types
from dotenv import dotenv_values

config = dotenv_values('.env')

client = genai.Client()

def generate_blog(paragraph_topic: str) -> str | None:
  response = client.models.generate_content( # type: ignore
    model="gemini-2.5-flash",
    contents=f'Write a detailed blog paragraph about {paragraph_topic}.',
    config=types.GenerateContentConfig(
      temperature=0.3,
    )
  )

  retrieve_blog = response.text
  return retrieve_blog

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False
