if __name__ == '__main__':
    import pandas as pd

    # 指定Excel文件的路径
    excel_file = "output/data.xlsx"

    # 读取Excel文件，指定要读取的列（例如，列A、B、C）
    columns_to_extract = ['word1', 'word2', 'word3']  # 请根据您的需求修改这里的列名

    # 读取指定的列到DataFrame
    df = pd.read_excel(excel_file, usecols=columns_to_extract)

    # 指定输出文本文件的路径
    output_text_file = "output/word_freq_to_txt.txt"

    # 将DataFrame保存为文本文件，以制表符分隔（可以根据需要更改分隔符）
    df.to_csv(output_text_file, sep='\t', index=False)

    print(f"Excel文件的指定列已保存到 {output_text_file}")
