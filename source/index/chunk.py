from source.embedding.base_embedding import BaseEmbedding


def chunk_text(content: str, chunk_size, overlap):
    length = len(content)
    if length < 1:
        raise ValueError("There is nothing in the content")
    
    chunks = []

    for i in range(0, length, chunk_size - overlap):

        chunk_content = content[i:min(i + chunk_size, length)]
        chunks.append(chunk_content)

    return chunks

def index(content: str, embedding_model:BaseEmbedding, chunk_size: int = 1000, overlap: int = 50):
    chunks = chunk_text(content, chunk_size, overlap)

    datas = []
    for chunk in chunks:
        data = {
            "text": chunk,
            "embedding": embedding_model.embed(chunk)
        }
        datas.append(data)
    return datas
