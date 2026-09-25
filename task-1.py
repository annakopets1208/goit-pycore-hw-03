from datetime import datetime 

def get_days_from_today(date: str) -> int:

  try:
    entered_date = datetime.strptime(date, "%Y-%m-%d")
  except ValueError:
    raise ValueError(f'Невірний формат дати: {date}')
  
  current_date = datetime.today()
  result = current_date.date() - entered_date.date()
  return result.days

print(get_days_from_today("2026-08-25"))