# -----Task 1-----
test_results = [True, False, True, True, False, False, True]
total=len(test_results)
success_count=test_results.count(True)
# failure_count=test_results.count(False) # or
failure_count=total-success_count
success_percentage=(success_count/total)*100
print(f"Колличество тестов: {total}")
print(f"Количество успешных тестов: {success_count}")
print(f"Количество неуспешных тестов: {failure_count}")
print(f"Процент успешных кейсов: {success_percentage:.2f}%")
#  Alternotivs
# #входные данные
test_results = [True, False, True, True, False, False, True]
#общее количество кол-во тестов
total_tests = len(test_results)
#подсчет успешных и неуспешных
succes_count = 0
failure_count  = 0
for i in test_results:
    if i:
        succes_count +=1
    else:
        failure_count +=1
#посчитать процент
succes_percentage = (succes_count / total_tests) * 100
print(f'Общее количество тестов: {total_tests}')
print(f'Количество успешных тестов: {succes_count}')
print(f'Количество неуспешных тестов: {failure_count}')
print(f'Процент успешных кейсов {succes_percentage:.2f}%')