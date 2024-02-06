import json
from pprint import pprint

def load_operation(filename):
    with open('bank_operation.json', 'r', encoding='utf8') as f:
        information = json.load(f)
        return information


def sort_operation(operations):
    if operations:  # Проверяем, что список операций не пустой
        return sorted(operations, key=lambda operation: operation.get('date', ''), reverse=True)[:5]
    return operations


def filter_operations(operations):
    desired_state = 'EXECUTED'  # Определяем состояние, которое мы ищем в операциях
    filtered_operations = []  # Создаем пустой список для хранения отфильтрованных операций
    for operation in operations:  # Для каждой операции в списке операций
        if operation.get('state') == desired_state:  # Проверяем, соответствует ли состояние операции желаемому состоянию
            filtered_operations.append(operation)  # Если да, добавляем операцию в список отфильтрованных операций
    return filtered_operations

# Загрузка операций из файла
filename = 'bank_operation.json'
bank_operations = load_operation(filename)

# Сортировка операций
sorted_operations = sort_operation(bank_operations)

# Фильтрация операций
filtered_operations = filter_operations(sorted_operations)

print("\nSorted Operations:")
pprint(sorted_operations)

print("\nFiltered Executed Operations:")
pprint(filtered_operations)