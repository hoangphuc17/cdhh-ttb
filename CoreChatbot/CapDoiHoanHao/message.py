# -*- coding: utf-8 -*-
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page
from CoreChatbot.TheVoiceKid.database import *


from underthesea import word_sent

import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS
NOFAQ = db.NOFAQ


def answer(message, sender_id):
    if message is not None:

        # kiem tra user, neu chua co thi them vao database
        check_user = USER.find_one({'id_user': sender_id})
        if bool(check_user):
            # pass
            # page.send(sender_id, "user da co trong database")
            print('user da co trong database')
        else:
            user_profile = page.get_user_profile(sender_id)  # return dict
            first_name = user_profile["first_name"]
            last_name = user_profile["last_name"]
            id_user = user_profile["id"]
            insert_new_user(first_name, last_name, id_user)

        found_question = False

        for data in FAQ.find():
            final_data = {}
            count = 0
            metadata = data['metadata']
            for word in metadata:
                if word in message:
                    count = count + 1

            if count == len(data['metadata']):
                final_data = data
                found_question = True
                break

        if found_question:
            page.send(sender_id, final_data['answer'])
        else:
            new_nofaq = {'message': message}
            NOFAQ.insert_one(new_nofaq)
            print('khong tim thay cau hoi trong FAQ, vao nofaq de xem')
            text = "Oops..!Hiện tại mình chưa có dữ liệu câu hỏi của bạn, mình sẽ cập nhật và trả lời bạn sớm nhất. Hãy tiếp tục kết nối với chương trình qua các tính năng khác bạn nhé!"
            buttons = [
                Template.ButtonPostBack(
                    "Home", "home")
            ]
            page.send(sender_id, Template.Buttons(text, buttons))

    else:
        pass

    return


