from datetime import datetime 

def get_days_from_today(date: str) -> int:
  """
  Функція повертає кількість днів між заданою та сьогоднішньою датою.

  Параметри:
    date - дата у форматі 'РРРР-ММ-ДД'

  Повертає:
    Кількість повних днів від заданої дати до сьогодні.
    Якщо дата в минулому, результат додатний,
    якщо в майбутньому, від'ємний.

  Викидає:
    ValueError - якщо дата має невірний формат.
  """
  try:
    entered_date = datetime.strptime(date, "%Y-%m-%d")
  except ValueError:
    raise ValueError(f'Невірний формат дати: {date}')
  
  current_date = datetime.today()
  result = current_date.date() - entered_date.date()
  return result.days

print(get_days_from_today("2026-09-28"))