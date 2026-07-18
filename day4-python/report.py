# 导入 json 模块，用于解析 JSON 文件
import json
# 导入 os 模块，用于检查文件是否存在
import os

# 定义进度文件的相对路径
file_path = "progress.json"

# 使用 try/except 结构捕获可能的异常
try:
    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 文件不存在时抛出 FileNotFoundError 异常
        raise FileNotFoundError(f"文件 {file_path} 不存在")
    
    # 使用 with 语句打开文件，自动管理文件句柄
    with open(file_path, "r", encoding="utf-8") as f:
        # 用 json.load() 将文件内容解析为 Python 字典
        data = json.load(f)

# 捕获文件不存在的异常
except FileNotFoundError as e:
    # 打印错误信息
    print(f"错误: {e}")
    # 退出程序，状态码 1 表示出错
    exit(1)

# 捕获 JSON 格式错误的异常
except json.JSONDecodeError as e:
    # 打印错误信息
    print(f"错误: JSON 格式无效 - {e}")
    # 退出程序
    exit(1)

# 捕获其他未预期的异常
except Exception as e:
    # 打印错误信息
    print(f"错误: {e}")
    # 退出程序
    exit(1)

# 从 data 字典中获取学习者名字并打印
print(f"学习者: {data['learner']['name']}")
# 从 data 字典中获取学习者角色并打印
print(f"角色: {data['learner']['role']}")

# 获取每日记录列表
daily_records = data["daily_records"]

# 计算总天数：每日记录的条数
total_days = len(daily_records)

# 统计已完成天数：遍历记录，筛选 completed 为 True 的项并计数
completed_days = sum(1 for record in daily_records if record["completed"])

# 计算完成百分比，避免除以0，保留1位小数
completion_percent = (completed_days / total_days) * 100 if total_days > 0 else 0

# 打印学习进度统计
print(f"\n学习进度: {completed_days}/{total_days} 天完成 ({completion_percent:.1f}%)")

# 列表推导式：筛选已完成记录中的技能，展开为扁平列表
all_skills = [skill for record in daily_records if record["completed"] for skill in record["skills"]]

# 去重：将列表转为集合（自动去重），再转回列表
unique_skills = list(set(all_skills))

# 打印已掌握技能的数量和列表
print(f"\n已掌握技能 ({len(unique_skills)} 项):")
# 遍历去重后的技能列表并打印
for skill in unique_skills:
    print(f"- {skill}")

# 获取薄弱点列表
weaknesses = data["weaknesses"]

# 打印薄弱点的数量和列表
print(f"\n薄弱点 ({len(weaknesses)} 项):")
# 遍历薄弱点列表并打印
for weakness in weaknesses:
    print(f"- {weakness}")
