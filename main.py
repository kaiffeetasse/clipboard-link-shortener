import win32clipboard
import time
import requests
from django.core.validators import URLValidator
from win10toast import ToastNotifier
from dotenv import load_dotenv
import os


def set_cb_data(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()


def get_cb_data():
    win32clipboard.OpenClipboard()
    current_clipboard_data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return current_clipboard_data


def cb_checker():
    current_clipboard_data = get_cb_data()
    last_clipboard_data = current_clipboard_data

    val = URLValidator()
    toaster = ToastNotifier()

    link = ""

    while True:

        current_clipboard_data = get_cb_data()

        if current_clipboard_data != last_clipboard_data and current_clipboard_data != link:
            print("new cb data: " + current_clipboard_data)

            try:
                val(current_clipboard_data)
                r = requests.post(os.getenv("KUTT_URL"),
                                  data={'target': current_clipboard_data},
                                  headers={'X-API-KEY': os.getenv("KUTT_API_KEY")})

                link = r.json()['link']
                set_cb_data(link)
                print("short URL: " + link)
                toaster.show_toast("Short URL pasted to clipboard", link)
            except:
                toaster.show_toast("Error in creating short URL", current_clipboard_data)

            last_clipboard_data = current_clipboard_data

        time.sleep(1)


if __name__ == "__main__":
    load_dotenv()
    cb_checker()
