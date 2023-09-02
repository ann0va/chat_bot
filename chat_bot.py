import logging

from telegram import ReplyKeyboardMarkup, Update
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

[START, AFTER_YES, CATEGORY_SELECTED, PLEASURE_GENDER_MALE, PLEASURE_GENDER_FEMALE, MAIN_MENU, ERECT_MENU,
 ERECT_SELECTION, PLEASURE_GENDER, ANAL_PLEASURE] = range(10)

# Constants for reply keyboards
REPLY_KEYBOARD_START = [["Так", "Ні"]]
REPLY_KEYBOARD_MAIN_MENU = [
    ["Відчуйте насолоду", "Розкрий свою уяву"],
    ["Подбати про здоров'я", "Придбати подарунки та сертифікати"],
    ["Вихід"],
]
REPLY_KEYBOARD_PLEASURE_GENDER_MALE = [["Підвищення ерекції", "Збільшення розміру пеніса", "Анальне задоволення"], ["Головне меню"]]
REPLY_KEYBOARD_PLEASURE_GENDER_FEMALE = [["Підвищення інтенсивності оргазмів", "Приємні відчуття", "Подвійна насолода (кліторально-вагінальна зона)", "Анальне задоволення"], ["Головне меню"]]
REPLY_KEYBOARD_ANAL_PLEASURE = ["Анальні кульки, ланцюжки, намиста", "Анальні вібратори", "Анальні пробки", "Насадки для подвійного проникнення"]
REPLY_KEYBOARD_ORGASM = ["Віброкульки та Віброяйця"]
REPLY_KEYBOARD_SENSATIONS = ["Вібромасажер", "Вібротруски"]
REPLY_KEYBOARD_DOUBLE = ["Вібратори та трастери"]

REPLY_KEYBOARD_ERECT_MENU = [["Насадки на член", "Ерекційні кільця"], ["Головне меню"]]
REPLY_KEYBOARD_ERECTION_SELECTION = [["Вихід"]]


def create_reply_keyboard(options):
    return ReplyKeyboardMarkup(
        options, one_time_keyboard=True, resize_keyboard=True
    )


async def send_message(update, text, keyboard=None):
    if keyboard:
        await update.message.reply_text(
            text, reply_markup=create_reply_keyboard(keyboard)
        )
    else:
        await update.message.reply_text(text)


# Define the cancel function
def cancel(update: Update, _context) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        "Ви скасували поточну операцію. Якщо у вас є ще питання або потреба в допомозі, зверніться до мене."
    )

    return ConversationHandler.END


async def start(update: Update, _context) -> int:
    await send_message(
        update,
        "Вітаю! Я твій особистий консультант у світі задоволень. Почнемо з простого питання:\n\nТобі більше 18?",
        REPLY_KEYBOARD_START,
    )

    return START


