from source.embedding.base_embedding import BaseEmbedding
import torch
import numpy as np

def cosine_similarity(a, b):
    if isinstance(a, torch.Tensor):
        return torch.nn.functional.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0))
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_topk_chunks(query: str, embedding_model: BaseEmbedding, index_datas, k: int = 5):
    query_embedding = embedding_model.embed(query)
    scores = []
    for i, index_data in enumerate(index_datas):
        score = cosine_similarity(query_embedding, index_data["embedding"])
        scores.append((i, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    top_indices = [indice for indice, _ in scores[:k]]
    return [index_datas[i] for i in top_indices]
