# AgentFramework

一个基于Go语言和tRPC框架构建的智能代理框架，提供模块化的AI代理服务能力。

## 项目简介

AgentFramework是一个轻量级的AI代理服务框架，采用现代化的微服务架构设计，支持快速构建和部署智能代理应用。

### 技术栈

- **编程语言**: Go 1.22.4+
- **RPC框架**: tRPC v1.0.3
- **协议**: gRPC/Protobuf
- **依赖管理**: Go Modules

## 项目结构

```
agent_framework/
├── entity/           # 实体定义和工具类
│   ├── consts/       # 常量定义
│   └── utils/        # 工具函数
├── logic/            # 业务逻辑层
├── pb/               # Protobuf定义和生成代码
├── repo/             # 数据仓库层
│   └── deepseek/     # DeepSeek API集成
├── main.go           # 应用入口
├── agent_framework.proto  # API接口定义
└── go.mod           # 依赖管理
```

## 快速开始

### 环境要求

- Go 1.22.4 或更高版本
- Git
- tRPC

### 安装依赖

```bash
# 安装项目依赖
cd pb
go mod tidy

# 返回根目录
cd ..
```

### 构建项目

```bash
# 构建应用
go build -o agent_framework
```

### 运行服务

```bash
# 启动服务
./agent_framework
```

## API接口

### Hello服务

当前框架提供了一个简单的Hello服务用于测试：

```protobuf
syntax = "proto3";

service Service {
  rpc Hello(Request) returns(Response);
}

message Request {
  string query = 1;
}

message Response {
  string msg = 1;
}
```

## 开发指南

### 添加新的API接口

1. 在 `agent_framework.proto` 中定义新的RPC方法
2. 重新生成Protobuf代码
3. 在 `logic/` 目录下实现业务逻辑
4. 在 `main.go` 中注册新的服务处理器

### 模块说明

- **entity**: 定义数据模型和共享工具
- **logic**: 实现核心业务逻辑
- **repo**: 数据访问层，集成外部API和数据库
- **pb**: Protobuf接口定义和生成的客户端代码

## 命令行工具

### 安装 trpc-cmdline

1. 请将以下配置添加到 `~/.gitconfig` 文件中：

   ```ini
   [url "ssh://git@github.com/"]
       insteadOf = https://github.com/
   ```

2. **安装trpc命令行工具**：
   
   ```bash
   go install trpc.group/trpc-go/trpc-cmdline/trpc@latest
   ```

### 生成桩代码

使用以下命令从Protobuf文件生成RPC桩代码：

```bash
# 在项目根目录执行
trpc create -p agent_framework.proto -o pb --rpconly
```

**参数说明**：
- `-p`: 指定Protobuf文件路径
- `-o`: 指定输出目录

### 验证安装

安装完成后，可以通过以下命令验证trpc工具是否安装成功：

```bash
trpc version
```

## 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 许可证

本项目采用 MIT 许可证

## 联系方式

- 问题反馈: 821342264@qq.com
