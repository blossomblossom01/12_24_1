import ctypes
import os


def check_function_in_dll(dll_path, function_name):
    try:
        # 加载 DLL
        dll = ctypes.CDLL(dll_path)

        # 尝试获取函数
        func = getattr(dll, function_name, None)

        # 如果函数存在，返回 True
        if func:
            print(f"函数 '{function_name}' 存在于 DLL 中")
            return True
        else:
            print(f"函数 '{function_name}' 不存在于 DLL 中")
            return False
    except Exception as e:
        print(f"加载 DLL 时发生错误: {e}")
        return False


# 示例使用
dll_path = 'F:\Anaconda\envs\PyTorch\Lib\site-packages\pythonfmu\\blossom_1.dll'  # 替换为你实际的 DLL 文件路径
function_name = 'do_step'  # 替换为你要检查的函数名
# function_name = 'fmi2GetRealArray'  # 替换为你要检查的函数名

check_function_in_dll(dll_path, function_name)