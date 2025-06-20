from typing import Union
from .base_embedding import BaseEmbedding
from sentence_transformers import SentenceTransformer

class Qwen3Embedding(BaseEmbedding):
    def __init__(self, checkpoint_dir):
        self.model = SentenceTransformer(checkpoint_dir)

    def embed(self, text: Union[str, list[str]]):
        embedding = self.model.encode(text)
        return embedding
    
    def embed_with_prompt(self, text: Union[str, list[str]], prompt:str):
        embedding = self.model.encode(text, prompt)
        return embedding
    
if __name__ == "__main__":
    embedding = Qwen3Embedding("/mnt/MyDisk/1_checkpoints/Qwen/Qwen3-Embedding-0.6B")
    query_1 = "What is the capital of France?"
    document_1 = ["captial is Berlin","Paris", "Berlin", "France"]
    embedding_1 = embedding.embed_with_prompt(query_1)
    embedding_2 = embedding.embed(document_1)
    print(len(embedding_1))
    print(len(embedding_2))
    sim = embedding.model.similarity(embedding_1, embedding_2)
    print(sim)
    # print(len(query))
