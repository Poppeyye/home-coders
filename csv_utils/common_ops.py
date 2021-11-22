import itertools

import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)


def load_csv(path: str):
    return pd.read_csv(path)


if __name__ == '__main__':
    test_conf = {'Agency': [1, 2], 'Id': ['ra', 're'], 'Agency 1': [4, 5], 'Id 1': ['ro', 'ri'], 'Submission': ['ña', 'Ñe'],
                 'Agency 4': [4, 5], 'Id 4': ['ro', 'ri'], 'Name': ['alvaro', 'sara'],'Agency 4 (first)': [1, 2], 'Id5': ['ra', 're']}
    test_df = pd.DataFrame(data=test_conf)
    search_cols = ['Agency', 'Id']
    result_dfs = []
    res_dict = {}
    # TODO falta incorporar submission al final de final_df
    for column_name in search_cols:
        target_cols = [col for col in test_df.columns if column_name in col]
        list_dfs = []
        for col in target_cols:
            list_dfs.append(test_df[col].to_list())
            merged = list(itertools.chain(*list_dfs))
        result_dfs.append(merged)
        for i in result_dfs:
            res_dict[column_name] = i
            #res_dict['Submission'] =
    final_df = pd.DataFrame(res_dict)
    print(0)
    #test_df = load_csv('/home/alvaro/personal_project/home-coders/csv_utils/data/test.csv')
