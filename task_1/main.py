from typing import Tuple

def total_salary(path:str) -> Tuple[int, int]:
    sum_salary=0
    count=0
    
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                sum_salary += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except Exception as e:
        print(f"File '{path}' has reading error: {e}")
        return None
    
    if count == 0:
        print(f"File '{path}' has no data")
        return None
    
    avg_salary = sum_salary / count          
    return sum_salary, avg_salary