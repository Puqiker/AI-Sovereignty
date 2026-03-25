# 开发框架

---

## 构建AI工具的技术栈

### 后端
- **FastAPI / Flask**：Python Web框架，提供API服务
- **LangChain / LlamaIndex**：LLM编排框架
- **vLLM / Ollama**：模型推理引擎

### 前端
- **Gradio / Streamlit**：快速构建AI应用的界面
- **React / Vue**：更灵活的前端框架

### 基础设施
- **Docker**：容器化部署
- **Kubernetes**：大规模容器编排
- **向量数据库**：Chroma、Milvus、Pinecone等

### 选择策略
快速原型/内部工具 → Gradio + FastAPI + Ollama
生产级应用 → React + FastAPI + vLLM + Docker + K8s
边缘部署 → llama.cpp + 轻量级Web服务

