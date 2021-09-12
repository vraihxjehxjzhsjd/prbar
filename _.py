from alive_progress import alive_bar

with alive_bar(20, bar='classic', title='Тест", length=20) as bar:
    count = range(1, 21)
    for count in count:
        print(f"[{coun}] sended.")
        bar()
