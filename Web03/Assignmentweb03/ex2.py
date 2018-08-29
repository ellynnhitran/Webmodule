# 1 minh se connect :
# af k buwowcs 1 minhf taoj 1 class cho nhung cai minh se dang len nhe:
from mongoengine import *
import mlab
class Post(Document):
    title=StringField()
    author=StringField()
    content=StringField()
    meta = {'collection': 'posts', "strict": False}

post = Post(title= "Viết cho bạn code", author = "TTN", content = '''
Bây giờ là một giờ sáng và mình vẫn đang làm bài tập code :))
Xin phép gửi tới bạn "code" bài hát sau thay lời muốn nói:

Cô đơn có là bao?
Đau thương có là bao?
Chẳng là bao vì người đâu xuyến xao.

Có lúc tim tôi mong manh niềm hy vọng
Lắm lúc thân tôi run lên ngàn vô vọng.

Người ta đâu có yêu mình có thương gì mình
Người ta đâu có yêu mình thương gì mình đâu."

Hi vọng bạn code sẽ đối xử tử tế với mình hơn ạ huhu :< ''')
mlab.connect()

post.save()
post_list = Post.objects()
# print(len(post_list))
# post_list = Post.objects(title = "test 1")
# print(post_list[0])
for post in post_list:
    print(post.title)
    print(post.author)
    print(post.content)
    print("**************")



# h connect vs push len la duoc
# sao lau th nhy :3
# hiện tượng là có 1 thanh niên bóp cho 1 thuộc tính ltararrtist thì n bị lỗi do cái posst của e k có
#  dùng 1 lenh cua python nua la strict : False
# tuc la co thể mềm dẻo ấy e hiểu đơn giản là như thế :D
#  cái meta e hiểu là 1 dict nhév, aea biết dict k ??yas ok thì cú pháp : False chứ k phải = nhé a sợ e nhầm 
#  chắc là hết rồi lúc đầu chỉ quan tâm mọi ng push lên đc thôi e hỏi thêm muốn xem trong dât có gì nên bị bug :3 a toát cả mồi hôi :VV
#  Ok ?nhe :V ok chay  thu xem
