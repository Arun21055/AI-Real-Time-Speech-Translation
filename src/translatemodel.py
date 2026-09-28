
import os
from openai import AzureOpenAI
 
# -----------------------------------------------
# Azure OpenAI Translation Script - Milestone 2
# -----------------------------------------------
 
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "YOUR_AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "YOUR_ENDPOINT_URL")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")  # your deployment name
 
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-06-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)
 
 
def translate_text(text, target_language="fr"):
    """
    Translate text using an Azure OpenAI (GPT-based) model.
    target_language examples: 'fr' (French), 'es' (Spanish), 'ta' (Tamil)
    """
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": (
                    f"You are a translator. Translate the user's text into "
                    f"{target_language}. Reply with ONLY the translation."
                ),
            },
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content.strip()
 
 
if __name__ == "__main__":
    print("Azure OpenAI Translation Demo")
    input_text = input("Enter text to translate: ")
    lang = input("Enter target language code (e.g., fr, es, ta): ")
 
    translated_output = translate_text(input_text, lang)
    print(f"\nTranslated Text ({lang}): {translated_output}")
 
