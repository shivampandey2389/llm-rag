from groq import Groq

client = Groq(api_key="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")

resp = client.models.list()
print(resp)
print("Successfully listed Groq models.")