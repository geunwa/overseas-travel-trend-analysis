"""명절 연휴 주의 검색 관심도가 평소와 얼마나 달랐는지 확인한다.

입력: data/weekly_clean.csv (analysis.ipynb 실행으로 생성)
출력: 표 출력, data/holiday_event_study.csv 저장
편차(deviation) = 그 주 값 - 그 주를 가운데 둔 13주 중앙값 (이상치 규칙과 같은 기준)
"""
import pandas as pd

# 설날·추석 당일 (음력 명절, 달력 서비스 dallyeok.com 등으로 확인). 데이터 시작(2021-11-07) 이후 10번
HOLIDAYS = [
    ("설날", "2022-02-01", False), ("설날", "2023-01-22", False), ("설날", "2024-02-10", False),
    ("설날", "2025-01-29", True),   # 2025-01-27 임시공휴일로 연휴 6일
    ("설날", "2026-02-17", False),
    ("추석", "2022-09-10", False),
    ("추석", "2023-09-29", True),   # 2023-10-02 임시공휴일로 연휴 6일
    ("추석", "2024-09-17", False),
    ("추석", "2025-10-06", True),   # 대체공휴일 10-08 포함, 개천절·한글날과 이어짐
    ("추석", "2026-09-25", False),
]
OFFSETS = range(-2, 3)  # 명절이 든 주를 0으로 앞뒤 2주

d = pd.read_csv("data/weekly_clean.csv", encoding="utf-8-sig", parse_dates=["date"]).reset_index(drop=True)
rows = []
for name, day, long_break in HOLIDAYS:
    day = pd.Timestamp(day)
    i = d.index[(d.date <= day) & (d.date + pd.Timedelta(days=6) >= day)][0]
    row = {"명절": name, "당일": day.date(), "그 주 시작일": d.date[i].date(), "긴 연휴": long_break}
    for o in OFFSETS:
        row[f"{o:+d}주"] = d.deviation[i + o]
    rows.append(row)
t = pd.DataFrame(rows)
cols = [f"{o:+d}주" for o in OFFSETS]
t.to_csv("data/holiday_event_study.csv", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 200)
print(t.to_string(index=False))
print("\n전체 평균(10번):", t[cols].mean().round(2).to_dict())
print("명절 주(0주) 평균 %.2f, 범위 %.0f ~ %.0f" % (t["+0주"].mean(), t["+0주"].min(), t["+0주"].max()))
for k, g in t.groupby("긴 연휴"):
    print("긴 연휴" if k else "그 외", len(g), "번 | 0주 평균 %.2f | -1~+1주 평균 %.2f | 절댓값 최대 %.0f" % (g["+0주"].mean(), g[["-1주", "+0주", "+1주"]].values.mean(), g[cols].abs().values.max()))
print("참고: 전체 261주 편차 표준편차 %.2f, 절댓값 중앙값 %.1f" % (d.deviation.std(), d.deviation.abs().median()))
