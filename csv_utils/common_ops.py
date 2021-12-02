import csv
import itertools
import re

import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

#SCHEMA_DICT = {'Agency': [], 'Id': [], 'Submission': []}

test_conf = {'Agency': [1, 2], 'Id': ['ra', 're'], 'Agency 1': [4, 5], 'Id 1': ['ro', 'ri'],
             'Submission': ['ña', 'Ñe'],
             'Agency 4': [4, 5], 'Id 4': ['ro', 'ri'], 'Name': ['alvaro', 'sara'], 'Agency 4 (first)': [1, 2],
             'Id5': ['ra', 're']}
#search_cols = ['Agency', 'Id']



def load_csv(path: str):
    return pd.read_csv(path)


def detect_columns_by_name(col_name: str, conf):
    return [col for col in conf.keys() if col_name in col]


def build_new_dict_with_target_columns(data: dict, targets: list, final_col_name: str, final_schema: dict, n_row: int):
    key_cols_dict = {col: data[col] for col in targets}
    aux_list = []
    for col in targets:
        first_n_values = list(key_cols_dict[col])[n_row]
        aux_list.append(first_n_values)
    final_schema[final_col_name] = aux_list
    return final_schema


def include_individual_columns(data: dict, target_col: str, inital_data: dict):
    for k, v in data.items():
        if k == 'Agency':
            n_elements = len(v[0])
            for i in range(len(inital_data['Submission'])):
                for j in range(n_elements):
                    data[target_col].append(inital_data[target_col][i])
        return data


def mergeDict(dict1, dict2):
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value , dict1[key]]
    return dict3


def prepare_final_output(res: dict):
    for key, value in res.items():
        if key in search_cols:
            res.update({key: [item for sublist in value for item in sublist]})
    return pd.DataFrame(res)


if __name__ == '__main__':
    # Iterate over target columns to merge them in one
    with open("/home/alvaro/personal_project/home-coders/csv_utils/data/test.csv", 'r', encoding='utf-8-sig') as data:
        a = [{k: str(v) for k, v in row.items()}
             for row in csv.DictReader(data, skipinitialspace=True)]
    test_conf = {}
    for li in a:
        test_conf = mergeDict(test_conf, li)
    file = open('/home/alvaro/personal_project/home-coders/csv_utils/data/app1.csv', 'r', encoding='utf-8-sig')
    content = file.read()
    search_cols = content.split(",")
    SCHEMA_DICT = dict.fromkeys(search_cols, [])
    for name in search_cols:
        # For each row in data
        for i in range(len(test_conf[name])):
            # search similar name columns
            same_key_columns = detect_columns_by_name(name, test_conf)
            # merge columns in a new dictionary
            build_new_dict_with_target_columns(test_conf, same_key_columns, name, SCHEMA_DICT, i)
    # Add those columns with 1 occurrence
    result = include_individual_columns(SCHEMA_DICT, 'Submission', test_conf)
    # Build desired DataFrame
    final_df = prepare_final_output(result)
    print(final_df)
