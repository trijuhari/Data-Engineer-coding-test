
def iterator(actual, predict, dict_actual_pred, cek, matrix):
	for data in  zip(actual ,predict):
		result =cek(data, dict_actual_pred)
	
	print(f"{result} \n")
	matrix_pred = matrix(result)
	print(matrix_pred)

def cek(data, dict_actual_pred):
    if data[0] == 0 and data[1] == 0:
        value = 'TN'
        dict_actual_pred[value] = dict_actual_pred.get(value, 0) + 1

    elif data[0] == 0 and data[1] == 1:
        value = 'FP'
        dict_actual_pred[value] = dict_actual_pred.get(value, 0) + 1

    elif data[0] == 1 and data[1] == 0:
        value = 'FN'

        dict_actual_pred[value] = dict_actual_pred.get(value, 0) + 1

    elif data[0] == 1 and data[1] == 1:
        value = 'TP'
        dict_actual_pred[value] = dict_actual_pred.get(value, 0) + 1

    return (dict_actual_pred)


def matrix(data_dict):
    result = {}
    accuracy = (data_dict["TP"] + data_dict["TN"]) / (data_dict["TP"] + data_dict["TN"] + data_dict["FP"] + data_dict["FN"])
    Precission = data_dict["TP"] / (data_dict["TP"] + data_dict["FP"])
    Recall = data_dict["TP"] / (data_dict["TP"] + data_dict["FN"])
    result['accuracy'] = round(accuracy * 100, 2)
    result['Precission'] = round(Precission * 100, 2)
    result['Recall'] = round(Recall * 100, 2)
    return result


def view(actual, predict):
    print("Data:")
    print("0 = Not Spam")
    print("1 = Spam")
    print("====================")
    print("| Actual | Predict |")
    print("====================")
    for data in zip(actual, predict):
        print(f"|    {data[0]}   |    {data[1]}    |")
    print("==================== \n")
    print("Result: \n")


def main():
    actual = [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]
    predict = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    dict_actual_pred = {}
    view(actual, predict)

    iterator(actual, predict, dict_actual_pred, cek, matrix)


if __name__ == '__main__':
    main()

# OUTPUT
# Data:
# 0 = Not Spam
# 1 = Spam
# ====================
# | Actual | Predict |
# ====================
# |    1   |    0    |
# |    1   |    0    |
# |    1   |    1    |
# |    1   |    1    |
# |    0   |    0    |
# |    0   |    1    |
# |    0   |    0    |
# |    1   |    1    |
# |    1   |    1    |
# |    0   |    0    |
# ====================
#
# Result:
#
# {'FN': 2, 'TP': 4, 'TN': 3, 'FP': 1}
#
# {'accuracy': 70.0, 'Precission': 80.0, 'Recall': 66.67}
#

