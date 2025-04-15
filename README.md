<p align="center">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

# 화가 스타일 분류 AI 프로젝트

## 프로젝트 소개
이 프로젝트는 인공지능을 활용하여 그림의 화풍을 분석하고 어떤 화가의 작품인지 분류하는 모델을 구현했습니다. 4명의 유명 화가 작품을 학습시켜 새로운 그림이 어떤 화가의 스타일인지 예측합니다.

## 기술 스택
- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pandas

## 설치 방법
프로젝트를 실행하기 위해 다음 단계를 따라주세요:

```bash
# 저장소 클론
git clone [저장소 URL]
cd [프로젝트 폴더명]

# 필요한 패키지 설치
pip install -r requirements.txt
```

## 실행 방법
설치가 완료되면 다음 명령어로 애플리케이션을 실행할 수 있습니다:

```bash
streamlit run app.py
```

## 데이터셋
이 프로젝트는 Kaggle의 "Collections of Paintings from 50 Artists" 데이터셋을 활용했으며, 4명의 화가 작품으로 범위를 좁혀 학습을 진행했습니다.

## 개발 후기 및 느낀점

이번 프로젝트를 진행하면서 처음에 계획했던 방향은 지금과 조금 달랐습니다. 처음에는 Kaggle에서 "I'm Something of a Painter Myself"라는 이미지를 업로드하면 모네 그림 스타일로 변환하는 챌린지를 발견했는데, 주제가 흥미로워서 도전해보고 싶었습니다. 참가자들의 코드를 따라 해봤지만, 배우지 않은 내용이 너무 많았고 학습 과정에서 기술적 문제(빈번한 튕김 현상 등)로 인해 반나절을 허비하게 됐습니다.

남은 시간은 하루와 PPT 작성에 반나절뿐이라 시간이 촉박했어요. 결국 좀 더 간단한 주제로 방향을 틀어서 CNN 기반으로 강아지와 고양이를 분류하는 모델을 만들어봤습니다. 모델은 나름 완성했는데, 털이 많거나 귀가 쫑긋한 강아지를 자꾸 고양이로 오분류 하더라고요. 그래도 프로토타입 화면과 PPT까지 다 준비했지만, 솔직히 이 주제가 더 재밌을 것 같아서 여기엔 담지 않기로 했습니다.

그 후에 시간이 조금 남아서 다시 Kaggle을 뒤적이다가 "Collections of Paintings from 50 Artists"라는 데이터셋을 발견했습니다. 아무래도 그림 주제에 대한 미련이 마음 한구석에 남아 있었던 것 같아요. 결국 그림에 대한 집착이 다시 발동해서 이 데이터셋을 활용해보기로 했습니다.

처음에는 50명이나 되는 화가를 다 다루기엔 무리가 있다고 판단해서 5명으로 추려서 모델 학습을 시작했습니다. 하지만 이 과정도 쉽지 않았습니다. 화풍을 예측하려면 그림의 구조가 어느 정도 비슷해야 했는데, 그렇다고 샘플 이미지를 하나하나 고르자니 학습에 사용할 데이터가 너무 적어져서 의미가 없어지더라고요. 그래서 클래스를 여러 번 조정하며 실험을 반복했고, 결국 4명의 화가로 범위를 좁혀 모델을 완성했습니다.

그런데 결과는 썩 만족스럽지 않았습니다. 예측 정확도가 60% 정도밖에 안 나오더라고요. 이번 경험을 통해 데이터셋의 중요성을 뼈저리게 깨달았고, 앞으로는 주제 선정에 좀 더 신중하게 시간을 투자해야겠다는 생각이 들었습니다.

처음의 화려한 아이디어에서 시작해 여러 시행착오를 거치며 결국 현실적인 한계를 마주한 과정이었지만, 그 속에서 많은 배움을 얻은 것 같습니다.

## 이메일
[ssszzy333@gmail.com]

## 블로그
[ssuuoo12.github.io]
