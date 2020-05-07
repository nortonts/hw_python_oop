import datetime as dt


class Record():
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date == '':
            self.date = self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_sum = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                today_sum += record.amount
        return today_sum

    def get_week_stats(self):
        week_sum = 0
        week_d = dt.datetime.now().date() - dt.timedelta(days=7)
        for rec in self.records:
            if dt.datetime.now().date() >= rec.date and week_d < rec.date:
                week_sum += rec.amount
        return week_sum


class CashCalculator(Calculator):
    USD_RATE = 68.65
    EURO_RATE = 76.64

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        self.currency = currency
        today_cash = self.limit - self.get_today_stats()
        if self.currency == "rub":
            val = 'руб'
        elif self.currency == "usd":
            today_cash = round(today_cash / self.USD_RATE, 2)
            val = 'USD'
        elif self.currency == "eur":
            today_cash = round(today_cash / self.EURO_RATE, 2)
            val = 'Euro'
        if today_cash == 0:
            return ('Денег нет, держись')
        elif today_cash > 0:
            return (f'На сегодня осталось {today_cash} {val}')
        elif today_cash < 0:
            return (f'Денег нет, держись: твой долг - {abs(today_cash)} {val}')


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        ca_ost = self.limit - self.get_today_stats()
        if ca_ost > 0:
            return (
                f'Сегодня можно съесть что-нибудь ещё, но с '
                f'общей калорийностью не более {ca_ost} кКал'
            )
        else:
            return 'Хватит есть!'
