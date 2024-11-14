my_list: list[str | int] = [1, "hi"]

my_dict: dict[str, int] = {"a": 1}

my_tuple: tuple[int, str, int] = (1, "hi", 3)

my_tuple2: tuple[int, ...] = (1, 2, 3, 4)  # 길이는 모르겠지만 요소는 다 int 형이야.


import os

print(os.environ.get("temp", "없음"))
