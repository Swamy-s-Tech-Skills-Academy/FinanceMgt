from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired


class TransactionForm(FlaskForm):
    description = StringField("Description", validators=[InputRequired()])
    amount = FloatField("Amount", validators=[InputRequired()])
    type = SelectField(
        "Type", choices=[("Income", "Income"), ("Expense", "Expense")])
    submit = SubmitField("Add Transaction")
