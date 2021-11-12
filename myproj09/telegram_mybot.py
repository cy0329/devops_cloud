import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요.", file=sys.stderr)
    sys.exit(1)  # 종료 상탯값을 1로 지정하고, 프로그램 종료

token = TELEGRAM_TOKEN
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수.
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text="왜 또 뭐 왜")


def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [
        tasks.get_current_lotto_numbers,
        tasks.ya,
        tasks.naver_search,
        tasks.time,
        tasks.WAYD,
        tasks.calsel,
        tasks.mulcal,
        tasks.mulcal2,
        tasks.pluscal,
        tasks.pluscal2,
        tasks.weather,
    ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
    else:
        response_text = "뭐라는겨"

    # tasks.get_current_lotto_numbers.check_available()
    # tasks.get_current_lotto_numbers.make_response()
    #
    #
    # if tasks.ya.check_available(received_text):
    #     response_text = tasks.ya.make_response(received_text)
    #
    # elif tasks.naver_search.check_available(received_text):
    #     response_text = tasks.naver_search.make_response(received_text)
    #
    # elif tasks.weather.check_available(received_text):
    #     response_text = tasks.weather.make_response(received_text)
    #
    # elif tasks.calsel.check_available(received_text):
    #     response_text = tasks.calsel.make_response(received_text)
    #
    # elif tasks.pluscal.check_available(received_text):
    #     response_text = tasks.pluscal.make_response(received_text)
    #
    # elif tasks.pluscal2.check_available(received_text):
    #     response_text = tasks.pluscal2.make_response(received_text)
    #
    # elif tasks.mulcal.check_available(received_text):
    #     response_text = tasks.mulcal.make_response(received_text)
    #
    # elif tasks.pluscal2.check_available(received_text):
    #     response_text = tasks.pluscal2.make_response(received_text)
    #
    # elif tasks.WAYD.check_available(received_text):
    #     response_text = tasks.WAYD.make_response(received_text)
    #
    # elif tasks.time.check_available(received_text):
    #     response_text = tasks.time.time_sleep(received_text)
    #
    # else:
    #     response_text = "뭐라는겨~"

    # def handler(update, context):
    #     user_text = update.message.text
    #     if "계산" in user_text:
    #         #계산 기능은 실패
    # if received_text == "야":
    #     reply_text = "왜"
    # elif received_text.startswith("네이버 검색:"):
    #     query = received_text[7:]
    #     post_list = tasks.naver_search(query)
    #     # TODO: 응답 문자열을 생성해야함
    #     reply_text = ""
    #     for post in post_list:
    #         reply_text += post["title"] + "\n"
    # else:
    #     reply_text = "뭐라는겨"
    #
    # # tasks.naver_search(query)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

print("Started bot ...")

updater.start_polling()
updater.idle()


# bot = telegram.Bot(token)
# info = bot.getMe()
# pprint.pprint(info)
# resp = bot.getUpdates()
# pprint.pprint(resp)
#
# chat_id =
# bot.sendMessage(chat_id=chat_id, text="안녕. 나는 봇이야!!!")
