from alive_progress import alive_bar
from time import sleep

with alive_bar(bar = "smooth", title = "Bots joining", length = 100) as bar:
    count = range(1, 101)
    for count in count:
        bar()
        sleep(.5)
