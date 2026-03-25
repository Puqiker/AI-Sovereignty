# AI术语表

> 按字母顺序排列的AI核心术语精确定义。
> 每个术语包含定义和对应的项目模块引用。

---

## A

### Attention Mechanism（注意力机制）
让模型在处理某个位置时能够"关注"输入中其他位置的信息。通过Query-Key-Value的点积计算实现。
→ [注意力机制](../../02-foundations/deep-learning/attention-mechanism/)

### Adversarial Attack（对抗性攻击）
通过对输入做微小的、人类察觉不到的修改，让模型给出完全错误的输出。
→ [对抗性攻击](../../03-security/threat-landscape/adversarial-attacks/)

### Agent
具有工具调用能力和规划能力的AI系统，能够不仅生成文本，还能执行操作。
→ [Agent架构](../../04-mastery/advanced-ai-techniques/agent-architecture/)

### Alignment（对齐）
调整AI模型的行为使其符合人类的价值观和偏好。通常通过RLHF或DPO实现。
→ [RLHF与对齐](../../02-foundations/llm-internals/rlhf-alignment/)

## B

### Backpropagation（反向传播）
通过链式法则计算损失函数对每个参数的梯度的算法。是训练神经网络的核心算法。
→ [微积分与优化 → AI](../../02-foundations/mathematics/calculus-optimization/)

### BPE（Byte Pair Encoding，字节对编码）
一种子词分词算法，通过迭代合并高频token对来构建词表。GPT系列等主流模型使用。
→ [分词与嵌入](../../02-foundations/llm-internals/tokenization-embedding/)

## C

### CNN（Convolutional Neural Network，卷积神经网络）
利用卷积操作处理网格状数据的神经网络。通过局部连接和权重共享高效处理图像。
→ [CNN架构](../../02-foundations/deep-learning/cnn-architectures/)

### Cross-Entropy（交叉熵）
衡量两个概率分布差异的度量。语言模型训练的标准损失函数。
→ [信息论基础](../../02-foundations/mathematics/information-theory/)

### Context Window（上下文窗口）
模型一次能处理的最大token数量，包括输入和输出。
→ [上下文窗口与记忆](../../02-foundations/llm-internals/context-window-memory/)

## D

### DPO（Direct Preference Optimization）
直接从人类偏好数据优化模型的方法，跳过了RLHF中训练奖励模型的步骤。
→ [RLHF与对齐](../../02-foundations/llm-internals/rlhf-alignment/)

### Dropout
训练时随机关闭一定比例的神经元以防止过拟合的正则化技术。
→ [神经网络基础](../../02-foundations/deep-learning/neural-network-fundamentals/)

## E

### Embedding（嵌入）
将离散的符号（如词语、token）映射为连续的向量表示。语义相近的符号在嵌入空间中距离相近。
→ [分词与嵌入](../../02-foundations/llm-internals/tokenization-embedding/)

## F

### Fine-tuning（微调）
在预训练模型的基础上，使用特定任务的数据继续训练，以适配特定的任务或行为模式。
→ [微调方法](../../02-foundations/llm-internals/fine-tuning-methods/)

## G

### Gradient Descent（梯度下降）
通过沿损失函数的负梯度方向更新参数来最小化损失的优化算法。
→ [微积分与优化 → AI](../../02-foundations/mathematics/calculus-optimization/)

### GPU（Graphics Processing Unit）
专为并行计算设计的处理器，AI训练和推理的标准硬件。
→ [GPU计算](../../02-foundations/ai-infrastructure/gpu-computing/)

## H

### Hallucination（幻觉）
模型生成看似合理但事实上不正确的内容。是概率语言模型的固有特性。
→ [幻觉分析](../../02-foundations/llm-internals/hallucination-analysis/)

## K

### KL Divergence（KL散度）
衡量两个概率分布差异的非对称度量。在RLHF中用于约束模型不偏离原始分布太远。
→ [信息论基础](../../02-foundations/mathematics/information-theory/)

### KV Cache
在推理时缓存已计算的Key和Value向量以避免重复计算的优化技术。
→ [推理机制](../../02-foundations/llm-internals/inference-mechanism/)

## L

### LLM（Large Language Model，大语言模型）
在大规模文本数据上训练的、参数量在数十亿以上的语言模型。
→ [大模型内核](../../02-foundations/llm-internals/)

### LoRA（Low-Rank Adaptation）
通过添加低秩矩阵旁路来实现参数高效微调的方法。
→ [微调方法](../../02-foundations/llm-internals/fine-tuning-methods/)

## P

### Prompt Injection（提示注入）
通过在输入中嵌入恶意指令来操纵AI模型行为的攻击方式。
→ [Prompt注入](../../03-security/threat-landscape/prompt-injection/)

### Perplexity（困惑度）
衡量语言模型预测能力的指标，是交叉熵的指数形式。越低越好。
→ [信息论基础](../../02-foundations/mathematics/information-theory/)

## R

### RAG（Retrieval-Augmented Generation，检索增强生成）
在模型生成回答之前先从外部知识库检索相关信息的技术。
→ [RAG系统](../../04-mastery/advanced-ai-techniques/rag-systems/)

### RLHF（Reinforcement Learning from Human Feedback）
用人类反馈信号通过强化学习优化模型行为的方法。
→ [RLHF与对齐](../../02-foundations/llm-internals/rlhf-alignment/)

### RNN（Recurrent Neural Network，循环神经网络）
通过在时间步之间传递隐藏状态来处理序列数据的神经网络。已被Transformer取代。
→ [RNN与序列模型](../../02-foundations/deep-learning/rnn-lstm-sequence/)

## S

### Softmax
将一组实数转换为概率分布的函数。模型输出层的标准操作。
→ [概率统计 → AI](../../02-foundations/mathematics/probability-statistics/)

### Scaling Law
模型性能和模型大小、数据量、计算量之间的幂律关系。
→ [预训练范式](../../02-foundations/llm-internals/pretraining-paradigm/)

## T

### Temperature
控制模型输出概率分布尖锐程度的参数。低温度更确定，高温度更随机。
→ [推理机制](../../02-foundations/llm-internals/inference-mechanism/)

### Token
文本被分词后的基本单元。可能是一个词、一个子词、或一个字符。
→ [分词与嵌入](../../02-foundations/llm-internals/tokenization-embedding/)

### Transformer
完全基于注意力机制的神经网络架构，当前所有主流大模型的基础。
→ [Transformer架构](../../02-foundations/deep-learning/transformer-architecture/)
