# Finance Management App – Vibe Coding Starter

## 💼 **Finance Management App – Vibe Coding Starter**

### 🚀 **Goal (Pitch)**

A simple, clean **Finance Tracker** that helps users manage their income and expenses in real-time.

> 🔹 Stack: **Python + Flask + SQLite + Bootstrap (or Tailwind)**
> 🔹 Mode: **Live Coding / Solo Sprint**
> 🔹 Time Limit: **45 minutes**

---

### 📁 Folder Structure

```
finance-tracker/
├── src/
│   ├── app.py
│   ├── models.py
│   ├── forms.py
│   ├── config.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── add_transaction.html
│   └── static/
│       └── style.css
├── instance/
│   └── finance.db
├── requirements.txt
├── .gitignore
└── README.md
```

---

### ✅ **Key Features in Scope**

| Feature                          | Route                | Template               |
| -------------------------------- | -------------------- | ---------------------- |
| View all transactions            | `/`                  | `index.html`           |
| Add transaction (income/expense) | `/add`               | `add_transaction.html` |
| Delete transaction               | `/delete/<id>`       | —                      |
| Summary stats                    | Included in homepage | `index.html`           |

---

### 📦 requirements.txt

```txt
Flask==3.0.0
Flask-WTF==1.2.1
WTForms==3.1.1
Flask-SQLAlchemy==3.1.1
email-validator==2.1.0
```

---

### 🔧 .gitignore

```txt
.venv/
__pycache__/
*.pyc
instance/
*.db
.env
```

---

## 🧱 Step-by-Step Coding Plan

### 1️⃣ `app.py` (Basic App)

```python
from flask import Flask, render_template, redirect, url_for, request
from models import db, Transaction
from forms import TransactionForm

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/')
def index():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    income = sum(t.amount for t in transactions if t.type == 'Income')
    expense = sum(t.amount for t in transactions if t.type == 'Expense')
    return render_template('index.html', transactions=transactions, income=income, expense=expense)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TransactionForm()
    if form.validate_on_submit():
        new_txn = Transaction(description=form.description.data, amount=form.amount.data, type=form.type.data)
        db.session.add(new_txn)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_transaction.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    txn = Transaction.query.get_or_404(id)
    db.session.delete(txn)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 2️⃣ `models.py`

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # Income or Expense
    date = db.Column(db.DateTime, default=datetime.utcnow)
```

---

### 3️⃣ `forms.py`

```python
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired

class TransactionForm(FlaskForm):
    description = StringField("Description", validators=[InputRequired()])
    amount = FloatField("Amount", validators=[InputRequired()])
    type = SelectField("Type", choices=[("Income", "Income"), ("Expense", "Expense")])
    submit = SubmitField("Add Transaction")
```

---

### 4️⃣ `config.py`

```python
class Config:
    SECRET_KEY = 'vibe-coding-finance-app'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/finance.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

### 5️⃣ Initialize DB (`flask shell`)

```bash
export FLASK_APP=app.py
flask shell
>>> from models import db
>>> db.create_all()
>>> exit()
```

---

### 🖼 Sample `index.html`

```html
{% extends 'layout.html' %} {% block content %}
<h2>Transactions</h2>
<p>💰 Income: ₹{{ income }} | 💸 Expense: ₹{{ expense }}</p>
<a href="{{ url_for('add') }}">Add New</a>
<ul>
  {% for txn in transactions %}
  <li>
    {{ txn.date.strftime("%d-%b") }} - {{ txn.description }} - ₹{{ txn.amount }}
    ({{ txn.type }}) <a href="{{ url_for('delete', id=txn.id) }}">🗑️</a>
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

---

## 🏁 You’re Ready!

### ✅ What You’ll Have After 45 Minutes:

- Add/view/delete income & expenses
- See real-time totals
- Minimal UI powered by HTML & Bootstrap or TailwindCDN
- Extensible structure (categories, charts, login)

---

## 📌 Bonus Ideas (if time permits):

- Add transaction category
- Export as CSV
- Add login (Flask-Login)
- Use Chart.js to show spending trends

---

Would you like a **PowerPoint deck** or **Copilot-ready markdown instructions** as well?
