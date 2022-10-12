import write_data as wd
import read_data as rd
import delete_data as dd
import log


def ask_user():
    choice = input('"w" for import, "r" for export, "d" for delete: ')
    if choice == 'w':
        log.write_log(wd.get_data(), choice)
    elif choice == 'r':
        log.write_log(rd.find_data(), choice)
    elif choice == 'd':
        log.write_log(dd.delete_data(), choice)
    else:
        print('wrong input')
