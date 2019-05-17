


import requests
import redis
import yaml

r = redis.StrictRedis(host='localhost', port=6379, db=0)

class MessageBuild:
    r = redis.StrictRedis(host='localhost', port=6379, db=0) #адрес и порт  базы данных
    msgWELCOME = [
        {
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "Добрый день! Данное приложение предоставляет доступ к технологической информации о работе оборудования. "
		}
	},
	{
		"type": "divider"
	},
	{
		"type": "actions",
		"elements": [
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Начать",
					"emoji":  True 
				},
                "style": "primary",
				"value": "begin"
                
			}
		]
	}
    ]


    msgMAINMENU = [
        {
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Главное меню*\nЧетверг, Май 21 16:45"
		},
		"accessory": {
			"type": "image",
			"image_url": "https://image.flaticon.com/icons/png/512/1027/1027038.png",
			"alt_text": "main menu"
		}
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Выберите из:*"
		}
	},
	{
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Последние критические данные*"
		},
		"accessory": {
			"type": "button",
			"text": {
				"type": "plain_text",
				"emoji":  True ,
				"text": "Выбрать"
			},
			"style": "primary",
			"value": "lastcrit"
		}
	},
	{
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Список оборудования*"
		},
		"accessory": {
			"type": "button",
			"text": {
				"type": "plain_text",
				"emoji":  True ,
				"text": "Выбрать"
			},
			"style": "primary",
			"value": "listmachine"
		}
	},
	{
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*График за последние 7 дней*"
		},
		"accessory": {
			"type": "button",
			"text": {
				"type": "plain_text",
				"emoji":  True ,
				"text": "Выбрать"
			},
			"style": "primary",
			"value": "grafic"
		}
	},
	{
		"type": "divider"
	},
	{
		"type": "actions",
		"elements": [
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Отмена",
					"emoji":  True 
				},
                "style": "danger",
				"value": "backwelcome"
			}
		]
	}
    ]


    msgLASTCRIT = [
        {
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Последние критические данные*\nЧетверг, Май 21 16:45:53\n *Тип:* Tool error \n *Оборудование:* Стенд АксиОМА, Стенд, Аудитория 349  \n *Подробности:* В таблице инструментов нет инструмента с таким номером."
		},
		"accessory": {
			"type": "image",
			"image_url": "https://imageog.flaticon.com/icons/png/512/164/164584.png?size=1200x630f&pad=10,10,10,10&ext=png&bg=FFFFFFFF",
			"alt_text": "main menu"
		}
	},
	{
		"type": "divider"
	},
	{
		"type": "actions",
		"elements": [
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Назад",
					"emoji":  True 
				},
				"style": "danger",
				"value": "backtomain"
			}
		]
	}
    ]


    msgLISTMACHINE =[
        {
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Оборудование*\n*Выберите из:*"
		},
		"accessory": {
			"type": "image",
			"image_url": "https://social-earnings.info/img/gears.png",
			"alt_text": "main menu"
		}
	},

    {"type": "section", "text": {"type": "mrkdwn", "text": "*Стенд АксиОМА*\n Стенд, Аудитория 349 "}}, {"type": "actions", "block_id": "3", "elements": [{"type": "button", "text": {"type": "plain_text", "text": "Моточасы"}, "value": "mototime"}, {"type": "button", "text": {"type": "plain_text", "text": "Канал 1"}, "value": "chanel"}, {"type": "button", "text": {"type": "plain_text", "text": "ПЛК"}, "value": "plc"}]}, {"type": "divider"}, {"type": "section", "text": {"type": "mrkdwn", "text": "*Стенд АксиОМА*\n Стенд, Аудитория 3-6 "}}, {"type": "actions", "block_id": "5", "elements": [{"type": "button", "text": {"type": "plain_text", "text": "Моточасы"}, "value": "mototime"}, {"type": "button", "text": {"type": "plain_text", "text": "Канал 1"}, "value": "chanel"}, {"type": "button", "text": {"type": "plain_text", "text": "ПЛК"}, "value": "plc"}]}, {"type": "divider"}, {"type": "section", "text": {"type": "mrkdwn", "text": "*Мини станок*\n Стенд, Аудитория 355 "}}, {"type": "actions", "block_id": "6", "elements": [{"type": "button", "text": {"type": "plain_text", "text": "Моточасы"}, "value": "mototime"}, {"type": "button", "text": {"type": "plain_text", "text": "Канал 1"}, "value": "chanel"}, {"type": "button", "text": {"type": "plain_text", "text": "ПЛК"}, "value": "plc"}]}, {"type": "divider"}, {"type": "section", "text": {"type": "mrkdwn", "text": "*CAN станок*\n Фрезерный, Аудитория 355 "}}, {"type":"actions", "block_id": "7", "elements": [{"type": "button", "text": {"type": "plain_text", "text": "Моточасы"}, "value": "mototime"}, {"type": "button", "text": {"type": "plain_text", "text": "Канал 1"}, "value": "chanel"}, {"type": "button", "text": {"type": "plain_text", "text": "ПЛК"}, "value": "plc"}]}, {"type": "divider"},


	
	
	{
		"type": "actions",
		"elements": [
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Назад"
				
				},
				"style": "danger",
				"value": "backtomain"
			}
		]
	}
    ]


    msgGRAFIC = [
        {
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*График возникновения критических ситуаций за последние 7 дней*\n Май 21 16:45 - Май 28 16:45\n   *Макс. количество:* Стенд АксиОМА, Стенд, Аудитория 349   \n *Подробности:* 6 раз за неделю"
		}
	},
    {
		"type": "image",
		"title": {
			"type": "plain_text",
			"text": "image1",
			"emoji":  True 
		},
		"image_url": "https://pp.userapi.com/c844616/v844616078/20871c/oebPFra3kOQ.jpg",
		"alt_text": "image1"
	},
	{
		"type": "actions",
		"elements": [
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Назад",
					"emoji":  True 
				},
				"style": "danger",
				"value": "backtomain"
			}
		]
	}
    ]


    msgCHANEL = [
        {
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Оборудование:* данные\n *Канал 1*\n *Время работы канала(всего):* данные \n *Время работы канала(текущее):* данные \n *Статус канала:* данные \n *Режим канала:* данные \n *Программа:* данные"
		},
        "accessory": {
			"type": "image",
			"image_url": "https://imageog.flaticon.com/icons/png/512/1366/1366120.png?size=1200x630f&pad=10,10,10,10&ext=png&bg=FFFFFFFF",
			"alt_text": "computer thumbnail"
		}
	},
	{
		"type": "actions",
		"block_id": "actionblock789",
		"elements": [
			
            {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "  Обновить  ",
					"emoji":  True 
				},
				"style": "primary",
				"value": "chanel"
			},
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Назад",
					"emoji":  True 
				},
				"action_id": "update",
				"style": "danger",
				"value": "backtolistmachine"
			}
		]
	}
    ]


    msgMOTOTIME = [
        {
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Оборудование:* данные\n *Моточасы*\n *Время работы ядра(всего):* данные \n *Время работы ядра(текущее):* данные \n *Количество перезапусков ядра:* данные \n *Количество каналов:* данные \n "
		},
        "accessory": {
			"type": "image",
			"image_url": "https://lh4.ggpht.com/aaGEIX8BCsoj4aCSoI40WMezz2leht0-8CyGqlxlapZVinccPwPN2UQOinweglJWYg=w1200-h630-p-k-no-nu",
			"alt_text": "computer thumbnail"
		}
	},
	{
		"type": "actions",
		"block_id": "actionblock789",
		"elements": [
			
            {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "  Обновить  ",
					"emoji":  True 
				},
				"action_id": "update",
				"style": "primary",
				"value": "mototime"
			},
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Назад",
					"emoji":  True 
				},
				"style": "danger",
				"value": "backtolistmachine"
			}
		]
	}
    ]


    msgPLC = [{
		"type": "divider"
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Оборудование:* данные\n *ПЛК*\n *Состояние SoftPLC:* данные \n *К-во элементов в ядре:* данные \n *К-во элементов на гл.форме:* данные \n *Проверка:* данные \n "
		},
        "accessory": {
			"type": "image",
			"image_url": "https://image.flaticon.com/icons/png/512/752/752568.png",
			"alt_text": "computer thumbnail"
		}
	},
	{
		"type": "actions",
		"block_id": "actionblock789",
		"elements": [
			
            {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "  Обновить  ",
					"emoji":  True 
				},
				"action_id": "update",
				"style": "primary",
				"value": "plc"
			},
			{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Назад",
					"emoji":  True 
				},
				"style": "danger",
				"value": "backtolistmachine"
			}
		]
	}
    ]
    listMACHINE = {
			'3':['Стенд АксиОМА','Стенд','Аудитория 349'],
			'5':['Стенд АксиОМА','Стенд','Аудитория 3-6'],
			'6':['Мини станок','Стенд','Аудитория 355'],
			'7':['CAN станок','Фрезерный','Аудитория 355']
	}

    def getAnswer(self, param, machine):
		####### берет yaml, преобразует в словарь и возвращает словарь
    	listGot = {'mototime':'Моточасы','chanel': 'Канал 1','plc': 'ПЛК'}
    	infoparam = listGot[param]
    	listParam = {'Моточасы':['mototimes','mototime'],'Канал 1':['chan1_entries', 'chan1'],'ПЛК':['plc_entries','plc']}
    	var1 = listParam[infoparam][0]
    	var2 = listParam[infoparam][1]
    	response = requests.get('https://eio.ksu.ru.com/locales/ru.yml')
    	convert = bytes(response.content)
    	convert = convert.decode('utf-8')
    	convert = yaml.load(convert)
    	convert = convert['ru'][var1]  # готовый словарь с названиями
    	############работа с редис
    	mach = machine
    	mach = int(mach[-1])
    	#if mach >=4:
    	#	mach += 1
    	red = str(r.get(str(mach)))
    	red = red.replace('=>',':')
    	dict1=eval(red)
    	dict1 = eval(dict1)#словарь со значениями
    	strAnsver = ''
    	#соединение значений с названиями
    	for key in convert:
    		newkey = var1+'.'+key
    		try:
    			newstr = convert[key]+': *'+dict1[var2][newkey]+'*\n'
    		except:
    			continue
    		strAnsver += newstr
    	nameMACHINE =''
    	for i in self.listMACHINE[machine]:
    		nameMACHINE+= i+', '

    	strAnsver = '*'+ nameMACHINE +':*\n *'+infoparam+'*\n' + strAnsver

    	if param == 'plc':
            self.msgPLC[2]['block_id'] = machine
            self.msgPLC[1]["text"]["text"] = strAnsver
    	elif param == 'chanel':
            self.msgCHANEL[2]['block_id'] = machine
            self.msgCHANEL[1]["text"]["text"] = strAnsver
    	elif param == 'mototime':
            self.msgMOTOTIME[2]['block_id'] = machine
            self.msgMOTOTIME[1]["text"]["text"] = strAnsver
    	
    	#return strAnsver  #возвращает строку ответа


    def getcomand(self,comand,id):
        comanddict = {
			'begin': self.msgMAINMENU,
			'lastcrit': self.msgLASTCRIT,
			'listmachine': self.msgLISTMACHINE,
			'grafic': self.msgGRAFIC,
			'backwelcome':self.msgWELCOME,
			'backtomain': self.msgMAINMENU,
			'mototime':self.msgMOTOTIME,
			'chanel': self.msgCHANEL,
			'plc': self.msgPLC,
			'backtolistmachine': self.msgLISTMACHINE

			}

        if len(id)>1:
            com = comanddict[comand]
            return com 

        if comand == 'plc'or comand == 'chanel' or comand == 'mototime':
        	self.getAnswer(comand,id)
            
        com = comanddict[comand]
        return com 


  









m = MessageBuild()
print(m.getcomand('plc','6'))
print(m.getAnswer('chanel','3'))



