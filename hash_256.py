'''
Date: 2024-12-15 17:24:20
LastEditors: yangyehan 1958944515@qq.com
LastEditTime: 2024-12-15 18:23:22
FilePath: /vscode/hash加密算法/hash_256.py
Description: 
'''
import hashlib

def desensitize(private_info, seed: str) -> str:
    """
    对隐私信息进行脱敏处理，使用哈希算法加盐值加密。
    
    参数：
    private_info (str): 隐私信息（如姓名或学号）
    seed (str): 盐值，用于增加哈希的安全性
    
    返回：
    str: 加密后的脱敏信息
    """
    if not private_info or not seed:
        raise ValueError("隐私信息和盐值不能为空")
    
    # 将隐私信息和盐值结合
    combined_info = f"{str(private_info)}{seed}"
    
    # 使用SHA-256哈希算法对组合信息进行加密
    hash_object = hashlib.sha256(combined_info.encode('utf-8'))
    
    # 获取加密后的十六进制字符串
    encrypted_info = hash_object.hexdigest()
    
    return encrypted_info

if __name__ == "__main__":
    # 输入隐私信息和盐值
    private_info = 2021213038
    seed = "secure_salt_value_123"
    
    # 调用脱敏函数
    encrypted_result = desensitize(private_info, seed)
    
    print(f"原始信息: {private_info}")
    print(f"加密后的信息: {encrypted_result}")