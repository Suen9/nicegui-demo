# nicegui-demo

任务目标：使用Nicegui开发一个简单的Web应用程序，包含用户注册和登录功能

所使用到的技术栈：python312 + nicegui + ex4nicegui + Tailwind + quasarchs  + fastapi + sqlalchemy +sqllite

包管理：poetry

 

## 项目效果图

1. 登录
   ![](https://i0.hdslb.com/bfs/article/827a38c9fd24487958b8a0c36c286fd148708594.png)
2. 注册
   ![](https://i0.hdslb.com/bfs/article/49244991737cc2f93519751dcc4b730948708594.png)



## 本地运行与Docker部署项目

### 本地运行

环境：python312 

1. 进入到项目
   ``` bash
   cd nice-demo

2. 启动项目
   ```bash
   uvicorn main:app --reload
   ```

3. 启动路径

   > http://127.0.0.1:8000/login 登录界面
   >
   > http://127.0.0.1:8000/register 注册界面

### docker容器化部署

环境：archlinux 

1. 将项目文件上传到linux服务器中

2. 进入到项目中
   ```bash
   cd nice-demo
   ```

3. 构建镜像
   ```bash
   docker build -t my-python-app .
   ```

4. 运行容器（映射端口 8000 到宿主机）
   ```bash
   docker run -p 8000:8000 -v $(pwd):/usr/src/app my-python-app
   ```

5. 输入服务器ip + port打开web程序

   > http://192.168.10.107:8000/login

效果：

![](https://i0.hdslb.com/bfs/article/63e0926b74df9267336c8b35567fafe648708594.png)

![](https://i0.hdslb.com/bfs/article/6edda80d2deba42d9d33e3df6a46e11748708594.png)

