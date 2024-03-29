from bridge import load_operation, sort_operation, filter_operations, formatter_date, formatter_from, formatter_to

filename = 'bank_operation.json'
bank_operations = load_operation(filename)
sorted_operations = sort_operation(bank_operations)
filtered_operations = filter_operations(sorted_operations)
limit = 5


def operation(filtered_operations):
    """Функция собирает всю информацию в 1 список"""
    results = []
    for filtered in filtered_operations:
        formatted_to = formatter_to(filtered['to'])
        formatted_date = formatter_date(filtered['date'])
        formatted_from = formatter_from(filtered.get('from'))
        done = f'{formatted_date} {filtered['description']}\n{formatted_from} -> {formatted_to}\n{filtered['operationAmount']['amount']} {filtered['operationAmount']['currency']['name']}'
        results.append(done)
    return results


results = operation(filtered_operations)

for index, item in enumerate(results):
    test = ''.join(item)
    print(test)
    if index == limit - 1:
        break





