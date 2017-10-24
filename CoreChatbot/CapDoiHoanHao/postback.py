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

import PIL

from PIL import Image, ImageDraw, ImageFont


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS

danh_sach_hinh_anh_HLV = {
    "Vũ Cát Tường": "hinh5_minigame.jpg",
    "Tiên Cookie và Hương Tràm": "hinh6_minigame.jpg",
    "Soobin": "hinh7_minigame.jpg"
}


def greeting(sender_id):
    # get user info
    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]
    print (user_profile)

    # kiem tra user, neu chua co thi them vao database
    check_user = USER.find_one({'id_user': sender_id})
    if bool(check_user):
        # pass
        # page.send(sender_id, "user da co trong database")
        print('day la ham greeting, user da co trong database')
    else:
        insert_new_user(first_name, last_name, id_user)

    space = " "
    a = "Chào"
    b = "đến với Giọng Hát Việt Nhí. Tại đây, bạn có thể đặt câu hỏi, chơi Mini game và theo dõi những tin tức “nóng hổi” nhất từ chương trình. Còn chần chừ gì mà không bắt đầu cuộc “trò chuyện thân mật” ngay nào !!! ;) ;)\n⏩⏩⏩ Quay về tính năng chính bằng cách ấn phím “Home” hoặc gõ vào chữ “Home” hoặc “Menu” 👇\n⏩⏩⏩ Chương trình “Giọng Hát Việt Nhí” 2017 sẽ được phát sóng vào lúc 21h10 thứ 7 hằng tuần trên kênh VTV3📺 "
    seq = (a, first_name, b)
    text = space.join(seq)
    buttons = [
        Template.ButtonPostBack(
            "Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    return


def home(sender_id):

    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    # kiem tra user, neu chua co thi them vao database
    check_user = USER.find_one({'id_user': sender_id})
    if bool(check_user):
        print('user da co trong database')
    else:
        insert_new_user(first_name, last_name, id_user)

    elements = [
        Template.GenericElement("Fansign",
                                subtitle="Cùng đón nhận những lời chúc từ các huấn luyện viên Giọng Hát Việt Nhí 2017!!!",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh1_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Lấy Fansign", "fansign")
                                ]),
        Template.GenericElement("Tin tức mới nhất từ chương trình “Giọng Hát Việt Nhí” 2017",
                                subtitle="Nơi cập nhật những tin tức mới nhất từ chương trình “Giọng Hát Việt Nhí” 2017",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh1_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "read_news"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "subscribe_news")
                                ]),
        Template.GenericElement("Video Full - The Voice Kids 2017 | Giọng Hát Việt Nhí mùa 5",
                                subtitle="Xem lại bản đầy dủ các tập đã được phát sóng trên Youtube, Live Streaming",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh2_xem_video.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Xem lại tập đã phát", "https://www.youtube.com/user/btcgionghatvietnhi"),
                                    Template.ButtonWeb(
                                        "Oh my kids", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBml5RPOlILDvj5DqNwmG9AI"),
                                    Template.ButtonWeb(
                                        "Off the air", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBk1BX8Jks9152rkNTIZQWuK")
                                ]),

        Template.GenericElement("Dự đoán kết quả và giành lấy cơ hội nhận quà",
                                subtitle="Tham gia dự đoán kết quả của cuộc thi để nhận được những phần quà hấp dẫn nhất từ ban tổ chức",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh3_du_doan.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Minigame 1", "minigame1"),
                                    Template.ButtonPostBack(
                                        "Minigame 2", "minigame2")
                                ]),
        Template.GenericElement("About us",
                                subtitle="Theo dõi chương trình Giọng Hát Việt Nhí 2017 tại các kênh truyền thông",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh4_about_us.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Facebook", "https://www.facebook.com/gionghatvietnhi/"),
                                    Template.ButtonPostBack(
                                        "Giờ phát sóng", "time line"),
                                    Template.ButtonPostBack(
                                        "Giới thiệu", "introduce")
                                ])
    ]
    page.send(sender_id, Template.Generic(elements))
    return


def minigame1(sender_id):
    text = "Minigame 1:\n   Dự đoán đội quán quân"
    buttons = [
        Template.ButtonPostBack(
            "Tham gia dự đoán 👍", "minigame1_menu"),
        Template.ButtonPostBack(
            "Thể lệ dự đoán 📜", "minigame1_rule")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))
    return


