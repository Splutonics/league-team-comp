from tkinter import *
from tkinter import ttk
from lookup_summoner import *
from run_chromedriver import *
import psutil

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


def lookup_action(summoner, level):
    lookup_summoner()


def quit():
    root.destroy()
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == "chromedriver.exe":
            proc.kill()


# button to open chromedriver
ttk.Button(frm, text="Run Chromedriver",
           command=run_chromedriver).grid(column=0, row=0)


summoner_names = ['summoner'+str(i) for i in range(1, 11)]
summoner_levels = ['summoner_level'+str(i) for i in range(1, 11)]
summoner_buttons = ['summoner_button'+str(i) for i in range(1, 11)]

# print(summoner_names)
# print(summoner_levels)

summoner_name_dict = dict()
summoner_level_dict = dict()
summoner_button_dict = dict()

for i, summoner, level, button in zip(range(10), summoner_names, summoner_levels, summoner_buttons):
    ttk.Label(frm, text="Summoner "+str(i+1)+": ").grid(column=0, row=i+1)
    summoner_name_dict[summoner_names[i]] = ttk.Entry(frm)
    summoner_name_dict[summoner_names[i]].grid(column=1, row=i+1)

    summoner_level_dict[summoner_levels[i]] = ttk.Entry(frm)
    summoner_level_dict[summoner_levels[i]].grid(column=2, row=i+1)

    # summoner_button_dict[summoner_buttons[i]] = ttk.Button(frm, text='test'+str(
    #     i+1), command=lambda i=i: print(summoner_level_dict[summoner_levels[i]].get()))
    # summoner_button_dict[summoner_buttons[i]].grid(column=4, row=i+1)

    summoner_button_dict[summoner_buttons[i]] = ttk.Button(frm,
                                                           text="Get Champions",
                                                           command=lambda i=i: lookup_summoner(
                                                               summoner_name_dict[summoner_names[i]].get(), int(summoner_level_dict[summoner_levels[i]].get()))
                                                           )
    summoner_button_dict[summoner_buttons[i]].grid(column=3, row=i+1)
    # ttk.Button(frm,
    #            text="Get Champions",
    #            command=lambda: lookup_summoner(
    #                'thorthepriest', 5)
    #            )

ttk.Label(frm, text="Min Level").grid(column=2, row=0)


# takes input from enty boxes, looks up summoner


ttk.Button(frm, text="Quit", command=quit).grid(column=12, row=12)
root.mainloop()
