import streamlit as st
from PIL import Image
import time

st.title('心の描画アプリ　～Imano Kimochi～')
#スクレイピングで画像を探す、またはストック画像をランダムに描画、またはストック画像をボタンに割り振っておく
st.title('Welcome!')

condision = st.slider('スライダーを動かしてあなたの調子を教えて！', 0, 100, 50)
'あなたの調子：', condision

ready = st.radio('準備は良いですか？', ('no', 'yes'), horizontal=True)
if ready == 'yes':
    st.write('あなたの心をスキャンします。心の準備をして下さい。')
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Now Loading... {i+1}')
        bar.progress(i + 1)
        time.sleep(0.03)
        
    if condision >=80:
        img = Image.open('pink_image.png')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 70 <= condision <= 79:
        img = Image.open('programing.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 60 <= condision <= 69:
        img = Image.open('heart.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 50 <= condision <= 59:
        img = Image.open('rainbow.png')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 40 <= condision <= 49:
        img = Image.open('yellow_tree.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 30 <= condision <= 39:
        img = Image.open('csl.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 20 <= condision <= 29:
        img = Image.open('f.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 10 <= condision <= 19:
        img = Image.open('Fresh pink rose -2.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)
    elif 0 <= condision <= 9:
        img = Image.open('japan_csl.jpg')
        st.image(img, caption='診断結果：あなたは元気！', use_column_width=True)





# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('右カラムです。')

# st.sidebar.text('たまにある質問')
st.text('たまにある質問')
expander1 = st.expander('いつ使うアプリですか？')
expander1.write('あなたが気分を害した時')
expander2 = st.expander('このアプリで何が得られますか？')
expander2.write('現実逃避します　※根本の問題は解決しません')
expander3 = st.expander('これまでの評判は？')
expander3.write('ご自身でお確かめください')

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# option = st.selectbox(
#     'ああなたが好きな数字を教えて。',
#     list(range(1,11)))
# f'あなたが好きな数字は{option}です。'

# feel = st.sidebar.text_input('今の天気は？')
# '今の天気：', feel