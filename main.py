def compare_data(data1, data2, path=''):
    differences = []

    if isinstance(data1, dict) and isinstance(data2, dict):
        keys = set(data1.keys()) | set(data2.keys())
        for key in keys:
            new_path = f"{path}['{key}']"
            if key not in data1:
                differences.append((new_path, 'Key missing in first dict'))
            elif key not in data2:
                differences.append((new_path, 'Key missing in second dict'))
            else:
                differences.extend(compare_data(data1[key], data2[key], new_path))
    elif isinstance(data1, list) and isinstance(data2, list):
        for index, (item1, item2) in enumerate(zip(data1, data2)):
            new_path = f"{path}[{index}]"
            differences.extend(compare_data(item1, item2, new_path))
        if len(data1) != len(data2):
            differences.append((path, 'List lengths differ'))
    else:
        if isinstance(data1, float) and isinstance(data2, float):
            if round(data1, 5) != round(data2, 5):
                differences.append((path, data1, data2))
        else:
            if data1 != data2:
                differences.append((path, data1, data2))
    return differences


if __name__ == "__main__":
    obj1 = {
        'key_0': {
            'key_0': {
                'key_0': [15.020073, 'Bob', 'Bob'],
                'key_1': {'key_0': 52.256413, 'key_1': 'Alice', 'key_2': 74.245079},
                'key_2': ['Dave', 'Dave', 74]
            },
            'key_1': [
                {'key_0': 'Dave', 'key_1': 'Bob', 'key_2': 'Bob'},
                {'key_0': 33, 'key_1': 44, 'key_2': 76},
                ['Alice', 38.645442, 'Dave']
            ],
            'key_2': [
                {'key_0': 'Charlie', 'key_1': 53.867847, 'key_2': 67.092642},
                [98, 20.410157, 'Dave'],
                {'key_0': 'Dave', 'key_1': 42.574107, 'key_2': 'Bob'}
            ]
        },
        'key_1': [
            {'key_0': [28, 80, 80],
             'key_1': {'key_0': 61, 'key_1': 'Charlie', 'key_2': 67},
             'key_2': {'key_0': 62, 'key_1': 73, 'key_2': 76.879064}},
            [['Alice', 54.139813, 'Charlie'],
             {'key_0': 10.520224, 'key_1': 98, 'key_2': 21.467476},
             ['Dave', 9.86673, 'Bob']],
            [{'key_0': 25, 'key_1': 77.52233, 'key_2': 67},
             [89, 'Bob', 88],
             [95.895811, 37, 'Dave']]
        ],
        'key_2': [
            [{'key_0': 37.247708, 'key_1': 25, 'key_2': 3.933647},
             {'key_0': 'Charlie', 'key_1': 98, 'key_2': 81.626665},
             [26, 5.25379, 68.284449]],
            [{'key_0': 'Alice', 'key_1': 'Bob', 'key_2': 'Bob'},
             [2, 80, 84],
             [44.681556, 'Charlie', 6]],
            [{'key_0': 19, 'key_1': 20.884736, 'key_2': 28},
             {'key_0': 47.63154, 'key_1': 74.237558, 'key_2': 77.690348},
             {'key_0': 44, 'key_1': 53.247314, 'key_2': 95.763904}]
        ]
    }

    obj2 = {
        'key_0': {
            'key_0': {
                'key_0': [15.020073, 'Bob', 'Bob'],
                'key_1': {'key_0': 52.256413, 'key_1': 'Alice', 'key_2': 74.245079},
                'key_2': ['Dave', 'Dave', 74]
            },
            'key_1': [
                {'key_0': 'Dave', 'key_1': 'Bob', 'key_2': 'Bob'},
                {'key_0': 33, 'key_1': 44, 'key_2': 76},
                ['Alice', 38.645442, 'Dave']
            ],
            'key_2': [
                {'key_0': 'Charlie', 'key_1': 53.867847, 'key_2': 67.092642},
                [98, 20.410157, 'Dave'],
                {'key_0': 'Dave', 'key_1': 42.574107, 'key_2': 'Bob'}
            ]
        },
        'key_1': [
            {'key_0': [28, 80, 80],
             'key_1': {'key_0': 61, 'key_1': 'Charlie', 'key_2': 67},
             'key_2': {'key_0': 62, 'key_1': 73, 'key_2': 76.879064}},
            [['Meugh', 54.139813, 'Charlie'],
             {'key_0': 10.520224, 'key_1': 98, 'key_2': 21.44476},
             ['Dave', 9.86673, 'Bob']],
            [{'key_0': 25, 'key_1': 77.52233, 'key_2': 67},
             [89, 'Bob', 88],
             [95.895811, 37, 'Dave']]
        ],
        'key_2': [
            [{'key_0': 37.247708, 'key_1': 25, 'key_2': 3.9347},
             {'key_0': 'Charlie', 'key_1': 98, 'key_2': 81.624665},
             [26, 5.25379, 68.284449]],
            [{'key_0': 'DEG', 'key_1': 'Bob', 'key_2': 'Bob'},
             [2, 80, 84],
             [44.681556, 'Charlie', 6]],
            [{'key_0': 19, 'key_1': 20.884736, 'key_2': 28},
             {'key_0': 47.63154, 'key_1': 74.237558, 'key_2': 77.690348},
             {'key_0': 44, 'key_1': 53.247314, 'key_2': 95.763934}]
        ]
    }

    # Compare your data
    diffs = compare_data(obj1, obj2)
    for diff in diffs:
        print(f"{diff[0]} {diff[1]} {diff[2]}")
