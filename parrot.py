prompt = "If thou sharest thy name, we can personalize the messages thou seest."
prompt += "\nWhat is thy first name?" 

message = ''
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
        