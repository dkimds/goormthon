import requests

# ChatGPT API endpoint
api_endpoint = "https://api.openai.com/v1/chat/completions"

# OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
api_key = "YOUR_API_KEY"

# Prompts for collecting emotional data
prompts = [
    "오늘은 날씨가 정말 좋아서 나가기 좋은 날이에요.",
    "시험 기간에는 항상 스트레스가 너무 많이 쌓여요.",
    "지하철에서 출근하는 것은 항상 정신 없는 일이에요."
]

# Specify the number of responses to collect for each prompt
responses_per_prompt = 100

# Emotional classes
emotional_classes = ["Positive", "Negative", "Neutral"]

# Collecting data
collected_data = []

for prompt in prompts:
    for _ in range(responses_per_prompt):
        # Formulate the prompt as a conversation
        conversation = [{"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Translate the following Korean sentence: {prompt}"}]

        # Make the API request
        response = requests.post(api_endpoint,
                                 headers={"Authorization": f"Bearer {api_key}"},
                                 json={"messages": conversation})

        # Parse the response and extract the model's reply
        model_reply = response.json()["choices"][0]["message"]["content"]

        # Add the collected data to the list
        collected_data.append({"prompt": prompt, "model_reply": model_reply})

# Print the collected data
for data_point in collected_data:
    print(f"Prompt: {data_point['prompt']}")
    print(f"Model Reply: {data_point['model_reply']}\n")
