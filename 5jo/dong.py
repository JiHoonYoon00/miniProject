import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np



option = st.sidebar.selectbox(
    'HOUSE TYPE을 골라주세요',('아파트', '단독다가구', '오피스텔', '연립다세대')
    )
data = pd.read_csv(f'data1/{option}.csv')
# 사용자 입력을 통한 데이터 선택
selected_SGG = st.selectbox('구를 선택해주세요:', data['SGG_NM'].unique())
selected_index = st.selectbox('동을 선택해주세요:', data.loc[data['SGG_NM'] == selected_SGG, 'BJDONG_NM'].unique())




# PyDeck 차트 표시
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=37.5665,  # 서울시 중심 좌표
        longitude=126.9780,
        zoom=10,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ColumnLayer',
            data=data,
            get_position=['CENTER_LONG', 'CENTER_LATI'],
            get_elevation='PRICE_PER',
            elevation_scale=0.5,  # 높이 스케일 조정
            radius=100,  # 막대의 반지름
            get_fill_color=[255, 165, 0, 100],  # 막대 색상 설정
            pickable=True,
            auto_highlight=True,
        ),
        pdk.Layer(
            'ColumnLayer',
            data=data[data['BJDONG_NM'] == selected_index],
            get_position=['CENTER_LONG', 'CENTER_LATI'],
            get_elevation='PRICE_PER',
            elevation_scale=0.5,  # 높이 스케일 조정
            radius=200,  # 막대의 반지름
            get_fill_color=[0, 0, 255, 200],  # 막대 색상 설정
            pickable=True,
            auto_highlight=True,
        ),
    ],
))

st.write(data[data['BJDONG_NM'] == selected_index])