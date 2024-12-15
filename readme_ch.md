<!--
 * @Date: 2024-12-15 17:24:31
 * @LastEditors: yangyehan 1958944515@qq.com
 * @LastEditTime: 2024-12-15 18:28:49
 * @FilePath: /vscode/hash加密算法/readme.md
 * @Description: 
-->

# 哈希加密算法-SHA-256

实现代码

```python
import hashlib

def desensitize(private_info, seed: str) -> str:
    """
    对隐私信息进行脱敏处理，使用哈希算法加盐值加密。
    
    参数：
    private_info (any): 隐私信息（如姓名或学号）
    seed (str): 盐值，用于增加哈希的安全性
    
    返回：
    str: 加密后的脱敏信息
    """
    if not private_info or not seed:
        raise ValueError("隐私信息和盐值不能为空")
    
    combined_info = f"{str(private_info)}{seed}"
    
    # 使用SHA-256哈希算法对组合信息进行加密
    hash_object = hashlib.sha256(combined_info.encode('utf-8'))

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
```


### 输出示例

原始信息: 张三
加密后的信息: 7815696ecbf1c96e6894b779456d330e36f3c3db24d2059d1dc3d7992f0f8d9e

### 说明

1.	哈希算法：
    - 	使用的是 SHA-256 哈希算法，它是一种常见且安全的单向加密算法，输出固定长度的 64 位十六进制字符串。
	- 单向性意味着无法从加密结果中还原原始数据。
2.	安全建议：
	- 确保 seed 是一个随机且难以预测的字符串，避免弱盐值（如常见字典单词）导致的安全性下降。

### 关于入参类型
- 入参:
    - private_info:any(str,int,float,bool,list,tuple,dict,set,object)
    - seed:str
- 输出:
    - encrypted_info:str

### 调研关于hash理论限制

以下是一些常见哈希算法对输入长度的理论限制（以字节为单位）：

| 哈希算法  | 输入长度限制                   | 输出长度（比特） |
|-----------|-------------------------------|-----------------|
| MD5       | 2³² - 1 位（约 512 MB）       | 128 位          |
| SHA-1     | 2⁶⁴ - 1 位（约 2 EB = 2⁶⁴ 位）| 160 位          |
| SHA-256   | 2⁶⁴ - 1 位（约 2 EB）         | 256 位          |
| SHA-512   | 2¹²⁸ - 1 位（几乎无限）       | 512 位          |

### 由于算法优化，实际上并没有长度限制：
- 常见的哈希算法（如 SHA-256、SHA-512）对输入长度通常没有实际限制，因为这些算法使用分块处理数据，理论上可以处理任意长度的输入。
- 输入被分块后，算法逐块计算哈希值，因此只受限于：
- 内存可用性：处理非常大的输入可能需要更多内存。
- 实现约束：某些编程库可能对输入长度施加限制。






