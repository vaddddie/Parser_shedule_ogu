from parser_lib.shedule import get_shedule

# Код объекта распиания:
# 1 - Студент
# 2 - Преподаватель
# 3 - Аудитория
#
# Все остальные коды можно посмотреть на сайте
# -> http://www.osu.ru/pages/schedule/ <-
#

if __name__ == '__main__':
    shedule = get_shedule(
        object_type=2,         # Код объекта расписания
        faculty=5220,          # Код факультета
        departament=5230,      # Код кафедры
        teacher=76789          # Код преподавателя
    )

    with open("output.txt", "w") as file:
        for key in shedule:
            file.write(str(key) + ': ' + str(shedule[key]) + '\n')
