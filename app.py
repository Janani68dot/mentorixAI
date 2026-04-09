from pathlib import Path
import os
import sys
import runpy

BASE_DIR = Path(__file__).resolve().parent
APP_PATH = BASE_DIR / "ai-study-planner-main" / "app.py"

if not APP_PATH.exists():
    raise FileNotFoundError(f"Could not find app.py at {APP_PATH}")

sys.path.insert(0, str(APP_PATH.parent))
os.chdir(APP_PATH.parent)
runpy.run_path(str(APP_PATH), run_name="__main__")
