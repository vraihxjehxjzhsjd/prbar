from alive_progress import alive_bar
from time import sleep

with alive_bar(100, bar = "smooth", title = "Bots joining") as bar:
    count = range(1, 101)
    for count in count:
        bar()
        sleep(.5)
