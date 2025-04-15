# pt.py
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image as PILImage
import io

# 모델 로드
@st.cache_resource
def load_cnn_model():
    model = load_model('./model/painting4_classification_model.h5')
    return model

model = load_cnn_model()

# 클래스 이름 정의 (폴더명 기준)
#  Andy_Warhol , Frida_Kahlo, Kazimir_Malevich, Paul_Klee
class_names = ['Andy Warhol(앤디 워홀)', 'Frida Kahlo(프리다 칼로)', 'Paul Klee(파울 클레)', 'Salvador Dali(살바도르 달리)']

# 제목
st.title("화풍 분류기")
st.write("이미지를 업로드하면 AI가 어떤 화풍인지 알려드립니다!")

st.markdown(
    "<span style='font-weight:bold;'>앤디 워홀, 프리다 칼로, 파울 클레, 살바도르 달리</span> 중 아무 그림을 업로드하면 예측할 수 있습니다!",
    unsafe_allow_html=True
)
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='업로드한 이미지', use_container_width=True)
    img = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(180, 180))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  


    # 예측
    prediction = model.predict(img_array)
    
    #  예측 디버깅
    # st.write("예측 결과 (Softmax):", prediction)
    st.write("클래스별 확률:")
    max_index = np.argmax(prediction)

    for i, class_name in enumerate(class_names):
        prob = prediction[0][i] * 100
        if i == max_index:
            # 확률이 가장 높은 경우 색상 강조
            st.markdown(f"<span style='color:SteelBlue; font-weight:bold'>{class_name}: {prob:.2f}%</span>", unsafe_allow_html=True)
        else:
            st.write(f"{class_name}: {prob:.2f}%")
    
    # for i, class_name in enumerate(class_names):
    #     st.write(f"{class_name}: {prediction[0][i]*100:.2f}%")
    
    predicted_class = class_names[np.argmax(prediction)]

    # 출력
    st.success(f"이 이미지는 **{predicted_class}** 화풍일 가능성이 높습니다!")
