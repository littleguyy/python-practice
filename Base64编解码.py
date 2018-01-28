# python 3.6.3
import base64
import codecs
string_test=r'''
# python3.6

class 你好():
    class 在干吗():
        class 你需要():
            class 学习():
                class 编程技术():
                    def 吗():
                        print("不需要谢谢，我都会。")

你好.在干吗.你需要.学习.编程技术.吗()

'''
print(string_test)

print(base64.b64encode(bytes(string_test,"utf-8")))

print(base64.b64decode(bytes('5Lul5ZCO5pyJ5LqL5oiR6YO95YaZ5oiQQmFzZTY0IFVURi0455qE5paH5pys',"utf-8")).decode('utf-8'))


decodedata=codecs.decode(bytes("5Y+v5Lul5YWI55yL55yL57O757uf5Y6f55CG","utf8"),'base64')
print(decodedata.decode('utf-8'))
