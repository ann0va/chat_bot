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

(START,
 AFTER_YES,
 CATEGORY_SELECTED,
 PLEASURE_MANN,
 PLEASURE_WOMAN,
 ERECTION,
 ERECTION_SELECTED,
 INCREASE_SIZE,
 ANAL_PLEASURE_SELECTED,
 MAIN_MENU) = range(10)


async def start(update: Update, _context) -> int:
    reply_keyboard = [["Так", "Ні"]]

    await update.message.reply_text(
        "Вітаю! Я твій особистий консультант у світі задоволень. Почнемо з простого питання:\n\n"
        "Тобі більше 18?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Тобі більше 18?"
        ),
    )

    return START



async def ask_interests(update: Update, _context) -> int:

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
        await update.message.reply_text(
            "Вам ще зарано сюди. Дякуємо за увагу, та чекаємо коли буде 18+!"
        )
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
        return CATEGORY_SELECTED
    elif user_response == "Розкрий свою уяву":
        await update.message.reply_text(
            "Ви обрали 'Розкрий свою уяву'. Поки що ця категорія знаходиться в розробці."
        )
        return ConversationHandler.END  # End the conversation
    elif user_response == "Подбати про здоров'я":
        await update.message.reply_text(
            "Ви обрали 'Подбати про здоров\'я'. Поки що ця категорія знаходиться в розробці."
        )
        return ConversationHandler.END  # End the conversation
    elif user_response == "Придбати подарунки та сертифікати":
        await update.message.reply_text(
            "Ви обрали 'Придбати подарунки та сертифікати'. Поки що ця категорія знаходиться в розробці."
        )
        return ConversationHandler.END  # End the conversation
    elif user_response == "Вихід":
        await cancel(update, context)
        return ConversationHandler.END


