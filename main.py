from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import logging
from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

START, AFTER_YES = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with two inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Так", callback_data="yes"),
            InlineKeyboardButton("Ні", callback_data="no"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Вітаю! Я твій особистий консультант у світі задоволень. Почнемо з простого питання:\n \tТобі більше 18?",
        reply_markup=reply_markup)


async def ask_interests(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Shows the next set of options after choosing 'Так'."""
    keyboard = [
        [
            InlineKeyboardButton(text="Відчуйте насолоду", callback_data="pleasure"),
            InlineKeyboardButton(text="Розкрий свою уяву", callback_data="imagination"),
            InlineKeyboardButton(text="Подбати про здоров\'я", callback_data="health"),
            InlineKeyboardButton(text="Придбати подарунки та сертифікати", callback_data="gifts"),
        ],
        [InlineKeyboardButton(text="Вихід", callback_data="no")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.edit_message_text("Вітаю! Оберіть, будь ласка, опцію:", reply_markup=reply_markup,
                                                  disable_web_page_preview=True)


async def category_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the selected category button."""
    query = update.callback_query
    query.answer()

    category_data = query.data  # This will contain 'pleasure', 'imagination', etc.

    # You can use category_data to determine which category button was selected and perform appropriate actions.
    if category_data == "pleasure":
        await query.edit_message_text("Ви обрали 'Відчуйте насолоду'. Оберіть опцію:  ")

        keyboard = [
            [
                InlineKeyboardButton(text="Чоловік", callback_data="pleasure_mann"),
                InlineKeyboardButton(text="Жінка", callback_data="pleasure_woman"),
            ],
            [InlineKeyboardButton(text="Назад", callback_data="backword")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Для кого ти шукаєш іграшку цього разу?",
                                      reply_markup=reply_markup, disable_web_page_preview=True)

    elif category_data == "imagination":
        await query.edit_message_text("Ви обрали 'Розкрий свою уяву'.")
    elif category_data == "health":
        await query.edit_message_text("Ви обрали 'Подбати про здоров\'я'.")
    elif category_data == "gifts":
        await query.edit_message_text("Ви обрали 'Придбати подарунки та сертифікати'.")
    elif category_data == "no":
        await query.edit_message_text("Вам ще зарано сюди. Дякуємо за увагу, та чекаємо коли буде 18+!")


async def pleasure_mann(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the selected gender for the pleasure category."""
    query = update.callback_query
    query.answer()

    category_data = query.data
    await query.edit_message_text('Відмінно! А які конкретні побажання?')

    keyboard = [
        [
            InlineKeyboardButton(text="Підвищення ерекції та сексуальної функції для нього",
                                 callback_data="erection"),
            InlineKeyboardButton(text="Збільшення розміру пеніса", callback_data="increase_size"),
            InlineKeyboardButton(text="Анальне задоволення", callback_data="anal_pleasure"),
        ],
        [InlineKeyboardButton(text="Назад", callback_data="backword")],
        [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(
        "Ви обрали категорію 'Підвищення ерекції та сексуальної функції для нього'. Виберіть далі:",
        reply_markup=reply_markup)


async def pleasure_woman(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the selected gender for the pleasure category."""
    query = update.callback_query
    query.answer()

    category_data = query.data

    keyboard = [
        [
            InlineKeyboardButton(text="Підвищення інтенсивності оргазмів", callback_data="orgasm"),
            InlineKeyboardButton(text="Приємні відчуття", callback_data="pleasant_sensations"),
            InlineKeyboardButton(text="Подвійна насолода (кліторально-вагінальна зона)",
                                 callback_data="double_pleasure"),
            InlineKeyboardButton(text="Анальне задоволення", callback_data="anal_pleasure"),
        ],
        [InlineKeyboardButton(text="Назад", callback_data="backword")],
        [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("Відмінно! А які конкретні побажання?",
                                  reply_markup=reply_markup)


async def erection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()

    category_data = query.data

    keyboard = [
            [
                InlineKeyboardButton(text="Насадки на член", callback_data="penis_attachment"),
                InlineKeyboardButton(text="Ерекційні кільця", callback_data="erection_ring"),
            ],
            [InlineKeyboardButton(text="Назад", callback_data="backword")],
            [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.edit_message_text("О, це вже серйозно!", reply_markup=reply_markup,
                                              disable_web_page_preview=True)
    await update.callback_query.edit_message_text(
        "Для більш стійкої й крутезної ерекції ми маємо декілька варіантів: насадки, ерекційні кільця та ласо.",
        reply_markup=reply_markup, disable_web_page_preview=True)
    await update.callback_query.edit_message_text(
            "Що Ви бажаєте?", reply_markup=reply_markup, disable_web_page_preview=True)


async  def penis_attachment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()

    category_data = query.data

    await query.edit_message_text("O, це як турборежим для члена!")
    await query.edit_message_text("Насадки на член для подовження – це як підвищення рівня на ваших ігрових ресурсах.")
    await query.edit_message_text(
        "Зверни увагу, що насадки можна використовувати з лубрикантами лише на водній основі та антисептиками без спирту.")
    await query.edit_message_text("Ось список рекомендованих товарів:")
    await query.edit_message_text("Оберіть та дізнайтесь більше за посиланням.")

async def erection_ring(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()

    await query.edit_message_text("Доктор Крутизна вітає на борту! Давайте розберемося з ерекційними кільцями.")
    await query.edit_message_text("Давайте розберемося з ерекційними кільцями.")
    await query.edit_message_text(
        "Зверни увагу, що ерекційні кільця можна використовувати з лубрикантами лише на водній основі та антисептиками без спирту.")
    await query.edit_message_text("Ось список рекомендованих товарів:")


async def anal_pleasure(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()
    category_data = query.data

    keyboard = [
        [
            InlineKeyboardButton(text="Анальні кульки, ланцюжки, намиста", callback_data="anal_equipment"),
            InlineKeyboardButton(text="Анальні вібратори", callback_data="anal_vibrators"),
            InlineKeyboardButton(text="Анальні пробки", callback_data="anal_plugs"),
            InlineKeyboardButton(text="Насадки для подвійного проникнення", callback_data="double_penetration"),
        ],
        [InlineKeyboardButton(text="Назад", callback_data="backword")],
        [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("А тут ми маємо 'Ворота до Веселощів!'")
    await query.message.edit_text("Шукаєш анальне задоволення, обери що тебе зараз цікавить?", reply_markup=reply_markup)


async def orgasm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()
    category_data = query.data

    await query.message.edit_text(
        "Для досягнення інтенсивних оргазмів ми маємо особливий рецепт: виберіть рекомендовану іграшку і додайте до нього лубриканти та той-клінери на водній основі.")
    keyboard = [
        [InlineKeyboardButton(text="Віброкульки та Віброяйця", callback_data="vibrating_balls")],
        [InlineKeyboardButton(text="Назад", callback_data="backword")],
        [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("Обери те, що тебе зараз цікавить?", reply_markup=reply_markup)


async def pleasant_sensations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()
    category_data = query.data

    await query.message.edit_text(
        "Для досягнення приємних відчуттів ми маємо особливий рецепт: виберіть рекомендовану іграшку і додайте до нього лубриканти та той-клінери на водній основі.")
    keyboard = [
        [InlineKeyboardButton(text="Вібромасажер", callback_data="vibrating_massage")],
        [InlineKeyboardButton(text="Вібротруски", callback_data="vibrating_pants")],
        [InlineKeyboardButton(text="Назад", callback_data="backword")],
        [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("Обери те, що тебе зараз цікавить?", reply_markup=reply_markup)


async def double_pleasure(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()
    category_data = query.data
    await query.message.edit_text(
        "Для досягнення відчуття 'подвійної насолоди' ми маємо особливий рецепт: виберіть рекомендовану іграшку і додайте до нього лубриканти та той-клінери на водній основі.")
    keyboard = [
        [InlineKeyboardButton(text="Вібратори та трастери", callback_data="vibrating_trastor")],
        [InlineKeyboardButton(text="Назад", callback_data="backword")],
        [InlineKeyboardButton(text="Головне меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("Обери те, що тебе зараз цікавить?", reply_markup=reply_markup)



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:

    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6462101482:AAHktf763kunhUdcU-sH8_8HUuJU7SdqK4k").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(ask_interests, pattern="^yes$"))
    application.add_handler(CallbackQueryHandler(category_selected, pattern="^(pleasure|imagination|health|gifts|no)$"))
    application.add_handler(CallbackQueryHandler(pleasure_mann, pattern="^pleasure_mann$"))
    application.add_handler(CallbackQueryHandler(pleasure_woman, pattern="^pleasure_woman$"))
    application.add_handler(CallbackQueryHandler(erection, pattern="^erection$"))
    application.add_handler(CallbackQueryHandler(penis_attachment, pattern="^penis_attachment"))
    application.add_handler(CallbackQueryHandler(erection_ring, pattern="^erection_ring"))
    application.add_handler(CallbackQueryHandler(anal_pleasure, pattern="^anal_pleasure"))
    application.add_handler(CallbackQueryHandler(orgasm, pattern="^orgasm$"))
    application.add_handler(CallbackQueryHandler(pleasant_sensations, pattern="^pleasant_sensations$"))
    application.add_handler(CallbackQueryHandler(double_pleasure, pattern="^double_pleasure$"))

    application.add_handler(CallbackQueryHandler(help_command, pattern="^help$"))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()