# Generated by Django 2.0.5 on 2018-12-11 21:55

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('secretSanta', '0002_customuser_secret_santa_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='secret_santa_of',
            field=encrypted_model_fields.fields.EncryptedCharField(null='True'),
        ),
    ]
