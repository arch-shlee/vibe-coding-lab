# Vibe Coding Lab 프로젝트 계획서

> 구글 안티그라비티를 활용한 TDD 기반 바이브코딩 학습 플랫폼

## 📋 프로젝트 개요

### 목적
초심자가 **단계별로 안전하고 효율적**으로 바이브코딩(Vibe Coding)을 학습할 수 있는 체계적인 실습 환경을 제공합니다.

### 핵심 가치
- 🎯 **점진적 학습**: Level 1부터 시작하여 자연스럽게 확장
- 🛡️ **안전한 실습**: 검증된 예제와 가이드라인
- 🤝 **실전 중심**: 이론보다는 hands-on 실습
- 🚀 **현대적 도구**: 구글 안티그라비티, TDD, 멀티에이전트

### 대상 학습자
- **초급**: 프로그래밍 기본 지식은 있으나 AI 코딩 도구 경험 없음
- **중급**: AI 도구를 써봤으나 체계적인 방법론 필요
- **고급**: TDD와 멀티에이전트 시스템 활용 방법 학습 희망

---

## 🏗️ 전체 구조 설계

### 디렉토리 구조

```
vibe-coding-lab/
├── README.md                          # 프로젝트 메인 소개
├── PROJECT_PLAN.md                    # 이 문서
├── CONTRIBUTING.md                    # 기여 가이드
├── .gitignore
│
├── docs/                              # 전체 문서
│   ├── setup/                         # 초기 설정 가이드
│   │   ├── antigravity-setup.md
│   │   ├── environment.md
│   │   └── troubleshooting.md
│   │
│   ├── concepts/                      # 핵심 개념 설명
│   │   ├── vibe-coding.md
│   │   ├── tdd-basics.md
│   │   ├── multi-agent.md
│   │   └── best-practices.md
│   │
│   └── references/                    # 참고 자료
│       ├── glossary.md
│       ├── resources.md
│       └── faq.md
│
├── level-1-basics/                    # Level 1: 기초
│   ├── README.md
│   ├── 01-hello-vibe/
│   │   ├── README.md
│   │   ├── exercise.md
│   │   ├── solution/
│   │   └── tests/
│   ├── 02-first-tdd/
│   ├── 03-ai-assistant/
│   └── project/                       # 레벨 종합 프로젝트
│
├── level-2-intermediate/              # Level 2: 중급
│   ├── README.md
│   ├── 01-red-green-refactor/
│   ├── 02-single-agent/
│   ├── 03-prompt-engineering/
│   └── project/
│
├── level-3-advanced/                  # Level 3: 고급
│   ├── README.md
│   ├── 01-multi-agent-setup/
│   ├── 02-architect-builder/
│   ├── 03-workflow-optimization/
│   └── project/
│
├── level-4-mastery/                   # Level 4: 실전
│   ├── README.md
│   ├── 01-real-world-project/
│   ├── 02-team-collaboration/
│   ├── 03-production-ready/
│   └── capstone-project/
│
├── templates/                         # 재사용 가능한 템플릿
│   ├── agent-prompts/
│   ├── test-templates/
│   └── project-structure/
│
└── examples/                          # 완성된 예제 프로젝트
    ├── todo-app/
    ├── blog-platform/
    └── dashboard/
```

---

## 📚 레벨별 학습 로드맵

### Level 1: 기초 (Basics)
**목표**: 바이브코딩과 TDD의 기본 개념 이해, 안티그라비티 사용법 익히기

#### 학습 목표
- ✅ 바이브코딩이 무엇인지 이해
- ✅ TDD의 Red-Green-Refactor 사이클 체험
- ✅ 안티그라비티 기본 기능 사용
- ✅ 단일 AI 에이전트와 대화하며 코드 작성

#### 모듈 구성

**01-hello-vibe**: 첫 번째 바이브코딩 경험
- 안티그라비티 인터페이스 탐색
- 간단한 "Hello World" 프로그램을 AI와 함께 작성
- 바이브(의도)를 전달하는 방법 학습

**02-first-tdd**: TDD 입문
- Red-Green-Refactor 사이클 실습
- 간단한 계산기 함수를 TDD로 작성
- 테스트 먼저, 구현은 나중에

**03-ai-assistant**: AI를 조수로 활용하기
- 효과적인 프롬프트 작성법
- AI에게 테스트 작성 요청하기
- AI 결과물 검증하는 방법

**project**: Todo List 앱 (Level 1 종합)
- 배운 내용을 종합하여 간단한 Todo 앱 제작
- 단계별 체크리스트 제공
- 모범 답안 및 코드 리뷰 포함

