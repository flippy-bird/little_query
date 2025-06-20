# little_query
一个简单 的RAG个人项目，使用第三方框架，例如langchain或者llamaindex搭建一个RAG系统真的很容易，但是当我们想要去优化这个系统时，例如**修改query**、**优化文档chunk的方式**、**添加多个Retrive**、**构建GraphRAG**等方法时，就没那么简单了，同时框架帮我们做了哪些优化，我们也是不知道的，因此，从手搭的过程中，了解每一个模块的性能，效果，然后再去针对性的去看框架的源码，会让我们收获更多，因此，这个仓库记录我的RAG项目搭建过程。

### 项目结构

基于RAG的几个部分，代码结构如下

```
little_query/
├── README.md                # 项目说明文档
├── requirements.txt         # Python依赖包列表
├── main.py                  # 项目入口文件
├── source/                  # 核心源代码目录
│   ├── __init__.py
│   ├── config.py            # 配置文件
│   ├── llm/                 # 大语言模型相关
│   ├── embedding/           # 文本嵌入相关
│   ├── parser/              # 文档解析相关
│   ├── retrive/             # 检索相关
│   ├── index/               # 索引相关
│   └── rerank/              # 重排序相关
├── test_resources/          # 测试资源
└── util/                    # 工具脚本
```

### 测试
```bash
python main.py
```

### TODO
- [ ] 使用最新的pdf解析算法替换掉当前的`pymudf`包
- [ ] 优化建立索引过程的效率
- [ ] 添加各种chunk的优化方法，参考：[all_rag_techniques](https://github.com/FareedKhan-dev/all-rag-techniques?tab=readme-ov-file)
- [ ] 构建视频理解RAG
- [ ] 构建GraphRAG

