# grpc-python

## 环境准备
```shell
python -m pip install --upgrade pip

python -m pip install virtualenv
virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

### gRPC Python
```shell
python -m pip install grpcio
```

### gRPC tools
```shell
python -m pip install grpcio-tools
```

# gRPC Python 示例

## 更新gRPC服务
1. helloworld/helloworld.proto
2. helloworld/greeter_server.py
3. helloworld/greeter_client.py
## 生成代码
```shell
python -m grpc_tools.protoc -I./helloworld --python_out=./helloworld --grpc_python_out=./helloworld ./helloworld/helloworld.proto
```
命令参数说明：
- -I：指定proto文件的搜索目录，可以指定多个-I参数，指定多个搜索目录
- --python_out：指定生成python代码的目录
- --grpc_python_out：指定生成python gRPC代码的目录
- ./helloworld/helloworld/helloworld.proto：指定proto文件的路径
### 运行服务端
```shell
python helloworld/greeter_server.py
```
### 运行客户端
```shell
python helloworld/greeter_client.py
```