async def pleasure_mann(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Чоловік":
        reply_keyboard = [
            ["Підвищення ерекції", "Збільшення розміру пеніса", "Анальне задоволення"],
            ["Головне меню"],
        ]
        await update.message.reply_text(
            "Відмінно! А які конкретні побажання?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True),
            disable_web_page_preview=True,
        )
    return PLEASURE_MANN


async def pleasure_woman(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Жінка":

        reply_keyboard = [
            ["Підвищення інтенсивності оргазмів", "Приємні відчуття", "Подвійна насолода (кліторально-вагінальна зона)",
             "Анальне задоволення"],
            ["Головне меню"],
        ]
        await update.message.reply_text(
            "Відмінно! А які конкретні побажання?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True),
            disable_web_page_preview=True,
        )
    return PLEASURE_WOMAN


async def main_menu(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == 'Головне меню':
        reply_keyboard = [
            ["Відчуйте насолоду", "Розкрий свою уяву"],
            ["Подбати про здоров'я", "Придбати подарунки та сертифікати"],
            ["Вихід"],
        ]
        await update.message.reply_text(
            f"Вітаю, {update.message.from_user.first_name}. Оберіть, будь ласка, опцію:",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True),
            disable_web_page_preview=True,
        )
        return AFTER_YES
    elif user_response == "Вихід":
        await cancel(update, _context)
        return ConversationHandler.END

    return MAIN_MENU

async def cancel(update: Update, _context) -> int:
    user = update.message.from_user
    user_response = update.message.text

    if user_response == "Вихід":
        logger.info("User %s canceled the conversation.", user.first_name)
        await update.message.reply_text(
            "Дякую, що завітали до нас! Сподіваюсь, що ще раз до нас завітаєте!",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END

async def erection(update: Update, _context) -> int:
    user_response = update.message.text
    if user_response == 'Підвищення ерекції':
        reply_keyboard = [
            ["Насадки на член", "Ерекційні кільця"],
            ["Назад", "Головне меню"],
        ]
        await update.message.reply_text(
            "О, це вже серйозно!"
            "\nДля більш стійкої й крутезної ерекції ми маємо декілька варіантів: насадки, ерекційні кільця та ласо."
            "\n Що Ви бажаєте?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return ERECTION


async def erection_selected(update: Update, _context) -> int:
    user_response = update.message.text
    if user_response == "Насадки на член":
        await update.message.reply_text(
            "Насадки на член для подовження – це як підвищення рівня на ваших ігрових ресурсах."
            "\nЗверніть увагу, що насадки можна використовувати"
            " з лубрикантами лише на водній основі та антисептиками без спирту."
            "\nОберіть та дізнайтесь більше за посиланням."
            "\nОсь список рекомендованих товарів: "
        )
    elif user_response == "Ерекційні кільця":
        reply_keyboard = [["Назад", "Головне меню"]]
        await update.message.reply_text(
            "Доктор Крутизна вітає на борту! Давайте розберемося з ерекційними кільцями."
            "\nЗверніть увагу, що ерекційні кільця можна використовувати з лубрикантами "
            "лише на водній основі та антисептиками без спирту."
            "\nОберіть та дізнайтесь більше за посиланням."
            "\nОсь список рекомендованих товарів: ",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
        )

    return ERECTION_SELECTED
async def increase_size(update: Update, _context) -> int:

    user_response = update.message.text
    if user_response == 'Збільшення розміру пеніса':
        reply_keyboard = [
            ["Насадки на член", "Ерекційні кільця"],
            ["Назад", "Головне меню"],
        ]
        await update.message.reply_text(
            "О, це вже серйозно!"
            "\nДля більш стійкої й крутезної ерекції ми маємо декілька варіантів: насадки, ерекційні кільця та ласо."
            "\n Що Ви бажаєте?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
    return INCREASE_SIZE

async def anal_pleasure(update: Update, _context) -> int:

    user_response = update.message.text
    if user_response == 'Анальне задоволення':
        reply_keyboard = [
            ["Анальні кульки, ланцюжки, намиста", "Анальні вібратори", "Анальні пробки",
             "Насадки для подвійного проникнення"],
            ["Назад", "Головне меню"],
        ]
        await update.message.reply_text(
            "А тут ми маємо 'Ворота до Веселощів!'"
            "\nШукаєш анальне задоволення, обери що тебе зараз цікавить?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return ANAL_PLEASURE_SELECTED

async def anal_pleasure_selected(update: Update, _context) -> int:

    user_response = update.message.text
    if user_response == "Анальні кульки, ланцюжки, намиста":
        await update.message.reply_text(
            "Онови свій інтимний 'арсенал'!"
            "\nАнальні кульки, ланцюжки та намиста – ці аксесуари виявляться "
            "кращими друзями під час вашої веселої ігрової вечірки!"
        )
    elif user_response == "Анальні вібратори":
        await update.message.reply_text(
            "Онови свій інтимний 'арсенал'!"
            "\nЯкщо ви налаштовані на вібрації на абсолютно новому рівні, "
            "то анальні вібратори вже чекають, щоб внести справжній 'віу-віу' ефект у ваше життя!"
        )
    elif user_response == "Анальні пробки":
        await update.message.reply_text(
            "Онови свій інтимний 'арсенал'!"
            "\nАнальні пробки – ваш надійний співучасник у пошуках наповненості "
            "та веселощів для постійної або тимчасової стимуляції анусу."
        )
    elif user_response == "Насадки для подвійного проникнення":
        await update.message.reply_text(
            "Онови свій інтимний 'арсенал'!"
            "\nЯкщо ви налаштовані на новий рівень стимуляції, "
            "то насадки для подвійного проникнення готові додати цілу гаму відчуттів "
            "у ваші інтимні моменти."
        )
    return ANAL_PLEASURE_SELECTED
def main() -> None:

    application = Application.builder().token("6462101482:AAHktf763kunhUdcU-sH8_8HUuJU7SdqK4k").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [MessageHandler(filters.Text() & ~filters.COMMAND, ask_interests)],
            AFTER_YES: [
                MessageHandler(filters.Text() & ~filters.COMMAND, category_selected),
                MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_mann),
                MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_woman),
                MessageHandler(filters.Text() & ~filters.COMMAND, erection),
                MessageHandler(filters.Text() & ~filters.COMMAND, main_menu),
            ],
            CATEGORY_SELECTED: [
                MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_mann),
                MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_woman),
                MessageHandler(filters.Text() & ~filters.COMMAND, main_menu),
            ],
            PLEASURE_MANN: [
                MessageHandler(filters.Text() & ~filters.COMMAND, main_menu),
            ],
            PLEASURE_WOMAN: [
                MessageHandler(filters.Text() & ~filters.COMMAND, main_menu),
            ],
            ERECTION: [
                MessageHandler(filters.Text() & ~filters.COMMAND, erection_selected),
            ],
            INCREASE_SIZE: [
                MessageHandler(filters.Text() & ~filters.COMMAND, increase_size),
            ],
            ANAL_PLEASURE_SELECTED: [
                MessageHandler(filters.Text() & ~filters.COMMAND, anal_pleasure_selected),
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
