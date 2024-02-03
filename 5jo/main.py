import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# 서울 중심의 위도와 경도
seoul_center = [37.5665, 126.9780]

# 랜덤 위도 및 경도 값을 포함하는 DataFrame 생성
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + seoul_center,
   columns=['위도', '경도'])

st.write(chart_data)

# Streamlit을 사용하여 PyDeck 차트 표시
st.pydeck_chart(pdk.Deck(
    # 맵 스타일을 None으로 설정 (기본 스타일 사용)
    map_style=None,
    # 맵의 초기 뷰 상태 설정
    initial_view_state=pdk.ViewState(
        latitude=seoul_center[0],  # 서울의 위도를 초기값으로 설정
        longitude=seoul_center[1],  # 서울의 경도를 초기값으로 설정
        zoom=11,              # 초기 줌 레벨 설정
        pitch=50,             # 초기 피치 (기울임) 설정
    ),
    # 맵에 대한 레이어 정의
    layers=[
        # HexagonLayer: 맵에 육각형 형태의 빈 표시
      pdk.Layer(
           'HexagonLayer',
           data=chart_data,     # DataFrame을 데이터 소스로 사용
           get_position='[경도, 위도]',  # 위치 좌표 지정
           radius=200,          # 육각형의 반지름 설정
           elevation_scale=4,   # 고도 스케일 설정
           elevation_range=[0, 1000],  # 고도 범위 설정
           pickable=True,       # 육각형 선택 가능하게 설정
           extruded=True,       # 육각형을 3차원으로 확장
        ),
        # ScatterplotLayer: 맵에 개별 데이터 포인트 표시
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,     # DataFrame을 데이터 소스로 사용
            get_position='[경도, 위도]',  # 위치 좌표 지정
            get_color='[200, 30, 0, 160]',  # 데이터 포인트의 색상 지정
            get_radius=200,       # 데이터 포인트의 반지름 설정
        ),
    ],
))

pdk.Layer(
    'HexagonLayer',
    data=chart_data,  # 위도, 경도, 법정동코드, 높이 데이터를 가진 DataFrame을 사용
    get_position='[경도, 위도]',  # 위치 좌표 지정
    auto_highlight=True,  # 강조 효과 자동 활성화
    radius=200,  # 육각형의 반지름 설정
    elevation_scale=chart_data['높이'].max(),  # 고도 스케일 설정 (최대 높이로 설정)
    elevation_range=[0, chart_data['높이'].max()],  # 고도 범위 설정 (0부터 최대 높이까지)
    pickable=True,  # 육각형 선택 가능하게 설정
    extruded=True,  # 육각형을 3차원으로 확장
)