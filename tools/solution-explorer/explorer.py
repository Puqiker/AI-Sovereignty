#!/usr/bin/env python3
"""
AI-Sovereignty 解决方案检索系统
管理和搜索AI解决方案的完整推理链
"""

import os
import sys
import json
import datetime
from pathlib import Path

SOLUTIONS_DIR = os.path.join(os.path.dirname(__file__), "solutions")


def ensure_dir():
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)


def load_solutions():
    """加载所有解决方案"""
    ensure_dir()
    solutions = []
    for filepath in Path(SOLUTIONS_DIR).glob("*.json"):
        with open(filepath, 'r', encoding='utf-8') as f:
            sol = json.load(f)
            sol['_file'] = str(filepath)
            solutions.append(sol)
    return solutions


def search_solutions(query):
    """搜索匹配的解决方案"""
    solutions = load_solutions()
    query_lower = query.lower()
    results = []

    for sol in solutions:
        score = 0
        searchable = json.dumps(sol, ensure_ascii=False).lower()
        if query_lower in searchable:
            score += 1
        for tag in sol.get('tags', []):
            if query_lower in tag.lower():
                score += 2
        if query_lower in sol.get('title', '').lower():
            score += 3
        if score > 0:
            results.append((score, sol))

    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results]


def add_solution():
    """交互式添加新方案"""
    print("\n📝 添加新的解决方案")
    print("=" * 40)

    sol = {}
    sol['title'] = input("\n标题：").strip()
    sol['problem'] = input("问题描述：").strip()
    sol['constraints'] = input("背景约束：").strip()
    sol['initial_approach'] = input("最初的思路：").strip()
    sol['why_changed'] = input("为什么放弃最初思路：").strip()
    sol['final_approach'] = input("最终方案：").strip()
    sol['implementation'] = input("具体实现（简述）：").strip()
    sol['pitfalls'] = input("踩过的坑：").strip()
    sol['limitations'] = input("方案局限性：").strip()
    sol['security_review'] = input("安全审查情况：").strip()
    tags_input = input("标签（逗号分隔）：").strip()
    sol['tags'] = [t.strip() for t in tags_input.split(",") if t.strip()]
    sol['created_at'] = datetime.datetime.now().isoformat()

    # 保存
    ensure_dir()
    filename = f"{datetime.date.today().isoformat()}_{sol['title'][:20].replace(' ', '_')}.json"
    filepath = os.path.join(SOLUTIONS_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(sol, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 方案已保存到: {filepath}")


def list_solutions():
    """列出所有方案"""
    solutions = load_solutions()
    if not solutions:
        print("\n📭 暂无解决方案。使用 'python explorer.py add' 添加。")
        return

    print(f"\n📋 共 {len(solutions)} 个解决方案：")
    print("─" * 50)
    for sol in solutions:
        tags = ", ".join(sol.get('tags', []))
        print(f"\n  📌 {sol.get('title', '无标题')}")
        print(f"     标签：{tags}")
        print(f"     创建：{sol.get('created_at', '未知')[:10]}")


def display_solution(sol):
    """显示单个方案的详情"""
    print(f"\n{'=' * 50}")
    print(f"📌 {sol.get('title', '无标题')}")
    print(f"{'=' * 50}")
    print(f"\n问题：{sol.get('problem', '')}")
    print(f"\n约束：{sol.get('constraints', '')}")
    print(f"\n最初思路：{sol.get('initial_approach', '')}")
    print(f"\n为什么放弃：{sol.get('why_changed', '')}")
    print(f"\n最终方案：{sol.get('final_approach', '')}")
    print(f"\n实现：{sol.get('implementation', '')}")
    print(f"\n踩坑：{sol.get('pitfalls', '')}")
    print(f"\n局限性：{sol.get('limitations', '')}")
    print(f"\n安全审查：{sol.get('security_review', '')}")
    print(f"\n标签：{', '.join(sol.get('tags', []))}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：")
        print("  python explorer.py search <关键词>")
        print("  python explorer.py add")
        print("  python explorer.py list")
        sys.exit(1)

    command = sys.argv[1]

    if command == "search" and len(sys.argv) > 2:
        query = " ".join(sys.argv[2:])
        results = search_solutions(query)
        if results:
            print(f"\n🔍 搜索 '{query}' 找到 {len(results)} 个结果：")
            for sol in results:
                display_solution(sol)
        else:
            print(f"\n🔍 搜索 '{query}' 未找到匹配的解决方案。")
    elif command == "add":
        add_solution()
    elif command == "list":
        list_solutions()
    else:
        print("未知命令。使用 search / add / list")
