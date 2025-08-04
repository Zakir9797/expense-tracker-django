from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('expense', 'Expense'), ('income', 'Income')], max_length=7)),
                ('category', models.CharField(max_length=100)),
                ('unit_price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('total_amount', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=200)),
                ('currency', models.CharField(default='₸', max_length=5)),
            ],
        ),
    ]