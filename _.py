from alive_progress import alive_bar
from time import sleep

with alive_bar(20, title='Тест') as bar:
    count = range(1, 21)
    for count in count:
        bar()
        print(f"[{count}] sended.")
        sleep(.5)
