#!/usr/bin/env python3
"""
AI-Sovereignty 学习路径生成器
根据用户背景生成个性化的学习路径
"""

import json

STAGES = {
    "01-awakening": {
        "name": "觉醒（Awakening）",
        "modules": [
            "AI到底是什么",
            "人类心智 vs AI",
            "为什么必须理解底层原理",
            "认知范式转换",
            "认知卫生",
            "用AI学AI的悖论"
        ],
        "estimated_weeks": 1
    },
    "02-foundations-math": {
        "name": "筑基-数学基础",
        "modules": ["线性代数→AI", "概率统计→AI", "微积分与优化→AI", "信息论基础"],
        "estimated_weeks": 3
    },
    "02-foundations-ml": {
        "name": "筑基-机器学习",
        "modules": ["监督学习", "无监督学习", "强化学习", "评估方法论"],
        "estimated_weeks": 4
    },
    "02-foundations-dl": {
        "name": "筑基-深度学习",
        "modules": ["神经网络基础", "CNN架构", "RNN/LSTM", "注意力机制", "Transformer"],
        "estimated_weeks": 4
    },
    "02-foundations-llm": {
        "name": "筑基-大模型内核",
        "modules": ["分词与嵌入", "预训练范式", "微调方法", "RLHF与对齐",
                     "推理机制", "上下文窗口", "幻觉分析", "Prompt Engineering"],
        "estimated_weeks": 4
    },
    "02-foundations-infra": {
        "name": "筑基-基础设施与数据",
        "modules": ["GPU计算", "分布式训练", "模型服务", "数据管线",
                     "数据质量", "数据预处理", "数据集构建", "模型评估"],
        "estimated_weeks": 3
    },
    "03-security": {
        "name": "安全（Security）",
        "modules": ["Prompt注入", "数据投毒", "模型窃取", "对抗性攻击",
                     "隐私泄露", "供应链攻击", "安全体系建设", "法律合规"],
        "estimated_weeks": 4
    },
    "04-mastery": {
        "name": "精通（Mastery）",
        "modules": ["多模态AI", "Agent架构", "RAG系统", "AI推理",
                     "场景发现", "工作流编排", "AI调试", "AI测试", "AI运维"],
        "estimated_weeks": 6
    },
    "05-transcendence": {
        "name": "超越（Transcendence）",
        "modules": ["认知进化", "创造力放大", "经济主权", "持续进化框架"],
        "estimated_weeks": 2
    }
}

QUESTIONS = [
    {
        "question": "你的数学背景是什么水平？",
        "options": [
            ("a", "高中及以下", 0),
            ("b", "大学本科（学过高等数学、线性代数、概率统计）", 1),
            ("c", "研究生及以上（有扎实的数学基础）", 2)
        ],
        "key": "math_level"
    },
    {
        "question": "你对机器学习/深度学习了解多少？",
        "options": [
            ("a", "完全不了解", 0),
            ("b", "了解基本概念但没深入学过", 1),
            ("c", "学过相关课程或有实践经验", 2),
            ("d", "有专业经验（工作中用过ML/DL）", 3)
        ],
        "key": "ml_level"
    },
    {
        "question": "你对大语言模型（ChatGPT/Claude等）的理解程度？",
        "options": [
            ("a", "只是用过，不知道原理", 0),
            ("b", "大致知道Transformer和注意力机制", 1),
            ("c", "理解预训练、微调、RLHF的原理", 2)
        ],
        "key": "llm_level"
    },
    {
        "question": "你对AI安全了解多少？",
        "options": [
            ("a", "没想过这个问题", 0),
            ("b", "知道有安全风险但不了解细节", 1),
            ("c", "了解主要威胁类型和防御方法", 2)
        ],
        "key": "security_level"
    },
    {
        "question": "你的主要目标是什么？",
        "options": [
            ("a", "全面系统地学习AI", "comprehensive"),
            ("b", "重点关注AI安全", "security_focus"),
            ("c", "想要构建AI应用/产品", "builder_focus"),
            ("d", "提升对AI的认知和判断力", "cognitive_focus")
        ],
        "key": "goal"
    }
]


def ask_questions():
    """交互式问答"""
    print("\n" + "=" * 60)
    print("🛡️  AI-Sovereignty 学习路径生成器")
    print("=" * 60)
    print("\n回答以下问题，我会为你生成个性化的学习路径。\n")

    answers = {}
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\n问题 {i}/{len(QUESTIONS)}：{q['question']}")
        for code, text, *_ in q['options']:
            print(f"  {code}) {text}")

        while True:
            choice = input("\n你的选择：").strip().lower()
            valid_codes = [opt[0] for opt in q['options']]
            if choice in valid_codes:
                for opt in q['options']:
                    if opt[0] == choice:
                        answers[q['key']] = opt[2] if len(opt) > 2 else opt[1]
                break
            print(f"请输入有效选项：{', '.join(valid_codes)}")

    return answers


