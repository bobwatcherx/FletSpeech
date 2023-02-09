from flet import *
import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr



def main(page:Page):
	# YOU RESULT OF YOU VOICE
	youresult = Text()


	def recordnow(e):
		page.snack_bar = SnackBar(
			Text("start Record 5 second Now..",size=20,weight="bold"),
		bgcolor="blue"		
		)
		page.snack_bar.open = True
		page.update()

		freq = 44100
		duration = 5
		recording = sd.rec(int(duration * freq),
				samplerate=freq,channels=2
						)
		# AND RECORD 5 seconds
		# WAIT YOU VOICE UNTIL 5 seconds
		sd.wait()

		# AND SAVE YOU VOICE TO WAV FILE FORMAT
		wav.write("recording.wav",freq,recording)


		r = sr.Recognizer()
		with sr.Microphone() as source:
			audio_data = r.record(source,duration=5)
			print("RECOGNITIze You Sound now......")

			# SHOW SNACKBAR FOR NOTIF STOP YOU VOICE NOW
			page.snack_bar = SnackBar(
				Column([
				Text("stop you voice ....",size=20),
			Text("Recognizing you sound ",size=20,weight="bold"),
					],alignment="center"),
			bgcolor="blue"			
			)
			page.snack_bar.open = True
			page.update()

			# AND YOU CAN USE YOU CUSTOM LANGUAGE CODE
			text = r.recognize_google(audio_data,language="en-EN",show_all=True)
			transcript = text['alternative'][0]['transcript']
			
			# AND SHOW RESULT TO TEXT WIDGET IN FLET APP
			youresult.value = transcript
			print(transcript)
			page.update()





	page.add(
	Column([
	Text("Record sound to text",size=30,weight="bold"),
	Divider(),
	Text("Record only 5 seconds",size=20,weight="bold"),
	ElevatedButton("record now",
	bgcolor="blue",color="white",
	on_click=recordnow

		),

	# AND SHOW TEXT RESULT HERE
	youresult

	])

	)

flet.app(target=main)
