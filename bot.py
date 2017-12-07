import requests
import urllib.request
import facesdetector
import filterer
class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.api_file_url = "https://api.telegram.org/file/bot{}/".format(token)
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        #print(resp.url)
        print(self.api_url + method, params)
        return resp
    def get_filePath(self, chat_id, file_id):
        params = {'chat_id': chat_id, 'file_id': file_id}
        method = 'getFile'
        resp = requests.get(self.api_url + method, params)
        #print(resp.url)
        print(self.api_url + method, params)
        print(resp)
        return resp
    def download_file(self, file_id):
        params = {'file_id' : file_id}
        method = 'getFile'
        resp = requests.get(self.api_url + method, params)
        #print(resp)
        file_path = resp.json()['result']['file_path']
        print(self.api_file_url + file_path)
        urllib.request.urlretrieve(self.api_file_url + file_path, "file.jpg")
        #return file
    '''def get_file(self, chat_id, last_m):
        params = {'chat_id': chat_id}
        method = 'getFile'
        resp = requests.post(self.api_url + method, params)
        #print(resp.url)
        print(self.api_url + method, params)
        print(resp)
        return resp'''
    def send_photo(self, chat_id, path):

        files = {'photo': open(path, 'rb')}
        method = 'sendPhoto'
        params = {'chat_id': chat_id}
        #resp = requests.post(url, files=files)
        resp = requests.post(self.api_url + method, params, files=files)
        #resp = requests.post(self.api_url + method, chat_id, photo=open(path, 'rb'))

        #resp = requests.post(self.api_url + method, )
        #print(resp.url)
        #method = 'sendPhoto'
        #params = {'chat_id': chat_id, 'photo': open('/Users/Pomavau/test.png', 'rb')}
        #resp = requests.post(self.api_url + method, params)
        #print(self.api_url + method, params)
        print(resp)
        return resp
    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

automator = BotHandler('')
facedetector = facesdetector.FaceDetector()
filterer = filterer.Filterer()
def main():
    #drawer()
    #automator.download_file(last_update['message']['photo'][3]['file_path'])
    new_offset = None
    currentstate = 0
    while True:
        automator.get_updates(new_offset)
        last_update = automator.get_last_update()
        #automator.download_file(last_update['message']['photo'][3]['file_path'])
        last_update_id = last_update['update_id']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_text = ''
        last_photo_id = ''
        currentmode = -1 # 0 for text, 1 for images
        try:
            last_chat_text = last_update['message']['text']
            currentmode = 0
        except:
            try:
                last_photo_id = last_update['message']['photo'][3]['file_id']
            except:
                try:
                    last_photo_id = last_update['message']['photo'][2]['file_id']
                except:
                    try:
                        last_photo_id = last_update['message']['photo'][1]['file_id']
                    except:
                        last_photo_id = last_update['message']['photo'][0]['file_id']
            automator.download_file(last_photo_id)
            currentmode = 1
        continueflag = 0
        #currentstate = 0 #0 - start, 1 - wait for reply
        temp = ''
        if last_chat_text.lower() == 'hi':
            automator.send_message(last_chat_id, 'hi\ni\'m\njavasquirt bot')
        if last_chat_text.lower() == '/new':
            temp = last_chat_text.lower()
            temp_photo = last_photo_id
            automator.send_message(last_chat_id, 'Image1: ')
            while True:
                automator.get_updates(new_offset)
                last_update = automator.get_last_update()
                last_update_id = last_update['update_id']
                last_chat_id = last_update['message']['chat']['id']
                try:
                    last_chat_text = last_update['message']['text']
                except:
                    try:
                        last_photo_id = last_update['message']['photo'][3]['file_id']
                    except:
                        try:
                            last_photo_id = last_update['message']['photo'][2]['file_id']
                        except:
                            try:
                                last_photo_id = last_update['message']['photo'][1]['file_id']
                            except:
                                last_photo_id = last_update['message']['photo'][0]['file_id']
                    automator.download_file(last_photo_id)
                    currentmode = 1
                print('last if')
                if (last_chat_text.lower() != temp if currentmode == 0 else last_photo_id != temp):
                    while True:
                        automator.send_message(last_chat_id, 'What do we do? \n 1 - oldPhoto \n 2 - frescoOnTheChromaKey \n 3 - demonInConsole \n 4 - lemonParadise \n 5 - deepInPurple \n 6 - aquarium \n 7 - tonedCar \n 8 - roboPainter \n 3 - indigo')
                        while True:
                            try:
                                last_update = automator.get_last_update()
                                #print('')
                                last_update_id = last_update['update_id']
                                last_chat_text = last_update['message']['text']
                                choose = last_chat_text
                                last_chat_id = last_update['message']['chat']['id']
                                #if last_chat_text != temp:
                                facedetector.replacefaces('file.jpg')
                                print('\n Choose: ' + choose)
                                if choose == '0':
                                    imgtosend = filterer.freq_colorize('result.png')
                                if choose == '1':
                                    imgtosend = filterer.oldPhoto('result.png')
                                if choose == '2':
                                    imgtosend = filterer.frescoOnTheChromaKey('result.png')
                                if choose == '3':
                                    imgtosend = filterer.demonInConsole('result.png')
                                if choose == '4':
                                    imgtosend = filterer.lemonParadise('result.png')
                                if choose == '5':
                                    imgtosend = filterer.deepInPurple('result.png')
                                if choose == '6':
                                    imgtosend = filterer.aquarium('result.png')
                                if choose == '7':
                                    imgtosend = filterer.tonedCar('result.png')
                                if choose == '8':
                                    imgtosend = filterer.roboPainter('result.png')
                                if choose == '9':
                                    imgtosend = filterer.indigo('result.png')
                                #imgtosend = filterer.indigo('result.png')
                                imgtosend.save('result1.png')
                                #automator.send_photo(last_chat_id, 'result.png')
                                automator.send_photo(last_chat_id, 'result1.png')
                                #new_offset = last_update_id + 1
                                #automator.get_updates(new_offset)
                                new_offset = last_update_id + 1
                                automator.get_updates(new_offset)
                                print("cnt1")
                                return 0
                                #continue
                            except:
                                continue
                            continue
                        #continue
                    #continue
                    #break
                    return 0
                else:
                    new_offset = last_update_id + 1
                    print("cnt2")
                    #return 0
                    continue#∆
                print("return")
                return 0  # ∆ ∆
        new_offset = last_update_id + 1#∆
                                       #∆∆
     #åå∂˙®˚®˚ƒµ∂∆∂ß√´ƒ∂∆´

def robust_main():
    try:
        while True:
            main()
    except:
            robust_main()

#robust_main()
#while True:
robust_main()