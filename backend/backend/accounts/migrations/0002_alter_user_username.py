from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def null_usernames_to_blank(
    apps: StateApps,
    _schema_editor: BaseDatabaseSchemaEditor,
) -> None:
    """Replace NULL usernames so the column can become NOT NULL."""
    user_model = apps.get_model("accounts", "User")
    user_model.objects.filter(username__isnull=True).update(username="")


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(null_usernames_to_blank, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