def minigame2(sender_id):
    text = "Minigame 2:\n   Đoán từ khóa nhận Sticker"
    buttons = [
        Template.ButtonPostBack(
            "Tham gia dự đoán 👍", "minigame2_menu"),
        Template.ButtonPostBack(
            "Thể lệ dự đoán 📜", "minigame2_rule")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))
    return


def subscribe_news(sender_id):

    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    # kiem tra user, neu chua co thi them vao database
    check_user = USER.find_one({'id_user': sender_id})
    if bool(check_user):
        # pass
        # page.send(sender_id, "user da co trong database")
        print('user da co trong database')
    else:
        insert_new_user(first_name, last_name, id_user)

    question = "Bằng cách đồng ý theo dõi tin tức dưới đây, bạn sẽ nhận được thông báo mỗi khi tin tức mới của chương trình “Giọng Hát Việt Nhí” 2017 được cập nhật.\nBạn muốn nhận thông báo chứ?"
    quick_replies = [
        QuickReply(title="1 tuần 1 lần 😋", payload="yes1"),
        QuickReply(title="1 tuần 2 lần 😈", payload="yes2"),
        QuickReply(title="Nhắc lại sau 😜", payload="no")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return


def handle_subscribe_news(sender_id, quick_reply_payload):
    if quick_reply_payload == 'no':
        text = "Okey. Bất cứ khi nào bạn cần đăng ký nhận tin tức thì quay lại đây nhé!"
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
        USER.update_one(
            {'id_user': sender_id},
            {'$set': {'subscribe_news': quick_reply_payload}}
        )
    else:
        text = "Bạn đã đăng ký nhận thông báo thành công. \nMỗi khi có thông báo mới về chương trình The Voice Kid 2017, mình sẽ gửi tới bạn."
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
        USER.update_one(
            {'id_user': sender_id},
            {'$set': {'subscribe_news': quick_reply_payload}}
        )
    return


def read_news(sender_id):
    elements = []
    for news in NEWS.find():
        element = Template.GenericElement(
            title=news['title'],
            subtitle=news['subtitle'],
            image_url=news['image_url'],
            buttons=[
                Template.ButtonWeb('Đọc tin', news['item_url']),
                Template.ButtonPostBack('Về Home', 'home')
            ])
        elements.append(element)

    page.send(sender_id, Template.Generic(elements))

    return


def minigame1_vote(sender_id):
    question = "Bạn dự đoán thí sinh thuộc đội của huấn luyện viên nào sẽ xuất sắc giành lấy ngôi vị quán quân của chương trình?"
    quick_replies = [
        QuickReply(title="#teamcôTường", payload="Vũ Cát Tường"),
        QuickReply(title="#teamcôTiênvàcôTràm",
                   payload="Tiên Cookie và Hương Tràm"),
        QuickReply(title="#teamchúSoobin", payload="Soobin")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return


def minigame1_menu(sender_id):
    check_vote = USER.find_one({'id_user': sender_id})

    if check_vote["HLV_da_binh_chon"] == "":
        # user chua binh chon
        minigame1_vote(sender_id)
    else:
        # user da binh chon
        space = " "
        a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
        # a = a.decode('utf-8')
        b = check_vote["HLV_da_binh_chon"]
        seq = (a, b)
        text = space.join(seq)

        buttons = [
            Template.ButtonPostBack("Bình chọn lại", "minigame1_vote"),
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
    return


def minigame1_handle_quick_reply(sender_id, quick_reply_payload):
    hinh_hlv = "http://210.211.109.211/weqbfyretnccbsaf/" + \
        danh_sach_hinh_anh_HLV[quick_reply_payload]
    page.send(sender_id, Attachment.Image(hinh_hlv))

    space = " "
    a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
    seq = (a, quick_reply_payload)
    text = space.join(seq)
    buttons = [
        Template.ButtonPostBack("Bình chọn lại", "minigame1_vote"),
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    USER.update_one(
        {'id_user': sender_id},
        {'$set': {'HLV_da_binh_chon': quick_reply_payload}}
    )

    return


def minigame1_rule(sender_id):
    text = "- Mỗi bạn tham gia sẽ có 01 lựa chọn cho việc dự đoán đội huấn luyện viên có thí sinh đạt được giải quán quân 🎊 của chương trình.\n- Nếu bạn thay đổi ý kiến, dự đoán được BTC ghi nhận là dự đoán cuối cùng mà bạn chọn.\n- Nếu dự đoán đúng và may mắn, bạn sẽ nhận được 01 phần quà 🎁 hấp dẫn từ ban tổ chức.\n Hãy tận dụng “giác quan thứ 6” của mình để 'rinh' quà về nhà nào!\n👉👉👉 “Giọng Hát Việt Nhí” 2017 sẽ chính thức được phát sóng vào lúc 21h10 thứ 7 hằng tuần trên kênh VTV3"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))
    return


def minigame2_rule(sender_id):
    text = "- Mỗi bạn tham gia được dự đoán không giới hạn ‘Từ khóa’ may mắn để nhận được trọn bộ Sticker hình vẽ HLV Giọng Hát Việt Nhí 2017.\n- ‘Từ khóa’ có thể gồm 1 từ hoặc 1 cụm từ miêu tả gần giống với các HLV nhất.\n- Nếu dự đoán đúng từ khóa. Bạn sẽ nhận được những Sticker ‘Siêu Đáng Yêu’.\nNgại gì không thử??\n\n👉👉👉 “Giọng Hát Việt Nhí” 2017 sẽ chính thức được phát sóng vào lúc 21h10 thứ 7 hằng tuần (từ ngày 12/8/2017) trên kênh VTV3"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))
    return


