from nicegui import ui
from ex4nicegui import to_ref
import aiohttp

# 注册接口
REGISTER_API_URL = "http://localhost:8000/api/auth/register"

@ui.page("/register")
def register_page():
    ui.add_body_html('<style>html, body { margin: 0; padding: 0; overflow: hidden; background: #E9EBEC}</style>')

    username = to_ref("")
    password = to_ref("")
    confirm_password = to_ref("")

    async def handle_register():
        # 输入校验
        if not username.value:
            ui.notify("用户名不能为空", type="negative", position="top")
            return
        if not password.value or not confirm_password.value:
            ui.notify("密码不能为空", type="negative", position="top")
            return
        if password.value != confirm_password.value:
            ui.notify("两次输入的密码不一致", type="negative", position="top")
            return

        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "username": username.value,
                    "password": password.value
                }
                async with session.post(REGISTER_API_URL, json=payload) as response:
                    data = await response.json()
                    
                    if data['code'] == 200:
                        ui.notify("注册成功，请返回登录", type="positive", position="top")
                        # 清空表单
                        username.value = ""
                        password.value = ""
                        confirm_password.value = ""
                        
                    else:
                        ui.notify(f"注册失败：{data['message']}", type="negative", position="top")
        except Exception as e:
            ui.notify(f"注册请求失败：{str(e)}", type="negative", position="top")

    with ui.column().classes("w-screen h-screen justify-center items-center"):
        with ui.card().classes("w-96 p-8 shadow-lg"):
            ui.label("注册").classes("text-2xl font-bold mb-4 self-center")
            ui.label("欢迎注册，请输入用户名和密码").classes("mb-6 text-zinc-400 self-center")
            
            ui.input("用户名").bind_value(username).classes("w-full mb-4")
            ui.input("密码", password=True).bind_value(password).classes("w-full mb-4")
            ui.input("确认密码", password=True).bind_value(confirm_password).classes("w-full mb-6")
            
            ui.button("注册", on_click=handle_register).classes("w-full")
            ui.separator()
            ui.button("返回登录", on_click=lambda: ui.navigate.to("/login", False)).classes("w-full bg-secondary")
ui.run()