#### 완료 기준
- [ ] 안티그라비티에서 AI와 대화하며 코드 작성 가능
- [ ] Red-Green-Refactor 사이클을 이해하고 실습 완료
- [ ] Todo List 프로젝트를 TDD로 완성

---

### Level 2: 중급 (Intermediate)
**목표**: TDD 심화, 단일 에이전트 최적 활용, 프롬프트 엔지니어링

#### 학습 목표
- ✅ TDD를 실전 프로젝트에 적용
- ✅ AI 에이전트의 강점과 약점 파악
- ✅ 효과적인 프롬프트 패턴 습득
- ✅ 리팩토링 기법 마스터

#### 모듈 구성

**01-red-green-refactor**: TDD 심화
- 복잡한 비즈니스 로직을 TDD로 구현
- Edge case 처리
- 리팩토링 타이밍 학습

**02-single-agent**: 단일 에이전트 마스터
- Gemini 또는 Claude 하나를 선택하여 집중 학습
- 에이전트별 특성 이해
- 최적의 작업 방식 발견

**03-prompt-engineering**: 프롬프트 엔지니어링
- 명확한 요구사항 전달 방법
- 컨텍스트 제공 기법
- 반복 개선 (Iteration) 전략

**project**: 쇼핑몰 쿠폰 시스템 (Kent Beck 예제 기반)
- 할인 쿠폰 시스템을 TDD로 구현
- 다양한 할인 타입 (정액, 정률, 조건부)
- 에이전트를 활용한 효율적 개발

#### 완료 기준
- [ ] 복잡한 비즈니스 로직을 TDD로 구현 가능
- [ ] AI 에이전트에게 정확한 의도 전달 가능
- [ ] 쿠폰 시스템 프로젝트 완성 및 테스트 통과

---

### Level 3: 고급 (Advanced)
**목표**: 멀티 에이전트 시스템 활용, 협업 워크플로우 구축

#### 학습 목표
- ✅ 멀티 에이전트 시스템 설계 및 운영
- ✅ 에이전트별 역할 분담 전략
- ✅ 협업 워크플로우 최적화
- ✅ 대규모 프로젝트 설계 능력

#### 모듈 구성

**01-multi-agent-setup**: 멀티 에이전트 설정
- Agent Manager 사용법
- Gemini(Architect) + Claude(Builder) 팀 구성
- 시스템 프롬프트 작성

**02-architect-builder**: 아키텍트-빌더 패턴
- Gemini로 PRD 작성 → Claude로 구현
- 컨텍스트 공유 (Context Bridge)
- 에이전트 간 협업 실습

**03-workflow-optimization**: 워크플로우 최적화
- 효율적인 작업 분담
- 문서 기반 협업 (PRD, Architecture, Plan)
- 반복 개선 사이클

**project**: 실시간 주식 대시보드
- Gemini가 시스템 설계 (아키텍처, API 명세)
- Claude가 코드 구현 (React 컴포넌트, 테스트)
- 실시간 데이터 처리 및 시각화

#### 완료 기준
- [ ] 멀티 에이전트 시스템을 독립적으로 구성 가능
- [ ] 에이전트별 역할을 명확히 이해하고 활용
- [ ] 주식 대시보드 프로젝트 완성

---

### Level 4: 실전 (Mastery)
**목표**: 실무 적용, 팀 협업, 프로덕션 레디 코드 작성

#### 학습 목표
- ✅ 실제 프로젝트에 바이브코딩 적용
- ✅ 팀 환경에서의 멀티 에이전트 활용
- ✅ 프로덕션 수준의 코드 품질 유지
- ✅ CI/CD 파이프라인 통합

#### 모듈 구성

**01-real-world-project**: 실전 프로젝트
- 요구사항 분석부터 배포까지 전 과정
- 보안, 성능, 확장성 고려
- 에러 핸들링 및 모니터링

**02-team-collaboration**: 팀 협업
- 다수의 에이전트 관리
- 역할 전문화 (QA, DevOps, Security 에이전트)
- 코드 리뷰 프로세스

**03-production-ready**: 프로덕션 준비
- CI/CD 파이프라인 구축
- 테스트 커버리지 100% 달성
- 문서화 자동화

**capstone-project**: 최종 프로젝트 (선택형)
- 블로그 플랫폼
- API 서버
- 데이터 파이프라인
- 모바일 앱

