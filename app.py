import pathlib
import textwrap
import google.generativeai as genai

#from google.colab import userdata # to securely fetch and store the API key

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('.', '*')
    text = text.replace('$','\$')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

gemini_api_secret_name = 'AIzaSyC2oDT8FfOYDuqGyLKsIb-TujyEwGOT9Xo'

GOOGLE_API_KEY = gemini_api_secret_name
genai.configure(api_key=GOOGLE_API_KEY)

# try:
#     GOOGLE_API_KEY = userdata.get(gemini_api_secret_name)
#     genai.configure(api_key=GOOGLE_API_KEY)
# except userdata.SecretNotFoundError as e:
#    print(f'Secret not found\n\nThis expects you to create a secret named {gemini_api_secret_name}\n\nVisit https://makersuite.google.com/app/apikey to create an API key\n\nName the API {gemini_api_secret_name}')
#    raise e
# except userdata.NotebookAccessError as e:
#   print(f'You need to grant this notebook access to the {gemini_api_secret_name} secret in order for the notebook to access Gemini on your behalf.')
#   raise e
# except Exception as e:
#   # unknown error
#   print(f"There was an unknown error.")
#   raise e

# Getting the model ready
model = genai.GenerativeModel('gemini-pro')

# Getting our prompt ready
interests = "Running, hiking, playing outside" # user_input
foods_they_love = "Chocolate" # user_input
items_they_currently_love = "Creative stuff like Lego puzzles, play dough" #user_input
age = 20 # user_input
budget = 30 # user_input in $
relation = 'Friend' # user_input

prompt = f"I'm having a hard time deciding a holiday gift for my {relation}.\n\n"
prompt += f"You're great at coming with unique ideas about what one should present others in Christmas!!\n\n"
prompt += f"Their main interests are {interests} and they love to eat {foods_they_love}\n\n"
prompt += f"Items they use a lot are {items_they_currently_love}\n\n"
prompt += f"They are {age} years old and my budget for them is {budget} dollars\n\n"
prompt += f"Could you suggest three good holiday gift ideas that I could buy for them?\n"
prompt += f"Try to be as creative and delightful as possible.\n"
prompt += f"Please make the person happy with your gift ideas!!"

# Generating content using the model and our prompt
response = model.generate_content(prompt)

print(to_markdown(response.text))