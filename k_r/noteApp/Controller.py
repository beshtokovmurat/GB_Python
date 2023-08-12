import text
import view
import model
import os

my_noteBook = model.Note(os.path.dirname(__file__)+"\\"+text.note_file_name)

def start():
	while True:
		choice = view.main_menu() # вывод меню и предоставление выбора
		match choice:
			case 1: # Открыть файл +
				my_noteBook.open_note()
				view.print_message(text.load_successful)
			case 2: # Записать файл +
				my_noteBook.save_note()
				view.print_message(text.save_successful)
			case 3: # Показать заметки +
				notes = my_noteBook.get_notes()
				view.print_notes(notes, text.load_error)
			case 4: # Добавить заметку +
				note = view.input_notes(my_noteBook.get_max_id(),
				    text.input_new_note, text.cancel_input)
				title = my_noteBook.add_note(note)
				view.print_message(text.new_note_successful(title)) # type: ignore
			case 5: # Найти заметку +
				word = view.input_search(text.input_search)
				result = my_noteBook.search_notes(word)
				view.print_notes(result, text.empty_search(word))
			case 6: # Изменить заметку
				notes = my_noteBook.get_notes()
				index = view.input_index(text.input_index, notes, text.load_error)
				note = view.input_notes(index,
				    text.input_new_note, text.cancel_input)
				result = my_noteBook.change_notes(note, index)
				view.print_message(text.change_successful(note))
			case 7: # Удалить заметку +
				notes = my_noteBook.get_notes()
				index = view.input_index(
				    text.index_del_note, notes, text.load_error)
				title = my_noteBook.del_note(index)
				view.print_message(text.del_note(title)) # type: ignore
			case 8:
				break
