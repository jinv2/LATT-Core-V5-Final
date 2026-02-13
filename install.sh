#!/bin/bash

# 🦞 LATT-Core V5 Final (神思) 一键部署脚本

echo "--------------------------------------------------"
echo "🚀 开始部署 LATT-Core V5 Final..."
echo "--------------------------------------------------"

# 1. 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未检测到 python3，请先安装。"
    exit 1
fi

# 2. 安装必要依赖
echo "📦 正在安装依赖库 (requests, psutil)..."
pip3 install requests psutil --quiet

# 3. 检查 Ollama
if ! command -v ollama &> /dev/null; then
    echo "🌐 正在安装 Ollama 引擎..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama 已安装。"
fi

# 4. 创建必要目录
mkdir -p tools config

# 5. 提示模型部署
echo "--------------------------------------------------"
echo "⚠️ 重要提示: "
echo "由于 GitHub 文件限制，模型文件 config/model.gguf 未包含在内。"
echo "请手动将您的 GGUF 模型放入 config/ 目录，或执行以下指令下载默认模型："
echo "   ollama pull deepseek-v2:lite"
echo "--------------------------------------------------"

echo "✅ 部署完成！"
echo "👉 启动方式："
echo "   终端 A: ollama serve"
echo "   终端 B: python3 gui_protocol.py"
