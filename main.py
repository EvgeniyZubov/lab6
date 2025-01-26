from lab6_1 import Window1
from lab6_2 import Window2
import tkinter

task_list = {
    "1": (Window1, "Zubov_Yevgeniy Lab6.1", "1024x768"),
    "2": (Window2, "Zubov_Yevgeniy Lab6.1", "1024x768")

}

choice = input("Please, choose the task 1-2 (0-EXIT): ")
while choice != "0":
    # якщо даний ключ є у словнику
    if choice in task_list.keys():
            # Створення відповідного вікна
        application = tkinter.Tk()
        window_class, window_name, window_size = task_list.get(choice)
        window = window_class(application)
        application.geometry(window_size)
        application.title(window_name)
        application.mainloop()
    else:
        print("Wrong task number!")
    choice = input("Please, choose the task again (0-EXIT): ")
