# Level 1: 기초 (Basics)

> 바이브코딩과 TDD의 기본 개념을 익히고, AI 에이전트와 함께 첫 코드를 작성해봅니다.

## 🎯 학습 목표

이 레벨을 완료하면:

- ✅ 바이브코딩이 무엇인지 이해하고 실습
- ✅ TDD의 Red-Green-Refactor 사이클 체험
- ✅ 안티그라비티 기본 기능 사용
- ✅ 단일 AI 에이전트와 효과적으로 협업
- ✅ 간단한 Python 프로그램을 TDD로 작성

## 📋 사전 준비

### 필수
- [ ] [안티그라비티 계정 설정](../docs/setup/antigravity-setup.md) 완료
- [ ] [Python 환경 설정](../docs/setup/environment.md) 완료
- [ ] Python 기본 문법 이해 (변수, 함수, 조건문)

### 예상 소요 시간
- **전체**: 1-2주 (주 5시간 기준)
- **모듈당**: 2-4시간
- **프로젝트**: 4-6시간

---

## 📚 모듈 구성

### [01 - Hello Vibe](./01-hello-vibe/)
**목표**: 첫 번째 바이브코딩 경험

바이브코딩이 무엇인지 직접 체험해봅니다. AI와 대화하며 간단한 Python 프로그램을 만들어보세요.

**핵심 개념**:
- 바이브(의도) 전달하기
- AI 응답 이해하고 활용
- 코드 실행 및 검증

**소요 시간**: 2-3시간

---

### [02 - First TDD](./02-first-tdd/)
**목표**: TDD 입문 - Red-Green-Refactor

TDD의 핵심인 Red-Green-Refactor 사이클을 배우고 실습합니다.

**핵심 개념**:
- 🔴 Red: 실패하는 테스트 작성
- 🟢 Green: 최소한의 코드로 테스트 통과
- 🔵 Refactor: 코드 개선

**소요 시간**: 3-4시간

---

### [03 - AI Assistant](./03-ai-assistant/)
**목표**: AI를 효과적인 조수로 활용하기

AI에게 효과적으로 요청하는 방법을 배웁니다. 프롬프트 작성 기법과 AI 결과물 검증 방법을 익힙니다.

**핵심 개념**:
- 명확한 프롬프트 작성
- 컨텍스트 제공
- AI 응답 검증 및 개선

**소요 시간**: 2-3시간

---

### [Project - Todo List 앱](./project/)
**목표**: Level 1 종합 프로젝트

지금까지 배운 내용을 종합하여 간단한 Todo List 앱을 TDD로 만들어봅니다.

**구현 기능**:
- Todo 추가
- Todo 완료 체크
- Todo 삭제
- Todo 목록 조회

**소요 시간**: 4-6시간

---

## 🚀 시작하기

### 1. 순서대로 학습

모듈은 순서대로 진행하는 것을 권장합니다:

```
01-hello-vibe → 02-first-tdd → 03-ai-assistant → project
```

### 2. 각 모듈 진행 방법

1. **README.md 읽기**: 모듈 개요 및 학습 목표 확인
2. **GUIDE.md 따라하기**: 단계별 실습 가이드
3. **starter/ 폴더에서 실습**: 직접 코드 작성
4. **checkpoints/ 확인**: 진행 상황 점검
5. **solution/ 참고**: 막힐 때만 참고

### 3. 학습 팁

💡 **혼자 해결 시도하기**
- 먼저 스스로 문제를 해결해보세요
- 막히면 AI에게 질문하기
- 그래도 안되면 solution/ 참고

💡 **AI와 대화하며 학습**
- 이해 안 되는 부분은 AI에게 설명 요청
- 여러 방법으로 같은 기능 구현해보기
- "왜?"라고 질문하는 습관

💡 **테스트 먼저 작성**
- TDD의 핵심: 테스트 → 구현
- 테스트는 요구사항을 코드로 표현한 것
- 빨간불 → 초록불의 즐거움 경험하기

---

## ✅ 완료 기준

Level 1을 완료했는지 확인하세요:

### 지식 체크
- [ ] 바이브코딩이 무엇인지 설명할 수 있다
- [ ] Red-Green-Refactor 사이클을 이해하고 있다
- [ ] pytest로 테스트를 작성하고 실행할 수 있다
- [ ] AI에게 효과적으로 요청할 수 있다

### 실습 체크
- [ ] 01-hello-vibe 모듈 완료
- [ ] 02-first-tdd 모듈 완료
- [ ] 03-ai-assistant 모듈 완료
- [ ] Todo List 프로젝트 완료
- [ ] 모든 테스트가 통과한다

### 코드 품질 체크
- [ ] 코드가 명확하고 읽기 쉽다
- [ ] 테스트 커버리지가 80% 이상
- [ ] DRY 원칙을 따른다 (중복 최소화)
- [ ] 함수와 변수 이름이 의미를 전달한다

---

## 🎓 학습 후기 작성

Level 1을 완료하면 학습 후기를 작성해주세요!

**GitHub Discussions**에 다음 내용을 공유:
- 가장 어려웠던 부분
- 가장 재밌었던 부분
- 인사이트 및 배운 점
- 다른 학습자를 위한 팁

---

## 🔗 다음 단계

Level 1을 완료했다면:

1. [Level 2: 중급](../level-2-intermediate/README.md)으로 진행
2. TDD 심화 및 프롬프트 엔지니어링 학습
3. 더 복잡한 비즈니스 로직 구현

---

## 📚 참고 자료

### 핵심 개념
- [바이브코딩이란?](../docs/concepts/vibe-coding.md)
- [TDD 기초](../docs/concepts/tdd-basics.md)
- [베스트 프랙티스](../docs/concepts/best-practices.md)

### 추가 학습
- Kent Beck - "Test-Driven Development: By Example"
- 딩코딩코 유튜브 - 아규먼티드 코딩
- Python 공식 튜토리얼

---

## 🆘 도움이 필요하신가요?

- [FAQ](../docs/references/faq.md)
- [문제 해결 가이드](../docs/setup/troubleshooting.md)
- [GitHub Issues](https://github.com/arch-shlee/vibe-coding-lab/issues)
- [GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)

---

## 🎉 시작할 준비가 되셨나요?

[01-hello-vibe](./01-hello-vibe/)로 이동하여 첫 번째 모듈을 시작하세요!

**Let's Vibe Code! 🚀**

---

**레벨**: 기초 (Level 1)
**예상 시간**: 1-2주
**난이도**: ⭐☆☆☆☆
**작성일**: 2026-01-13
