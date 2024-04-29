def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_info = []
    
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_info = {"id": id, "name": name, "age": age}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except Exception as e:
        print(f"File '{path}' has reading error: {e}")
        return None
    
    if cats_info == []:
        print(f"File '{path}' has no data")
        return None

    return cats_info