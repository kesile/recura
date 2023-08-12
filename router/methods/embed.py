import openai

openai.api_key = "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"

def embed(inp):
    response = openai.Embedding.create(
        input=inp,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings