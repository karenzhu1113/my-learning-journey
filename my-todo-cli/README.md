# my-todo-cli

一个简单的命令行待办管理工具。

## 技术栈

- Python 3
- 标准库：json, os, sys, datetime

## 安装方法

```bash
# 克隆仓库
git clone https://github.com/karenzhu1113/my-learning-journey.git
cd my-learning-journey/my-todo-cli

# 运行（无需安装依赖，使用标准库）
python3 todo.py help
```

## 使用示例

```bash
# 添加待办
python3 todo.py add "学习 Python"

# 列出所有待办
python3 todo.py list

# 标记任务完成
python3 todo.py complete 1

# 删除任务
python3 todo.py delete 1
```

## 核心功能

1. 添加待办：输入任务名称，添加到列表，待办需要和日期时间绑定
2. 列出待办：显示所有待办列表
3. 标记完成：标记某个任务为已完成
4. 删除待办：删除某个任务

## 边界条件

- 标题为空：提示"请输入任务名称"
- id 不存在：提示"找不到该任务"
- todos.json 不存在：自动创建空列表
