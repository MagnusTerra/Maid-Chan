import os
import logging
import shutil
import MaidChan.fuctions as md
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()
token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    user_name = update.effective_user.first_name
    await context.bot.send_message(chat_id=chat_id, text=md.text.start_hello(user_name))

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Youtube")

async def upda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if update.message.caption == 'ocr':
        try:
            #Download the img
            folder_name = str(user_id)
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            photo_file = update.message.photo[-1].file_id
            file = await context.bot.get_file(photo_file)
            file_path = os.path.join(folder_name, file.file_unique_id + '.jpg')
            await file.download_to_drive(file_path)
            img_path = file_path
            await context.bot.send_message(chat_id=update.effective_chat.id, text=img_path)

            # OCR the img and send the text to tha chat
            text = md.OCR.manga_ocr(img_path)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        except Exception as e:
            print(e)
        finally:
            shutil.rmtree(folder_name)
    else :
        pass


app = ApplicationBuilder().token(token).build()

#app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("youtube", youtube))
app.add_handler(MessageHandler(filters.PHOTO, upda))

app.run_polling()



if __name__ == "__main__":
     app.run_polling()