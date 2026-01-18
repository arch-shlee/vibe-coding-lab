# Level 2: 중급 (Intermediate)

> TDD를 심화하고, AI 에이전트를 최적으로 활용하는 방법을 배웁니다.

## 🎯 학습 목표

이 레벨을 완료하면:

- ✅ 복잡한 비즈니스 로직을 TDD로 구현
- ✅ AI 에이전트의 강점과 약점 파악
- ✅ 효과적인 프롬프트 패턴 습득
- ✅ 리팩토링 타이밍과 기법 마스터
- ✅ 실전 수준의 프로젝트를 바이브코딩으로 완성

## 📋 사전 준비

### 필수
- [ ] [Level 1: 기초](../level-1-basics/README.md) 완료
- [ ] TDD의 Red-Green-Refactor 사이클 이해
- [ ] pytest 사용 경험
- [ ] AI와 기본적인 협업 경험

### 예상 소요 시간
- **전체**: 2-3주 (주 8시간 기준)
- **모듈당**: 4-6시간
- **프로젝트**: 8-12시간

---

## 📚 모듈 구성

### [01 - Red-Green-Refactor 심화](./01-red-green-refactor/)
**목표**: TDD를 실전 프로젝트에 적용하는 능력 향상

Level 1에서 배운 TDD를 더 복잡한 비즈니스 로직에 적용합니다.

**핵심 개념**:
- 복잡한 요구사항을 테스트로 표현하기
- Edge case와 예외 상황 처리
- 리팩토링 타이밍 파악
- 테스트 코드의 품질 향상

**실습 프로젝트**: 계산기 앱 (사칙연산, 괄호, 우선순위)

**소요 시간**: 4-5시간

---

### [02 - Single Agent 마스터](./02-single-agent/)
**목표**: 단일 AI 에이전트를 최적으로 활용하기

Gemini 또는 Claude 하나를 선택하여 집중적으로 학습합니다.

**핵심 개념**:
- 에이전트별 특성 이해 (Gemini vs Claude)
- 강점을 살리는 작업 분배
- 약점을 보완하는 전략
- 최적의 협업 워크플로우 발견

**실습 프로젝트**: 선택한 에이전트로 복잡한 기능 구현

**소요 시간**: 5-6시간

---

### [03 - Prompt Engineering](./03-prompt-engineering/)
**목표**: 효과적인 프롬프트 작성 기술 습득

AI에게 정확하게 의도를 전달하는 방법을 배웁니다.

**핵심 개념**:
- 명확한 요구사항 전달
- 적절한 컨텍스트 제공
- 반복 개선 (Iteration) 전략
- 프롬프트 패턴 라이브러리 구축

**실습 내용**: 다양한 시나리오별 프롬프트 연습

**소요 시간**: 4-5시간

---

### [Project - 쇼핑몰 쿠폰 시스템](./project/)
**목표**: Level 2 종합 프로젝트

Kent Beck의 TDD 예제를 기반으로 한 실전 프로젝트입니다.

**구현 기능**:
- 정액 할인 쿠폰
- 정률 할인 쿠폰
- 조건부 쿠폰 (최소 금액, 특정 상품)
- 쿠폰 중복 사용 정책
- 유효기간 관리

**기술 요구사항**:
- TDD로 전체 구현
- 테스트 커버리지 90% 이상
- AI 에이전트 활용한 효율적 개발

**소요 시간**: 8-12시간

---

## 🚀 시작하기

### 1. Level 1 복습

Level 2를 시작하기 전에 Level 1 내용을 간단히 복습하세요:

- ✅ Red-Green-Refactor 사이클
- ✅ pytest 기본 사용법
- ✅ AI와 대화하며 코드 작성하기
- ✅ 기본적인 리팩토링

### 2. 순차적 학습

모듈은 순서대로 진행하는 것을 권장합니다:

```
01-red-green-refactor → 02-single-agent → 03-prompt-engineering → project
```

### 3. 각 모듈 진행 방법

1. **README.md 읽기**: 모듈 개요 및 학습 목표 확인
2. **GUIDE.md 따라하기**: 단계별 실습 가이드
3. **starter/ 폴더에서 실습**: 직접 코드 작성
4. **checkpoints/ 확인**: 진행 상황 점검
5. **solution/ 참고**: 막힐 때만 참고

### 4. Level 1과의 차이점

**Level 1 (기초)**:
- 간단한 기능 구현
- 기본적인 TDD 사이클
- AI와의 기본 대화

**Level 2 (중급)**: ⬅️ 지금 여기!
- 복잡한 비즈니스 로직
- 고급 TDD 기법
- AI 최적 활용 전략
- 실전 수준의 프로젝트

---

## 💡 학습 전략

### TDD 심화

