import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image as PILImage
import io
import matplotlib.pyplot as plt


# 폰트지정
plt.rcParams['font.family'] = 'Malgun Gothic'


# 모델 로드
@st.cache_resource
def load_cnn_model():
    model = load_model('./model/cat_dog_classification_model.h5')
    return model

model = load_cnn_model()

# 클래스 이름 정의
class_names = ['Cat', 'Dog']

# 제목
st.title("강아지 🐶 vs 고양이 🐱 분류기")
st.write("이미지를 여러 개 업로드하면 AI가 강아지인지 고양이인지 각각 알려드립니다!")

# 여러 이미지 업로더
uploaded_files = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    # 결과 저장용 리스트
    predictions_list = []
    image_names = []

    # 업로드된 이미지 처리
    for uploaded_file in uploaded_files:
        # 이미지 표시
        st.image(uploaded_file, caption=f'업로드한 이미지: {uploaded_file.name}', use_container_width=True)
        
        # 이미지 전처리
        img = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(180, 180))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        # 예측
        prediction = model.predict(img_array)
        predictions_list.append(prediction[0])
        image_names.append(uploaded_file.name)

        # 예측 결과 출력
        st.write(f"### {uploaded_file.name} 예측 결과")
        st.write("클래스별 확률:")
        for i, class_name in enumerate(class_names):
            st.write(f"{class_name}: {prediction[0][i]*100:.2f}%")
        
        predicted_class = class_names[np.argmax(prediction)]
        st.success(f"이 이미지는 **{predicted_class}** 입니다!")

    # 시각화
    st.write("### 모든 이미지의 예측 확률 시각화")
    fig, ax = plt.subplots(figsize=(10, 6))

    # 각 이미지의 확률을 막대그래프로 표시
    bar_width = 0.35
    x = np.arange(len(image_names))
    cat_probs = [pred[0] * 100 for pred in predictions_list]  # Cat 확률
    dog_probs = [pred[1] * 100 for pred in predictions_list]  # Dog 확률

    ax.bar(x - bar_width/2, cat_probs, bar_width, label='Cat', color='skyblue')
    ax.bar(x + bar_width/2, dog_probs, bar_width, label='Dog', color='salmon')

    # 그래프 설정
    ax.set_xlabel('이미지')
    ax.set_ylabel('확률 (%)')
    ax.set_title('각 이미지의 Cat vs Dog 예측 확률')
    ax.set_xticks(x)
    ax.set_xticklabels(image_names, rotation=45, ha='right')
    ax.legend()

    # 그래프 출력
    plt.tight_layout()
    st.pyplot(fig)

else:
    st.write("이미지를 업로드해주세요.")
