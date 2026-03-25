#!/usr/bin/env python3
"""
AI-Sovereignty 能力自评系统
帮助你识别当前的知识水平和盲区
"""

ASSESSMENTS = {
    "01-awakening": {
        "name": "觉醒",
        "questions": [
            "你能否用自己的话解释AI的工作本质，而不使用'理解''思考'这类拟人化的词？",
            "你能说出至少3个人类心智具备而AI不具备的核心能力吗？",
            "你能解释为什么AI会'幻觉'——从概率机制角度而非拟人化角度？",
            "当AI给你一个回答时，你是否有系统性的方法来验证它的正确性？",
            "你是否有意识地维护自己的独立思考能力（如先想后问、定期AI断食）？"
        ]
    },
    "02-foundations-math": {
        "name": "数学基础",
        "questions": [
            "你能否解释为什么神经网络的每一层本质上是矩阵乘法+激活函数？",
            "你能否解释AI模型的输出为什么是概率分布而非确定性答案？",
            "你能否解释反向传播的本质是链式法则在计算图上的应用？",
            "你知道交叉熵损失函数在衡量什么吗？",
            "你能否解释KL散度在RLHF中的作用？"
        ]
    },
    "02-foundations-ml": {
        "name": "机器学习",
        "questions": [
            "你能否解释监督学习、无监督学习、强化学习各自解决什么问题？",
            "你能否解释过拟合和欠拟合的本质及偏差-方差权衡？",
            "你理解为什么RLHF需要强化学习而不只是监督学习吗？",
            "你知道为什么准确率可能是一个误导性的指标吗？",
            "面对一个具体问题，你能判断应该用哪种学习范式吗？"
        ]
    },
    "02-foundations-dl": {
        "name": "深度学习",
        "questions": [
            "你能否画出一个简单神经网络的结构并解释数据如何流过？",
            "你能否解释CNN对图像有效的根本原因（局部性+平移不变性）？",
            "你能否解释RNN的记忆为什么有限以及LSTM如何缓解？",
            "你能否用自己的话解释注意力机制在做什么（不背公式）？",
            "你能否解释Transformer为什么取代了RNN（并行+长距离依赖）？"
        ]
    },
    "02-foundations-llm": {
        "name": "大模型内核",
        "questions": [
            "你能否描述文字从输入到模型输出的完整数据流？",
            "你理解预训练、微调、RLHF三个阶段各自解决什么问题吗？",
            "你能否解释KV Cache是什么以及为什么需要它？",
            "你知道Temperature参数在数学上做了什么吗？",
            "你能否从原理出发解释思维链（CoT）为什么有效？"
        ]
    },
    "03-security": {
        "name": "安全",
        "questions": [
            "你能否解释Prompt注入的根本原因？",
            "你知道直接注入和间接注入的区别以及为什么后者更危险吗？",
            "你能否列出使用AI工具时的数据分级策略？",
            "你知道什么是AI供应链攻击以及pickle文件为什么危险吗？",
            "你能否为一个AI系统设计纵深防御策略？"
        ]
    },
    "04-mastery": {
        "name": "精通",
        "questions": [
            "面对一个业务问题，你能判断是否适合用AI解决吗？",
            "你能否设计一个包含RAG或Agent的AI系统架构？",
            "你知道如何为概率性系统设计测试吗？",
            "你能否系统性地调试AI系统的异常行为？",
            "你能否设计多供应商架构来避免供应商锁定？"
        ]
    },
    "05-transcendence": {
        "name": "超越",
        "questions": [
            "你能否清晰表达你和AI的关系？",
            "你有系统性的方法来保持认知进化吗？",
            "你是否定期做AI断食和深度工作？",
            "你的AI能力是否转化为了经济价值或职业发展？",
            "面对AI新闻时，你能跳出表面看到更深层趋势吗？"
        ]
    }
}


def run_assessment():
    print("\n" + "=" * 60)
    print("🛡️  AI-Sovereignty 能力自评系统")
    print("=" * 60)
    print("\n对于每个问题，回答 y（是）或 n（否）。\n")

    results = {}

    for stage_key, stage_data in ASSESSMENTS.items():
        print(f"\n{'─' * 40}")
        print(f"📋 {stage_data['name']}阶段")
        print(f"{'─' * 40}")

        score = 0
        total = len(stage_data['questions'])

        for i, question in enumerate(stage_data['questions'], 1):
            while True:
                answer = input(f"\n  {i}. {question}\n     (y/n): ").strip().lower()
                if answer in ('y', 'n'):
                    if answer == 'y':
                        score += 1
                    break
                print("     请输入 y 或 n")

        percentage = score / total * 100
        results[stage_key] = {
            "name": stage_data['name'],
            "score": score,
            "total": total,
            "percentage": percentage
        }

    display_results(results)


def display_results(results):
    print("\n" + "=" * 60)
    print("📊 评估结果")
    print("=" * 60)

    for stage_key, data in results.items():
        bar_length = 20
        filled = int(data['percentage'] / 100 * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)

        if data['percentage'] >= 80:
            status = "✅ 掌握"
        elif data['percentage'] >= 50:
            status = "⚠️  部分掌握"
        else:
            status = "❌ 需要学习"

        print(f"\n  {data['name']}: [{bar}] {data['percentage']:.0f}% ({data['score']}/{data['total']}) {status}")

    # 找出薄弱环节
    weak_areas = [d for d in results.values() if d['percentage'] < 60]
    if weak_areas:
        print(f"\n{'─' * 40}")
        print("🎯 建议重点学习的领域：")
        for area in weak_areas:
            print(f"  → {area['name']}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_assessment()
