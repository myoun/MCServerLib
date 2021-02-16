MCServerLib
===========

MCServerLib은 마인크래프트 서버 세팅을 위한 파이썬 라이브러리입니다.

# 설치

### PyPi에서:

`pip install MCServerLib`


### 깃허브 레포에서:

`python -m pip install git+https://github.com/myoung2namur/MCServerLib`

# 사용법

```py
import MCServerLib as mcs

properties = mcs.Prop.Properties()
properties.properties['enable-command-block'] = 'true'

setup = mcs.Setup.Setup(version='1.16.5',xmx='1024M',xms='3G',properties=properties)

# 서버 파일 세팅

# 모든 파일 다운로드 (권장)
setup.downloadAll() 

# 페이퍼 버킷만 다운로드
setup.downloadPaper()

# 베치파일만 작성
setup.makeBatch()

# EULA 파일만 작성
setup.makeEula()