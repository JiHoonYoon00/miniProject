import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

df = pd.read_csv('dandok.csv')
# 서울시 각 구의 중심 좌표와 임의의 데이터 예시

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
            data=df,
            get_position=['CENTER_LONG', 'CENTER_LATI'],
            get_elevation='PRICE_PER',
            elevation_scale=0.5,  # 높이 스케일 조정
            radius=100,  # 막대의 반지름
            get_fill_color=[255, 165, 0, 100],  # 막대 색상 설정
            pickable=True,
            auto_highlight=True,
        ),
    ],
))
