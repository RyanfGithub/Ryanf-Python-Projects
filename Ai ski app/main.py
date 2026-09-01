import ollama

while True:
    user_ability = input("What is your ability level?: (Beginner, Intermediate, Advanced, Expert): ")

    if user_ability.upper() == 'BEGINNER' or user_ability.upper() == 'INTERMEDIATE' or user_ability.upper() == 'ADVANCED' or user_ability.upper() == 'EXPERT':
        break
    else:
        print('Invalid ability level')


runs = [{'Down': 'Hard'}, {'Pakololo': 'Expert'}, {'Magoo': 'Easy'}]
snow_conditions = 'Good'

messages = [
    {'role': 'assistant', 'content': f"Runs and their difficulties are: {runs}"},
    {'role': 'assistant', 'content': f"User ability is: {user_ability} "},
    {'role': 'assistant', 'content': f"Snow condtions are: {snow_conditions} "},
    {'role': 'system', 
        'content': 'You give ski run recomendations based on the amount of snow, the users ability, and the difficulty of the runs given to you.'
        'Better snow means the user should do runs hard for their ability. Worse snow means the user should do runs easy for their ability'},
    {'role': 'user', 'content': 'Give me 1 run recomendation'}
]

client = ollama.Client(
    host='http://localhost:11434',
    timeout=600
)


response = client.chat(model='replace with model name', messages=messages)

print(response['message']['content'])
