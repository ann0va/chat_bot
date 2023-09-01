import logging
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
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


async def start(update: Update, context) -> None:
    reply_keyboard = [["Так", "Ні"]]

    await update.message.reply_text(
        "Вітаю! Я твій особистий консультант у світі задоволень. Почнемо з простого питання:\n\n"
        "Тобі більше 18?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Тобі більше 18?😏"
        ),
    )

    return START


async def ask_interests(update: Update, context) -> int:
    user_response = update.message.text
    if user_response == "Так":
        reply_keyboard = [
            ["Відчуйте насолоду", "Розкрий свою уяву"],
            ["Подбати про здоров'я", "Придбати подарунки та сертифікати"],
            ["Вихід"],
        ]
        await update.message.reply_text(
            f"Вітаю, {update.message.from_user.first_name}. Оберіть, будь ласка, опцію:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return AFTER_YES
    elif user_response == "Ні":
        await update.message.reply_text("Вам ще зарано сюди. Дякуємо за увагу, та чекаємо коли буде 18+!")
        return ConversationHandler.END


async def category_selected(update: Update, context) -> int:
    user_response = update.message.text

    if user_response == "Відчуйте насолоду":
        reply_keyboard = [
            ["Чоловік", "Жінка"],
            ["Вихід"],
        ]
        await update.message.reply_text(
            "Ви обрали 'Відчуйте насолоду'. Для кого ти шукаєш іграшку цього разу?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return AFTER_YES

    elif user_response == "Розкрий свою уяву":
        await update.message.reply_text("Ви обрали 'Розкрий свою уяву'. Поки що ця категорія знаходиться в розробці.")
    elif user_response == "Подбати про здоров'я":
        await update.message.reply_text("Ви обрали 'Подбати про здоров\'я'. Поки що ця категорія знаходиться в розробці.")
    elif user_response == "Придбати подарунки та сертифікати":
        await update.message.reply_text("Ви обрали 'Придбати подарунки та сертифікати'. Поки що ця категорія знаходиться в розробці.")
    elif user_response == "Вихід":
        await update.message.reply_text("Дякую, що обрали нас!")
        return ConversationHandler.END


async def pleasure_mann(update: Update, context) -> int:
    user_response = update.message.text
    if user_response == "Чоловік":
        reply_keyboard = [
            ["Підвищення ерекції", "Збільшення розміру пеніса", "Анальне задоволення"],
            ["Назад", "Головне меню"],
        ]
        await update.message.reply_text(
            "Відмінно! А які конкретні побажання?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True),
            disable_web_page_preview=True,
        )
        return AFTER_YES


async def pleasure_woman(update: Update, context) -> int:
    user_response = update.message.text
    if user_response == 'Жінка':
        reply_keyboard = [
            ["Підвищення інтенсивності оргазмів", "Приємні відчуття", "Подвійна насолода (кліторально-вагінальна зона)",
             "Анальне задоволення"],
            ["Назад", "Головне меню"],
        ]
        await update.message.reply_text(
            "Відмінно! А які конкретні побажання?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True),
            disable_web_page_preview=True,
        )
        return AFTER_YES


async def main_menu(update: Update, context) -> int:
    user_response = update.message.text
    if user_response == 'Головне меню':
        await ask_interests(update, context)
        return AFTER_YES


async def cancel(update: Update, context) -> int:
    user_response = update.message.text
    if user_response == "Вихід":
        logger.info("User %s canceled the conversation.", update.message.from_user.first_name)
        await update.message.reply_text(
            "Дякую, що завітали до нас! Сподіваюсь, що ще раз до нас завітаєте!",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END


def main() -> None:
    application = Application.builder().token("6462101482:AAHktf763kunhUdcU-sH8_8HUuJU7SdqK4k").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [MessageHandler(filters.Text() & ~filters.COMMAND, ask_interests)],
            AFTER_YES: [
                MessageHandler(filters.Text() & ~filters.COMMAND, ask_interests),
                MessageHandler(filters.Text() & ~filters.COMMAND, category_selected),
                MessageHandler(filters.Text() & ~filters.COMMAND, main_menu),
                MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_mann),
                MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_woman),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
