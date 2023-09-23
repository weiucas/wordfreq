import PyPDF2

# if __name__ == '__main__':
#     # 输入PDF文件名
#     pdf_file = "学术期刊综合评价数据标准化方法研究.pdf"
#
#     # 输出文本文件名
#     txt_file = "学术期刊综合评价数据标准化方法研究.txt"
#
#     # 打开PDF文件
#     with open(pdf_file, "rb") as pdf:
#         pdf_reader = PyPDF2.PdfFileReader(pdf)
#
#         # 创建一个空文本文件
#         with open(txt_file, "w", encoding="utf-8") as txt:
#             # 逐页读取PDF内容并写入文本文件
#             for page_num in range(pdf_reader.getNumPages()):
#                 page = pdf_reader.getPage(page_num)
#                 txt.write(page.extractText())
#
#     print(f"PDF已成功转换为文本文件：{txt_file}")

import PyPDF2
import re


def pdf_to_txt(pdf_file, txt_file):
    try:
        with open(pdf_file, "rb") as pdf:
            pdf_reader = PyPDF2.PdfFileReader(pdf)

            with open(txt_file, "w", encoding="utf-8") as txt:
                for page_num in range(pdf_reader.getNumPages()):
                    page = pdf_reader.getPage(page_num)
                    text = page.extractText()
                    # 使用正则表达式去除字间多余的空格
                    cleaned_text = re.sub(r'\s+', ' ', text)
                    txt.write(cleaned_text)
                    print(f"正在处理页 {page_num + 1}/{pdf_reader.getNumPages()}")

        print(f"PDF已成功转换为文本文件：{txt_file}")
    except Exception as e:
        print(f"转换失败：{e}")


if __name__ == "__main__":
    pdf_file = "Recommender Systems LLM.pdf"
    txt_file = "Recommender Systems LLM.txt"
    pdf_to_txt(pdf_file, txt_file)

