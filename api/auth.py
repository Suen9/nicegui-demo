from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.base import create_db_and_tables, async_session_maker
from crud.user import create_user, get_user_by_username

# 创建路由实例
router = APIRouter()

# 请求体
class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    password: str

# 响应体
class LoginResponse(BaseModel):
    code: int
    message: str
    username: str|None

class RegisterResponse(BaseModel):
    code: int
    message: str
    


#登录接口
@router.post("/api/auth/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    #创建数据库链接
    await create_db_and_tables()

    async with async_session_maker() as session:
        #查询用户实体
        user = await get_user_by_username(session, login_data.username)
        if user:
            if user.password != login_data.password:
                return {"code": 400,"message": "密码错误", "username": None}
        else:
            return {"code": 400,"message": "用户不存在", "username": None}

        return {"code": 200,"message": "登录成功", "username": user.username}
   
#注册接口
@router.post("/api/auth/register" , response_model=RegisterResponse)
async def register(register_data: RegisterRequest):
    #创建数据库链接
    await create_db_and_tables()

    #新增新用户
    async with async_session_maker() as session:

    #检查用户名是否存在
        user = await get_user_by_username(session, register_data.username)
        if user:
            return {"code": 400, "message": "用户名已存在"}
        new_user = await create_user(session, register_data.username, register_data.password)
        
    if not new_user:
        return {"code": 404, "message": "系统出现错误, 注册失败请联系管理员"}
    
    print(f"Created user: {new_user.username}")
    return {"code": 200,"message": "注册成功"}