def find_cat(sender_id, word_dict, message):
    dict_cat = {}
    count_word_in_cat = 0
    chosen_cat = {}
    for cat_document in FAQ2.find({'level': '1'}):
        for word in word_dict:
            if word in cat_document['cat_keyword']:
                count_word_in_cat = count_word_in_cat + 1
        dict_cat.update({cat_document['cat_title']: count_word_in_cat})
        count_word_in_cat = 0
        # print (dict_cat)

    # gom cac cat_title co count_word_in_cat giong nhau lai
    flipped = {}
    for key, value in dict_cat.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    # print(flipped)

    # xep lai de thanh maximum
    maximum_key = max(flipped)
    maximum_value = flipped[maximum_key]
    # print('maximum value cua find_cat la ', maximum_value, maximum_key)

    if len(maximum_value) == 1 and maximum_key > 0:  # chi co 1 cat co so luong keyword la max
        # print(maximum_value[0])
        chosen_cat = FAQ2.find_one(
            {'level': '1', 'cat_title': maximum_value[0]})
        # text = 'da chon dc cat ' + chosen_cat['cat_title']
        # page.send(sender_id, text)
        # return chosen_cat

    # co nhieu cat co so luong keyword max bang nhau
    elif len(maximum_value) > 1 and maximum_key > 0:
        question = 'Giúp mình tìm câu trả lời nhé, bạn muốn tìm biết về mục nào của chương trình 😜'
        quick_replies = []
        for cat_title in maximum_value:
            payload = '>' + \
                FAQ2.find_one({'level': '1', 'cat_title': cat_title})['cat_id']
            quick_replies.append(QuickReply(
                title=cat_title, payload=payload))
        page.send(sender_id,
                  question,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")

    else:  # khong co cat nao, max = 0
        new_nofaq = {'message': message, 'id_user': sender_id}
        NOFAQ.insert_one(new_nofaq)
        print('khong tim thay cau hoi trong FAQ2, vao NOFAQ de xem')
        text = "Oops..!Hiện tại mình chưa có dữ liệu câu hỏi của bạn, mình sẽ cập nhật và trả lời bạn sớm nhất. Hãy tiếp tục kết nối với chương trình qua các tính năng khác bạn nhé!😬😬"
        buttons = [
            Template.ButtonPostBack(
                "Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))

    return chosen_cat


def find_subcat(sender_id, word_dict, chosen_cat):
    dict_subcat = {}
    count_word_in_subcat = 0
    chosen_subcat = {}
    # print('chosen_cat ', chosen_cat)
    for subcat_document in FAQ2.find({'level': '2', 'cat_id': chosen_cat['cat_id']}):
        for word in word_dict:
            if word in subcat_document['subcat_keyword']:
                count_word_in_subcat = count_word_in_subcat + 1
        dict_subcat.update(
            {subcat_document['subcat_title']: count_word_in_subcat})
        count_word_in_subcat = 0
        # print (dict_subcat)

    # gom cac cat_title co count_word_in_cat giong nhau lai
    flipped = {}
    for key, value in dict_subcat.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    # print(flipped)

    # xep lai de thanh maximum
    maximum_key = max(flipped)
    maximum_value = flipped[maximum_key]
    # print('maximum value la ', maximum_value)

    if len(maximum_value) == 1:  # chi co 1 cat co so luong keyword la max
        # print(maximum_value[0])
        chosen_subcat = FAQ2.find_one(
            {'level': '2', 'subcat_title': maximum_value[0], 'cat_id': chosen_cat['cat_id']})
        # text = 'da chon dc subcat ' + chosen_subcat['subcat_id']
        # page.send(sender_id, text)
        # return chosen_subcat

    else:  # len(maximum_value) > 1
        question = 'Hee, câu hỏi nào sẽ giúp mình giải đáp thắc mắc của bạn 😇'
        quick_replies = []
        for subcat_title in maximum_value:
            subcat = FAQ2.find_one(
                {'level': '2', 'cat_id': chosen_cat['cat_id'], 'subcat_title': subcat_title})
            payload = '>' + chosen_cat['cat_id'] + '>' + subcat['subcat_id']
            quick_replies.append(QuickReply(
                title=subcat_title, payload=payload))
        page.send(sender_id,
                  question,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")
    return chosen_subcat


def find_qa(sender_id, word_dict, chosen_subcat):
    dict_qa = {}
    count_word_in_qa = 0
    chosen_qa = {}
    # print('chosen_subcat trong find_qa', chosen_subcat)
    for qa_document in FAQ2.find({'level': '3', 'cat_id': chosen_subcat['cat_id'], 'subcat_id': chosen_subcat['subcat_id']}):
        for word in word_dict:
            if word in qa_document['qa_keyword']:
                count_word_in_qa = count_word_in_qa + 1
        dict_qa.update(
            {qa_document['question']: count_word_in_qa})
        count_word_in_qa = 0
    # print ('dict_qa ', dict_qa)

    # gom cac cat_title co count_word_in_cat giong nhau lai
    flipped = {}
    for key, value in dict_qa.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    # print('flipped trong find_qa ', flipped)

    # xep lai de thanh maximum
    maximum_key = max(flipped)
    maximum_value = flipped[maximum_key]
    # print('maximum value cua qa la ', maximum_value)

    if len(maximum_value) == 1:  # chi co 1 cat co so luong keyword la max
        # print(maximum_value[0])
        chosen_qa = FAQ2.find_one(
            {'level': '3', 'question': maximum_value[0]})
        text = chosen_qa['answer']
        page.send(sender_id, text)
        # return chosen_qa

    else:  # len(maximum_value) > 1
        text = 'Câu hỏi nào giống với ý của nhất? 😋'
        quick_replies = []
        for question in maximum_value:
            text = text + \
                ('\n' + str(maximum_value.index(question) + 1) + '. ' + question)
            qa = FAQ2.find_one(
                {'level': '3', 'cat_id': chosen_subcat['cat_id'], 'subcat_id': chosen_subcat['subcat_id']})
            payload = '>' + chosen_subcat['cat_id'] + '>' + \
                chosen_subcat['subcat_id'] + '>' + qa['qa_id']
            quick_replies.append(QuickReply(
                title=str(maximum_value.index(question) + 1), payload=payload))
        page.send(sender_id,
                  text,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")
    return chosen_qa


def handle_faq_quickreply(sender_id, quickreply_dict):
    length = len(quickreply_dict)
    print('length of quick_reply_dict ', length)
    print(quickreply_dict)

    if length > 3:
        # length = 4
        cat_id = quickreply_dict[1]
        subcat_id = quickreply_dict[2]
        qa_id = quickreply_dict[3]
        result = FAQ2.find_one(
            {'level': '3', 'cat_id': cat_id, 'subcat_id': subcat_id, 'qa_id': qa_id})
        # print(result)
        text = result['answer']
        buttons = [
            Template.ButtonPostBack(
                "Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))

    elif length > 2:
        # length = 3
        print('quick_reply: co cat_id, co subcat_id, khong co qa_id')
        cat_id = quickreply_dict[1]
        subcat_id = quickreply_dict[2]
        question = 'Hee, câu hỏi nào sẽ giúp mình giải đáp thắc mắc của bạn 😇'
        cursor_qa = FAQ2.find(
            {'level': '3', 'cat_id': cat_id, 'subcat_id': subcat_id})
        dict_qa = []
        for i in cursor_qa:
            dict_qa.append(i)
        # print('dict_qa la ', dict_qa)
        quick_replies = []
        for qa in dict_qa:
            question = question + \
                ('\n' + str(dict_qa.index(qa) + 1) + '. ' + qa['question'])
            payload = '>' + cat_id + '>' + subcat_id + '>' + qa['qa_id']
            quick_replies.append(QuickReply(
                title=str(dict_qa.index(qa) + 1), payload=payload))
        page.send(sender_id,
                  question,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")
    else:
        # length = 2
        print('quick_reply: co cat_id, khong co subcat_id')
        cat_id = quickreply_dict[1]
        dict_subcat = FAQ2.find({'level': '2', 'cat_id': cat_id})
        question = 'Giúp mình tìm câu trả lời nhé, bạn muốn tìm biết về mục nào của chương trình 😜'
        quick_replies = []
        for subcat in dict_subcat:
            payload = '>' + cat_id + '>' + subcat['subcat_id']
            quick_replies.append(QuickReply(
                title=subcat['subcat_title'], payload=payload))
        page.send(sender_id,
                  question,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")

    # cat_id = quickreply_dict[1]
    # if length == 3:
    #     subcat_id = quickreply_dict[2]
    #     if length == 4:
    #         qa_id = quickreply_dict[3]
    #         result = FAQ2.find(
    #             {'level': '3', 'cat_id': cat_id, 'subcat_id': subcat_id, 'qa_id': qa_id})
    #         text = result['answer']
    #         page.send(sender_id, text)
    #     else:
    #         print('quick_reply: co cat_id, co subcat_id, khong co qa_id')
    #         question = 'Hee, câu hỏi nào sẽ giúp mình giải đáp thắc mắc của bạn 😇'
    #         dict_qa = FAQ2.find(
    #             {'level': '3', 'cat_id': cat_id, 'subcat_id': subcat_id})
    #         quick_replies = []
    #         stt = 0
    #         for qa in dict_qa:
    #             question = question + \
    #                 ('\n' + str(stt + 1) + '. ' + qa['question'])
    #             payload = '>' + cat_id + '>' + subcat_id + '>' + qa['qa_id']
    #             quick_replies.append(QuickReply(
    #                 title=str(stt + 1), payload=payload))
    #         page.send(sender_id,
    #                   question,
    #                   quick_replies=quick_replies,
    #                   metadata="DEVELOPER_DEFINED_METADATA")

    # else:
    #     print('quick_reply: co cat_id, khong co subcat_id')
    #     dict_subcat = FAQ2.find({'level': '2', 'cat_id': cat_id})
    #     question = 'Giúp mình tìm câu trả lời nhé, bạn muốn tìm biết về mục nào của chương trình 😜'
    #     quick_replies = []
    #     for subcat in dict_subcat:
    #         payload = '>' + cat_id + '>' + subcat['subcat_id']
    #         quick_replies.append(QuickReply(
    #             title=subcat['subcat_title'], payload=payload))

    #     page.send(sender_id,
    #               question,
    #               quick_replies=quick_replies,
    #               metadata="DEVELOPER_DEFINED_METADATA")


def handle_faq_message(sender_id, message):
    if message is not None:
        print('message la: ', message)
        # kiem tra user, neu chua co thi them vao database
        check_user = USER.find_one({'id_user': sender_id})
        if bool(check_user):
            # pass
            # page.send(sender_id, "user da co trong database")
            print('user da co trong database')
        else:
            user_profile = page.get_user_profile(sender_id)  # return dict
            first_name = user_profile["first_name"]
            last_name = user_profile["last_name"]
            id_user = user_profile["id"]
            insert_new_user(first_name, last_name, id_user)

        # TACH TU (word_segmentation)
        word_dict = word_sent(message)
        print('Word Segmentation: ', word_dict)

        chosen_cat = find_cat(sender_id, word_dict, message)
        if chosen_cat != {}:
            print('da tim thay chosen_cat')
            chosen_subcat = find_subcat(sender_id, word_dict, chosen_cat)
            if chosen_subcat != {}:
                print('da tim thay chosen_subcat')
                chosen_qa = find_qa(sender_id, word_dict, chosen_subcat)

                if chosen_qa != {}:
                    print('da tim thay chosen_qa')
                else:
                    print(
                        'tim thay chosen_cat,tim thay chosen_subcat, khong tim thay chosen_qa')
            else:
                print('tim thay chosen_cat, khong tim thay chosen_subcat')
        else:
            print('khong tim thay chosen_cat')
    else:
        print('Message is None')
