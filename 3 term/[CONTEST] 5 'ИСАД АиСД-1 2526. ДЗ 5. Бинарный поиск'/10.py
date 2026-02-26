''' .10 ' Железнодорожная задача + ''' #impossible

def query(d):
    print(f"? {d}", flush=True)
    response = input().strip().split()
    return response[0], response[1]


def answer(p):
    print(f"! {p}", flush=True)
    exit(0)


def get_properties(seat):
    level = "low" if seat % 2 == 1 else "high"
    section = "main" if seat <= 36 else "side"
    return level, section


level0, section0 = query(0)

candidates = [p for p in range(1, 55) if get_properties(p) == (level0, section0)]

if len(candidates) == 1:
    answer(candidates[0])

total_offset = 0
queries_used = 1

test_offsets = [18, -18, 9, -9, 4, -4]

for d in test_offsets:
    if len(candidates) == 1 or queries_used >= 6:
        break

    new_candidates = []
    for p in candidates:
        new_pos = p + total_offset + d
        if 1 <= new_pos <= 54:
            new_candidates.append(p)

    if not new_candidates:
        continue

    level_new, section_new = query(d)
    queries_used += 1
    total_offset += d

    filtered = []
    for p in new_candidates:
        expected = get_properties(p + total_offset)
        if expected == (level_new, section_new):
            filtered.append(p)

    if filtered:
        candidates = filtered

    if len(candidates) == 1:
        answer(candidates[0])

answer(candidates[0] if candidates else 1)
