# Generated manually to convert hidden field data from 'N'/'Y' to boolean

from django.db import migrations


def convert_hidden_to_boolean(apps, schema_editor):
    """Convert hidden field from 'N'/'Y' strings to boolean values"""
    Todo = apps.get_model('todo', 'Todo')
    for todo in Todo.objects.all():
        if hasattr(todo, 'hidden'):
            # Convert 'Y' to True, anything else to False
            todo.hidden = (todo.hidden == 'Y')
            todo.save()


def reverse_convert_hidden_to_string(apps, schema_editor):
    """Reverse conversion from boolean to 'N'/'Y' strings"""
    Todo = apps.get_model('todo', 'Todo')
    for todo in Todo.objects.all():
        if hasattr(todo, 'hidden'):
            # Convert True to 'Y', False to 'N'
            todo.hidden = 'Y' if todo.hidden else 'N'
            todo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_hidden'),  # Run before the field type change
    ]

    operations = [
        migrations.RunPython(
            convert_hidden_to_boolean,
            reverse_convert_hidden_to_string,
        ),
    ]