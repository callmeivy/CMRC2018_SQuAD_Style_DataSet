# -*- coding: utf-8 -*-
import json
import re

# train file回答格式统一
f = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\cmrc2018_train.json", encoding='utf-8')
file_out = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\output.json", "w", encoding='utf-8')
# dev file回答格式统一
# f = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\cmrc2018_dev.json", encoding='utf-8')
# file_out = open("F:\PycharmProjects\CMRC2018_SQuAD_Style_DataSet-master\CMRC2018_SQuAD_Style_DataSet-master\dev_output.json", "w", encoding='utf-8')
family = json.load(f)
# print(family)
# print (type((family['data'])))
count = 0
ind = 0
for para in family['data']:
    # print (type((para['paragraphs'])))dev_
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
            # print(222, answer)
            if ("何时" in question) or ("什么时候" in question) or ("谁" in question) or ("多少" in question) or ("哪里" \
                in question):
                context_2sentence = re.findall(r"[\w']+", context)
                answer_list = re.findall(r"[\w']+", answer)
                # print (question, answer,"####",context_2sentence)
                # 如果原文档中的答案就是一个小分句以上，保持原状
                for ele_sen in context_2sentence:
                    if len(answer_list) == 1:
                        if answer in ele_sen:
                            answer_start_index = context.index(ele_sen)
                            # print(111, question, answer, ele_sen)
                            if answer != ele_sen:
                                count += 1
                                ans['answers'][0]['text'] = ele_sen
                                print(question, answer, ele_sen, answer_start_index)
                            if answer[0] != ele_sen[0]:
                                ans['answers'][0]['answer_start'] = answer_start_index
                                print ("start no same")

print (ind, count)
file_out.write(json.dumps(family, ensure_ascii=False))
f.close()
file_out.close()
