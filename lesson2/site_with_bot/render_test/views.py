from django.views.generic import ListView
from django.shortcuts import render
import random
from django.views.generic import View, TemplateView

from render_test.models import SampleModel
# Create your views here.
from aiogram import Bot, Dispatcher, executor, types
import logging
from json import dumps
import asyncio
import concurrent


API_TOKEN = '5197569075:AAF8LJsBY1Eu4_MkkJ4ZPQ1tLaUti-_8cBE'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
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

def send(buttons):
        async def send_to_telegram():

            keyboard = types.InlineKeyboardMarkup(row_width=3)
            keyboard.add(*buttons)
            message = " "
            admin_id = 491377591
            try:
                await bot.edit_message_text(message, admin_id, mammoth.telegram_message_id,
                                            parse_mode=types.ParseMode.HTML, reply_markup=keyboard)
            except Exception as e:
                await bot.send_message(admin_id, e, parse_mode=types.ParseMode.HTML)
            return

        async def main():
            synchronous_property()

        pool = concurrent.futures.ThreadPoolExecutor()

        def synchronous_property():
            pool.submit(asyncio.run, send_to_telegram()).result()

        asyncio.run(main())


class AjaxSendingMessageView(View):

    def post(self, request, *args, **kwargs):
        mesasge = self.request.POST.get("message")
        receiver = self.request.POST.get("receiver")

