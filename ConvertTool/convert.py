import json

def convert_excel_to_json(file_path):
    df = pd.read_excel(file_path)

    data = []
    for _, row in df.iterrows():
        entry = {
            "question": row["Question"],
            "options": [
                row["Option1"],
                row["Option2"],
                row["Option3"],
                row["Option4"]
            ],
            "answer": row["Answer"]
        }
        data.append(entry)

    return json.dumps(data, ensure_ascii=False, indent=4)

json_output = convert_excel_to_json(file_path)
