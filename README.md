# 해외여행 검색 관심도 추이 분석

Google Trends의 "해외여행" 검색 관심도(대한민국, 최근 5년, 주간)를 시계열로 분석하는 프로젝트이다. 코디세이 AI Native 과정의 "AI 데이터 분석: 데이터 기반 트렌드 분석" 과제로 진행한다.

## 데이터

- 출처: Google Trends (https://www.google.com/trends)
- 기간: 2021-11-07 ~ 2026-11-08 (주간, 262개 데이터 포인트)
- 값: 0~100 상대 지수 (실제 검색 횟수가 아님)
- 원본: data/google_trends_overseas_travel_raw.csv (수정하지 않은 원본)
- 처리 결과: data/weekly_clean.csv (261주, analysis.ipynb 실행으로 생성)
- 수집 방법과 라이선스: DATA_SOURCE.md 참고
- 출처 표기: Data source: Google Trends (https://www.google.com/trends)

## 데이터 처리 기준

| 구분 | 기준 | 이유 |
|---|---|---|
| 결측치 | 있으면 채우지 않고 개수와 위치를 기록한다 (이번 데이터는 0개) | 상대 지수라 보간값은 근거가 약하다 |
| 마지막 주 | 통계에서 제외하고 원본 파일에는 유지한다 | 수집일(2026-11-09)에 끝나지 않은 주일 수 있다 |
| 이상치 | 13주 이동 중앙값 기준 로버스트 z 점수 3.5 초과를 표시만 하고 삭제하지 않는다 | 급증이 실제 관심 변화일 수 있고, 추세가 있어 전체 분포 기준은 부적합하다 |
| 집계 단위 | 주간을 기본으로 하고 월별 집계는 계절성 확인에만 쓴다 | 주간은 261개라 100개 이상 조건을 채우지만 월별은 약 60개라 채우지 못한다 |
| 월별 집계 | 각 주를 주 시작일이 속한 달에 넣고 평균을 낸다. 주가 4개 미만인 달은 뺀다 | 주가 걸치는 달 경계에서 배정 기준을 하나로 정하고, 주가 적은 달의 평균은 불안정하다 |

## 실행 환경

| 항목 | 버전 |
|---|---|
| Python | 3.13 계열 (Colab 3.13.18, 로컬 3.13.17), 3.10 이상 필요 |
| numpy | 2.4.6 |
| pandas | 2.2.3 |
| matplotlib | 3.10.0 |

버전은 Google Colab에서 확인한 값이며 로컬에서도 같은 버전으로 실행을 확인했다. Python 3.15.2에서는 numpy 2.4.6 설치가 실패(소스 빌드와 컴파일러가 필요)해서 3.13을 사용한다. 라이브러리 목록은 requirements.txt에 있다.

그래프의 한글은 Windows의 Malgun Gothic 글꼴로 확인했다. Colab에는 한글 글꼴이 없어 그래프 글자가 네모로 보일 수 있다. 노트북은 설치된 글꼴을 찾아 쓰며 없으면 경고를 출력한다.

## 실행 방법 (Google Colab)

1. https://colab.research.google.com 에 접속한다.
2. analysis.ipynb 파일을 업로드해 연다.
3. 상단 메뉴 `런타임` → `모두 실행`을 누른다.
4. 노트북은 data 폴더에 파일이 없으면 GitHub의 원본 CSV를 인터넷으로 직접 읽으므로 별도 업로드가 필요 없다.

## 실행 방법 (내 컴퓨터, Windows PowerShell)

```powershell
git clone https://github.com/geunwa/overseas-travel-trend-analysis.git
cd overseas-travel-trend-analysis
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt ipykernel
```

VS Code에서 폴더를 열고 analysis.ipynb의 커널을 `.venv`로 선택한 뒤 `모두 실행`을 누른다. 실행하면 images 폴더의 그래프 파일이 다시 만들어진다.

## 폴더 구조 (현재)

```text
data/                    원본 CSV와 처리 결과 CSV
evidence/                단계별 증빙 스크린샷
images/                  분석 그래프 3개 (노트북 실행으로 생성)
analysis.ipynb           분석 노트북 (품질 점검, 이상치 표시, 이동평균, 월별 분해, 급증 분석, 그래프)
DATA_SOURCE.md           데이터 수집 방법 문서
REPORT.md                분석 보고서 (작성 중, 단계마다 갱신)
requirements.txt         라이브러리 버전
README.md                프로젝트 안내
.gitignore               가상환경 등 제외 목록
```

통찰과 결론은 이후 단계에서 추가하며 이 문서를 함께 갱신한다.