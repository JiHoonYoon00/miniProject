import streamlit as st
import pandas as pd
import pydeck as pdk

# 강북구 중심의 위도와 경도
gangbuk_center = [37.6393, 127.0257]

# 주택 유형별 평균값 데이터
data = {
    'House_Type': ['단독다가구', '아파트', '연립다세대', '오피스텔'],
    'Value': [1896.405107, 2949.369926, 1698.954434, 1921.627272],
    'lat': [37.637, 37.6385, 37.64, 37.6415],  # 막대의 위치 조정으로 간격 증가
    'lon': [127.023, 127.0245, 127.026, 127.0275],
    # 각 주택 유형별로 다른 색상 및 투명도 조정 (RGBA 형식)
    'color': [[255, 0, 0, 120], [0, 255, 0, 120], [0, 0, 255, 120], [255, 255, 0, 120]]
}

df = pd.DataFrame(data)

# PyDeck 차트 표시
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=gangbuk_center[0],
        longitude=gangbuk_center[1],
        zoom=14,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ColumnLayer',
            data=df,
            get_position=['lon', 'lat'],
            get_elevation='Value',
            elevation_scale=3,  # 높이 스케일 조정
            radius=400,  # 막대의 반지름
            get_fill_color='color',  # 각 막대의 색상 및 투명도 지정
            pickable=True,
            auto_highlight=True,
        ),
    ],
))