# 1.Batch Process Script - Version 2.0

## 1.1 Updates

### Version Upgrades
1. **Support for Batch Processing of Student Files**  
   - Automatically load multiple student Excel files from a specified folder.
   - Process each row step by step, and add a new column in the original file to store the encrypted data.

2. **Real-Time Row Progress Updates**  
   - Utilize the `tqdm` progress bar library to clearly display file and row processing progress, enhancing user experience.

3. **Automatic Matching of Encryption Seeds**  
   - Extract the year from the first four digits of the student ID and automatically match the corresponding salt value in the `seed` file, ensuring consistency and security in data encryption.

4. **Unmatched Data Prompts**  
   - Automatically record student IDs that do not match a salt value and print them out after the task is completed, allowing for easy checking and correction.

5. **Optimized Data Structure**  
   - The encrypted column will be inserted before the original column being encrypted (e.g., "student ID"), keeping the table structure clear and logical.

6. **Enhanced Error Handling**  
   - If a file fails to be read or saved, it will be skipped, and detailed error information will be output without affecting the processing of other files.

---

## 2.Usage Instructions

### 2.1 Environment Setup
1. Install dependencies:
```bash
   pip install pandas openpyxl tqdm
```
2. Ensure the hash_256.py (Version 1.0) file is in the same directory as the main script.
3. Format requirements for seed.xlsx:
   - The file must contain two columns: year and seed, representing the year and the corresponding salt value, respectively.
4. Place the student Excel files into the specified folder (e.g., ./student/), with the following requirements:
   - The files must include the column to be encrypted (e.g., “student ID”).
   - If the column to be encrypted is not “student ID,” modify the encrypt_col parameter in batch_process.py.
5. Run the script:
   
```bash
   python batch_process.py
```

---

## 3.Hash Encryption Algorithm - SHA-256 — version 1.0

### 3.1 Implementation Code

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
### 4. Example Output

Original Information: 2021213038  
Encrypted Information: 69cb2854b108c36c078efb6bc1bd08c0ef3768a6e9d6af204a0b7ca18015dbcf

### 5. Description

1.	Hash Algorithm:
	- SHA-256 is used, a common and secure one-way hashing algorithm. It produces a fixed-length 64-character hexadecimal string as output.
	- Being one-way means the original data cannot be restored from the encrypted result.
2.	Security Recommendations:
	- Ensure the seed is a random and unpredictable string to avoid reduced security due to weak salt values (e.g., dictionary words).

### 6. Parameter Type Information

- Input:
	- private_info: any (supports str, int, float, bool, list, tuple, dict, set, object)
	- seed: str
- Output:
	- encrypted_info: str

### 7. Hash Algorithm Length Restrictions

Below is a table summarizing the theoretical input size limits for common hash algorithms (measured in bits):
| **Hash Algorithm** | **Input Length Limit**                  | **Output Length (Bits)** |
|---------------------|-----------------------------------------|--------------------------|
| MD5                | 2³² - 1 bits (approx. 512 MB)          | 128 bits                 |
| SHA-1              | 2⁶⁴ - 1 bits (approx. 2 EB)            | 160 bits                 |
| SHA-256            | 2⁶⁴ - 1 bits (approx. 2 EB)            | 256 bits                 |
| SHA-512            | 2¹²⁸ - 1 bits (virtually infinite)      | 512 bits                 |

### 8. Input Length Notes

- No Practical Input Length Limit:
Modern hash algorithms (e.g., SHA-256, SHA-512) have no practical input length restrictions as they process data in chunks.
- Memory Constraints:
While the algorithms theoretically accept infinite input lengths, processing very large inputs depends on system memory availability.
- Implementation Constraints:
Specific programming libraries or environments may impose additional input size limits.

### 9. Summary

This implementation combines sensitive data (private_info) with a salt (seed) to generate a secure hash using the SHA-256 algorithm. It supports various data types as input and ensures data security through one-way encryption. The algorithm produces consistent and predictable output, making it suitable for desensitization and data anonymization.

