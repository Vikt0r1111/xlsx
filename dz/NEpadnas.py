import pandas

p = pandas.read_csv('groep.csv')

groep_av = p.groupby('група')['оцінка'].mean()

average = p['оцінка'].mean()

m_a_grade = p[p['оцінка'] > average] [name]

print("Середнє значення оцінки по групі:")
print(groep_av)

print("Середня оцінка для всіх студентів:")
print(average)

print("Студенти, оцінка яких вище середньої:")
print(m_a_grade)