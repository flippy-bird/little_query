
from source.parser.pdf_parser import PdfParser
from source.index.chunk import index
from source.embedding.qwen3_embedding import Qwen3Embedding
from source.retrive.embedding_retrive import get_topk_chunks
from source.llm.qwen_llm import QwenLLM
from source.config import QWEN_API_KEY, MODEL


pdf_parser = PdfParser()
content = pdf_parser.parse("./test_resources/Qwen2.5_vl.pdf")
embedding_model = Qwen3Embedding("/mnt/MyDisk/1_checkpoints/Qwen/Qwen3-Embedding-0.6B")
index_datas = index(content, embedding_model)
query = "Qwen 2.5-vl的创新点在哪儿？"
topk_index_datas = get_topk_chunks(query=query, embedding_model=embedding_model, index_datas=index_datas)
background_info = ""
for topk_data in topk_index_datas:
    background_info += topk_data["text"]

print(background_info)

prompt = f"""
    请根据提供的背景信息，回答问题。
    背景信息：
    {background_info}
    问题：
    {query}
    """

llm = QwenLLM(api_key=QWEN_API_KEY, model=MODEL)
answer = llm.chat(prompt)
print(answer)
    