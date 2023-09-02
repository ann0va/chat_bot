# LoveSpace UA Bot

## Introduction

LoveSpace UA Bot is a Telegram bot designed to provide information and assistance related to intimate products and experiences. 
This bot offers various features and functionalities for users interested in enhancing their intimate life.

## Features

- Age Verification: Ensures users are 18 years or older before proceeding.
- Product Categories: Categorizes intimate products for men and women.
- Product Recommendations: Provides recommendations based on user preferences.
- Health Tips: Offers tips for maintaining a healthy intimate life.
- Gift Shopping: Helps users find gifts and certificates.

## Technologies Used

- Python: The core programming language used to develop the bot.
- Telegram Bot API: Used to interact with Telegram and handle user messages.
- SQLite: A lightweight, embedded relational database used for data storage.

## Getting Started

To run the LoveSpace UA Bot locally or deploy it to a server, follow these steps:

1. Clone this repository to your local machine.
2. Create a virtual environment (optional but recommended).
3. Create a .env file in the project directory and set your Telegram bot token.
   BOT_TOKEN=your_bot_token_here
4. Create an SQLite database named bot_database.db in the project directory.
5. You can use a SQLite management tool like DB Browser for SQLite to manage the database schema and data.
6. Run the bot:
   python chat_bot.py
   
## Database Schema
The SQLite database (bot_database.db) used in this project follows the following schema:

    users: Stores user information, including their Telegram user ID and age verification status.
    product_categories: Contains product category information.
    products: Stores information about intimate products, including their names, descriptions, and categories.
    preferences: Stores user preferences for product recommendations.
    gifts: Contains gift and certificate details.
    Add more tables as needed for your specific use cases.
