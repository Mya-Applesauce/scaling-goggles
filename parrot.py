prompt = "Telleth me something, and I shalt repeat it backe to thee."
prompt += "\nEntere 'quit' if thou wisheth to stoppe." 

message = ''
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    if message == "parrot":
        print("Doth thou considereth thine self a wise guy?")
        active = False
    else:
        print(message)
