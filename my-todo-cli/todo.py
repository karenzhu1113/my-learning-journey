#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

DATA_FILE = "todos.json"

def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(title):
    if not title.strip():
        print("错误：请输入任务名称")
        return
    
    todos = load_todos()
    
    new_id = max(t["id"] for t in todos) + 1 if todos else 1
    
    todo = {
        "id": new_id,
        "title": title.strip(),
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    
    todos.append(todo)
    save_todos(todos)
    print(f"已添加待办: [{new_id}] {title.strip()}")

def list_todos():
    todos = load_todos()
    
    if not todos:
        print("暂无待办任务")
        return
    
    print("\n待办列表:")
    print("-" * 50)
    
    for todo in todos:
        status = "[✓]" if todo["completed"] else "[ ]"
        created_at = todo.get("created_at", "")[:19].replace("T", " ")
        print(f"  {status} [{todo['id']}] {todo['title']}  ({created_at})")
    
    completed_count = sum(1 for t in todos if t["completed"])
    print("-" * 50)
    print(f"总计: {len(todos)} 个任务, 已完成: {completed_count} 个\n")

def complete_todo(task_id):
    todos = load_todos()
    
    found = False
    for todo in todos:
        if todo["id"] == task_id:
            todo["completed"] = True
            found = True
            break
    
    if not found:
        print(f"错误：找不到该任务 (id={task_id})")
        return
    
    save_todos(todos)
    print(f"已标记完成: [{task_id}]")

def delete_todo(task_id):
    todos = load_todos()
    
    original_count = len(todos)
    todos = [t for t in todos if t["id"] != task_id]
    
    if len(todos) == original_count:
        print(f"错误：找不到该任务 (id={task_id})")
        return
    
    save_todos(todos)
    print(f"已删除任务: [{task_id}]")

def show_help():
    print("""
my-todo-cli - 待办管理工具

用法:
  python3 todo.py add <任务名称>    添加待办
  python3 todo.py list              列出所有待办
  python3 todo.py complete <id>     标记任务为已完成
  python3 todo.py delete <id>       删除任务
  python3 todo.py help              显示帮助

示例:
  python3 todo.py add "学习 Python"
  python3 todo.py complete 1
  python3 todo.py delete 2
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("错误：请输入任务名称")
            print("用法: python3 todo.py add <任务名称>")
            return
        title = " ".join(sys.argv[2:])
        add_todo(title)
    
    elif command == "list":
        list_todos()
    
    elif command == "complete":
        if len(sys.argv) < 3:
            print("错误：请输入任务 ID")
            print("用法: python3 todo.py complete <id>")
            return
        try:
            task_id = int(sys.argv[2])
            complete_todo(task_id)
        except ValueError:
            print("错误：任务 ID 必须是数字")
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("错误：请输入任务 ID")
            print("用法: python3 todo.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
            delete_todo(task_id)
        except ValueError:
            print("错误：任务 ID 必须是数字")
    
    elif command == "help":
        show_help()
    
    else:
        print(f"未知命令: {command}")
        show_help()

if __name__ == "__main__":
    main()
