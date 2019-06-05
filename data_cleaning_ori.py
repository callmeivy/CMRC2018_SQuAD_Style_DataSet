# -*- coding: utf-8 -*-
import json
import re

f = open("F:\work\QA\CMRC2018 SQuAD Style DataSet\cmrc2018_train.json", encoding='utf-8')
file_out = open("F:\work\QA\CMRC2018 SQuAD Style DataSet\output.json", "w", encoding='utf-8')
family = json.load(f)
# print(family)
# print (type((family['data'])))
count = 0
ind = 0
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
            # print(222, answer)
            if ("何时" in question) or ("什么时候" in question) or ("谁" in question) or ("多少" in question):
            # if ("何时" in question):
                context_2sentence = re.findall(r"[\w']+", context)
                answer_list = re.findall(r"[\w']+", answer)
                # 如果原文档中的答案就是一个小分句以上，保持原状
                for ele_sen in context_2sentence:
                    if len(answer_list) == 1:
                        if answer in ele_sen:
                            answer_start_index = context.index(ele_sen)
                            # print(111, question, answer, ele_sen)
                            if answer != ele_sen:
                                count += 1
                                # answer是"1996年",全部改为将整句取出；但同样的"1996年“可能全文多处出现，根据answer_start定位
                                if abs(ans['answers'][0]['answer_start']-answer_start_index) <=20:
                                # print (abs(ans['answers'][0]['answer_start']-answer_start_index))
                                    ans['answers'][0]['text'] = ele_sen
                                    # print(question, answer, ele_sen, answer_start_index)
                                    if answer[0] != ele_sen[0]:
                                        ans['answers'][0]['answer_start'] = answer_start_index
                                        # print ("start no same")

print (ind, count)
file_out.write(json.dumps(family, ensure_ascii=False))
f.close()
file_out.close()
