from csv import DictReader, DictWriter


def cm_in(cm):
    return float(cm)*0.393701


with open('fighter.csv') as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open('height.csv', 'w') as file:
    headers = ('Name', 'Country', 'Height')
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            'Name': f['Name'],
            'Country': f['Country'],
            'Height': round(cm_in(f['Height (in cm)']), 4)
        })

# We can also use the nested approach, just like we did in the writer case
# Unlike writer, we need to pass in headers in a different manner
# We need to pass a list or tuple of headers under the key 'fieldnames'
# And then we need to call writeheader() which will write the Headers for us
# And for writerow(), we need to pass in Dictionaries