def generate_path(answers):
    """根据答案生成学习路径"""
    path = []
    total_weeks = 0

    math_level = answers.get("math_level", 0)
    ml_level = answers.get("ml_level", 0)
    llm_level = answers.get("llm_level", 0)
    security_level = answers.get("security_level", 0)
    goal = answers.get("goal", "comprehensive")

    # 觉醒阶段：所有人都应该学
    path.append({
        "stage": STAGES["01-awakening"],
        "priority": "必修",
        "reason": "认知地基，所有人的起点"
    })
    total_weeks += STAGES["01-awakening"]["estimated_weeks"]

    # 数学基础
    if math_level < 1:
        path.append({
            "stage": STAGES["02-foundations-math"],
            "priority": "必修",
            "reason": "数学基础不足，需要从头建立数学→AI的桥梁",
            "note": "⚠️ 建议先补齐大学数学基础再进入本模块"
        })
        total_weeks += STAGES["02-foundations-math"]["estimated_weeks"]
    elif math_level >= 1:
        path.append({
            "stage": STAGES["02-foundations-math"],
            "priority": "必修",
            "reason": "你有数学基础，本模块帮你建立数学→AI的桥梁"
        })
        total_weeks += max(1, STAGES["02-foundations-math"]["estimated_weeks"] - 1)

    # 机器学习
    if ml_level < 2:
        path.append({
            "stage": STAGES["02-foundations-ml"],
            "priority": "必修",
            "reason": "机器学习是AI的核心框架，需要系统学习"
        })
        total_weeks += STAGES["02-foundations-ml"]["estimated_weeks"]
    else:
        path.append({
            "stage": STAGES["02-foundations-ml"],
            "priority": "快速复习",
            "reason": "你有ML基础，快速过一遍确认无盲区"
        })
        total_weeks += 1

    # 深度学习
    if ml_level < 3:
        path.append({
            "stage": STAGES["02-foundations-dl"],
            "priority": "必修",
            "reason": "深度学习是通向Transformer的必经之路"
        })
        total_weeks += STAGES["02-foundations-dl"]["estimated_weeks"]
    else:
        path.append({
            "stage": STAGES["02-foundations-dl"],
            "priority": "快速复习",
            "reason": "你有DL经验，重点复习注意力机制和Transformer"
        })
        total_weeks += 2

    # 大模型内核
    if llm_level < 2:
        path.append({
            "stage": STAGES["02-foundations-llm"],
            "priority": "必修",
            "reason": "大模型内核是理解当前AI系统的关键"
        })
        total_weeks += STAGES["02-foundations-llm"]["estimated_weeks"]
    else:
        path.append({
            "stage": STAGES["02-foundations-llm"],
            "priority": "选择性学习",
            "reason": "你已理解LLM原理，重点关注幻觉分析和Prompt Engineering"
        })
        total_weeks += 1

    # 基础设施与数据
    path.append({
        "stage": STAGES["02-foundations-infra"],
        "priority": "必修" if goal in ["comprehensive", "builder_focus"] else "推荐",
        "reason": "工程和数据基础，对构建AI系统不可或缺"
    })
    total_weeks += STAGES["02-foundations-infra"]["estimated_weeks"] if goal in ["comprehensive", "builder_focus"] else 1

    # 安全
    if goal == "security_focus":
        path.append({
            "stage": STAGES["03-security"],
            "priority": "核心重点",
            "reason": "这是你的主要学习目标"
        })
        total_weeks += STAGES["03-security"]["estimated_weeks"] + 2  # 额外实践时间
    else:
        path.append({
            "stage": STAGES["03-security"],
            "priority": "必修",
            "reason": "安全是每个AI使用者必须掌握的"
        })
        total_weeks += STAGES["03-security"]["estimated_weeks"]

    # 精通
    if goal in ["comprehensive", "builder_focus"]:
        path.append({
            "stage": STAGES["04-mastery"],
            "priority": "必修" if goal == "builder_focus" else "推荐",
            "reason": "从使用者到创造者的跃迁"
        })
        total_weeks += STAGES["04-mastery"]["estimated_weeks"]
    else:
        path.append({
            "stage": STAGES["04-mastery"],
            "priority": "选择性学习",
            "reason": "根据你的需要选择相关模块"
        })
        total_weeks += 2

    # 超越
    path.append({
        "stage": STAGES["05-transcendence"],
        "priority": "推荐",
        "reason": "建立持续进化的认知框架"
    })
    total_weeks += STAGES["05-transcendence"]["estimated_weeks"]

    return path, total_weeks


def display_path(path, total_weeks):
    """显示学习路径"""
    print("\n" + "=" * 60)
    print("📋 你的个性化学习路径")
    print("=" * 60)
    print(f"\n预估总时长：{total_weeks} 周（按每周投入10-15小时计算）\n")

    for i, item in enumerate(path, 1):
        stage = item["stage"]
        priority = item["priority"]
        reason = item["reason"]

        priority_icon = {
            "必修": "🔴",
            "核心重点": "🔴🔴",
            "推荐": "🟡",
            "快速复习": "🟢",
            "选择性学习": "⚪"
        }.get(priority, "⚪")

        print(f"{i}. {priority_icon} [{priority}] {stage['name']}")
        print(f"   └ {reason}")
        if "note" in item:
            print(f"   └ {item['note']}")
        print(f"   └ 包含模块：{', '.join(stage['modules'])}")
        print()

    print("=" * 60)
    print("图例：🔴必修  🟡推荐  🟢快速复习  ⚪选择性学习")
    print("=" * 60)


if __name__ == "__main__":
    answers = ask_questions()
    path, total_weeks = generate_path(answers)
    display_path(path, total_weeks)
