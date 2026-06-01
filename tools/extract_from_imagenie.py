#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import re

def extract_wechat_article(url):
    """
    使用 imagenie.us 服务提取公众号文章
    """

    # 清理 URL，提取短链接 ID
    # 支持两种格式：
    # 1. https://mp.weixin.qq.com/s/XXXXX
    # 2. https://mp.weixin.qq.com/s?__biz=...&sn=XXXXX

    short_id_match = re.search(r'sn=([a-zA-Z0-9_-]+)', url)
    if short_id_match:
        short_id = short_id_match.group(1)
        clean_url = f"https://mp.weixin.qq.com/s/{short_id}"
    else:
        # 尝试直接从路径提取
        path_match = re.search(r'/s/([a-zA-Z0-9_-]+)', url)
        if path_match:
            clean_url = f"https://mp.weixin.qq.com/s/{path_match.group(1)}"
        else:
            clean_url = url

    print(f"处理 URL: {clean_url}")

    # 使用 imagenie API
    api_url = "https://wechat.imagenie.us/extract"

    try:
        response = requests.post(
            api_url,
            headers={"Content-Type": "application/json"},
            json={"url": clean_url},
            timeout=30
        )

        # 检查响应是否为 JSON（错误情况）
        content_type = response.headers.get('content-type', '')

        if 'application/json' in content_type:
            # JSON 响应，可能是错误
            try:
                result = response.json()
                if result.get("success") == False:
                    error = result.get('error', {})
                    error_code = error.get('code', 'UNKNOWN')

                    if error_code == 'POOR_CONTENT_QUALITY':
                        return {
                            'success': False,
                            'error': '文章内容质量不达标，可能是：',
                            'reasons': [
                                '文章需要登录才能查看',
                                '文章已删除或失效',
                                '链接格式不正确'
                            ]
                        }
                    else:
                        return {
                            'success': False,
                            'error': error.get('message', '未知错误'),
                            'code': error_code
                        }
            except:
                pass

        # 直接返回 markdown 内容
        markdown_content = response.text

        if markdown_content and len(markdown_content) > 100:
            return {
                'success': True,
                'content': markdown_content,
                'title': extract_title(markdown_content)
            }
        else:
            return {
                'success': False,
                'error': '提取的内容为空或过短',
                'content_preview': markdown_content[:200]
            }

    except Exception as e:
        return {
            'success': False,
            'error': f"请求失败: {str(e)}"
        }

def extract_title(content):
    """从 markdown 内容中提取标题"""
    lines = content.split('\n')
    for line in lines[:10]:  # 只看前10行
        line = line.strip()
        if line.startswith('#') and not line.startswith('##'):
            return line.lstrip('#').strip()
    return "未找到标题"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python extract_from_imagenie.py <公众号文章链接>")
        sys.exit(1)

    url = sys.argv[1]

    result = extract_wechat_article(url)

    if result['success']:
        print("\n" + "="*60)
        print(f"✅ 成功提取文章")
        print("="*60)
        print(f"标题: {result['title']}")
        print("="*60 + "\n")

        # 保存到文件
        output_file = '/tmp/wechat_article_extracted.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result['content'])

        print(f"内容已保存到: {output_file}")
        print(f"\n前 2000 字符预览:\n")
        print(result['content'][:2000])

        if len(result['content']) > 2000:
            print(f"\n... (还有 {len(result['content']) - 2000} 字符)")
    else:
        print("\n" + "="*60)
        print("❌ 提取失败")
        print("="*60)
        print(f"错误: {result.get('error', '未知错误')}")

        if 'reasons' in result:
            print("\n可能的原因:")
            for reason in result['reasons']:
                print(f"  - {reason}")
