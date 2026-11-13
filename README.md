# 해외여행 검색 관심도 추이 분석

Google Trends의 "해외여행" 검색 관심도(대한민국, 최근 5년, 주간)를 시계열로 분석하는 프로젝트이다. 코디세이 AI Native 과정의 "AI 데이터 분석: 데이터 기반 트렌드 분석" 과제로 진행했다.

분석 결과, 통찰, 결론과 한계, AI 사용 로그는 REPORT.md에 있다.

## 바로 가기

| 파일 | 내용 |
|---|---|
| [REPORT.md](REPORT.md) | 분석 보고서 (결과, 통찰, 결론과 한계, AI 사용 로그) |
| [analysis.ipynb](analysis.ipynb) | 분석 코드 전체 |
| [images/](images) | 그림 4개 (fig1–fig4) |
| [presentation.html](presentation.html) | 동료 평가용 발표 자료 (내려받아 브라우저로 열기) |
| [DATA_SOURCE.md](DATA_SOURCE.md) | 데이터 수집 방법과 라이선스 |

제출 최종본은 태그 `v1.2`다 ([v1.2 보기](https://github.com/geunwa/overseas-travel-trend-analysis/tree/v1.2)).

## 분석 질문

| 번호 | 질문 |
|---|---|
| Q1 | 5년간 관심도는 얼마나 늘었고 최근에도 계속 늘고 있는가 |
| Q2 | 연중 관심이 높은 달과 낮은 달이 있는가 (계절성) |
| Q3 | 2026년 10월 급증은 일시적인가 새로운 수준인가 |
| Q4 (보너스) | 단순 기준선 예측 중 무엇이 가장 정확하고, 그 기준선으로 보면 급증은 얼마나 큰가 |

## 데이터

- 출처: Google Trends (https://www.google.com/trends)
- 기간: 2021-11-07 ~ 2026-11-08 (주간, 262개 데이터 포인트)
- 값: 0–100 상대 지수 (실제 검색 횟수가 아님)
- 원본: data/google_trends_overseas_travel_raw.csv (수정하지 않은 원본)
- 처리 결과: data/weekly_clean.csv (261주, analysis.ipynb 실행으로 생성)
- 수집 방법과 라이선스: DATA_SOURCE.md 참고
- 출처 표기: Data source: Google Trends (https://www.google.com/trends)

외부 비교 자료(교차검증용):

- 출처: 한국관광공사 한국관광 데이터랩, 연도별 통계(1975-2025)의 국민 해외관광객(월별)
- 파일: data/external/korea_tourism_annual_stats_1975_2025.xlsx
- 이용 조건: 공공누리 제1유형(출처표시)
- 용도: 계절성과 증가 추세를 실제 출국자 수와 비교하는 데만 쓰고 본 분석 데이터에는 포함하지 않는다

## 데이터 처리 기준

| 구분 | 기준 | 이유 |
|---|---|---|
| 결측치 | 있으면 채우지 않고 개수와 위치를 기록한다 (이번 데이터는 0개) | 상대 지수라 보간값은 근거가 약하다 |
| 마지막 주 | 통계에서 제외하고 원본 파일에는 유지한다 | 수집일(2026-11-09, 월)은 그 주(11-08 ~ 11-14)가 시작된 지 이틀째라 끝나지 않은 주다 |
| 이상치 | 13주 이동 중앙값 기준 로버스트 z 점수 3.5 초과를 표시만 하고 삭제하지 않는다 | 급증이 실제 관심 변화일 수 있고, 추세가 있어 전체 분포 기준은 부적합하다. 창 길이를 바꾼 민감도 검증은 REPORT.md 5.4에 있다 |
| 집계 단위 | 주간을 기본으로 하고 월별 집계는 계절성 확인에만 쓴다 | 주간은 261개라 100개 이상 조건을 채우지만 월별은 약 60개라 채우지 못한다 |
| 월별 집계 | 각 주를 주 시작일이 속한 달에 넣고 평균을 낸다. 주가 4개 미만인 달은 뺀다 | 주가 걸치는 달 경계에서 배정 기준을 하나로 정하고, 주가 적은 달의 평균은 불안정하다 |

## 실행 환경

| 항목 | 버전 |
|---|---|
| Python | 3.13 계열 (Colab 3.13.18, 로컬 3.13.17), 3.10 이상 필요 |
| numpy | 2.4.6 |
| pandas | 2.2.3 |
| matplotlib | 3.10.0 |
| openpyxl | 3.1.5 (외부 비교 자료 xlsx 읽기용) |

로컬(Windows, Python 3.13.17)에서 위 버전으로 실행을 확인했다. Python 3.15.2에서는 numpy 2.4.6 설치가 실패(소스 빌드와 컴파일러가 필요)해서 3.13을 사용한다. 라이브러리 목록은 requirements.txt에 있다.

그래프의 한글은 Windows의 Malgun Gothic 글꼴로 확인했다. Colab에는 한글 글꼴이 없어 그래프 글자가 네모로 보일 수 있다. 노트북은 설치된 글꼴을 찾아 쓰며 없으면 경고를 출력한다.

## 실행 방법 (Google Colab)

1. https://colab.research.google.com 에 접속한다.
2. analysis.ipynb 파일을 업로드해 연다.
3. 상단 메뉴 `런타임` → `모두 실행`을 누른다.
4. 노트북은 data 폴더에 파일이 없으면 GitHub의 원본 CSV와 외부 비교 xlsx를 인터넷으로 직접 읽으므로 별도 업로드가 필요 없다.

Colab의 라이브러리 버전은 requirements.txt와 다를 수 있다.

## 실행 방법 (내 컴퓨터, Windows PowerShell)

```powershell
git clone https://github.com/geunwa/overseas-travel-trend-analysis.git
cd overseas-travel-trend-analysis
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt ipykernel
```

VS Code에서 폴더를 열고 analysis.ipynb의 커널을 `.venv`로 선택한 뒤 `모두 실행`을 누른다. 실행하면 data/weekly_clean.csv와 images 폴더의 그래프 파일이 다시 만들어진다. VS Code를 다시 열었을 때도 셀 하나만 실행하지 말고 `모두 실행`부터 한다.

## 노트북 구성 (analysis.ipynb)

| 순서 | 내용 | REPORT.md |
|---|---|---|
| 1 | 불러오기, 품질 점검, 마지막 주 제외, 이상치 표시, 저장 | 4장 |
| 2 | 이동평균, 52주 묶음 평균 (Q1) | 5.1 |
| 3 | 전주 대비 변화, 기준선, 잔존율, 2024-12 비교 (Q3) | 5.2 |
| 4 | 월별 집계, 추세·계절·잡음 분해, 연도별 최고·최저 달 (Q2) | 5.3 |
| 5 | 그림 1–3 (그림 4는 7번에서 그린다) | 6장 |
| 6 | 이상치 규칙 민감도, 외부 통계 교차검증, 9월 대비 10월 비교 | 5.3, 5.4 |
| 7 | 기준선 예측 3종 백테스트와 그림 4 (Q4) | 5.5, 6장 |

## 폴더 구조

```text
data/                    원본 CSV와 처리 결과 CSV
data/external/           외부 비교 자료 (한국관광공사 연도별 통계 xlsx)
evidence/                단계별 증빙 스크린샷
images/                  분석 그래프 4개 (노트북 실행으로 생성)
analysis.ipynb           분석 노트북
DATA_SOURCE.md           데이터 수집 방법과 라이선스 문서
REPORT.md                분석 보고서 (결과, 통찰, 결론과 한계, AI 사용 로그)
presentation.html        동료 평가용 발표 자료 (브라우저로 열기, G 키로 용어 사전)
requirements.txt         라이브러리 버전
README.md                프로젝트 안내
.gitignore               가상환경 등 제외 목록
```