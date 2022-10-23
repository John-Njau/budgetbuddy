from django.test import TestCase

from expenses.models import Expense, Category


# Create your tests here.
class ExpenseTestCase(TestCase):
    def setUp(self):
        category1 = Category.objects.create(name="Category1")
        category2 = Category.objects.create(name="Category2")
        category3 = Category.objects.create(name="Category3")
        Expense.objects.create(name="Expense1", amount=100, notes="Notes1", category=category1, date="2020-01-01")
        Expense.objects.create(name="Expense2", amount=200, notes="Notes2", category=category2, date="2020-01-02")
        Expense.objects.create(name="Expense3", amount=300, notes="Notes3", category=category3, date="2020-01-03")

    def test_expense(self):
        expense1 = Expense.objects.get(name="Expense1")
        expense2 = Expense.objects.get(name="Expense2")
        expense3 = Expense.objects.get(name="Expense3")
        self.assertEqual(expense1.amount, 100)
        self.assertEqual(expense2.amount, 200)
        self.assertEqual(expense3.amount, 300)

    def test_category(self):
        category1 = Category.objects.get(name="Category1")
        category2 = Category.objects.get(name="Category2")
        category3 = Category.objects.get(name="Category3")
        self.assertEqual(category1.name, "Category1")
        self.assertEqual(category2.name, "Category2")
        self.assertEqual(category3.name, "Category3")

    def test_expense_category(self):
        expense1 = Expense.objects.get(name="Expense1")
        expense2 = Expense.objects.get(name="Expense2")
        expense3 = Expense.objects.get(name="Expense3")
        self.assertEqual(expense1.category.name, "Category1")
        self.assertEqual(expense2.category.name, "Category2")
        self.assertEqual(expense3.category.name, "Category3")

    # def test_expense_date(self):
    #     expense1 = Expense.objects.get(name="Expense1")
    #     expense2 = Expense.objects.get(name="Expense2")
    #     expense3 = Expense.objects.get(name="Expense3")
    #     self.assertEqual(expense1.date, "2020-01-01")
    #     self.assertEqual(expense2.date, "2020-01-02")
    #     self.assertEqual(expense3.date, "2020-01-03")

    def test_expense_notes(self):
        expense1 = Expense.objects.get(name="Expense1")
        expense2 = Expense.objects.get(name="Expense2")
        expense3 = Expense.objects.get(name="Expense3")
        self.assertEqual(expense1.notes, "Notes1")
        self.assertEqual(expense2.notes, "Notes2")
        self.assertEqual(expense3.notes, "Notes3")

    def test_expense_str(self):
        expense1 = Expense.objects.get(name="Expense1")
        expense2 = Expense.objects.get(name="Expense2")
        expense3 = Expense.objects.get(name="Expense3")
        self.assertEqual(str(expense1), "Category1")
        self.assertEqual(str(expense2), "Category2")
        self.assertEqual(str(expense3), "Category3")




