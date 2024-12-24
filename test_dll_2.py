import ctypes
import inspect

# 加载 DLL 文件
dll_path = "F:\Anaconda\envs\PyTorch\Lib\site-packages\pythonfmu\\blossom_1.dll"  # 替换为你的 DLL 文件路径
funcs_1 = ctypes.CDLL(dll_path)

# 获取 DLL 中的所有函数
attributes = dir(funcs_1)

# 获取所有函数
functions = [name for name in attributes if callable(getattr(funcs_1, name))]
print("functions",functions)

for func_name in functions:
    function = getattr(funcs_1, func_name)  # 获取函数对象

    # 获取函数签名的地方，你需要提前了解每个函数的参数类型和返回类型
    # ctypes 函数需要手动指定类型
    # 假设该函数没有参数并返回整数类型
    # 根据实际情况修改函数签名
    function.argtypes = []  # 无参数
    function.restype = ctypes.c_int  # 返回类型是整数

    # 打印函数信息
    print(f"Function: {func_name}")
    print("Inputs:")
    for param_name in function.argtypes:
        print(f"  {param_name}")  # 打印输入参数的类型（如果有的话）

    print(f"Output: {function.restype}\n")
