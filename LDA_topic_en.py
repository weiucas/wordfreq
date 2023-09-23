if __name__ == '__main__':
    import gensim
    from gensim import corpora
    from gensim.models import LdaModel
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    import os

    # 示例文本数据存储在一个文件夹中，每个文件包含一篇文档
    document_directory = "/Users/wei/PycharmProjects/wordfreq/documents"
    documents = []

    # 分词和预处理文本
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    # 遍历文件夹中的文本文件并读取内容
    for filename in os.listdir(document_directory):
        if filename.endswith(".txt"):
            with open(os.path.join(document_directory, filename), "r", encoding="utf-8") as file:
                document = file.read()
                words = word_tokenize(document.lower())  # 分词并转为小写
                filtered_words = [word for word in words if word.isalpha() and word not in stop_words]  # 过滤停用词和非字母字符
                lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]  # 词形还原
                documents.append(lemmatized_words)

    # 创建字典和词袋模型
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]

    # 使用LDA模型提取主题
    num_topics = 5  # 指定主题数量
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

    # 打印每个主题的关键词
    topics = lda_model.print_topics(num_topics=num_topics, num_words=5)
    for topic in topics:
        print(topic)
