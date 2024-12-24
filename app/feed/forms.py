import typing as t
from wtforms import Form, StringField, URLField, SelectField
import wtforms.validators as v

if t.TYPE_CHECKING:
    from app.folder.models import Folder


@t.final
class FeedForm(Form):
    name = StringField('Name', [v.InputRequired(), v.Length(min=2)])
    url = URLField('URL')
    folder_id = SelectField('Folder')

    def set_folders(self, folders: list['Folder']):
        self.folder_id.choices = [('', '———'), *((folder.id, folder.name) for folder in folders)]