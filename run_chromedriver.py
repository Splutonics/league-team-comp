import os
import psutil


def run_chromedriver():

    if "chromedriver.exe" in (i.name() for i in psutil.process_iter()):
        print('chromedriver already running')
    else:
        print('starting chromedriver')
        os.startfile('chromedriver.exe')


if __name__ == '__main__':
    run_chromedriver()
