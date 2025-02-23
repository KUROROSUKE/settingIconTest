import pandas as pd
import ast  # 文字列を辞書に変換するために使用

data = pd.read_csv("train_AI/Data/data.csv")

print(data["p2_hand"])

dicts = {
    "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
    "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
    "Fe": 26, "Cu": 29, "Zn": 30, "I": 53
}

# `p2_hand` の変換
data["hand"] = data["p2_hand"].apply(lambda x: [dicts[elem] for elem in str(x).split(", ")] if pd.notna(x) else [])

# `droped_cards_p1` の変換（NAを適切に処理）
data["droped_cards_p1"] = data["droped_cards_p1"].apply(lambda x: [dicts[elem] for elem in str(x).split(", ")] if pd.notna(x) else pd.NA)

# `droped_cards_p2` の変換
data["droped_cards_p2"] = data["droped_cards_p2"].apply(lambda x: [dicts[elem] for elem in str(x).split(", ")] if pd.notna(x) else [])

# `select_card` の変換（辞書形式の文字列をリストに変換）
def convert_select_card(val):
    if pd.notna(val):
        try:
            card_dict = ast.literal_eval(val)  # 文字列を辞書に変換
            card_list = [dicts[key] for key, count in card_dict.items() for _ in range(count)]  # 要素を展開
            return card_list
        except (SyntaxError, ValueError):
            return []
    return []

data["select_card"] = data["select_card"].apply(convert_select_card)

# 元のデータをコピーして新しい行を作成
new_rows = data.copy()

# もとのデータにコピーを追加
data = pd.concat([data, new_rows], ignore_index=True)

# `p2_hand` を削除
data.drop(columns="p2_hand", inplace=True)

print(data)
data.to_csv("train_AI/Data/label.csv", index=False)