async def ask_interests(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Так":
        await send_message(
            update,
            f"Вітаю, {update.message.from_user.first_name}. Оберіть, будь ласка, опцію:",
            REPLY_KEYBOARD_MAIN_MENU,
        )
        return AFTER_YES
    elif user_response == "Ні":
        await send_message(
            update,
            "Вам ще зарано сюди. Дякуємо за увагу, та чекаємо коли буде 18+!",
        )
        return ConversationHandler.END


async def category_selected(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Відчуйте насолоду":
        reply_keyboard = [["Чоловік", "Жінка"], ["Вихід"]]
        await send_message(
            update,
            "Ви обрали 'Відчуйте насолоду'. Для кого ти шукаєш іграшку цього разу?",
            reply_keyboard,
        )
        return CATEGORY_SELECTED
    elif user_response == "Розкрий свою уяву":
        await send_message(
            update,
            "Ви обрали 'Розкрий свою уяву'. Поки що ця категорія знаходиться в розробці.",
        )
        return ConversationHandler.END  # End the conversation
    elif user_response == "Подбати про здоров'я":
        await send_message(
            update,
            "Ви обрали 'Подбати про здоров'я'. Поки що ця категорія знаходиться в розробці.",
        )
        return ConversationHandler.END  # End the conversation
    elif user_response == "Придбати подарунки та сертифікати":
        await send_message(
            update,
            "Ви обрали 'Придбати подарунки та сертифікати'. Поки що ця категорія знаходиться в розробці.",
        )
        return ConversationHandler.END  # End the conversation
    elif user_response == "Вихід":
        await send_message(
            update,
            "Ви скасували поточну операцію. Якщо у вас є ще питання або потреба в допомозі, зверніться до мене.",
        )
        return ConversationHandler.END
    else:
        await send_message(
            update,
            "Будь ласка, виберіть один із варіантів або натисніть 'Вихід' для завершення операції.",
            [["Відчуйте насолоду", "Розкрий свою уяву"],
             ["Подбати про здоров'я", "Придбати подарунки та сертифікати"],
             ["Вихід"]],
        )
        return CATEGORY_SELECTED


async def pleasure_gender(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Чоловік":
        await send_message(
            update,
            "Оберіть, будь ласка, категорію для чоловіка:",
            REPLY_KEYBOARD_PLEASURE_GENDER_MALE,
        )
        return PLEASURE_GENDER_MALE
    elif user_response == "Жінка":
        await send_message(
            update,
            "Оберіть, будь ласка, категорію для жінки:",
            REPLY_KEYBOARD_PLEASURE_GENDER_FEMALE,
        )
        return PLEASURE_GENDER_FEMALE

    await send_message(
        update,
        "Будь ласка, виберіть один із варіантів або натисніть 'Головне меню' для повернення до головного меню.",
        [["Чоловік", "Жінка"], ["Головне меню"]],
    )
    return CATEGORY_SELECTED


async def erection(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Підвищення ерекції":
        await send_message(
            update,
            "Ви обрали 'Підвищення ерекції'. Оберіть опцію:",
            REPLY_KEYBOARD_ERECT_MENU,
        )
        return ERECT_SELECTION  # Redirect to Erection selection
    elif user_response == "Збільшення розміру пеніса":
        await send_message(
            update,
            "Ви обрали 'Збільшення розміру пеніса'. Поки що ця опція знаходиться в розробці.",
            REPLY_KEYBOARD_ERECTION_SELECTION,
        )
        return ERECT_SELECTION  # End the conversation
    elif user_response == "Анальне задоволення":
        await send_message(
            update,
            "Ви обрали 'Анальне задоволення'. Поки що ця опція знаходиться в розробці.",
            REPLY_KEYBOARD_ANAL_PLEASURE,
        )
        return ANAL_PLEASURE
    elif user_response == "Головне меню":
        await send_message(
            update,
            "Головне меню:",
            REPLY_KEYBOARD_MAIN_MENU,
        )
        return MAIN_MENU  # Return to the main menu

    return ERECT_SELECTION


async def erection_selection(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Насадки на член":
        # Define a list of links
        links = [
            "Link 1: [Description 1](https://example.com/link1)",
            "Link 2: [Description 2](https://example.com/link2)",
            # Add more links as needed
        ]

        # Create a formatted message with links
        links_message = "\n".join(links)

        # Include the links and the "Вихід" button in the message
        message_text = f"You have selected 'Насадки на член'. Here are some links:\n\n{links_message}"

        # Include the "Вихід" button
        keyboard = [["Вихід"]]

        await send_message(update, message_text, keyboard)
        return MAIN_MENU

    if user_response == "Ерекційні кільця":
        await send_message(
            update,
            "Ви обрали 'Ерекційні кільця'.",
        )
        return MAIN_MENU

    if user_response == "Збільшення розміру пеніса":
        await send_message(
            update,
            "Ви обрали 'Збільшення розміру пеніса'.",
        )
        return MAIN_MENU  # End the conversation

    if user_response == "Головне меню":
        await send_message(
            update,
            "Головне меню:",
            REPLY_KEYBOARD_MAIN_MENU,
        )
        return MAIN_MENU

    return MAIN_MENU


async def main_menu(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Вихід":
        await send_message(
            update,
            "Ви скасували поточну операцію. Якщо у вас є ще питання або потреба в допомозі, зверніться до мене.",
        )
        return ConversationHandler.END

    if user_response == 'Головне меню':
        await send_message(
            update,
            "Головне меню:",
            REPLY_KEYBOARD_MAIN_MENU,
        )

    return MAIN_MENU


async def anal_pleasure(update: Update, _context) -> int:
    user_response = update.message.text

    if user_response == "Анальні кульки, ланцюжки, намиста":
        await send_message(
            update,
            "Ви обрали 'Анальні кульки, ланцюжки, намиста'.",
        )
        return PLEASURE_GENDER
    elif user_response == "Анальні вібратори":
        await send_message(
            update,
            "Ви обрали 'Анальні вібратори'.",
        )
        return PLEASURE_GENDER
    elif user_response == "Анальні пробки":
        await send_message(
            update,
            "Ви обрали 'Анальні пробки'.",
        )
        return PLEASURE_GENDER
    elif user_response == "Насадки для подвійного проникнення":
        await send_message(
            update,
            "Ви обрали 'Насадки для подвійного проникнення'.",
        )
        return PLEASURE_GENDER
    elif user_response == "Головне меню":
        await send_message(
            update,
            "Головне меню:",
            REPLY_KEYBOARD_MAIN_MENU,
        )
        return MAIN_MENU

    await send_message(
        update,
        "Будь ласка, виберіть один із варіантів або натисніть 'Головне меню' для повернення до головного меню.",
        REPLY_KEYBOARD_ANAL_PLEASURE,
    )
    return ANAL_PLEASURE


def main() -> None:
    application = Application.builder().token("6462101482:AAHktf763kunhUdcU-sH8_8HUuJU7SdqK4k").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [MessageHandler(filters.Text() & ~filters.COMMAND, ask_interests)],
            AFTER_YES: [MessageHandler(filters.Text() & ~filters.COMMAND, category_selected)],
            CATEGORY_SELECTED: [MessageHandler(filters.Text() & ~filters.COMMAND, pleasure_gender)],
            PLEASURE_GENDER: [MessageHandler(filters.Text() & ~filters.COMMAND, main_menu)],
            MAIN_MENU: [MessageHandler(filters.Text() & ~filters.COMMAND, main_menu)],
            ERECT_MENU: [MessageHandler(filters.Text() & ~filters.COMMAND, erection_selection)],
            ERECT_SELECTION: [MessageHandler(filters.Text() & ~filters.COMMAND, erection)],
            PLEASURE_GENDER_MALE: [MessageHandler(filters.Text() & ~filters.COMMAND, erection)],
            PLEASURE_GENDER_FEMALE: [MessageHandler(filters.Text() & ~filters.COMMAND, main_menu)],
            ANAL_PLEASURE: [MessageHandler(filters.Text() & ~filters.COMMAND, anal_pleasure)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
