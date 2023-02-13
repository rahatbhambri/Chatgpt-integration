import openai, os, sys
from gtts import gTTS
import os
#from playsound import playsound

while True:

  query = input("Please enter your query \n")
  openai.api_key = "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"
  completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  print(message, "\n")

  # mytext = message
  # audio = gTTS(text=mytext, lang="en", slow=False)
  # audio.save("example.mp3")
  # os.system("mpg123 " + "example.mp3")
