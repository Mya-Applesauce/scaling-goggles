prompt = "Telleth me something, and I shalt repeat it backe to thee."
prompt += "\nEntere 'quit' if thou wisheth to stoppe." 

while True:
    message = input(prompt)
    if message == "quit":
        break
    if message == "parrot":
        print("Doth thou considereth thine self a wise guy?")
        break
    else:
        print(message)
