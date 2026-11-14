# 데이터 수집 방법 문서 (Data Source)

## 1. 데이터 개요

| 항목 | 내용 |
|---|---|
| 분석 주제 | 해외여행 검색 관심도 추이 (Interest over time) |
| 출처 | Google Trends (https://www.google.com/trends) |
| 접속 주소 | https://trends.google.co.kr/trends/explore |
| 수집 방식 | 웹 화면에서 CSV 수동 다운로드 |
| 수집일 | 2026-11-09 |
| 검색어 | 해외여행 (검색어 항목 선택, 주제 항목 아님) |
| 지역 | 대한민국 |
| 기간 설정 | 지난 5년 |
| 카테고리 | 모든 카테고리 |
| 검색 유형 | 웹 검색 |
| 실제 데이터 기간 | 2021-11-07 ~ 2026-11-08 (주 시작일 기준) |
| 집계 단위 | 주간 (일요일 시작) |
| 데이터 포인트 수 | 262개 |
| 원본 파일 | data/google_trends_overseas_travel_raw.csv (수정하지 않은 원본) |

## 2. 수집 절차 (재현 방법)

1. trends.google.co.kr 에 접속한다.
2. 검색창에 `해외여행`을 입력하고 드롭다운에서 "검색어" 항목을 선택한다.
3. 지역은 "대한민국", 기간은 "지난 5년", 카테고리는 "모든 카테고리", 검색 유형은 "웹 검색"으로 설정한다.
4. 그래프 오른쪽 위의 다운로드 아이콘을 눌러 CSV 파일을 저장한다.
5. 저장된 파일(multiTimeline.csv)의 이름을 `google_trends_overseas_travel_raw.csv`로 바꾸고 `data/` 폴더에 보관한다. 내용은 수정하지 않는다.

## 3. 파일 구조

- 1행: 카테고리 정보 ("카테고리: 모든 카테고리")
- 2행: 빈 줄
- 3행: 헤더 ("주", "해외여행: (대한민국)")
- 4행 이후: 주 시작일(날짜), 관심도 값 (0~100)

## 4. 값의 의미

- 값은 실제 검색 횟수가 아니라 상대 지수(Relative Index)이다.
- 설정한 기간과 지역 안에서 가장 높은 지점을 100으로 두고 나머지를 비율로 나타낸다.
- Google Trends는 실제 검색 요청의 표본(sample)이며, 검색량이 적은 구간은 0으로 표시될 수 있다 (Google Trends 도움말 기준).
- 30일 이상 구간의 날짜는 협정 세계시(UTC) 기준이다 (Google Trends 도움말 기준).

## 5. 라이선스 및 출처 표기

- Google Trends 정보는 Google 서비스 약관(Terms of Service) 범위에서 사용할 수 있으며, 재사용 시 Google을 출처로 표기해야 한다 (Google Trends 도움말 기준).
- 표기 문구: Data source: Google Trends (https://www.google.com/trends)

## 6. 한계 및 주의

- 상대 지수이므로 서로 다른 시점에 받은 파일을 이어 붙일 수 없다.
- 표본 데이터이므로 같은 조건으로 다시 수집하면 값이 달라질 수 있다.
- 마지막 행(2026-11-08)은 수집 시점에 끝나지 않은 주일 수 있다. 처리 기준은 분석 단계에서 정한다.

## 7. 증빙

- 수집 조건 화면: evidence/step01_google_trends_settings.png