**Level 1에서 배운 것**:
```python
# 간단한 테스트
def test_add():
    result = calculator.add(2, 3)
    assert result == 5
```

**Level 2에서 배울 것**:
```python
# 복잡한 비즈니스 로직 테스트
def test_쿠폰_조건부_할인():
    """10만원 이상 구매 시 20% 할인 쿠폰"""
    coupon = ConditionalCoupon(
        discount_rate=0.2,
        min_amount=100000
    )

    # 조건 미달
    result = coupon.apply(90000)
    assert result == 90000

    # 조건 충족
    result = coupon.apply(150000)
    assert result == 120000  # 20% 할인
```

### AI 활용 전략

**Level 1 프롬프트**:
```
"계산기 add 함수 만들어줘"
```

**Level 2 프롬프트**:
```
"쿠폰 시스템을 TDD로 구현하려고 해.

요구사항:
1. 정액/정률 할인 지원
2. 최소 구매 금액 조건
3. 유효기간 검증

먼저 도메인 모델을 설계하고,
가장 간단한 케이스(정액 할인)부터
테스트를 작성해줘.

테스트 구조는 Given-When-Then으로."
```

**차이점**:
- 명확한 컨텍스트 제공
- 구체적인 요구사항 나열
- 작업 순서 제시
- 원하는 형식 명시

---

## ✅ 완료 기준

Level 2를 완료했는지 확인하세요:

### 지식 체크
- [ ] 복잡한 비즈니스 로직을 테스트로 표현할 수 있다
- [ ] 리팩토링 타이밍을 적절히 판단할 수 있다
- [ ] AI 에이전트의 강점과 약점을 이해한다
- [ ] 효과적인 프롬프트를 작성할 수 있다

### 실습 체크
- [ ] 01-red-green-refactor 모듈 완료
- [ ] 02-single-agent 모듈 완료
- [ ] 03-prompt-engineering 모듈 완료
- [ ] 쿠폰 시스템 프로젝트 완료
- [ ] 모든 테스트 통과 (커버리지 90% 이상)

### 코드 품질 체크
- [ ] 테스트가 비즈니스 요구사항을 명확히 표현한다
- [ ] 리팩토링을 통해 코드 품질이 향상되었다
- [ ] Edge case가 적절히 처리되었다
- [ ] AI를 효율적으로 활용했다

---

## 🎓 Level 1 vs Level 2 비교

### 프로젝트 복잡도

| 항목 | Level 1 | Level 2 |
|------|---------|---------|
| 프로젝트 | Todo List | 쿠폰 시스템 |
| 비즈니스 로직 | 간단 (CRUD) | 복잡 (조건, 계산, 검증) |
| 테스트 수 | ~25개 | ~50개 |
| 커버리지 목표 | 80% | 90% |
| 예상 시간 | 4-6시간 | 8-12시간 |

### 기술 수준

**Level 1**:
- ✅ 기본 TDD 사이클
- ✅ 단순 테스트 작성
- ✅ AI와 기본 대화

**Level 2**:
- ✅ 고급 TDD 패턴
- ✅ 복잡한 테스트 전략
- ✅ AI 최적 활용
- ✅ 프롬프트 엔지니어링

---

## 🔗 다음 단계

Level 2를 완료했다면:

1. [Level 3: 고급](../level-3-advanced/README.md)으로 진행
2. 멀티 에이전트 시스템 학습
3. 아키텍트-빌더 패턴 실습
4. 대규모 프로젝트 설계

---

## 📚 참고 자료

### 핵심 개념
- [TDD 심화](../docs/concepts/tdd-advanced.md)
- [프롬프트 엔지니어링](../docs/concepts/prompt-engineering.md)
- [AI 에이전트 활용](../docs/concepts/ai-agents.md)

### 추천 학습 자료
- Kent Beck - "Test-Driven Development: By Example"
  - 특히 "Money Example" 파트
- Martin Fowler - "Refactoring"
- OpenAI - "Prompt Engineering Guide"

---

## 🆘 도움이 필요하신가요?

### 학습 자료
- [FAQ](../docs/references/faq.md)
- [문제 해결 가이드](../docs/setup/troubleshooting.md)

### 커뮤니티
- [GitHub Issues](https://github.com/arch-shlee/vibe-coding-lab/issues)
- [GitHub Discussions](https://github.com/arch-shlee/vibe-coding-lab/discussions)

---

## 🎉 시작할 준비가 되셨나요?

[01-red-green-refactor](./01-red-green-refactor/)로 이동하여 첫 번째 모듈을 시작하세요!

**Let's Level Up! 🚀**

---

**레벨**: 중급 (Level 2)
**예상 시간**: 2-3주
**난이도**: ⭐⭐⭐☆☆
**작성일**: 2026-01-18
