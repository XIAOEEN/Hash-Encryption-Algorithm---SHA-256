import os
import re
import pandas as pd
from tqdm import tqdm  
from hash_256 import desensitize


def get_seed_by_year(student_id, seed_df):
    """
    根据学号前四位的年份，从 seed 数据表中获取对应的 seed。
    
    参数：
    student_id (str): 学号
    seed_df (pd.DataFrame): 包含年份和对应 seed 的 DataFrame
    
    返回：
    str: 匹配到的 seed 或 None
    """
    match = re.match(r'^(\d{4})', str(student_id))
    if match:
        year = match.group(1)
        seed_row = seed_df[seed_df['year'] == int(year)]
        if not seed_row.empty:
            return seed_row['seed'].values[0]
    return None


def process_excel_files(student_folder, seed_file, column_name):
    """
    批量处理学生 Excel 文件，读取指定列并根据年份使用对应 seed 加密，将加密数据插入学号列前一列。
    
    参数：
    student_folder (str): 包含学生 Excel 文件的文件夹路径
    seed_file (str): 包含年份和 seed 的 Excel 文件路径
    column_name (str): 要加密的列名
    """
    if not os.path.exists(student_folder):
        raise FileNotFoundError("指定的学生文件夹不存在")
    if not os.path.exists(seed_file):
        raise FileNotFoundError("指定的 seed 文件不存在")
    
    # 加载 seed 数据
    seed_df = pd.read_excel(seed_file, engine='openpyxl')
    if 'year' not in seed_df.columns or 'seed' not in seed_df.columns:
        raise ValueError("seed Excel 文件必须包含 'year' 和 'seed' 列")
    
    # 获取学生 Excel 文件列表
    excel_files = [f for f in os.listdir(student_folder) if f.endswith('.xlsx') or f.endswith('.xls')]
    
    if not excel_files:
        print("未找到任何学生 Excel 文件")
        return

    unmatched_ids = []  # 用于记录未匹配到 seed 的学号

    for file_name in excel_files:
        file_path = os.path.join(student_folder, file_name)
        print(f"正在处理文件: {file_name}")
        
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
        except Exception as e:
            print(f"文件 {file_name} 无法读取，错误信息: {e}")
            continue
        
        # 检查是否包含指定列
        if column_name not in df.columns:
            print(f"文件 {file_name} 中未找到 '{column_name}' 列，跳过处理")
            continue
        
        # 加密处理并记录未匹配学号
        def encrypt_with_seed(student_id):
            seed = get_seed_by_year(student_id, seed_df)
            if seed:
                return desensitize(student_id, seed)
            else:
                unmatched_ids.append(student_id)
                return None
        
        with tqdm(total=len(df), desc=f"处理 {file_name}") as pbar:
            encrypted_data = []
            for student_id in df[column_name]:
                encrypted_data.append(encrypt_with_seed(student_id))
                pbar.update(1) 
            
            df[f'{column_name}_hash'] = encrypted_data
        
    
        col_idx = df.columns.get_loc(column_name)
        encrypted_col = df.pop(f'{column_name}_hash')
        df.insert(col_idx, f'{column_name}_hash', encrypted_col)
        
        try:
            df.to_excel(file_path, index=False, engine='openpyxl')
            print(f"文件 {file_name} 处理完成并保存")
        except Exception as e:
            print(f"文件 {file_name} 保存失败，错误信息: {e}")
    
    if unmatched_ids:
        unmatched_ids = list(set(unmatched_ids))  # 去重
        print("\n以下学号未匹配到对应的 seed, 请检查是否包含年份对应的seed值:")
        for student_id in unmatched_ids:
            print(student_id)


if __name__ == "__main__":
    student_folder = "./student/"  
    seed_file = "./seed.xlsx" 
    encrypt_col = "学号" 

    process_excel_files(student_folder, seed_file, encrypt_col)