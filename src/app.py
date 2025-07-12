from flask import Flask, render_template, redirect, url_for, request
from models import db, Transaction
from forms import TransactionForm

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()
    print("📊 Database tables created successfully!")


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
        new_txn = Transaction(description=form.description.data,
                              amount=form.amount.data, type=form.type.data)
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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
