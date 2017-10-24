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


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS


# def insert_question(metadata, question, answer, rank):
#     check_question = FAQ.find_one({'question': question})
#     if bool(check_question):
#         pass
#     else:
#         new_question = {
#             "metadata": metadata,
#             "question": question,
#             "answer": answer,
#             "rank": rank
#         }
#         FAQ.insert_one(new_question)


def insert_new_questions():
    # insert_question(["ai", "vũ cát tường"],
    #                 "ai là Vũ Cát Tường?", "VCT là ...", "")
    # insert_question(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
    # insert_question(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")
    # insert_question(["đăng ký", "tham dự"], "để đăng ký tham gia Giọng Hát Việt Nhí ?",
    #                 "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    # insert_question(["vòng giấu mặt", "tập"], "Vòng giấu mặt có bao nhiêu tập?",
    #                 "Bạn thân mến! Vòng giấu mặt Giọng Hát Việt Nhí có tất cả 5 tập. Xem lại chương trình đã phát sóng trên Youtube: http://youtube.com/btcgionghatvietnhi/", "")
    # insert_question(["hlv"], "HLV Giọng Hát Việt Nhí 2017 là ai?",
    #                 "HLV Giọng Hát Việt Nhí 2017 bao gồm ghế đôi ca sĩ Hương Tràm & nhạc sĩ Tiên Cookie, ghế đơn ca sĩ Soobin Hoàng Sơn và sự trở lại của HLV Giọng Hát Việt Nhí 2016 Vũ Cát Tường. Theo dõi chương trình và ủng hộ các đội mà bạn yêu thích nhé! ❤", "")
    # insert_question(["tuyển"], "đăng ký tham gia Giọng Hát Việt Nhí ?",
    #                 "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")

    insert_question(["đăng ký", "tuyển sinh"], "Mình muốn tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    insert_question(["đăng ký", "tham gia"], "muốn tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    insert_question(["đăng ký", "thi"], "Mình tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")

    insert_question(["phát sóng", "tuần này"], "Tuần này có phát sóng Giọng Hát Việt Nhí 2017 không Ad?",
                    "Bạn thân yêu ơi Giọng Hát Việt Nhí 2017 sẽ được phát sóng vào 21h thứ bảy trên kênh VTV3. Bạn nhớ đón xem nha!", "")
    insert_question(["quán quân"], "Quán quân năm nay là ai vậy ạ?",
                    "Tham gia dự đoán quán quân Giọng Hát Việt Nhí tại Chatbot bạn nhé!", "")
    insert_question(["hlv", "giọng hát việt nhí"], "HLV Giọng Hát Việt Nhí 2017 là ai?",
                    "HLV Giọng Hát Việt Nhí 2017 bao gồm ghế đôi ca sĩ Hương Tràm & nhạc sĩ Tiên Cookie, ghế đơn ca sĩ Soobin Hoàng Sơn và sự trở lại của HLV Giọng Hát Việt Nhí 2016 Vũ Cát Tường. Theo dõi chương trình và ủng hộ các đội mà bạn yêu thích nhé! ❤", "")
    insert_question(["lịch phát sóng"], "Em muốn hỏi lịch phát sóng Giọng Hát Việt nhí",
                    "Giọng Hát Việt Nhí 2017 được phát sóng vào lúc 21 giờ thứ Bảy hàng tuần trên kênh VTV3 bạn nhé! ❤", "")
    insert_question(["bình chọn"], "Làm sao để bình chọn cho thí sinh",
                    "Hệ thống bình chọn chỉ hoạt động để bình chọn chiếc vé may mắn cho thí sinh quay trở lại đêm chung kết và bình chọn cho quán quân chương trình Giọng Hát Việt Nhí 2017 trong đêm chung kết được mở từ ngày 19/11 - 25/11/2017", "")
    insert_question(["hậu trường"], "Admin có quay cảnh hậu trường không? ",
                    "Để xem lại những khoảnh khắc hậu trường vui nhộn bạn nhớ subcribe kênh VIVA Shows: http://bit.ly/vivashows nhé!", "")
    insert_question(["full"], "Tại sao the voice kids không có bản full trên youtube",
                    "Vì lý do bản quyền The Voice Kids không cho phép công bố bản Full trên Youtube nên chúng tôi rất tiếc vì sự bất tiện này. Tuy nhiên, khán giả có thể dễ dàng theo dõi từ thí sính mà mình yêu thích một cách dễ dàng mà không tốn quá nhiều thời gian.", "")
    insert_question(["tuyển"], "Bây giờ còn đăng ký được nữa không?",
                    "Tuyển sinh Giọng Hát Việt Nhí 2018 sẽ được mở ngay sau khi Chung Kết Giọng Hát Việt Nhí 2017 kết thúc. Các bạn theo dõi Fanpage để cập nhật thông tin sớm nhất nhé!", "")
    insert_question(["trực tiếp"], "Năm nay các vòng Liveshow có phát trực tiếp không?",
                    "Liveshow chung kết Giọng Hát Việt Nhí sẽ được phát sóng trực tiếp trên kênh VTV3 vào ngày 25/11/2017 các bạn nhé!", "")
    insert_question(["bao nhiêu", "tập", "thí sinh"], "Một tập gồm mấy thí sinh vậy Ad?",
                    "Bạn ơi bạn à! Bạn muốn hỏi tập mấy nà? Ahihi Mình đùa đấy!! Tùy theo mỗi tập sẽ có số lượng thí sinh khác nhau. Bạn nhớ xem chương trình vào 21h tối Thứ Bảy Hàng tuần trên VTV3 để nắm thông tin nhé!", "")
    insert_question(["phát lại"], "GHVN có phát sóng lại không Ad?",
                    "Giọng Hát Việt Nhí 2017 sẽ được phát sóng vào lúc 21h thứ bảy hàng tuần trên VTV3 và được phát lại vào lúc 14h30 thứ hai tuần tiếp theo cũng trên kênh VTV3 nhé bạn dấu yêu.", "")
    insert_question(["web"], "Website Giọng Hát Việt Nhí là gì vậy?",
                    "Webssite chính thức của chương trình Giọng Hát Việt Nhí/The Voice Kids Việt Nam truy cập vào link: http://gionghatvietnhi.com.vn", "")
    insert_question(["hlv", "năm sau"], "Vũ Cát Tường/Soobin Hoàng Sơn/Hương Tràm/Tiên Cookie có làm HLV năm sau nữa không?",
                    "Cám ơn @user đã quan tâm và theo dõi chương trình. Thông tin về 'ghế nóng' năm sau vẫn là một 'ẩn số'. Theo dõi Fanpage để cập nhật tin tức mới nhất 'nóng hổi nhất' bạn nhé! ;)", "")
    insert_question(["tập mới"], "Cho mình xin link tập @mới nha",
                    "Bạn thân mến! Để xem lại tập vừa phát sóng hãy trở lại phím 'Home' và nhấp vào 'Xem lại tập phát sóng' trên kênh Youtube chính thức của chương trình bạn nhé!", "")
    insert_question(["tuổi", "đăng ký"], "Bao nhiêu tuổi thì được tham gia chương trình vậy ạ?",
                    "Độ tuổi đăng ký tham gia chương trình Giọng Hát Việt Nhí là từ 5 tuổi - 15 tuổi bạn nhé!", "")
    insert_question(["tuổi", "tham gia"], "Bao nhiêu tuổi thì được tham gia chương trình vậy ạ?",
                    "Độ tuổi đăng ký tham gia chương trình Giọng Hát Việt Nhí là từ 5 tuổi - 15 tuổi bạn nhé!", "")
    insert_question(["đăng ký", "thử giọng"], "Tham gia thử giọng ở đâu vậy ad?",
                    "Theo dõi Fanpage để cập nhật thông tin đăng  ký và địa điểm ghi hình sớm nhất bạn nhé!", "")
    insert_question(["năm sau", "tổ chức"], "Năm sau còn tổ chức nữa không ạ?",
                    "Bạn 'đáng yêu' ơi! Giọng Hát Việt Nhí đã trải qua 5 mùa và sẽ tiếp tục đồng hành cùng khán giả yêu mến chương trình vào những năm tiếp theo bạn nhé!", "")
    insert_question(["tsổ chức", "ở đâu"], "Giọng Hát Việt Nhí tổ chức ở đâu vậy ạ?",
                    "Giọng Hát Việt Nhí được tổ chức ghi hình tại TP. HCM bạn nhé! Để biết thêm thông tin địa điểm ghi hình chương trình bạn vui lòng theo dõi Fanpage thường xuyên nhé!", "")
    insert_question(["giấu mặt"], "Vòng giấu mặt có bao nhiêu tập?",
                    "Vòng giấu mặt thường có 4-5 tập bạn nhé!", "")
    insert_question(["xem lại"], "Làm sao xem lại GHVN được ạ?",
                    "Bạn có thể xem phát sóng lại Giọng Hát Việt Nhí vào lúc 14h30 thứ 2 tuần tiếp theo trên VTV3 hoặc vào Youtube chính thức của chương trình để xem lại những tiết mục yêu thích bạn nhé!", "")

    print('da them new question')


def insert_new_news():
    # insert_news("Sau Thụy Bình, Vũ Cát Tường lại chiêu mộ thành công ‘hoàng tử dân ca’ Tâm Hào", "Dự thi với ca khúc mang âm hưởng dân ca vô cùng mộc mạc nhưng cậu bé Nguyễn Tâm Hào vẫn khiến cả trường quay dậy sóng bởi tiếng hò reo, cổ vũ.",
    #             "https://img.saostar.vn/265x149/2017/08/19/1500005/8.jpg", "https://saostar.vn/tv-show/sau-thuy-binh-vu-cat-tuong-lai-chieu-mo-thanh-cong-hoang-tu-dan-ca-tam-hao-1500005.html")
    # insert_news("Thể hiện hit của diva Hà Trần, ‘thiên thần nhí’ khiến Soobin, Vũ Cát Tường phải tung ‘chiêu’ hết mình chinh phục", "Lần đầu tiên ở mùa giải năm nay, Giọng hát Việt nhí 2017 đã có một thí sinh khiến các HLV phải tung hết tất cả các chiêu trò để chiêu dụ về đội của mình. ",
    #             "https://img.saostar.vn/265x149/2017/08/19/1500621/mg_8085.jpg", "https://saostar.vn/tv-show/hien-hit-cua-diva-ha-tran-thien-nhi-khien-soobin-vu-cat-tuong-phai-tung-chieu-het-minh-chinh-phuc-1500621.html")
    insert_news("Vũ Cát Tường khoe ảnh nhí nhố cùng trò cưng tập luyện tại vòng Liveshow The Voice Kids", "Một Vũ Cát Tường chính chắn, điềm đạm trên ghế nóng khi ở bên cạnh các học trò lại trẻ trung và nữ tính hẳn ra!",
                "https://img.saostar.vn/360x203/2017/10/19/1687499/page-1.jpg", "https://saostar.vn/tv-show/vu-cat-tuong-khoe-anh-nhi-nho-cung-tro-cung-tap-luyen-tai-vong-liveshow-voice-kids-1687499.html")
    insert_news("Tập 10 The Voice Kids: Vì trò cưng, Vũ Cát Tường lần đầu khoe khả năng bắn ‘rap’ cực ngầu! ", " Khoảnh khắc Vũ Cát Tường hóa thân thành rapper chỉ là một trong những đểm nhấn ấn tượng trong tập 10 sắp lên sóng của chương trình Giọng hát Việt nhí. ",
                "https://img.saostar.vn/265x149/2017/10/15/1673813/trrr.jpg", "https://saostar.vn/tv-show/tap-10-voice-kids-vi-tro-cung-vu-cat-tuong-lan-dau-khoe-kha-nang-ban-rap-cuc-ngau-1673813.html")
    insert_news("Thuỵ Bình, Thảo Nguyên và học trò Giọng hát Việt nhí 2017 đáng yêu mừng sinh nhật Vũ Cát Tường ", " Có mặt từ sớm ở hậu trường, các học trò của Vũ Cát Tường cùng nhau gửi lời chúc tốt đẹp nhất đến cô giáo trong đêm Birthday Concert mừng sinh nhật tuổi 25. ",
                "https://img.saostar.vn/265x149/2017/10/14/1672817/sntuong.jpg", "https://saostar.vn/tv-show/thuy-binh-thao-nguyen-va-hoc-tro-giong-hat-viet-nhi-2017-dang-yeu-mung-sinh-nhat-vu-cat-tuong-1672817.html")
    insert_news("Tâm Hào - Thu Hà ‘đốn tim’ fan bằng Bolero, Phi Long - Quốc Thái bùng nổ với hit quốc tế ", " Đêm liveshow 1 vòng Đấu loại trực tiếp của Giọng hát Việt nhí đầy màu sắc với những tiết mục được 'đo ni đóng giày' cho từng thí sinh, phần nào cũng khiến cho chính những HLV phải đau đầu lựa chọn ai đi ai ở. ",
                "https://img.saostar.vn/265x149/2017/10/14/1671675/avakids.jpg", "https://saostar.vn/tv-show/tam-hao-thu-ha-don-tim-fan-bang-bolero-phi-long-quoc-thai-bung-no-voi-hit-quoc-te-1671675.html")
    insert_news("Soobin Hoàng Sơn ‘chơi lớn’ khi cho 2 học trò hát hit Michael Jackson, G-Dragon ", " Thể hiện lại hai ca khúc nổi tiếng Beat It và Untitled, có vẻ Phi Long và Quốc Thái đã khiến Soobin Hoàng Sơn thật sự hài lòng. ",
                "https://img.saostar.vn/265x149/2017/10/14/1672297/long-thai.jpg", "https://saostar.vn/tv-show/soobin-hoang-son-choi-lon-khi-cho-2-hoc-tro-hat-hit-michael-jackson-g-dragon-1672297.html")
    insert_news("Xử lý quá ‘ngọt’, học trò HLV Vũ Cát Tường xứng đáng là ‘truyền nhân Bolero’ ", " Thể hiện ca khúc Xin trả tôi về trong vòng loại trực tiếp của Giọng hát Việt nhí 2017, Thu Hà như 'đốn tim' những ai theo dõi phần thi của cô bé vì hát Bolero quá ngọt. ",
                "https://img.saostar.vn/265x149/2017/10/14/1672235/avthuha.jpg", "https://saostar.vn/tv-show/xu-ly-qua-ngot-hoc-tro-hlv-vu-cat-tuong-xung-dang-la-truyen-nhan-bolero-1672235.html")
    print('da them new news')


def insert_new_faq():
    # TO CHUC
    # TO CHUC - LA GI
    add_cat('tc', 'tổ chức', ["huấn luận viên", "địa điểm", "quay hình", "ở", "đâu", "ghvn", "tvk", "tổ chức", "năm sau", "2018", "bao nhiêu", "số lượng", "thí sinh", "giấu mặt", "bao nhiêu", "quán quân", "hlv",
                              "giọng hát việt nhí", "top 15", "team vũ cát tường", "team hương tràm tiên cookie", "team soobin", "trang web", "website", "địa chỉ web", "mỗi", "đội", "thí sinh", "mùa sau", "năm sau"])

    add_subcat('tc', 'tc_lg', 'là gì', ["bao nhiêu", "số lượng", "thí sinh", "giấu mặt", "bao nhiêu", "top 15", "team Vũ Cát Tường",
                                        "team Hương Tràm Tiên Cookie", "team Soobin Hoàng Sơn", "trang web", "website", "địa chỉ web"])
    add_qa('tc', 'tc_lg', 'tc_lg_1', "Một tập gồm mấy thí sinh vậy Ad?", ["bao nhiêu", "số lượng", "thí sinh"],
           "Bạn ơi bạn à! Bạn muốn hỏi tập mấy nà? Ahihi Mình đùa đấy!! Tùy theo mỗi tập sẽ có số lượng thí sinh khác nhau. Bạn nhớ xem chương trình vào 21h tối Thứ Bảy Hàng tuần trên VTV3 để nắm thông tin nhé!")
    add_qa('tc', 'tc_lg', 'tc_lg_2', 'Vòng giấu mặt có bao nhiêu tập?', [
           "giấu mặt", "bao nhiêu"], 'Vòng giấu mặt thường có 4-5 tập bạn nhé!')
    add_qa('tc', 'tc_lg', 'tc_lg_3', 'Top 15 của mỗi đội gồm bé nào vậy?', [
           "top 15", "team Vũ Cát Tường", "team Hương Tràm Tiên Cookie", "team Soobin"]	, 'Team Vũ Cát Tường bao gồm 15 thí sinh:')
    add_qa('tc', 'tc_lg', 'tc_lg_4', 'Website Giọng Hát Việt Nhí là gì vậy?', ["trang web", "website", "địa chỉ web"	],
           'Website chính thức của chương trình Giọng Hát Việt Nhí/The Voice Kids Việt Nam truy cập vào link: http://gionghatvietnhi.com.vn')

    # TO CHUC - DIA DIEM
    add_subcat('tc', 'tc_dd', 'địa điểm', [
               "địa điểm", "quay hình", "ở", "đâu", "ghvn", "tvk", "tổ chức", ])
    add_qa('tc', 'tc_dd', 'tc_dd_1', 'Địa điểm quay hình ở đâu?',	["địa điểm", "quay hình", "ở", "đâu"],
           'Theo dõi Fanpage để cập nhật thông tin địa điểm ghi hình sớm nhất bạn nhé!')
    add_qa('tc', 'tc_dd', 'tc_dd_2', 'Giọng Hát Việt Nhí tổ chức ở đâu vậy ạ?', [
           "ghvn", "tvk", "tổ chức", "ở", "đâu"],	'Giọng Hát Việt Nhí được tổ chức ghi hình tại TP. HCM bạn nhé! Để biết thêm thông tin địa điểm ghi hình chương trình bạn vui lòng theo dõi Fanpage thường xuyên nhé!')

    # TO CHUC - THOI GIAN
    add_subcat('tc', 'tc_tg', 'thời gian', ["năm", "sau", "2018", "tổ chức"])
    add_qa('tc', 'tc_tg', 'tc_tg_1', 'Năm sau còn tổ chức nữa không ạ?', [
           "năm", "sau", "2018", "tổ chức"], 'Bạn đáng yêu ơi! Giọng Hát Việt Nhí đã trải qua 5 mùa và sẽ tiếp tục đồng hành cùng khán giả yêu mến chương trình vào những năm tiếp theo bạn nhé!')

    # TO CHUC - NHAN SU
    add_subcat('tc', 'tc_ns', 'nhân sự', ["huấn luận viên",
                                          "quán quân", "năm nay", "hlv", "tvk", "ghvn", "Giọng hát việt nhí", "mùa", "năm", "sau"])
    add_qa('tc', 'tc_ns', 'tc_ns_1', 'Quán quân năm nay là ai vậy ạ?', [
           "quán quân", "năm", "nay"], 'Tham gia dự đoán quán quân Giọng Hát Việt Nhí tại Chatbot bạn nhé!')
    add_qa('tc', 'tc_ns', 'tc_ns_2', 'HLV Giọng Hát Việt Nhí 2017 là ai?', ["huấn luận viên",
                                                                            "HLV", "TVK", "GHVN", "giọng hát việt nhí"], 'HLV Giọng Hát Việt Nhí 2017 bao gồm ghế đôi ca sĩ Hương Tràm & nhạc sĩ Tiên Cookie, ghế đơn ca sĩ Soobin Hoàng Sơn và sự trở lại của HLV Giọng Hát Việt Nhí 2016 Vũ Cát Tường. Theo dõi chương trình và ủng hộ các đội mà bạn yêu thích nhé! ❤')
    add_qa('tc', 'tc_ns', 'tc_ns_3', 'Vũ Cát Tường/Soobin Hoàng Sơn/Hương Tràm/Tiên Cookie có làm HLV năm sau nữa không?',
           ["HLV", "mùa", "năm", "sau", "huấn luận viên"], "Cám ơn @user đã quan tâm và theo dõi chương trình. Thông tin về 'ghế nóng' năm sau vẫn là một 'ẩn số'. Theo dõi Fanpage để cập nhật tin tức mới nhất 'nóng hổi nhất' bạn nhé!")

    # TUYEN SINH - LA GI
    add_cat('ts', 'tuyển sinh', ["đăng ký", "còn", "tuyển sinh", "dự tuyển", "sao", "cách", "như thế nào",
                                 "thi", "hà nội", "thử giọng", "tham gia", "tuổi", "tham gia", "đi thi"])
    add_subcat('ts', 'ts_lg', 'là gì', ["tuổi", "tham gia", "đăng ký"])
    add_qa('ts', 'ts_lg', 'ts_lg_1', 'Bao nhiêu tuổi thì được tham gia chương trình vậy ạ?', [
           "tuổi", "tham gia", "đăng ký"], 'Độ tuổi đăng ký tham gia chương trình Giọng Hát Việt Nhí là từ 5 tuổi - 15 tuổi bạn nhé!')

    # TUYEN SINH - NHU THE NAO
    add_subcat('ts', 'ts_ntn', 'như thế nào', ["sao", "cách", "như thế nào",
                                               "đăng ký", "hà nội", "thử giọng", "tham gia", "thi", "tuyển sinh", "đi thi"])
    add_qa('ts', 'ts_ntn', 'ts_ntn_1', 'Địa điểm đăng ký ở Hà Nội', [
           "đăng ký", "hà nội"], 'Theo dõi Fanpage để cập nhật thông tin địa điểm đăng ký, tham gia dự tuyển vòng sơ loại nhanh nhất bạn nhé!')
    add_qa('ts', 'ts_ntn', 'ts_ntn_2', 'Tham gia thử giọng ở đâu vậy ad?', [
           "đăng ký", "thử giọng"], 'Theo dõi Fanpage để cập nhật thông tin đăng  ký và địa điểm ghi hình sớm nhất bạn nhé!')
    add_qa('ts', 'ts_ntn', 'ts_ntn_3', 'Mình muốn tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?',	[
           "đăng ký", "tham gia", "thi", "tuyển sinh", "đi thi", "sao", "cách", "như thế nào"]	, 'Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!')
    # TUYEN SINH - THOI GIAN
    add_subcat('ts', 'ts_tg', 'thời gian', [
               "đăng ký", "còn", "tuyển sinh", "dự tuyển", "thi"])
    add_qa('ts', 'ts_tg', 'ts_tg_1', 'Bây giờ còn đăng ký được nữa không?', ["đăng ký", "còn", "tuyển sinh", "dự tuyển", "thi"],
           'Tuyển sinh Giọng Hát Việt Nhí 2018 sẽ được mở ngay sau khi Chung Kết Giọng Hát Việt Nhí 2017 kết thúc. Các bạn theo dõi Fanpage để cập nhật thông tin sớm nhất nhé!')
    # PHAT SONG - LA GI
    add_cat('ps', 'phát sóng', ["khi", "nào", "phát sóng", "tuần", "này", "lịch", "lịch chiếu", "giờ", "chiếu", "lại", "phát", "xem", "full", "bản", "cut",
                                "youtube", "GHVN", "TVK", "link", "tập", "mới", "Livestream", "hậu trường", "behind", "sence", "bts", "trực tiếp", "liveshow"])
    add_subcat('ps', 'ps_lg', 'là gì', ["phát sóng", "tuần", "này", "trực tiếp", "liveshow",
                                        "youtube", "GHVN", "TVK", "link", "tập", "mới", "hậu trường", "behind", "sence", "bts"])
    add_qa('ps', 'ps_lg', 'ps_lg_3', 'Chương trình có trên Youtube không?', [
           'ghvn', 'youtube', 'tvk'], 'Để xem chương trình trên Youtube bạn truy cập vào link: http://youtube.com/btcgionghatvietnhi Nhớ nhấn Subcribe để xem các tiết mục đầu tiên.')
    add_qa('ps', 'ps_lg', 'ps_lg_1', 'Tuần này có phát sóng Giọng Hát Việt Nhí 2017 không Ad?', [
           "phát sóng", "tuần", "này"], 'Bạn thân yêu ơi Giọng Hát Việt Nhí 2017 sẽ được phát sóng vào 21h thứ bảy trên kênh VTV3. Bạn nhớ đón xem nha!')
    add_qa('ps', 'ps_lg', 'ps_lg_2', 'Năm nay các vòng Liveshow có phát trực tiếp không?', [
           "trực tiếp", "liveshow"], 'Liveshow chung kết Giọng Hát Việt Nhí sẽ được phát sóng trực tiếp trên kênh VTV3 vào ngày 25/11/2017 các bạn nhé!')
    add_qa('ps', 'ps_lg', 'ps_lg_4', 'Cho mình xin link tập mới nha', [
           "link", "tập", "mới"], "Bạn thân mến! Để xem lại tập vừa phát sóng hãy trở lại phím 'Home' và nhấp vào 'Xem lại tập phát sóng' trên kênh Youtube chính thức của chương trình bạn nhé!")
    add_qa('ps', 'ps_lg', 'ps_lg_5', 'Admin có quay cảnh hậu trường không?', [
           "hậu trường", "behind", "sence", "bts"], 'Để xem lại những khoảnh khắc hậu trường vui nhộn bạn nhớ subcribe kênh VIVA Shows: http://bit.ly/vivashows nhé!')
    add_qa('ps', 'ps_lg', 'ps_lg_6', 'Tại sao the voice kids không có bản full trên youtube', [
           "full", "youtube", "bản", "cut"], 'Vì lý do bản quyền The Voice Kids không cho phép công bố bản Full trên Youtube nên chúng tôi rất tiếc vì sự bất tiện này. Tuy nhiên, khán giả có thể dễ dàng theo dõi từ thí sính mà mình yêu thích một cách dễ dàng mà không tốn quá nhiều thời gian.')

    # PHAT SONG - THOI GIAN
    add_subcat('ps', 'ps_tg', 'thời gian', ["khi", "nào", "lịch", "phát sóng", "chiếu", "mấy", "giờ", "thời gian",
                                            "GHVN", "TVK", "chiếu", "phát", "lại", "livestream", "trực tiếp", "liveshow"])
    add_qa('ps', 'ps_tg', 'ps_tg_1', 'Em muốn hỏi lịch phát sóng Giọng Hát Việt nhí', ["thời gian", "chiếu",
                                                                                       "phát sóng", "lịch", "mấy", "giờ", "khi", "nào"], 'Giọng Hát Việt Nhí 2017 được phát sóng vào lúc 21 giờ thứ Bảy hàng tuần trên kênh VTV3 bạn nhé! ❤')
    add_qa('ps', 'ps_tg', 'ps_tg_2', 'GHVN có phát sóng lại không Ad?', [
           "GHVN", "TVK", "chiếu", "phát", "lại"], "Giọng Hát Việt Nhí 2017 sẽ được phát sóng vào lúc 21h thứ bảy hàng tuần trên VTV3 và được phát lại vào lúc 14h30 thứ hai tuần tiếp theo cũng trên kênh VTV3 nhé 'bạn dấu yêu'.")
    add_qa('ps', 'ps_tg', 'ps_tg_3', 'Có Livestream phát sóng không ad?', [
           "Livestream", "phát sóng"], 'Chương trình Giọng Hát Việt Nhí sẽ được Livestream phát sóng trực tiếp trên Fanpage Saostar vào 21h30 tối thứ Bảy hàng tuần. Đừng bỏ lỡ nhé bạn yêu !!!')
    add_qa('ps', 'ps_tg', 'ps_tg_4', 'Năm nay các vòng Liveshow có phát trực tiếp không?', [
           "trực tiếp", "liveshow"], 'Liveshow chung kết Giọng Hát Việt Nhí sẽ được phát sóng trực tiếp trên kênh VTV3 vào ngày 25/11/2017 các bạn nhé!')
    add_qa('ps', 'ps_tg', 'ps_tg_5', 'Làm sao xem lại GHVN được ạ?'	, [
           "xem", "lại", "GHVN", "TVK"], 'Bạn có thể xem phát sóng lại Giọng Hát Việt Nhí vào lúc 14h30 thứ 2 tuần tiếp theo trên VTV3 hoặc vào Youtube chính thức của chương trình để xem lại những tiết mục yêu thích bạn nhé!')

    # KHAN GIA
    # KHAN GIA - NHU THE NAO
    add_cat('ks', 'khán giả', ["bình chọn", "dùng", "sử dụng", "chatbot", "mua",
                               "vé", "trực tiếp", "minigame", "tham gia", "hình", "fansign", "HLV"])
    add_subcat('ks', 'ks_ntn', 'như thế nào', ["bình chọn", "dùng", "sử dụng", "chatbot", "mua",
                                               "vé", "trực tiếp", "minigame", "tham gia", "hình", "fansign", "HLV"])
    add_qa('ks', 'ks_ntn', 'ks_ntn_1', 'Làm sao để bình chọn cho thí sinh',	[
           "bình chọn"]	, 'Hệ thống bình chọn chỉ hoạt động để bình chọn chiếc vé may mắn cho thí sinh quay trở lại đêm chung kết và bình chọn cho quán quân chương trình Giọng Hát Việt Nhí 2017 trong đêm chung kết được mở từ ngày 19/11 - 25/11/2017')
    add_qa('ks', 'ks_ntn', 'ks_ntn_2', 'Làm sao để sử dụng Chatbot', [
           "dùng", "sử dụng", "chatbot"], "Bạn truy cập vào link m.me/gionghatvietnhi và nhấn nút 'Bắt đầu' để tham gia Chatbot Giọng Hát Việt Nhí nhé!")
    add_qa('ks', 'ks_ntn', 'ks_ntn_3', 'Làm sao để mua vé xem trực tiếp?', [
           "mua", "vé", "trực tiếp"], 'Vé xem ghi hình Giọng Hát Việt Nhí được phát miễn phí cho các bạn tham gia Minigame trên Fanpage. Theo dõi Fanpage, nhanh tay tham gia Minigame để có cơ hội nhận vé miễn phí nhé!')
    add_qa('ks', 'ks_ntn', 'ks_ntn_4', 'Tham gia mini game như thế nào?', [
           "minigame", "tham gia"], "Tham gia Chatbot Giọng Hát Việt Nhí và nhấn 'Home' => Tiếp theo vào menu 'Minigame 1/2' nhấn 'Tham gia dự đoán' và bắt đầu chơi game thật vui nhé!")
    add_qa('ks', 'ks_ntn', 'ks_ntn_5', 'Gửi cho mình hình của Vũ Cát Tường/Hương Tràm/Tiên Cookie/Soobin Hoàng Sơn được không ạ?',
           ["hình", "fansign", "HLV"], "Bạn vào 'Home' chọn menu 'Fansign' => chọn HLV mà bạn yêu thích để nhận được Fansign của HLV thần tượng bạn nhé!")
    # TUONG TAC USER
    add_cat('ttu', 'tương tác user', ["vâng", "bye", "vang"
                                      "Xin chào", "chào", "hi", "hey", "hello", "Cảm ơn", "Thankyou", "Thank", "ok", "cam", "on", "chao"])
    add_subcat('ttu', "ttu_ntn", 'như thế nào', ["chao", "bye", "vang"
                                                 "Xin chào", "chào", "hi", "hey", "hello", "Cảm ơn", "Thankyou", "Thank", "ok", "cam", "on"])
    add_qa('ttu', 'ttu_ntn', 'ttu_ntn_1', "Xin chào", ["chao", "vâng", "vang"
                                                       "Xin chào", "chào", "hi", "hey", "hello"], 'Chào bạn đáng yêu, Bot có thể giúp gì cho bạn?')
    add_qa('ttu', 'ttu_ntn', 'ttu_ntn_2', "Cảm ơn", ["ok", "Cảm ơn", "vâng", "bye", "Thankyou", "Thank", "Thanks", "cam", "on"],
           "Chúc bạn 1 ngày tốt lành, nếu có gì thắc mắc về chương trình,nhắn ngay cho Bot nhé, Bot luôn sẵn lòng giải đáp cho bạn")


# insert_new_faq()
insert_new_news()
