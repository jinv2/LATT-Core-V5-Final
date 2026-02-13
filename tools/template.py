from runtime.sandbox import run_command

def ffmpeg_compress(input_file, output_file):
    # 仿照 ffmpeg-buddy 的参数封装层
    cmd = f"ffmpeg -i {input_file} -vcodec libx264 -crf 28 {output_file}"
    return run_command(cmd)
