import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == '__main__':
    # 从文本文件中读取文章
    def read_text_from_file(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


    # 读取文章内容
    file_path = "学术期刊综合评价数据标准化方法研究.txt"
    text = read_text_from_file(file_path)


    # 分词
    def tokenize(text):
        words = jieba.cut(text)
        return " ".join(words)


    # 文本预处理
    preprocessed_text = tokenize(text)

    # 计算 TF-IDF 值
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([preprocessed_text])

    # 获取特征词汇
    feature_names = vectorizer.get_feature_names_out()

    # 选择主题词语（可以根据 TF-IDF 值高低选择）
    threshold = 0.1
    topics = []

    tfidf_scores = tfidf_matrix.toarray()[0]
    topic_words = [feature_names[j] for j, score in enumerate(tfidf_scores) if score > threshold]
    topics.append(topic_words)

    # 输出主题词
    print(f"文章的主题词：{', '.join(topics[0])}")
