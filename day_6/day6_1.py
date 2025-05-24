####装饰器
# def 装饰器名(func):    # func 是要装饰的函数
#     def 包装函数(*args, **kwargs):  # 用来包裹原函数
#         # 添加新功能（如日志、计时等）
#         result = func(*args, **kwargs)  # 调用原函数
#         # 添加新功能（如清理工作）
#         return result
#     return 包装函数


#  *args 和 **kwargs 的作用
# *args：接收任意数量的位置参数（Positional Arguments），以元组（Tuple）形式保存。
# **kwargs：接收任意数量的关键字参数（Keyword Arguments），以字典（Dict）形式保存。
# 它们让装饰器的包装函数（wrapper）能接受被装饰函数（func）的所有参数类型，保证装饰器可以通用地处理不同参数的函数。

def cleanup(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 先执行原函数
        print("正在清理资源...")          # 后置代码
        return result
    return wrapper

@cleanup
def read_file():
    print("读取文件中...")
    return "文件内容"

print(read_file())
# 输出:
# 读取文件中...
# 正在清理资源...
# 文件内容