#### 완료 기준
- [ ] 실무 수준의 프로젝트를 바이브코딩으로 완성
- [ ] 팀 환경에서 멀티 에이전트 시스템 운영 경험
- [ ] Capstone 프로젝트 완성 및 배포

---

## 📖 각 모듈의 표준 구조

모든 학습 모듈은 일관된 구조를 따릅니다:

### 폴더 구조
```
module-name/
├── README.md              # 모듈 소개 및 학습 목표
├── GUIDE.md               # 단계별 실습 가이드
├── exercise.md            # 실습 문제
├── solution/              # 모범 답안
│   ├── README.md
│   ├── src/
│   └── tests/
├── starter/               # 시작 템플릿 (학습자용)
│   ├── README.md
│   ├── src/
│   └── tests/
├── resources/             # 참고 자료
│   ├── concepts.md
│   └── references.md
└── checkpoints/           # 체크포인트 (진행 상황 확인)
    ├── checkpoint-1.md
    ├── checkpoint-2.md
    └── final-review.md
```

### README.md 템플릿

```markdown
# [모듈명]

## 🎯 학습 목표
- 목표 1
- 목표 2
- 목표 3

## 📋 사전 준비
- 필요한 지식
- 필요한 도구
- 이전 모듈 완료 여부

## 🚀 시작하기
1. starter/ 폴더로 이동
2. README.md 지침 따르기
3. GUIDE.md 참고하며 진행

## 📚 학습 내용
### 개념
### 실습
### 도전 과제

## ✅ 완료 기준
- [ ] 체크리스트 1
- [ ] 체크리스트 2

## 🔗 다음 단계
- 다음 모듈 소개

## 💡 추가 자료
- 참고 링크
```

---

## 🎓 학습 방법론

### 1. Guided Learning (가이드 학습)
- 각 모듈의 GUIDE.md를 따라 단계별 학습
- 체크포인트마다 이해도 확인
- 막히는 부분은 solution/ 참고

### 2. Project-Based Learning (프로젝트 기반)
- 각 레벨 마지막에 종합 프로젝트 제공
- 실전처럼 처음부터 끝까지 구현
- 모범 답안과 비교 분석

### 3. Iterative Improvement (반복 개선)
- 첫 번째: 작동하는 코드 만들기
- 두 번째: 테스트 추가하기
- 세 번째: 리팩토링하기
- 네 번째: AI 활용하여 개선하기

### 4. Peer Review (동료 리뷰)
- 다른 학습자의 코드 리뷰
- 피드백 주고받기
- GitHub Discussion 활용

---

## 🛠️ 기술 스택

### 필수 도구
- **Google Antigravity**: 멀티 에이전트 플랫폼
- **Git/GitHub**: 버전 관리
- **Node.js/Python**: 프로그래밍 언어 (선택)
- **Jest/Pytest**: 테스트 프레임워크

### AI 모델
- **Gemini 3 Pro**: 아키텍처 설계
- **Claude Sonnet 4.5**: 코드 구현

### 선택 도구
- **VS Code**: 코드 에디터
- **Docker**: 환경 일관성
- **GitHub Actions**: CI/CD

---

## 📅 학습 예상 시간

| 레벨 | 예상 시간 | 내용 |
|------|----------|------|
| **Level 1** | 1-2주 | 기초 개념, 안티그라비티 익히기 |
| **Level 2** | 2-3주 | TDD 심화, 단일 에이전트 마스터 |
| **Level 3** | 3-4주 | 멀티 에이전트 시스템 구축 |
| **Level 4** | 4-6주 | 실전 프로젝트, Capstone |
| **전체** | 10-15주 | 주 5시간 학습 기준 |

---

## 🎯 성공 기준

### Level 1 완료 기준
- ✅ 안티그라비티 기본 기능 사용 가능
- ✅ TDD의 Red-Green-Refactor 이해
- ✅ AI와 협업하여 Todo 앱 완성

### Level 2 완료 기준
- ✅ 복잡한 비즈니스 로직을 TDD로 구현
- ✅ 효과적인 프롬프트 작성 능력
- ✅ 쿠폰 시스템 프로젝트 완성

### Level 3 완료 기준
- ✅ 멀티 에이전트 시스템 독립 구성
- ✅ 에이전트별 역할 분담 전략 수립
- ✅ 주식 대시보드 완성

### Level 4 완료 기준
- ✅ 실무 수준 프로젝트 완성
- ✅ 프로덕션 배포 경험
- ✅ Capstone 프로젝트 완성

---

## 🚀 구현 우선순위

