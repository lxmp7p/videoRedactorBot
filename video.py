import telebot
import urllib.request
import os
import config
from random import randint
bot = telebot.TeleBot(config.token)

path_script = '/root/zenVideoRotate/'
fix = 'root/zenVideoRotate/'

def delete_files(file_path, FileName):
        file_path = '/' + str(file_path)
        os.system('rm ' + path_script + file_path)
        os.system('rm ' + path_script + FileName)


@bot.message_handler(content_types=["video"])
def content_document(message):
        bot.send_message(message.chat.id, 'Ожидай хуле')
        video_id = message.video.file_id
        file_info = bot.get_file(video_id)
        download = 'http://api.telegram.org/file/bot' + config.token + '/' + file_info.file_path
        FileName = str(randint(10000,99999)) + '.mp4'
        urllib.request.urlretrieve(download,  file_info.file_path)
        os.system('ffmpeg -i ' + path_script + file_info.file_path + ' -vf "hflip" -c:a copy ' + FileName)
        #path = path_script + NameFile
        #print(path)
        video = open(path_script + FileName, 'rb')
        bot.send_video(message.chat.id, video)
        video.close()
        delete_files(file_info.file_path, FileName)


bot.polling() # запускаем бота
