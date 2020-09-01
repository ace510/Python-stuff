from python_omegle.randomchat import RandomChat
from python_omegle.chatevent import ChatEvent

chat = RandomChat()
chat.start()
while True:
    event, argument = chat.get_event()
    if event == ChatEvent.CHAT_READY:
        break
# Connected, let's send the message
chat.send("Goodbye")
chat.disconnect()
