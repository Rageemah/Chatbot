from google import genai

client = genai.Client(api_key ="AIzaSyAUOKKvJ6zN1RYl0dvfN5kRUiALZxsMoOU")

while True:
    user_msg = input("Enter a message / Q to quit: ")
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = user_msg
    )
    if(user_msg.upper() == "Q" ):
        print("Goodbye!:)")
        break
    else:
        print(f"Bot: {response.text} ","\n")

