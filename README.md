<!--
 * @Date: 2024-12-15 17:24:31
 * @LastEditors: yangyehan 1958944515@qq.com
 * @LastEditTime: 2024-12-15 18:37:06
 * @FilePath: /vscode/hash加密算法/readme_eng.md
 * @Description: 
-->

# Hash Encryption Algorithm - SHA-256

## Implementation Code

```python
import hashlib

def desensitize(private_info, seed: str) -> str:
    """
    Process sensitive information using a hash algorithm with a salt value.
    
    Parameters:
    private_info (any): Sensitive information (e.g., name or ID)
    seed (str): Salt value used to enhance hashing security
    
    Returns:
    str: Encrypted desensitized information
    """
    if not private_info or not seed:
        raise ValueError("Private information and salt value cannot be empty")
    
    combined_info = f"{str(private_info)}{seed}"
    
    # Encrypt the combined information using the SHA-256 hash algorithm
    hash_object = hashlib.sha256(combined_info.encode('utf-8'))

    encrypted_info = hash_object.hexdigest()
    
    return encrypted_info

if __name__ == "__main__":
    # Input private information and salt value
    private_info = 2021213038
    seed = "secure_salt_value_123"
    
    # Call the desensitization function
    encrypted_result = desensitize(private_info, seed)
    
    print(f"Original Information: {private_info}")
    print(f"Encrypted Information: {encrypted_result}")
```
### Example Output

Original Information: 2021213038  
Encrypted Information: 69cb2854b108c36c078efb6bc1bd08c0ef3768a6e9d6af204a0b7ca18015dbcf

### Description

1.	Hash Algorithm:
	- SHA-256 is used, a common and secure one-way hashing algorithm. It produces a fixed-length 64-character hexadecimal string as output.
	- Being one-way means the original data cannot be restored from the encrypted result.
2.	Security Recommendations:
	- Ensure the seed is a random and unpredictable string to avoid reduced security due to weak salt values (e.g., dictionary words).

### Parameter Type Information

- Input:
	- private_info: any (supports str, int, float, bool, list, tuple, dict, set, object)
	- seed: str
- Output:
	- encrypted_info: str

### Hash Algorithm Length Restrictions

Below is a table summarizing the theoretical input size limits for common hash algorithms (measured in bits):
| **Hash Algorithm** | **Input Length Limit**                  | **Output Length (Bits)** |
|---------------------|-----------------------------------------|--------------------------|
| MD5                | 2³² - 1 bits (approx. 512 MB)          | 128 bits                 |
| SHA-1              | 2⁶⁴ - 1 bits (approx. 2 EB)            | 160 bits                 |
| SHA-256            | 2⁶⁴ - 1 bits (approx. 2 EB)            | 256 bits                 |
| SHA-512            | 2¹²⁸ - 1 bits (virtually infinite)      | 512 bits                 |

### Input Length Notes

- No Practical Input Length Limit:
Modern hash algorithms (e.g., SHA-256, SHA-512) have no practical input length restrictions as they process data in chunks.
- Memory Constraints:
While the algorithms theoretically accept infinite input lengths, processing very large inputs depends on system memory availability.
- Implementation Constraints:
Specific programming libraries or environments may impose additional input size limits.

### Summary

This implementation combines sensitive data (private_info) with a salt (seed) to generate a secure hash using the SHA-256 algorithm. It supports various data types as input and ensures data security through one-way encryption. The algorithm produces consistent and predictable output, making it suitable for desensitization and data anonymization.

