# 速查手册

> 常用概念和公式的快速参考。适合在需要时快速查阅。

---

## 核心数学公式
注意力计算：
Attention(Q, K, V) = softmax(QK^T / √d_k) × V

交叉熵损失：
L = -Σᵢ P(xᵢ) × log Q(xᵢ)
简化（one-hot标签）：L = -log Q(真实标签)

梯度下降：
θ_new = θ_old - η × ∇L(θ_old)

Softmax：
softmax(zᵢ) = exp(zᵢ) / Σⱼ exp(zⱼ)

KL散度：
D_KL(P || Q) = Σᵢ P(xᵢ) × log(P(xᵢ) / Q(xᵢ))

困惑度：
PPL = exp(-1/N × Σᵢ log Q(xᵢ))

## Transformer关键参数
嵌入维度 (d_model)：768 / 1024 / 4096 / 8192
注意力头数 (n_heads)：12 / 16 / 32 / 64
层数 (n_layers)：12 / 24 / 32 / 80
词表大小 (vocab_size)：32000 - 128000
上下文窗口：4K / 8K / 32K / 128K / 200K

## 模型大小估算
参数量 → 显存需求（推理）：
FP16：参数量 × 2字节
INT8：参数量 × 1字节
INT4：参数量 × 0.5字节

例：7B参数模型
FP16 → 14GB
INT8 → 7GB
INT4 → 3.5GB

## 评估指标速查
精确率 = TP / (TP + FP) "模型说是的里面有多少真的是"
召回率 = TP / (TP + FN) "真的是的里面有多少被模型找到了"
F1 = 2 × P × R / (P + R) "精确率和召回率的调和平均"

