import os
import jieba


def cut_words(raw_dataset: list) -> list:

    stopwords_dict = os.listdir("stopwords/")
    stop_list = []
    for dic in stopwords_dict:
        stop_list.append([line.strip() for line in open('stopwords/' + dic, 'r', encoding='utf-8').readlines()])
    cut_dataset = []
    for data in raw_dataset:
        cut_dataset.append(jieba.lcut(data))
    clean_dataset = []
    for data in cut_dataset:
        clean_data = []
        for word in data:
            if word not in stop_list:
                clean_data.append(word)
        clean_dataset.append(clean_data)
    dataset = []
    for data in clean_dataset:
        str_data = ' '.join(data)
        dataset.append(str_data)
    return dataset

