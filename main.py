import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from engine.llm import OllamaLLM
from engine.planner import _respond_and_execute

def main():
    llm = OllamaLLM()
    print("\n🚀 LATT-Core V6.0 [完全隔离·稳定版]")
    while True:
        try:
            task = input("\n[指令] > ").strip()
            if not task: continue
            _respond_and_execute(llm, task)
        except KeyboardInterrupt: break
        except Exception as e: print(f"❌ 运行错误: {e}")

if __name__ == "__main__":
    main()
