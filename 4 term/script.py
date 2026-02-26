from pathlib import Path
root = Path('D:/Apps/PyCharm/pythonProject/algorithms-data-structures-IDAS_course-/4 term')
for path in root.rglob('9.py'):
    print('FOUND', path)
    print('parts', list(path.parts))
    try:
        with path.open('r', encoding='utf-8') as f:
            print('SUCCESS', len(f.read()))
    except Exception as e:
        print('ERR', e)
