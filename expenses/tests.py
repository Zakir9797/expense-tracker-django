from django.test import TestCase
from .models import Entry

class EntryModelTest(TestCase):
    def test_create_expense_entry(self):
        entry = Entry.objects.create(
            type='expense',
            category='Food',
            unit_price=100,
            quantity=2,
            total_amount=200,
            description='Lunch',
            currency='$'
        )
        self.assertEqual(entry.total_amount, 200)
        self.assertEqual(entry.type, 'expense')
        self.assertEqual(str(entry), f"{entry.date} {entry.time} | expense | Food | 200$")

    def test_create_income_entry(self):
        entry = Entry.objects.create(
            type='income',
            category='Salary',
            unit_price=500,
            quantity=1,
            total_amount=500,
            description='August',
            currency='$'
        )
        self.assertEqual(entry.type, 'income')
        self.assertEqual(entry.category, 'Salary')


