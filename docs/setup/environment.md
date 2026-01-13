# Python 개발 환경 설정

> Vibe Coding Lab 학습을 위한 로컬 Python 환경 구성

## 📋 개요

이 가이드는 Vibe Coding Lab에서 Python 코드를 작성하고 테스트하기 위한 로컬 환경 설정 방법을 안내합니다.

---

## 🐍 Python 설치

### 1. Python 버전 확인

먼저 Python이 설치되어 있는지 확인하세요:

```bash
python --version
# 또는
python3 --version
```

**필요 버전**: Python 3.9 이상

### 2. Python 설치 (필요시)

#### Windows
1. [Python 공식 사이트](https://www.python.org/downloads/) 방문
2. "Download Python 3.x.x" 클릭
3. 설치 시 **"Add Python to PATH"** 체크 ✅
4. "Install Now" 클릭

<!-- 📸 TODO: 스크린샷 추가 - python-install-windows.png -->

#### macOS
```bash
# Homebrew 사용 (권장)
brew install python3

# 또는 공식 인스톨러 사용
# https://www.python.org/downloads/macos/
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

---

## 📦 가상 환경 설정

### 1. 가상 환경이란?

프로젝트별로 독립된 Python 환경을 만들어 패키지 충돌을 방지합니다.

### 2. 가상 환경 생성

프로젝트 루트에서:

```bash
# vibe-coding-lab 디렉토리로 이동
cd vibe-coding-lab

# 가상 환경 생성
python -m venv venv

# 또는 python3
python3 -m venv venv
```

### 3. 가상 환경 활성화

#### Windows
```bash
# Command Prompt
venv\Scripts\activate

# PowerShell
venv\Scripts\Activate.ps1

# Git Bash
source venv/Scripts/activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

활성화되면 프롬프트 앞에 `(venv)` 표시:
```
(venv) $
```

### 4. 가상 환경 비활성화

```bash
deactivate
```

---

## 🧪 pytest 설치

TDD 학습을 위해 pytest를 설치합니다.

### 1. pytest 설치

```bash
# 가상 환경이 활성화된 상태에서
pip install pytest

# 버전 확인
pytest --version
```

### 2. pytest 플러그인 설치 (권장)

```bash
# 코드 커버리지 측정
pip install pytest-cov

# 더 나은 출력
pip install pytest-sugar

# 병렬 실행
pip install pytest-xdist
```

### 3. requirements.txt 생성

```bash
# 현재 설치된 패키지 목록 저장
pip freeze > requirements.txt
```

---

## 🛠️ 코드 에디터 설정

### VS Code (권장)

#### 1. VS Code 설치
- [VS Code 다운로드](https://code.visualstudio.com/)

#### 2. Python 확장 설치
1. VS Code 실행
2. 좌측 Extensions 아이콘 클릭 (Ctrl+Shift+X)
3. "Python" 검색
4. Microsoft의 "Python" 확장 설치

<!-- 📸 TODO: 스크린샷 추가 - vscode-python-extension.png -->

#### 3. Python 인터프리터 선택
1. `Ctrl+Shift+P` (Command Palette)
2. "Python: Select Interpreter" 입력
3. 가상 환경의 Python 선택 (`./venv/bin/python`)

<!-- 📸 TODO: 스크린샷 추가 - vscode-select-interpreter.png -->

#### 4. 유용한 VS Code 확장

```
- Python (Microsoft)
- Pylance (Microsoft)
- Python Test Explorer
- autoDocstring
- Python Indent
```

### VS Code 설정 (선택사항)

프로젝트에 `.vscode/settings.json` 생성:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
```

---

## ✅ 환경 설정 확인

모든 설정이 완료되었는지 확인:

### 1. Python 테스트

```bash
# Python 버전 확인
python --version

# 인터프리터 경로 확인
which python  # macOS/Linux
where python  # Windows
```

### 2. pytest 테스트

간단한 테스트 파일 생성:

```bash
# test_hello.py 생성
cat > test_hello.py << 'EOF'
def test_hello():
    assert "Hello" == "Hello"

def test_addition():
    assert 1 + 1 == 2
EOF

# 테스트 실행
pytest test_hello.py
```

성공 메시지가 표시되면 환경 설정 완료!

```
==================== 2 passed in 0.01s ====================
```

### 3. 체크리스트

- [ ] Python 3.9 이상 설치 완료
- [ ] 가상 환경 생성 및 활성화 성공
- [ ] pytest 설치 및 실행 성공
- [ ] VS Code 설치 및 Python 확장 설정
- [ ] 테스트 파일 실행 확인

---

## 🎯 프로젝트별 환경 설정

각 Level의 모듈로 이동할 때마다:

```bash
# 예: Level 1의 첫 모듈
cd level-1-basics/01-hello-vibe/starter

# 가상 환경 활성화 (프로젝트 루트에서 생성한 경우)
source ../../../venv/bin/activate  # macOS/Linux
..\..\..\venv\Scripts\activate     # Windows

# 필요한 패키지 설치 (requirements.txt가 있는 경우)
pip install -r requirements.txt

# 테스트 실행
pytest
```

---

## 🔧 추가 도구 (선택사항)

### 코드 포맷터: Black

```bash
pip install black

# 사용법
black your_file.py
```

### 린터: Pylint

```bash
pip install pylint

# 사용법
pylint your_file.py
```

### 타입 체커: mypy

```bash
pip install mypy

# 사용법
mypy your_file.py
```

---

## 🆘 문제 해결

### 문제 1: "python: command not found"

**해결책**:
```bash
# python3로 시도
python3 --version

# 별칭 설정 (macOS/Linux)
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc
```

### 문제 2: pip 권한 오류

**해결책**:
```bash
# --user 플래그 사용
pip install --user pytest

# 또는 가상 환경 사용 (권장)
python -m venv venv
source venv/bin/activate
pip install pytest
```

### 문제 3: pytest를 찾을 수 없음

**해결책**:
```bash
# 가상 환경이 활성화되었는지 확인
# (venv) 표시가 있어야 함

# pytest 재설치
pip install --upgrade pytest

# 경로에서 직접 실행
python -m pytest
```

---

## 🔗 다음 단계

1. [Level 1 시작하기](../../level-1-basics/README.md)
2. [바이브코딩 개념](../concepts/vibe-coding.md)
3. [TDD 기초](../concepts/tdd-basics.md)

---

## 📸 이미지 가이드

**이 문서에 필요한 스크린샷 목록:**

| 파일명 | 설명 |
|--------|------|
| `python-install-windows.png` | Windows Python 설치 화면 |
| `vscode-python-extension.png` | VS Code Python 확장 설치 |
| `vscode-select-interpreter.png` | Python 인터프리터 선택 화면 |

**이미지 저장 경로**: `docs/setup/images/`

---

**작성일**: 2026-01-13
**작성자**: arch-shlee & Claude (협업)
**상태**: 초안 (이미지 추가 필요)
