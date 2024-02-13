import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)

def add_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input('Введите название заметки: ')
    body = input('Введите текст заметки: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {
        'id': note_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно добавлена.')

def edit_note():
    notes = load_notes()
    note_id = int(input('Введите номер заметки, которую нужно изменить: '))
    for note in notes:
        if note['id'] == note_id:
            title = input('Введите новое название заметки: ')
            body = input('Введите новый текст заметки: ')
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print('Заметка успешно изменена.')
            return
    print('Заметка с таким номером не найдена.')

def delete_note():
    notes = load_notes()
    note_id = int(input('Введите номер заметки, которую нужно удалить: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена.')
            return
    print('Заметка не найдена.')

def view_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Timestamp: {note['timestamp']}")
        print('---')

def main():
    while True:
        print('1. Добавить заметку')
        print('2. Изменить заметку')
        print('3. Удалить заметку')
        print('4. Все заметки')
        print('5. Выход из приложения')
        choice = input('Выберите нужное действие : ')

        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            view_notes()
        elif choice == '5':
            break
        else:
            print('Операции под таким номером не существует. Попробуйте снова.')

if __name__ == '__main__':
    main()