from modelscope import snapshot_download

cache_dir = "/mnt/MyDisk/1_checkpoints"
snapshot_download(model_id="Qwen/Qwen3-Embedding-0.6B", cache_dir=cache_dir)


