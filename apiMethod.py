
from google import genai
import os
apiKey = os.environ["GEMINI_API_KEY"]

def aiHelper(query):
    client = genai.Client(api_key=f"{apiKey}")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"{query}"
    )
    print(f"Question is:\t{query}")
    print(f"Answer is: \n\t{response.text}")
    return response.text

