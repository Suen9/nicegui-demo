from fastapi import FastAPI
from nicegui import ui
from pathlib import Path
import importlib

app = FastAPI()

# 动态导入 modules 目录下所有 .py 文件
modules_dir = Path("pages")
for module_file in modules_dir.glob("*.py"):
    if module_file.name != "__init__.py":
        module_name = module_file.stem
        module = importlib.import_module(f"pages.{module_name}")


# 动态导入 api 目录下所有 .py 文件
api_dir = Path("api")
for api_file in api_dir.glob("*.py"):
    if api_file.name != "__init__.py":
        api_name = api_file.stem
        api_module = importlib.import_module(f"api.{api_name}")
        if hasattr(api_module, "router"):
            app.include_router(api_module.router)

ui.run_with(app)
