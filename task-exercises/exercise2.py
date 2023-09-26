import csv
with open('example.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    counter = 0
    sum = 0
    for row in reader:
        counter += 1
        sum += float(row['Calificacion'])
        average = sum / counter
        print('calificacion ', counter, ': ', row['Calificacion'])

print('Se tienen ', counter, ' calificaciones')
print('El promedio del grupo A es: ', round(average, 2))
