import os
import json
import argparse


def fix_subtitle(input_path, replacements):
    if not os.path.exists(input_path):
        print(f"❌ 文件不存在: {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)

    # 如果有改动，写回文件
    if content != original_content:
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"√ 已完成替换并保存到: {input_path}")
    else:
        print("ℹ️ 未发现需要替换的内容，文件未修改~")


def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    if 'srt_file' not in config:
        raise ValueError("配置文件缺少 'srt_file' 字段")
    if 'replacements' not in config:
        raise ValueError("配置文件缺少 'replacements' 字段")
    if not isinstance(config['replacements'], list):
        raise ValueError("'replacements' 必须是列表")
    for item in config['replacements']:
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError("每个替换规则必须是长度为2的列表 [old, new]")

    return config['srt_file'], config['replacements']


def main():
    parser = argparse.ArgumentParser(description="批量替换字幕文件中的文本")
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        default="subtitle_config.json",
        help="JSON 配置文件路径（默认: subtitle_config.json）"
    )
    args = parser.parse_args()

    try:
        srt_file, replacements = load_config(args.config)
        fix_subtitle(srt_file, replacements)
    except Exception as e:
        print(f"❌ 错误: {e}")
        exit(1)


if __name__ == "__main__":
    main()
