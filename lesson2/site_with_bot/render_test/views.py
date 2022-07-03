from django.dispatch import receiver
from django.views.generic import ListView
from django.shortcuts import render
import random
from django.views.generic import View, TemplateView

from render_test.models import SampleModel
from aiogram import Bot, Dispatcher, types
import logging
from json import dumps
import asyncio
import concurrent


API_TOKEN = '5197569075:AAF8LJsBY1Eu4_MkkJ4ZPQ1tLaUti-_8cBE'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



def first_page(request):
    return render(request, 'home.html', {})
    
def web_tech(request):
    var = random.randrange(-10000, 10000)
    string = ''.join([chr(i) for i in [random.randrange(65, 122) for i in range(200)]])
    return render(request, 'web_tech.html', 
    {"random": var,
    "string": string})
    

class SampleModelView(ListView):
    model = SampleModel
    context_object_name = 'samples'
    template_name='class_view_test.html'

class AiogramTesting(TemplateView):
    template_name = "aiogram_testing.html"


def send(receiver, message, buttons={}):
        async def send_to_telegram():

            keyboard = types.InlineKeyboardMarkup(row_width=3)
            keyboard.add(*buttons)
            message = " "
            await bot.send_message(receiver, message, reply_markup=buttons, parse_mode=types.ParseMode.HTML)

        async def main():
            synchronous_property()

        pool = concurrent.futures.ThreadPoolExecutor()

        def synchronous_property():
            pool.submit(asyncio.run, send_to_telegram()).result()

        asyncio.run(main())


class AjaxSendingMessageView(View):

    def get(self, request, *args, **kwargs):
        message = self.request.GET.get("message")
        receiver = self.request.GET.get("receiver")
        send(message, receiver)

    def post(self, request, *args, **kwargs):
        message = self.request.POST.get("message")
        receiver = self.request.POST.get("receiver")