### Phase 1: 기반 구축 (1-2주) ✅ 완료
- [x] 프로젝트 구조 생성 (Level 1-4 전체 폴더)
- [x] 메인 README.md 작성
- [x] PROJECT_PLAN.md 작성
- [x] .gitignore 설정
- [x] docs/setup/ 문서 작성
  - [x] antigravity-setup.md
  - [x] environment.md
  - [x] 이미지 플레이스홀더 추가
- [x] Level 1 폴더 구조 생성
- [x] Level 1 README 작성
- [x] 01-hello-vibe 모듈 완성
  - [x] README.md
  - [x] starter/ 폴더
  - [x] solution/ 폴더 (4개 파일)
- [x] 1차 commit 완료

**완료일**: 2026-01-13
**산출물**: 15개 파일, 2,325줄

### Phase 2: Level 1 완성 (2-3주) 🚧 진행 예정
**우선순위 1: 실습 기반 검증 (추천)**
- [ ] 01-hello-vibe 직접 실습
- [ ] 스크린샷 캡처 및 문서에 추가
- [ ] 실습 중 발견한 개선점 반영
- [ ] checkpoints/ 파일 작성

**우선순위 2: 나머지 모듈 작성**
- [ ] 02-first-tdd 모듈 완성
  - [ ] README.md (TDD 기본 개념)
  - [ ] GUIDE.md (단계별 실습)
  - [ ] starter/ 폴더
  - [ ] solution/ 폴더
  - [ ] checkpoints/
- [ ] 03-ai-assistant 모듈 완성
  - [ ] README.md (프롬프트 엔지니어링)
  - [ ] GUIDE.md
  - [ ] starter/ 폴더
  - [ ] solution/ 폴더
  - [ ] checkpoints/

**우선순위 3: Level 1 종합 프로젝트**
- [ ] project/ (Todo 앱) 설계
  - [ ] README.md (프로젝트 요구사항)
  - [ ] GUIDE.md (단계별 구현 가이드)
  - [ ] starter/ (기본 구조)
  - [ ] solution/ (완성 코드)
  - [ ] tests/ (테스트 코드)

**우선순위 4: 추가 문서**
- [ ] CONTRIBUTING.md 작성
- [ ] docs/concepts/ 핵심 개념 문서
- [ ] docs/references/ 참고 자료

**우선순위 5: 초기 사용자 테스트**
- [ ] 2-3명 테스터 모집
- [ ] 피드백 수집 및 반영

### Phase 3: Level 2-3 구축 (4-6주) ⏳ 예정
- [ ] Level 2 모듈 작성
- [ ] Level 3 모듈 작성
- [ ] 중간 피드백 수집 및 개선

### Phase 4: Level 4 및 마무리 (4-8주) ⏳ 예정
- [ ] Level 4 실전 프로젝트
- [ ] Capstone 프로젝트 템플릿
- [ ] 전체 문서화 완성
- [ ] 커뮤니티 론칭

---

## 🤝 커뮤니티 및 기여

### 기여 방법
- 버그 리포트: GitHub Issues
- 새로운 모듈 제안: GitHub Discussions
- 코드 기여: Pull Request
- 번역: i18n 지원

### 라이선스
MIT License

---

## 📊 측정 지표

### 학습 효과 측정
- 각 레벨 완료율
- 프로젝트 완성도
- 테스트 커버리지
- 코드 품질 점수

### 커뮤니티 성장
- GitHub Stars
- Contributors 수
- Discussion 활동
- 완료자 수

---

## 🔮 향후 계획

### 단기 (3개월)
- Level 1-2 완성
- 초기 사용자 확보 (50명)
- 피드백 기반 개선

### 중기 (6개월)
- Level 3-4 완성
- 다양한 언어 지원 (Python, TypeScript, Go)
- 온라인 워크샵 개최

### 장기 (1년)
- 바이브코딩 인증 프로그램
- 기업 교육 프로그램
- 글로벌 커뮤니티 확장

---

## 💡 핵심 원칙

### 학습자 중심
- 초심자도 쉽게 시작할 수 있도록
- 단계별 난이도 조절
- 충분한 예제와 가이드

### 실전 중심
- 이론보다는 hands-on
- 실제 프로젝트 기반 학습
- 현업에서 바로 적용 가능

### 커뮤니티 중심
- 함께 배우고 성장
- 지식 공유 문화
- 오픈소스 정신

---

**작성일**: 2026-01-13
**최종 수정**: 2026-01-13
**버전**: 1.1
**작성자**: arch-shlee & Claude
**상태**: Phase 1 완료, Phase 2 진행 예정
