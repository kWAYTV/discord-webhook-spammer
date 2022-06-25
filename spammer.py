import colorama, os , time, requests, pyfiglet, json
from requests.structures import CaseInsensitiveDict
from colorama import Fore, Back, Style
from colorama import init

logo = pyfiglet.figlet_format("WEBHOOK SPAMMER")
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def create_config():
    try:
        with open("config.json") as f:
            config = json.load(f)
    except FileNotFoundError:
        with open("config.json", "w") as f:
            config = {
                "message": "empty",
                "webhook": "empty",
                "amount": "empty",
                "delay": "empty"
            }
            json.dump(config, f)
    return config

count = 0
def rCount():
    count = 0

create_config()
with open("config.json", "r") as config_file:
        config = json.load(config_file)
        message = config["message"]
        webhook = config["webhook"]
        amount = config["amount"]
        delay = config["delay"]

def check_config():
    global message, amount, webhook, delay
    if message == "empty":
        clear()
        print("\n" + Fore.CYAN + "["+ Fore.RESET + "Input"+ Fore.CYAN + "]" + Fore.RESET + " Please" + Fore.MAGENTA + " type " + Fore.RESET +  "the message to spam: ")
        message = input()
        print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " Successfully added" + Fore.MAGENTA + f" {message} " + Fore.RESET + "as message.")
    if webhook == "empty":
        clear()
        print("\n" + Fore.CYAN + "["+ Fore.RESET + "Input"+ Fore.CYAN + "]" + Fore.RESET + " Please" + Fore.MAGENTA + " type " + Fore.RESET +  "the webhook link: ")
        webhook = input()
        print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " Successfully added" + Fore.MAGENTA + Fore.RESET + f" {webhook} as webhook.")
    if amount == "empty":
        clear()
        print("\n" + Fore.CYAN + "["+ Fore.RESET + "Input"+ Fore.CYAN + "]" + Fore.RESET + " How" + Fore.MAGENTA + " many " + Fore.RESET +  "messages do you want to send: ")
        amount = input()
        print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " We will try to send" + Fore.MAGENTA +  f" {amount} "+ Fore.RESET +"messages.")
        amount = int(amount)
    if delay == "empty":
        clear()
        print("\n" + Fore.CYAN + "["+ Fore.RESET + "Input"+ Fore.CYAN + "]" + Fore.RESET + " How long do you want to wait between messages: ")
        delay = input()
        print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " We will wait" + Fore.MAGENTA + f" {delay} " + Fore.RESET + "seconds between messages.")
        delay = int(delay)
    clear()

def spam(message, webhook):
    global count, amount, delay
    while count < amount:
        try:
            data = requests.post(webhook, json={'content': message})
            time.sleep(1)
            if data.status_code == 204:
                print(Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " Sent message with content: " + Fore.MAGENTA +  f"{message}" + Fore.RESET +".")
                count += 1
                os.system(f"title Webhook Spammer - {count} messages sent. - Press CTRL + C or close at anytime to stop.")
                time.sleep(delay)
                print(Fore.YELLOW + "["+ Fore.RESET + "Sleep"+ Fore.YELLOW + "]" + Fore.RESET + " Waiting " + Fore.MAGENTA + f"{delay} " + Fore.RESET + "seconds before sending next message.")
        except:
            clear()
            print("\n" + Fore.RED + "["+ Fore.RESET + "Error" + Fore.RED + "]" + Fore.RESET + " Response from server: " + str(data.status_code))
            print("\n" + Fore.RED + "["+ Fore.RESET +"Error" + Fore.RED + "]" + Fore.RESET + " Wrong webhook: " + Fore.RESET + webhook)
            print("\n" + Fore.RED + "["+ Fore.RESET +"Error" + Fore.RED + "]" + Fore.RESET + " Exiting..." + Fore.RESET)
            time.sleep(3)
            exit()
    if count == amount:
        clear()
        print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " Successfully sent" + Fore.MAGENTA + f" {amount} " + Fore.RESET + "messages!")
        print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " Exiting...")
        time.sleep(3)
        exit()

def start():
    clear()
    os.system(f"title Webhook Spammer - Checking config...")
    print("\n" + Fore.YELLOW + "["+ Fore.RESET + "Check"+ Fore.YELLOW + "]" + Fore.RESET + " Checking config...")
    time.sleep(1)
    check_config()
    os.system(f"title Webhook Spammer - Starting...")
    print("\n" + Fore.GREEN + "["+ Fore.RESET + "OK"+ Fore.GREEN + "]" + Fore.RESET + " Starting...")
    time.sleep(1)
    clear()
    os.system(f"title Webhook Spammer - Started!")
    print(logo + Fore.BLUE +"\nhttps://github.com/kWAYTV\n\n" + Fore.RESET)
    rCount()
    global message, webhook, amount, delay
    spam(message, webhook)

start()