# 해외여행 검색 관심도 추이 분석

Google Trends의 "해외여행" 검색 관심도(대한민국, 최근 5년, 주간)를 시계열로 분석하는 프로젝트이다. 코디세이 AI Native 과정의 "AI 데이터 분석: 데이터 기반 트렌드 분석" 과제로 진행한다.

## 데이터

- 출처: Google Trends (https://www.google.com/trends)
- 기간: 2021-11-07 ~ 2026-11-08 (주간, 262개 데이터 포인트)
- 값: 0~100 상대 지수 (실제 검색 횟수가 아님)
- 수집 방법과 라이선스: DATA_SOURCE.md 참고
- 출처 표기: Data source: Google Trends (https://www.google.com/trends)

## 실행 환경

| 항목 | 버전 |
|---|---|
| Python | 3.13.18 (3.10 이상 필요) |
| numpy | 2.4.6 |
| pandas | 2.2.3 |
| matplotlib | 3.10.0 |

위 버전은 Google Colab에서 확인한 값이다. 라이브러리 목록은 requirements.txt에 있다.

## 실행 방법 (Google Colab)

1. https://colab.research.google.com 에 접속한다.
2. 노트북 파일(.ipynb)을 업로드해 연다.
3. 상단 메뉴 `런타임` → `모두 실행`을 누른다.
4. 노트북은 GitHub의 원본 CSV를 인터넷으로 직접 읽으므로 별도 파일 업로드가 필요 없다.

## 실행 방법 (내 컴퓨터)

```bash
pip install -r requirements.txt
```

## 폴더 구조 (현재)

```text
data/        원본 CSV (수정하지 않은 원본)
evidence/    단계별 증빙 스크린샷
DATA_SOURCE.md     데이터 수집 방법 문서
requirements.txt   라이브러리 버전
README.md          프로젝트 안내
```

분석 노트북, 시각화 이미지, 보고서는 이후 단계에서 추가하며 이 문서를 함께 갱신한다.