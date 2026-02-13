import customtkinter as ctk
import threading
import os
import sys

# 基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# 尝试导入引擎
try:
    from engine.llm import OllamaLLM
    from engine.planner import _respond_and_execute
    ENGINE_READY = True
except ImportError:
    ENGINE_READY = False

from PIL import Image

LOCAL_LOGO_PATH = "/home/mmm/桌面/截屏/LOGO/logo_ts.png"

class ShensistProtocolGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.BRAND_CYAN = "#00FFFF"
        self.BG_DEEP = "#05050A"
        self.PANEL_BLUE = "#0D0D1F"

        self.grab_release() 
        self.title("LATT-Protocol | 神思庭AI无人研究室")
        self.geometry("1100x850")
        self.configure(fg_color=self.BG_DEEP)
        self.after(500, lambda: self.config(cursor="left_ptr"))

        # --- UI ---
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color=self.PANEL_BLUE)
        self.sidebar.pack(side="left", fill="y")
        ctk.CTkLabel(self.sidebar, text="神思庭", font=("Microsoft YaHei", 24, "bold"), text_color="#FFFFFF").pack(pady=(30, 0))
        ctk.CTkLabel(self.sidebar, text="AI无人研究室", font=("Microsoft YaHei", 14), text_color=self.BRAND_CYAN).pack(pady=(5, 20))

        self.logo_container = ctk.CTkFrame(self.sidebar, width=120, height=120, fg_color="#080815", corner_radius=15)
        self.logo_container.pack(pady=20, padx=20)
        self.logo_container.pack_propagate(False)
        self.logo_label = ctk.CTkLabel(self.logo_container, text="")
        self.logo_label.pack(expand=True)
        threading.Thread(target=self.safe_load_logo, daemon=True).start()

        self.main_view = ctk.CTkFrame(self, fg_color="transparent")
        self.main_view.pack(side="right", fill="both", expand=True, padx=30)
        self.console = ctk.CTkTextbox(self.main_view, font=("Cascadia Code", 14), fg_color="#000000", text_color=self.BRAND_CYAN, border_width=1, border_color="#1A1A3A")
        self.console.pack(fill="both", expand=True, pady=(40, 20))

        self.entry_frame = ctk.CTkFrame(self.main_view, fg_color="transparent")
        self.entry_frame.pack(fill="x", pady=(0, 40))
        self.entry = ctk.CTkEntry(self.entry_frame, placeholder_text="下达任务指令...", height=50, border_color=self.BRAND_CYAN, fg_color="#0A0A15")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 15))
        self.entry.bind("<Return>", lambda e: self.execute())

        self.run_btn = ctk.CTkButton(self.entry_frame, text="执行指令", width=120, height=50, fg_color=self.BRAND_CYAN, text_color="#000000", font=("Microsoft YaHei", 14, "bold"), command=self.execute)
        self.run_btn.pack(side="right")

        self.log_msg(">>> 神思庭核心协议 [V12.7] 已上线\n")
        if not ENGINE_READY: self.log_msg("⚠️ 警告: 未检测到 engine 模块！\n")
        self.log_msg("-" * 50 + "\n")

    def safe_load_logo(self):
        if os.path.exists(LOCAL_LOGO_PATH):
            try:
                img = Image.open(LOCAL_LOGO_PATH)
                ctk_img = ctk.CTkImage(img, size=(100, 100))
                self.after(0, lambda: self.logo_label.configure(image=ctk_img))
            except: pass

    def log_msg(self, text):
        # 线程安全更新
        self.after(0, lambda: self._sync_log(text))

    def _sync_log(self, text):
        self.console.insert("end", text)
        self.console.see("end")

    def execute(self):
        task = self.entry.get()
        if not task: return
        self.log_msg(f"\n[COMMAND] > {task}\n")
        self.entry.delete(0, 'end')
        threading.Thread(target=self.run_engine_logic, args=(task,), daemon=True).start()

    def run_engine_logic(self, task):
        if ENGINE_READY:
            try:
                llm = OllamaLLM()
                _respond_and_execute(llm, task, gui_callback=self.log_msg)
            except Exception as err:
                # 显式传递参数，解决 NameError
                error_msg = str(err)
                self.log_msg(f"❌ 执行出错: {error_msg}\n")
        else:
            self.log_msg("❌ 错误: 引擎未就绪。\n")

if __name__ == "__main__":
    app = ShensistProtocolGUI()
    app.mainloop()
