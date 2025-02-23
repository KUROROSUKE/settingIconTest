import os
import pandas as pd
import json

# データセットフォルダのパス
dataset_dir = "train_AI/Datasets"

# JSONデータを格納するリスト
json_data = []

# JSONファイルをリストから取得
file_names = sorted([f for f in os.listdir(dataset_dir) if f.endswith(".json")])

for file_name in file_names:
    file_path = os.path.join(dataset_dir, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):  # JSONがリスト形式なら展開して追加
                json_data.extend(data)
            else:  # 辞書形式ならそのまま追加
                json_data.append(data)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

# DataFrameに変換
df = pd.DataFrame(json_data)

# リスト型のデータを文字列に変換（見やすくするため）
# リスト型のデータを文字列に変換（見やすくするため）
list_columns = ["p2_hand", "dropped_cards_p1", "dropped_cards_p2"]
for col in list_columns:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: ", ".join(x) if isinstance(x, list) and x else "")

print(df["p2_hand"])

df.to_csv("train_AI/data.csv",index=False)