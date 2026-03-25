#!/usr/bin/env python3
"""
AI-Sovereignty 链接健康检查工具
扫描项目中所有Markdown文件的外部链接，检查有效性
"""

import os
import re
import json
import datetime
from pathlib import Path

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("⚠️  requests库未安装。运行 pip install requests 后重试。")
    print("   当前仅执行链接提取（不检查有效性）。\n")


def find_markdown_files(root_dir):
    """递归查找所有Markdown文件"""
    md_files = []
    for path in Path(root_dir).rglob("*.md"):
        if ".git" not in str(path):
            md_files.append(str(path))
    return md_files


def extract_links(filepath):
    """从Markdown文件中提取外部链接"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 [text](url) 和裸URL
    md_links = re.findall(r'\[([^\]]*)\]\((https?://[^\)]+)\)', content)
    bare_links = re.findall(r'(?<!\()(https?://[^\s\)\]]+)', content)

    links = []
    for text, url in md_links:
        links.append({"text": text, "url": url, "file": filepath})
    for url in bare_links:
        # 避免重复（已在md_links中捕获的）
        if not any(l["url"] == url for l in links):
            links.append({"text": "", "url": url, "file": filepath})

    return links


def check_link(url, timeout=10):
    """检查链接是否有效"""
    if not HAS_REQUESTS:
        return "unknown", "requests库未安装"
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True,
                                 headers={"User-Agent": "AI-Sovereignty-LinkChecker/1.0"})
        if response.status_code < 400:
            return "active", f"HTTP {response.status_code}"
        else:
            return "dead", f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        return "timeout", "请求超时"
    except requests.exceptions.ConnectionError:
        return "dead", "连接失败"
    except Exception as e:
        return "error", str(e)


def extract_keywords(text, url):
    """从链接文本和URL中提取关键词"""
    keywords = []
    if text:
        # 简单分词
        words = re.findall(r'[\w\u4e00-\u9fff]+', text)
        keywords.extend([w for w in words if len(w) > 1])
    # 从URL路径中提取
    path_parts = url.split('/')
    for part in path_parts:
        words = re.findall(r'[a-zA-Z]+', part)
        keywords.extend([w for w in words if len(w) > 2])
    return list(set(keywords))[:10]


def run_check(root_dir="../../"):
    """运行完整检查"""
    print("🔍 AI-Sovereignty 链接健康检查")
    print("=" * 50)

    # 查找文件
    md_files = find_markdown_files(root_dir)
    print(f"\n📄 发现 {len(md_files)} 个Markdown文件")

    # 提取链接
    all_links = []
    for filepath in md_files:
        links = extract_links(filepath)
        all_links.extend(links)

    print(f"🔗 提取到 {len(all_links)} 个外部链接")

    # 检查链接
    results = {"active": [], "dead": [], "timeout": [], "error": [], "unknown": []}
    report_time = datetime.datetime.now().isoformat()

    for i, link in enumerate(all_links, 1):
        print(f"\r  检查中... {i}/{len(all_links)}", end="", flush=True)
        status, detail = check_link(link["url"])
        link["status"] = status
        link["detail"] = detail
        link["keywords"] = extract_keywords(link["text"], link["url"])
        link["checked_at"] = report_time
        results[status].append(link)

    print(f"\r  检查完成！{'':30}")

    # 显示结果
    print(f"\n{'=' * 50}")
    print(f"📊 检查结果")
    print(f"{'=' * 50}")
    print(f"  ✅ 有效链接：{len(results['active'])}")
    print(f"  ❌ 失效链接：{len(results['dead'])}")
    print(f"  ⏱️  超时链接：{len(results['timeout'])}")
    print(f"  ⚠️  异常链接：{len(results['error'])}")
    print(f"  ❓ 未检查：{len(results['unknown'])}")

    if results['dead']:
        print(f"\n{'─' * 50}")
        print("❌ 失效链接详情：")
        for link in results['dead']:
            print(f"\n  URL: {link['url']}")
            print(f"  来源文件: {link['file']}")
            print(f"  链接文本: {link['text']}")
            print(f"  状态: {link['detail']}")
            print(f"  保留关键词: {', '.join(link['keywords'])}")

    # 保存报告
    report_path = os.path.join(os.path.dirname(__file__), "reports",
                                f"report_{datetime.date.today().isoformat()}.json")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({"checked_at": report_time, "results": results}, f,
                  ensure_ascii=False, indent=2)
    print(f"\n📝 报告已保存到: {report_path}")


if __name__ == "__main__":
    run_check()