def timeline(sender_id):
    text = "📣📣📣 Chương trình “Giọng Hát Việt Nhí” 2017 sẽ được phát sóng vào lúc 9h10 tối thứ 7 hằng tuần từ (ngày 12/08/2017) trên kênh VTV3"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))
    return


def introduce(sender_id):
    text = "Đến hẹn lại lên, 'Giọng Hát Việt Nhí' đã trở lại và lợi hại hơn bao giờ hết. Với dàn huấn luyện viên là những nghệ sỹ trẻ nổi tiếng tài năng và sở hữu lượng fan hùng hậu nhất nhì làng giải trí Việt. Đó là cặp đôi Hương Tràm –Tiên Cookie, ca sĩ – nhạc sĩ Vũ Cát Tường, ca sĩ Soobin Hoàng Sơn. Họ hứa hẹn sẽ mang đến cho Giọng Hát Việt Nhí mùa 5 nhiều điều thú vị với độ cạnh tranh, “chặt chém” quyết liệt trên ghế nóng.\n📣📣📣 21h10 thứ 7 hằng tuần trên kênh VTV3 - Giọng Hát Việt Nhí 2017 với những bất ngờ đang chờ bạn khám phá!"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))
    return


def handle_subscribe_1(sender_id):
    question = "Bằng cách đồng ý theo dõi, để nhận các tin tức mới nhất của Giọng Hát Việt Nhí 2017, các nhắc nhở giờ phát sóng của tập mới, bạn muốn nhận thông báo chứ?"
    quick_replies = [
        QuickReply(title="1 tuần 1 lần 😋", payload="yes1"),
        QuickReply(title="1 tuần 2 lần 😈", payload="yes2"),
        QuickReply(title="Nhắc lại sau 😜", payload="no")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return


# def handle_subscribe_2():


# def handle_subscribe_3():
def minigame2_menu(sender_id):
    text = "Nhập một từ khóa bất kỳ để có cơ hội nhận Sticker 'Siêu Đáng Yêu' hình vẽ các HLV mà bạn yêu thích !! Ngại gì không thử ?? 👇👇.\n=> Gợi ý: Những từ/cụm từ được các HLV sử dụng nhiều nhất trong chương trình Giọng Hát Việt Nhí 2017."
    page.send(sender_id, text)
    return


def minigame2_handle_result(message, sender_id):
    message = message.lower()
    huong_tram = ["đỉnh", "xinh", "bánh bèo"]
    vu_cat_tuong = ["chất", "cá tính", "phũ"]
    soobin = ["đẹp trai", "ế", "cao"]
    tien_cookie = ["hit", "cute", "nhọ"]
    if message in huong_tram:
        game2_hlv_url = "http://210.211.109.211/weqbfyretnccbsaf/game2_huongtram.jpg"
        page.send(sender_id, Attachment.Image(game2_hlv_url))
        text = "Chính xác!!!!!!!!"
        buttons = [
            Template.ButtonPostBack("Đoán thêm lần nữa 😻", "minigame2_menu"),
            Template.ButtonPostBack("Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))
    elif message in vu_cat_tuong:
        game2_hlv_url = "http://210.211.109.211/weqbfyretnccbsaf/game2_vucattuong.jpg"
        page.send(sender_id, Attachment.Image(game2_hlv_url))
        text = "Chính xác!!!!!!!!"
        buttons = [
            Template.ButtonPostBack("Đoán thêm lần nữa 😻", "minigame2_menu"),
            Template.ButtonPostBack("Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))
    elif message in soobin:
        game2_hlv_url = "http://210.211.109.211/weqbfyretnccbsaf/game2_soobin.jpg"
        page.send(sender_id, Attachment.Image(game2_hlv_url))
        text = "Chính xác!!!!!!!!"
        buttons = [
            Template.ButtonPostBack("Đoán thêm lần nữa 😻", "minigame2_menu"),
            Template.ButtonPostBack("Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))
    elif message in tien_cookie:
        game2_hlv_url = "http://210.211.109.211/weqbfyretnccbsaf/game2_tiencookie.jpg"
        page.send(sender_id, Attachment.Image(game2_hlv_url))
        text = "Chính xác!!!!!!!!"
        buttons = [
            Template.ButtonPostBack("Đoán thêm lần nữa 😻", "minigame2_menu"),
            Template.ButtonPostBack("Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))


# def receive_feedback:
    # template để hiện nút và hình cho user gửi feedback
def fansign_menu(sender_id):
    user_profile = page.get_user_profile(sender_id)
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]
    print(last_name + ' ' + first_name)

    check_user = USER.find_one({'id_user': sender_id})
    if bool(check_user):
        print('user da co trong database')
    else:
        insert_new_user(first_name, last_name, id_user)

    space = " "
    a = "ơi, bạn muốn nhận fansign từ HLV nào?"
    seq = (last_name, first_name, a)
    question = space.join(seq)

    quick_replies = [
        QuickReply(title="Soobin", payload="sb"),
        QuickReply(title="Vũ Cát Tường", payload="vct"),
        QuickReply(title="Hương Tràm", payload="ht"),
        QuickReply(title="Tiên Cookie", payload="tc")
    ]
    page.send(sender_id, question, quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")
    return


def image_fs(sender_id, sizeFont, hlv, first_name, last_name, x_Text, y_Text):
    userName = last_name + ' ' + first_name
    font = ImageFont.truetype("./font.ttf", sizeFont)
    imageFile = "image/" + hlv + ".jpg"
    im = Image.open(imageFile)
    draw = ImageDraw.Draw(im)
    draw.text((x_Text, y_Text), userName, (0, 0, 0), font=font)
    draw = ImageDraw.Draw(im)
    name_fansigned = "/home/hoangphuc/Bot_Pictures/fs_" + hlv + \
        sender_id + ".jpg"
    im.save(name_fansigned)

    hlv_dict = {
        'sb': 'Soobin',
        'vct': 'Vũ Cát Tường',
        'ht': 'Hương Tràm',
        'tc': 'Tiên Cookie'
    }

    text1 = hlv_dict.get(
        hlv) + " đang viết lời chúc dành cho bạn. " + userName + " chờ xíu nhé 😉"
    page.send(sender_id, text1)

    page.send(sender_id, Attachment.Image(
        "http://210.211.109.211/weqbfyretnccbsaf/fs_" + hlv + sender_id + ".jpg"))
    text2 = 'Phía trên là hình fansign của ' + \
        hlv_dict.get(
            hlv) + ' dành riêng cho bạn. Hãy chia sẻ món quà này ngay kèm hashtag #gionghatvietnhifansign nha bạn ơi'
    buttons = [
        Template.ButtonPostBack("Fansign khác", "fansign"),
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text2, buttons))
    print('da gui hinh fansign')


def fansign_handle_quick_reply(sender_id, quickreply):
    user_profile = page.get_user_profile(sender_id)
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    userName = last_name + ' ' + first_name

    def fs_vct():
        if len(userName) < 11:
            image_fs(sender_id, 90, "vct", first_name, last_name, 180, 370)
        else:
            image_fs(sender_id, 80, "vct", first_name, last_name, 90, 370)

    def fs_ht():
        if len(userName) < 11:
            image_fs(sender_id, 80, "ht", first_name, last_name, 180, 330)
        else:
            image_fs(sender_id, 65, "ht", first_name, last_name, 180, 330)

    def fs_tc():
        if len(userName) < 11:
            image_fs(sender_id, 90, "tc", first_name, last_name, 180, 390)
        else:
            image_fs(sender_id, 80, "tc", first_name, last_name, 90, 380)

    def fs_sb():
        if len(userName) < 11:
            image_fs(sender_id, 85, "sb", first_name, last_name, 30, 450)
        else:
            image_fs(sender_id, 70, "sb", first_name, last_name, 30, 455)

    fs_hlv_list = {
        'sb': fs_sb,
        'vct': fs_vct,
        'ht': fs_ht,
        'tc': fs_tc
    }

    if quickreply in fs_hlv_list:
        fs_hlv_list[quickreply]()
