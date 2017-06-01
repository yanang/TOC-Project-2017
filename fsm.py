from transitions.extensions import GraphMachine
import telegram
import pygame
import random

API_TOKEN = '318702613:AAGaEL6D6WAz7-ErNiL4e67rLMYY4KrL1uw'
bot = telegram.Bot(token=API_TOKEN)
choice =  random.randint(0,2)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_pos0(self, update):
        text = update.message.text
        if '正' in text:
            return True

    def is_going_to_pos1(self, update):
        text = update.message.text
        if len(text) >= 1:
            if '不' in text:
                return True
            elif '更' in text:
                return True
            else:
                answer = "我才不管你說"+text+"呢"
                update.message.reply_text(answer)
                return True

    def is_going_to_pos2(self, update):
        text = update.message.text
        print(choice)
        if choice == 0:
            if '正' in text:
                return True

    def is_going_to_pos3(self, update):
        text = update.message.text
        if choice == 1:
            if '正' in text:
                return True

    def is_going_to_pos4(self, update):
        text = update.message.text
        if choice == 2:
            if '正' in text:
                return True

    def is_going_to_neg0(self, update):
        text = update.message.text
        if '負' in text:
            return True      
        elif '好' in text:
            return True

    def is_going_to_neg0_from(self, update):
        text = update.message.text
        if '負' in text:
            return True

    def is_going_to_none(self, update):
        text = update.message.text
        if len(text) >= 1:
            if '正' in text:
                return False
            elif '負' in text:
                return False
            elif '/start' in text:
                update.message.reply_text("要不要來點正能量或是負能量阿？")
                return False
            else:
                return True

    def on_enter_user(self, update):
        print('enter-user')
        text = update.message.text
        update.message.reply_text("要不要來點正能量或是負能量阿？")

    def on_enter_pos0(self, update):
        print('enter-pos0')
        text = update.message.text
        update.message.reply_text("I am the sunshin f❤️r U")
        #bot.send_photo(chat_id=update.message.chat_id, photo=open('pic5.png','rb'))
        bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/ybmI7MQ.jpg')
        update.message.reply_text("你覺的這樣夠嗎？")

    def on_enter_pos1(self, update):
        print('enter-pos1')
        text = update.message.text
        update.message.reply_text("I still shin f❤️r U at night")
        #bot.send_photo(chat_id=update.message.chat_id, photo=open('pic6.png','rb'))
        bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/C1O5HtF.jpg')
        update.message.reply_text("天呀～我已經無時無刻都在你身邊了 不能在多了")
        update.message.reply_text("需要再來點正能量或是負能量嗎？")
        

    def on_enter_pos2(self, update):
        print('enter-pos2')
        text = update.message.text
        update.message.reply_text("不得了，你有道光從天靈蓋噴出來，簡直就是百年一見的練武奇才阿！")
        #bot.send_photo(chat_id=update.message.chat_id, photo=open('pic1.png','rb'))
        bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/HW8wNYU.jpg')
        global choice
        choice =  random.randint(0,2)
        self.go_back_user(update)

    def on_enter_pos3(self, update):
        print('enter-pos3')
        text = update.message.text
        update.message.reply_text("相信自己和你的全部，你的內在有一個比任何障礙都還要強大的東西！")
        #bot.send_photo(chat_id=update.message.chat_id, photo=open('pic3.png','rb'))
        bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/aU4rXdO.jpg')
        global choice
        choice =  random.randint(0,2)
        self.go_back_user(update)

    def on_enter_pos4(self, update):
        print('enter-pos4')
        text = update.message.text
        update.message.reply_text("每一個不努力的日子就是對生命的辜負！")
        #bot.send_photo(chat_id=update.message.chat_id, photo=open('pic4.png','rb'))
        bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/tONib7C.jpg')
        global choice
        choice =  random.randint(0,2)
        self.go_back_user(update)

    def on_enter_neg0(self, update):
        print('enter-neg0')
        text = update.message.text
        ran =  random.randint(0,2)
        if ran == 0:
            update.message.reply_text("努力不一定有結果，但是不努力會")
            bot.send_document(chat_id=update.message.chat_id, document=open('gif2.gif', 'rb'))
            update.message.reply_text("          很輕鬆")
        elif ran == 1:
            update.message.reply_text("努力不懈的繼續奔跑吧～")
            bot.send_document(chat_id=update.message.chat_id, document=open('gif3.gif', 'rb'))
            update.message.reply_text("雖然你永遠瘦不下來")
        else:
            update.message.reply_text("今天解決不了的問題，別著急了")
            bot.send_document(chat_id=update.message.chat_id, document=open('gif1.gif', 'rb'))
            update.message.reply_text("反正你明天也解決不了")
        self.go_back_user(update)

    def on_enter_none(self, update):
        print('enter-none')
        text = update.message.text
        update.message.reply_text("原來你什麼都不想要 🎵🎵 ")
        bot.send_audio(chat_id=update.message.chat_id, audio=open('music.mp3', 'rb'))
        #bot.send_video(chat_id=update.message.chat_id, video=open('music.mp4', 'rb'))
        self.go_back_user(update)

    def on_exit_pos0(self, update):
        print('Leaving pos0')

    def on_exit_pos1(self, update):
        print('Leaving pos1')

    def on_exit_pos2(self, update):
        print('Leaving pos2')

    def on_exit_pos3(self, update):
        print('Leaving pos3')

    def on_exit_pos4(self, update):
        print('Leaving pos4')

    def on_exit_neg0(self, update):
        print('Leaving neg0')

    def on_exit_none(self, update):
        print('Leaving none')
