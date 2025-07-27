from openai import OpenAI

client = OpenAI(
    api_key="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", 
    base_url="https://api.groq.com/openai/v1"
)

print("🎬 Welcome to Life-as-a-Movie Bot!")
print("Describe your day or an incident, and I'll turn it into a movie scene.")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("👤 You: ")

    if user_input.lower() == "quit":
        print("🤖 Bot: The credits roll. Thanks for sharing your story! 🎥✨")
        break

    genre = input("🎭 What genre do you want? (drama/comedy/romance/action/fantasy): ")

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a creative movie script writer. The user will describe an incident or day. "
                    "Turn it into a short movie scene with a title, scene description, dialogues, and background music suggestion. "
                    "Match the chosen genre (drama/comedy/romance/action/fantasy)."
                )
            },
            {"role": "user", "content": f"Incident: {user_input}\nGenre: {genre}"}
        ]
    )

    print(f"\n🎥 Bot:\n{response.choices[0].message.content}\n")
    print("-" * 60 + "\n")
