# -*- coding: utf-8 -*-
import json
import re

# f_dev = open("F:\work\QA\CMRC2018 SQuAD Style DataSet\cmrc2018_dev.json", encoding='utf-8')
# f_dev = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\sentence_answer_trial.json", encoding='utf-8')
f_dev = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\\test_xiqu.json", encoding='utf-8')
# f_predict = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\predictions_trial.json", encoding='utf-8')
# f_predict = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\predictions_xiqu.json", encoding='utf-8')
# f_predict = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\predictions06121032.json", encoding='utf-8')
f_predict = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\predictions_xiqu_20190612.json", encoding='utf-8')
# file_out = open("F:\work\QA\CMRC2018 SQuAD Style DataSet\compare.json", "w", encoding='utf-8')
family = json.load(f_dev)
predict_fam = json.load(f_predict)
# print(family)
# print (type((family['data'])))
count = 0
ind = 0
count = 0
count_w = 0
count_r = 0
for para in family['data']:
    # print (type((para['paragraphs'])))
    for que in para['paragraphs']:
        context = que['context']
        for ans in que['qas']:
            # 问题
            question = ans['question']
            # 答案,注意有多个备选答案，这里先安答案都一致处理
            answer_dev = ans['answers'][0]['text']
            # for answer in ans['answers']:
            #     print (type(answer), answer)
            id_dev = ans['id']
            for k in predict_fam.items():
                # k is tuple
                if k[0] == id_dev:
                    count +=1
                    if k[1] != answer_dev:
                        # 问题 预测的答案 测试集答案
                        count_w+=1
                        print (id_dev,"#",question, "#",k[1],"#", answer_dev,"#","异")
                        # print (question, "#",k[1],"#", answer_dev)
                    else:
                        count_r+=1
                        print(id_dev, "#", question, "#", k[1], "#", answer_dev, "#", "同")
            # print(id_dev, answer_dev)
# print(type(predict_fam))
# print((predict_fam))
# for k in predict_fam.items():
#     print(k)
# 准确率大概是82.5
print(count, count_w, count_r)
f_dev.close()
f_predict.close()