from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import *
from urllib.parse import unquote_plus
import json
import os
import slack

import messagebuild
SLACK_BOT_TOKEN = '###############################' #ваш токен
second_SLACK_BOT_TOKEN = '#######################################' #ваш токен

slack_client = slack.WebClient(second_SLACK_BOT_TOKEN)

def index(request):
    if request.method == 'POST':
       
        a = json.loads(request.POST.get('payload'))
        print(type(a),a)
        print(a['actions'][0]['value'])
        print(a['actions'][0]['block_id'])
        m = messagebuild.MessageBuild()
        
        v = m.getcomand(a['actions'][0]['value'],a['actions'][0]['block_id'])
        response = slack_client.chat_update(

            channel = a['channel']['id'],
            ts = a['message']['ts'],
            text = 'd',
            blocks = v
        )
        #print(m.getcomand(a['actions'][0]['value']))
        assert response["ok"]
        assert response["message"]["text"] == 'd'

    return HttpResponse('',200)
