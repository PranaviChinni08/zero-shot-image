from gtts import gTTS
import gradio as gr
from IPython.display import Audio,display
def text_to_speech(text):
  tts=gTTS(text=text,lang="en")
  tts.save("speech.mp3")
  return "speech.mp3"
demo=gr.Interface(
      fn=text_to_speech,
      inputs=gr.Textbox(label="input"),
      outputs=gr.Audio(type="filepath"),
      title="Text to Speech"
)
demo.launch()
