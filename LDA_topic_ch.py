if __name__ == '__main__':
    import gensim
    from gensim import corpora
    from gensim.models import LdaModel
    import jieba
    import os

    # 加载停用词
    stop_words = set()
    with open("stopwordlist.txt", "r", encoding="utf-8") as file:
        for line in file:
            stop_words.add(line.strip())


    # 分词函数
    def tokenize(text):
        words = jieba.cut(text)
        return [word for word in words if word not in stop_words]


    # 读取文本文件
    def read_documents(directory):
        documents = []
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                text = file.read()
                documents.append(tokenize(text))
        return documents


    # 从文件夹中读取文档
    document_directory = "/Users/wei/PycharmProjects/wordfreq/documents"
    documents = read_documents(document_directory)

    # 创建词典和文档-词频矩阵
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]

    # 训练LDA模型
    num_topics = 5  # 指定主题数量
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

    # 打印每个主题的词语分布
    topics = lda_model.print_topics(num_topics=num_topics, num_words=10)
    for topic in topics:
        print(topic)
