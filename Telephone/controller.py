import model
import view


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Книга открыта')
            case 2:
                model.save_file()
                view.show_message('Книга сохранена')
            case 3:
                view.show_contacts(pb, 'Книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index - 1].get("name")} изменен')
            case 6:
                search = view.input_search('Введите искомое: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контанкты не найдены')
            case 7:
                if view.show_contacts(pb, 'Книга пуста или не открыта'):
                    index = view.input_index('Введите номер удаляемого контакта: ')
                    contact = index
                    model.delete_contact(contact)
                    view.show_message(f'Контакт {model.get_phone_book()[index - 1].get("name")} удален')
            case 8:
                return
