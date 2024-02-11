class Regulator(object):

    def __init__(self, model, look):
        self.model = model
        self.look = look

    def show_notes(self):
        notes = self.model.read_notes()
        self.look.show_number_point_list(notes)

    def show_note(self, note_id):
        try:
            note = self.model.read_note(note_id)
            self.look.show_note(note)
        except ValueError:
            self.look.display_note_id_not_exist(note_id)

    def create_note(self, note):
        self.model.create_note(note)
        self.look.display_note_stored()

    def update_note(self, note_id, note):
        self.model.update_note(note_id, note)
        self.look.display_note_updated(note_id)

    def delete_note(self, note_id):
        try:
            self.model.delete_note(note_id)
            self.look.display_note_deletion(note_id)
        except ValueError:
            self.look.display_note_id_not_exist(note_id)

    def delete_all_notes(self):
        self.model.delete_all_notes()
        self.look.display_all_notes_deletion()

    def notes_exist(self):
        notes = self.model.read_notes()
        if len(notes) == 0:
            self.look.show_empty_list_message()
            return False
        else:
            return True

    def note_id_exist(self, search_id):
        notes = self.model.read_notes()
        for note in notes:
            if note.note_id == search_id:
                return True
        else:
            self.look.display_note_id_not_exist(search_id)
            return False