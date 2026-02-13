import re
import subprocess

def _respond_and_execute(llm, task, gui_callback=None):
    # 极简指令，减少 AI 思考负担
    system_prompt = "你是一个 Bash 终端助手。请直接输出 [RUN]命令[/RUN]，不要解释。"
    context = f"{system_prompt}\n任务: {task}"
    
    for i in range(1, 3): # 减少步数限制，防止死循环
        if gui_callback: gui_callback(f"\n🧠 [神思推理步数 {i}] ")
        response = llm.chat(context)
        
        # 只要包含 [RUN] 就抓取
        match = re.search(r"\[RUN\]\s*(.*?)\s*\[/RUN\]", response, re.DOTALL | re.IGNORECASE)
        
        if match:
            cmd = match.group(1).strip()
            if gui_callback: gui_callback(f"⚡ 执行: {cmd}\n")
            try:
                # 强制在上一级目录执行 ls，绕过 cd 的状态保持问题
                if "上一级" in task or ".." in task:
                    cmd = "ls -la .."
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, timeout=15)
                result = "\n".join(result.splitlines()[:10]) # 只取前10行
            except Exception as e:
                result = f"错误: {str(e)}"
            
            if gui_callback: gui_callback(f"👁️ 回显:\n{result}\n")
            break # 执行完就跳出，防止 Q2 模型乱绕路
        else:
            # 【重要】如果没有匹配到 [RUN]，直接把 AI 的原话喷出来，方便调试
            if gui_callback: gui_callback(f"⚠️ 未检测到指令，AI 回复：\n{response}\n")
            break
