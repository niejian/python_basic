### fastapi 安装
```shell
# 
pip install fastapi
```
#### 安装ASGI
> Uvicorn是一个基于ASGI（Asynchronous Server Gateway Interface）的异步Web服务器，用于运行异步Python web应用程序。
> 它是由编写FastAPI框架的开发者设计的，旨在提供高性能和低延迟的Web服务

```shell
# ASGI是异步网关协议接口，一个介于网络协议服务和 Python 应用之间的标准接口，能够处理多种通用的协议类型，包括 HTTP，HTTP2和 WebSocket。
pip install "uvicorn[standard]"
# 启动

```
#### 启动调试
```shell
uvicorn main:app --reload
#动命令uvicorn main:app --reload中的app，指的是app = FastAPI()变量，也可以是其他自己定义的名称;
```