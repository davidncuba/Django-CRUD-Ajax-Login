# Generated by Django 3.2.2 on 2021-05-13 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_name'),
        ('transactions', '0005_auto_20210513_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='delivered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
        ),
    ]
