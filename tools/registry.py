def get_native_cmd(task):
    """根据关键词返回预设的硬核指令"""
    if ".py" in task and ("移动" in task or "move" in task):
        return "mkdir -p ~/桌面/LATT_POWER && mv ~/桌面/*.py ~/桌面/LATT_POWER/ && du -sh ~/桌面/LATT_POWER && ls ~/桌面/LATT_POWER"
    if "htop" in task:
        return "sudo apt update && sudo apt install -y htop && htop"
    if "压缩" in task or "ffmpeg" in task:
        return "ffmpeg -i ~/桌面/001.mp4 -vcodec libx264 ~/桌面/output.mp4"
    return None
