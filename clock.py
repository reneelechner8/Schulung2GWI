import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    tz_name = os.environ.get('TIMEZONE', 'Europe/Berlin')
    tz = ZoneInfo(tz_name)
    location = tz_name.replace('_', ' ')
    try:
        while True:
            clear_screen()
            now = datetime.now(tz)
            print(f"Datum: {now.strftime('%Y-%m-%d')}")
            print(f"Uhrzeit: {now.strftime('%H:%M:%S')}")
            print(f"Ort: {location}")
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
