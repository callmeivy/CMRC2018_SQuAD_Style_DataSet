# -*- coding: utf-8 -*-
'''
此版本是正确回答问题，如问时间，就仅回答时间，用ner
'''
import json
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'C:\Program Files\Python35\Lib\site-packages\stanfordcorenlp\stanford-corenlp-full-2018-10-05', lang='zh')
import nltk
f = open("F:\work\QA\CMRC2018 SQuAD Style DataSet\cmrc2018_train.json", encoding='utf-8')
file_out = open("F:\work\QA\CMRC2018 SQuAD Style DataSet\output.json", "w", encoding='utf-8')
family = json.load(f)
count = 0
ind = 0
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0


# 将答案末尾的标点删除
def punctuation_del(text):
    text = text[:len(text) - 1]
    return text


# 时间问题的答案结构清理
def data_cleaning_when(text):
    print("answer_ori", text)
    named_entities = nlp.ner(text)
    if (len(named_entities)) > 1 and ("（" not in text):
        text_produce = ""
        ind = 0
        for element in named_entities:
            if (element[1] == "DATE") or (element[0] in ["（", "）", "(", ")"]):
                text_produce += element[0]
                ind += 1
        # 两个及以上词为DATE
        # 1185到1216年 DATE之间的内容，；利用一前一后的index来切片
        if ind > 1:
            try:
                text = text[text.index(text_produce[:2]):text.index(text_produce[-2:]) + 2]
            except:
                print("error")
        # 1个词为DATE
        elif ind == 1:
            text = text_produce
        # 没有词为DATE
        # else:
        #     print("为0",text)
    print (text)
    return (text)
    

# 人问题的答案结构清理
def data_cleaning_who(text):
    named_entities = nlp.ner(text)
    print(named_entities)
    if (len(named_entities)) > 1:
        person = ''
        ind = 0
        for element in named_entities:
            if element[1] == "PERSON":
                ind += 1
                person += element[0]
        if ind > 1:
            try:
                text_produce = text[text.index(person[:2]):text.index(person[-2:]) + 2]
            except:
                text_produce = text
    print(person, text_produce)
    return (person, text_produce)


for para in family['data']:
    # print (type((para['paragraphs'])))
    for que in para['paragraphs']:
        context = que['context']
        for ans in que['qas']:
            # 问题
            question = ans['question']
            # print(111, context)
            # print(333, question)
            # 答案
            answer = ans['answers'][0]['text']
            ind += 1
            ans_start = ans['answers'][0]['answer_start']
            # if ("何时" in question) or ("什么时候" in question) or ("谁" in question) or ("多少" in question):
            # 将答案末尾的标点删除
            if answer[len(answer)-1] in ['，', '。']:
                answer = punctuation_del(answer)
                # print(answer)

            # 时间问题
            if (("何时" in question) or ("什么时候" in question) or ("哪一年" in question)) and ("何地" not in question) \
                    and ("哪个" not in question) and ("什么" not in question) and ("起讫" not in question) and ("分别" \
                  not in question):
                answer_cleaning = data_cleaning_when(answer)

            # # 人物问题
            # if "谁" in question:
            #     data_cleaning_who(answer)





nlp.close()
print ("总问题:", ind, "单纯时间问句数量：", count, "符合时间+动词的句式数量：",count_0, count_1, count_2,  count_3)
# file_out.write(json.dumps(family, ensure_ascii=False))
f.close()
# file_out.close()
