# Generated by Django 4.1.7 on 2023-04-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_product_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="number",
            new_name="discount",
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]