from nicegui import ui
from ex4nicegui import to_ref
import aiohttp

#登录接口
LOGIN_API_URL = "http://localhost:8000/api/auth/login"

@ui.page("/login")
def login_page():
    ui.add_body_html('<style>html, body { margin: 0; padding: 0; overflow: hidden; background: #E9EBEC}</style>')

    username = to_ref("")
    password = to_ref("")

    #登录方法
    async def handle_login():
        if not username.value or not password.value:
            ui.notify("登录失败：用户名和密码不能为空", type="negative", position="top")
            return
        try:
            # 发起异步登录请求
            async with aiohttp.ClientSession() as session:
                payload = {"username": username.value, "password": password.value}
                async with session.post(LOGIN_API_URL, json=payload) as response:
                    data = await response.json()
                    if data['code'] == 200:
                            ui.notify(f"欢迎：{data['username']}回来！", type="positive", position="top")
                    else:
                        ui.notify(f"登录失败：{data['message']}", type="negative", position="top")
        except Exception as e:
            ui.notify("登录失败", type="negative", position="top")

    with ui.column().classes("w-screen h-screen justify-center items-center"):
        with ui.card().classes("w-96 p-8 shadow-lg"):
            ui.label("登录").classes("text-2xl font-bold mb-4 self-center")
            ui.label("在进入系统之前请先输入用户名和密码进行登录").classes("mb-6 text-zinc-400")
            ui.input("用户名").bind_value(username).classes("w-full mb-4")
            ui.input("密码", password=True).bind_value(password).classes("w-full mb-6")
            ui.button("登录", on_click=handle_login).classes("w-full")
            ui.separator()
            ui.button("注册", on_click=lambda: ui.navigate.to("/register", False)).classes("w-full bg-amber")
ui.run()
