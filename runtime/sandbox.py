import subprocess, os, sys

def run_command(cmd):
    full_cmd = os.path.expanduser(cmd)
    
    # 交互式命令检测：如果是 htop 或需要输入密码的任务，直接调用系统 shell
    interactive_keywords = ['htop', 'sudo', 'nano', 'vim', 'top']
    is_interactive = any(kw in full_cmd for kw in interactive_keywords)

    try:
        if is_interactive:
            # 直接在当前进程执行，允许用户输入密码和交互
            return_code = os.system(full_cmd)
            return {"output": f"交互式任务执行完成，退出码: {return_code}", "code": return_code}
        else:
            # 普通任务继续使用静默捕获，并将超时增加到 300 秒
            p = subprocess.Popen(["/bin/bash", "-c", full_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = p.communicate(timeout=300)
            return {"output": stdout + stderr, "code": p.returncode}
    except subprocess.TimeoutExpired:
        return {"output": "❌ 错误: 任务超时。这可能是因为网络下载过慢或命令在等待交互。", "code": 1}
    except Exception as e:
        return {"output": str(e), "code": 1}
