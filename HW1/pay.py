import math

company_hourly_pay = 15

# unfairly computation
def unfair_weekly_paycheck_amount(hours):
    weekly_hours = math.floor(hours)
    return int(weekly_hours * company_hourly_pay)

# fair computation
def fair_weekly_paycheck_amount(hours):
    weekly_hours = float(hours)
    return float(weekly_hours * company_hourly_pay)