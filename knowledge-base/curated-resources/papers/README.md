# 经典论文

> 这些论文定义了AI领域的关键转折点。
> 你不需要读懂每一行数学推导——
> 重点是理解每篇论文解决了什么问题、提出了什么方法、以及它为什么重要。

---

## 深度学习

### ⭐ Attention Is All You Need (Vaswani et al., 2017)
- **关键词**：Transformer、自注意力、多头注意力、位置编码
- **重要性**：提出了Transformer架构，奠定了当前所有主流大模型的基础。
- **链接**：https://arxiv.org/abs/1706.03762
- **对应模块**：[Transformer架构](../../../02-foundations/deep-learning/transformer-architecture/)
- **阅读建议**：重点看第3节（模型架构），理解自注意力和多头注意力的计算过程。

### Deep Residual Learning for Image Recognition (He et al., 2015)
- **关键词**：ResNet、残差连接、深度网络训练
- **重要性**：提出了残差连接，解决了深层网络训练困难的问题。Transformer中也使用了残差连接。
- **链接**：https://arxiv.org/abs/1512.03385
- **对应模块**：[Transformer架构](../../../02-foundations/deep-learning/transformer-architecture/)

### ImageNet Classification with Deep Convolutional Neural Networks (Krizhevsky et al., 2012)
- **关键词**：AlexNet、CNN、GPU训练、深度学习复兴
- **重要性**：标志着深度学习复兴的起点。证明了深度神经网络在大规模数据上的威力。
- **链接**：https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- **对应模块**：[CNN架构](../../../02-foundations/deep-learning/cnn-architectures/)

---

## 大模型

### ⭐ Language Models are Few-Shot Learners (Brown et al., 2020)
- **关键词**：GPT-3、few-shot学习、scaling law、上下文学习
- **重要性**：GPT-3论文。证明了足够大的语言模型可以通过few-shot提示完成各种任务，开启了大模型时代。
- **链接**：https://arxiv.org/abs/2005.14165
- **对应模块**：[预训练范式](../../../02-foundations/llm-internals/pretraining-paradigm/)

### Training language models to follow instructions with human feedback (Ouyang et al., 2022)
- **关键词**：InstructGPT、RLHF、对齐、人类反馈
- **重要性**：提出了RLHF方法来对齐语言模型，是ChatGPT等产品背后的关键技术。
- **链接**：https://arxiv.org/abs/2203.02155
- **对应模块**：[RLHF与对齐](../../../02-foundations/llm-internals/rlhf-alignment/)

### LoRA: Low-Rank Adaptation of Large Language Models (Hu et al., 2021)
- **关键词**：LoRA、参数高效微调、低秩适配
- **重要性**：提出了LoRA方法，大幅降低了大模型微调的成本，使得个人和小团队也能微调大模型。
- **链接**：https://arxiv.org/abs/2106.09685
- **对应模块**：[微调方法](../../../02-foundations/llm-internals/fine-tuning-methods/)

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., 2020)
- **关键词**：RAG、检索增强生成、知识密集型任务
- **重要性**：提出了RAG的概念，解决了语言模型的知识局限问题。
- **链接**：https://arxiv.org/abs/2005.11401
- **对应模块**：[RAG系统](../../../04-mastery/advanced-ai-techniques/rag-systems/)

---

## AI安全

### ⭐ Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection (Greshake et al., 2023)
- **关键词**：间接Prompt注入、LLM应用安全、攻击面
- **重要性**：系统性地展示了间接Prompt注入对真实LLM应用的威胁。
- **链接**：https://arxiv.org/abs/2302.12173
- **对应模块**：[Prompt注入](../../../03-security/threat-landscape/prompt-injection/)

### Universal and Transferable Adversarial Attacks on Aligned Language Models (Zou et al., 2023)
- **关键词**：对抗性攻击、安全绕过、对齐脆弱性
- **重要性**：展示了通过优化的对抗性后缀可以绕过几乎所有主流大模型的安全对齐。
- **链接**：https://arxiv.org/abs/2307.15043
- **对应模块**：[对抗性攻击](../../../03-security/threat-landscape/adversarial-attacks/)

### Extracting Training Data from Large Language Models (Carlini et al., 2021)
- **关键词**：训练数据提取、隐私泄露、记忆化
- **重要性**：证明了大语言模型可以被诱导输出训练数据中的原始内容，揭示了严重的隐私风险。
- **链接**：https://arxiv.org/abs/2012.07805
- **对应模块**：[隐私泄露](../../../03-security/threat-landscape/privacy-leakage/)
