from openai import OpenAI

client =OpenAI(

    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-5",
    messages=[
        
            {"role": "system","content":"you are a virtual assistant named jarvis skilled in general task likr alexa and google cloud"},
            {"content": "Say 'double bubble bath' ten times fast."},
        {"role": "user","content":"what is coding"}

        
    ],

)

print(completion.choices[0].message.content)

