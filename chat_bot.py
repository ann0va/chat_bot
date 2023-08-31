import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

START, AFTER_YES = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Так", "Ні"]]

    await update.message.reply_text(
        "Вітаю! Я твій особистий консультант у світі задоволень. Почнемо з простого питання:\n\n"
        "Тобі більше 18?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Тобі більше 18?"
        ),
    )

    return START


async def ask_interests(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [
        ["Відчуйте насолоду", "Розкрий свою уяву"],
        ["Подбати про здоров'я", "Придбати подарунки та сертифікати"],
        ["Вихід"],
    ]

    await update.message.reply_text(
        "Вітаю, {}. Оберіть, будь ласка, опцію:".format(update.message.from_user.first_name),
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )

    return AFTER_YES

async def pleasure_mann(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


   reply_keyboard = [
       ["Підвищення ерекції","Збільшення розміру пеніса",  "Анальне задоволення",]
       ["Назад","Головне меню"]


    ]
   await query.message.edit_text(
        "Відмінно! А які конкретні побажання?",
        reply_markup=reply_markup, disable_web_page_preview=True
    )

async def pleasure_woman(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()

    reply_keyboard = [
        ["Підвищення інтенсивності оргазмів","Приємні відчуття","Подвійна насолода (кліторально-вагінальна зона)","Анальне задоволення"]
        ],
        ["Назад", "Головне меню"],
    ]

    await query.message.edit_text(
        "Відмінно! А які конкретні побажання?",
        reply_markup=reply_markup, disable_web_page_preview=True
    )

def main() -> None:

    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [MessageHandler(filters.Text(equals="Так"), ask_interests)],
            AFTER_YES: [
                MessageHandler(
                    filters.Text(equals="Відчуйте насолоду"), pleasure_option_handler
                ),
                MessageHandler(
                    filters.Text(equals="Розкрий свою уяву"), imagination_option_handler
                ),
                MessageHandler(
                    filters.Text(equals="Подбати про здоров'я"), health_option_handler
                ),
                MessageHandler(
                    filters.Text(equals="Придбати подарунки та сертифікати"),
                    gifts_option_handler,
                ),
                MessageHandler(filters.Text(equals="Вихід"), exit_option_handler),
                # Add more states and corresponding MessageHandlers for each callback data
                MessageHandler(filters.Text(equals="pleasure_mann"), pleasure_mann),
                MessageHandler(filters.Text(equals="pleasure_woman"), pleasure_woman),
                # Add more MessageHandlers for other callback data options
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
