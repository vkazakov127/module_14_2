# -*- coding: utf-8 -*-
# module_14_2.py
import sqlite3

conn = sqlite3.connect("not_telegram.db")
c = conn.cursor()

# 1 . Удалить запись с id = 6
c.execute("DELETE FROM Users WHERE id = ?", (6, ))
# Записываем изменения
conn.commit()

# 2 .  Подсчитать общее количество записей.
c.execute("SELECT COUNT(*) FROM Users")
total_count = c.fetchone()[0]
print(f"total_count={total_count}")

# 3 . Посчитать сумму всех балансов.
c.execute("SELECT SUM(balance) FROM Users")
balance_sum = c.fetchone()[0]
print(f"balance_sum={balance_sum}")

# 4 . Вывести в консоль средний баланс всех пользователя.
c.execute("SELECT AVG(balance) FROM Users")
balance_avg = c.fetchone()[0]
print(f"balance_avg={balance_avg}")

# Закрываем соединение
conn.close()
print("------------- The End -------------")
