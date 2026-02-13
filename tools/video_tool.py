import os
from runtime.sandbox import run_command

def compress_video(input_name, output_name=None):
    """
    FFmpeg 封装层：实现高质量压缩
    """
    desktop = os.path.expanduser("~/桌面/")
    input_path = os.path.join(desktop, input_name)
    
    if not output_name:
        output_name = f"compressed_{input_name}"
    output_path = os.path.join(desktop, output_name)
    
    # 封装 crf=28 的压缩逻辑
    cmd = f"ffmpeg -i {input_path} -vcodec libx264 -crf 28 {output_path}"
    return cmd

