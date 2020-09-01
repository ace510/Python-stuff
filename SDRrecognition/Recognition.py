import speech_recognition

print(speech_recognition.__version__)

recognizer = speech_recognition.Recognizer()

radiohead = speech_recognition.AudioFile("/export/users/Clips/7-19-19.flac")
print("got the file")

with radiohead as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.record(source)

print("audio is recognized")

foo = recognizer.recognize_sphinx(audio)

print("hold onto your butts")
output_list = list()
line = ""
spaces = 0

for i in range(len(foo)):
    if foo[i] is " ":
        spaces += 1

    line += foo[i]

    if spaces > 9:
        output_list.append(line)
        spaces = 0
        line = ""

for i in output_list:
    print(i)
