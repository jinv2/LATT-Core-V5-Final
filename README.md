# 🦞 LATT-Core V5 Final (神思)

**专为 1050 Ti 深度优化的纯本地 AI Agent 驱动框架。**



## 🌟 项目亮点
- **极简骨架**: 剔除冗余 UI，保留 OpenInterpreter 01 协议最核心的“思考-执行”逻辑。
- **低功存优化**: 专为 4GB 显存设计，推理时显存占用稳定在 ~3.5GB。
- **神思协议**: 自动捕获并执行代码块，支持文件系统、视频处理（ffmpeg）的物理操作。

## 🚀 快速启动
```bash
# 克隆本项目
git clone [https://github.com/jinv2/LATT-Core-V5-Final.git](https://github.com/jinv2/LATT-Core-V5-Final.git)
cd LATT-Core-V5-Final

# 一键安装环境依赖
chmod +x install.sh
./install.sh

# 运行神思核心
python3 gui_protocol.py
\```

## ⚠️ 模型准备
- 本仓库不包含 **2GB** 的 `model.gguf`。
- 请将您的模型放入 `config/` 目录并命名为 `model.gguf`。

## 🛠️ 实战案例
- **视频处理**: 自动调用 `ffmpeg` 进行去水印（delogo）。
- **文件管理**: 自动创建工具脚本并物理落盘。
