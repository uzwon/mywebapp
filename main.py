import re
import requests
import pandas as pd
import streamlit as st
import plotly.express as px


# =========================================================
# 0. 페이지 설정
# =========================================================
st.set_page_config(
    page_title="전국 인구 구조 지도",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 전국 인구 구조 지도")
st.caption(
    "행정안전부 주민등록 인구 데이터를 이용해 "
    "시군구별 고령화율과 유소년율을 비교합니다."
)


# =========================================================
# 1. 데이터 주소
# =========================================================
POP_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/"
    "main/data/population_yearly.csv.gz"
)

GEO_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/"
    "main/data/boundaries/sigungu_kr.geojson"
)


# =========================================================
# 2. 데이터 불러오기
# =========================================================
@st.cache_data(show_spinner="인구 데이터를 불러오는 중입니다...")
def load_population():

    # 코드의 앞자리 0 등이 사라지지 않도록 문자열로 읽음
    df = pd.read_csv(
        POP_URL,
        dtype={"코드": str}
    )

    return df


@st.cache_data(show_spinner="지도 경계를 불러오는 중입니다...")
def load_geojson():

    response = requests.get(
        GEO_URL,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


df_all = load_population()
geojson = load_geojson()


# =========================================================
# 3. 지도 경계 파일에서 지역 이름 정리
# =========================================================
names = pd.DataFrame(
    [
        {
            "시군구코드": str(feature["properties"]["코드"]),
            "시군구": feature["properties"]["시군구"],
            "시도": feature["properties"]["시도"],
        }
        for feature in geojson["features"]
    ]
)

# 혹시 중복된 코드가 있을 경우 제거
names = names.drop_duplicates(
    subset="시군구코드"
)


# =========================================================
# 4. 연령 계산 함수
# =========================================================
def age_of(column_name):

    match = re.match(
        r"계_(\d+)세",
        column_name
    )

    if match:
        return int(match.group(1))

    return None


# '계_'로 시작하는 열만 사용
# 남_ / 여_ 열까지 더하면 인구가 중복 계산되므로 사용하지 않음
total_cols = [
    col
    for col in df_all.columns
    if col.startswith("계_")
]


# 65세 이상 인구 열
elderly_cols = [
    col
    for col in total_cols
    if age_of(col) is not None
    and age_of(col) >= 65
]


# 0~14세 유소년 인구 열
youth_cols = [
    col
    for col in total_cols
    if age_of(col) is not None
    and 0 <= age_of(col) <= 14
]


# =========================================================
# 5. 옛 행정구역 코드 → 현재 경계 코드 변환
# =========================================================
def convert_sigungu_code(code):

    code = str(code).zfill(5)

    # -----------------------------
    # 군위군
    # 경상북도 군위군 → 대구광역시 군위군
    # -----------------------------
    if code == "47720":
        return "27720"

    # -----------------------------
    # 옛 강원도 코드 42
    # → 강원특별자치도 코드 51
    # -----------------------------
    if code.startswith("42"):
        return "51" + code[2:]

    # -----------------------------
    # 옛 전라북도 코드 45
    # → 전북특별자치도 코드 52
    # -----------------------------
    if code.startswith("45"):
        return "52" + code[2:]

    return code


# =========================================================
# 6. 선택 메뉴
# =========================================================

control1, control2, control3 = st.columns(
    [2, 2, 2]
)


# ---------------------------------------------------------
# 연도 선택
# ---------------------------------------------------------
years = sorted(
    df_all["연도"]
    .dropna()
    .astype(int)
    .unique()
)

min_year = int(min(years))
max_year = int(max(years))


with control1:

    selected_year = st.slider(
        "📅 연도 선택",
        min_value=min_year,
        max_value=max_year,
        value=max_year,
        step=1
    )


# ---------------------------------------------------------
# 지표 선택
# ---------------------------------------------------------
with control2:

    selected_indicator = st.selectbox(
        "📊 지표 선택",
        [
            "65세 이상 고령화율",
            "0~14세 유소년율"
        ]
    )


# ---------------------------------------------------------
# 시도 선택
# ---------------------------------------------------------
province_list = sorted(
    names["시도"]
    .dropna()
    .unique()
)

with control3:

    selected_province = st.selectbox(
        "📍 지역 선택",
        ["전국"] + province_list
    )


# =========================================================
# 7. 선택한 연도 데이터만 추출
# =========================================================
df = df_all[
    df_all["연도"].astype(int)
    == selected_year
].copy()


# =========================================================
# 8. 전체 인구 / 고령 인구 / 유소년 인구 계산
# =========================================================
df["전체인구"] = df[
    total_cols
].sum(axis=1)


df["고령인구"] = df[
    elderly_cols
].sum(axis=1)


df["유소년인구"] = df[
    youth_cols
].sum(axis=1)


# =========================================================
# 9. 시군구 코드 생성
# =========================================================
# 읍면동 코드의 앞 5자리 = 시군구 코드

df["시군구코드"] = (
    df["코드"]
    .astype(str)
    .str[:5]
)


# 행정구역 개편 코드 변환
df["시군구코드"] = (
    df["시군구코드"]
    .apply(convert_sigungu_code)
)


# =========================================================
# 10. 시군구 단위로 합계 계산
# =========================================================
grouped = (
    df.groupby("시군구코드")[
        [
            "전체인구",
            "고령인구",
            "유소년인구"
        ]
    ]
    .sum()
    .reset_index()
)


# =========================================================
# 11. 비율 계산
# =========================================================

grouped["고령화율"] = (
    grouped["고령인구"]
    / grouped["전체인구"]
    * 100
).round(2)


grouped["유소년율"] = (
    grouped["유소년인구"]
    / grouped["전체인구"]
    * 100
).round(2)


# =========================================================
# 12. 전국 전체 비율 계산
# =========================================================

national_population = df[
    "전체인구"
].sum()


national_elderly = df[
    "고령인구"
].sum()


national_youth = df[
    "유소년인구"
].sum()


national_elderly_rate = (
    national_elderly
    / national_population
    * 100
)


national_youth_rate = (
    national_youth
    / national_population
    * 100
)


# =========================================================
# 13. 현재 지도 경계와 데이터 연결
# =========================================================

# 여기서는 지도 경계 파일을 기준으로 merge함
# 따라서 해당 연도에 데이터가 없는 현재 행정구역도
# 지도에는 남아 있고 회색으로 표시할 수 있음

map_df = names.merge(
    grouped,
    on="시군구코드",
    how="left"
)


# =========================================================
# 14. 지도 경계와 맞지 않는 옛 코드 확인
# =========================================================

boundary_codes = set(
    names["시군구코드"]
)

population_codes = set(
    grouped["시군구코드"]
)


unmatched_codes = sorted(
    population_codes
    - boundary_codes
)


# =========================================================
# 15. 선택 지표에 따라 설정 변경
# =========================================================

if selected_indicator == "65세 이상 고령화율":

    rate_column = "고령화율"

    population_column = "고령인구"

    metric_name = "고령화율"

    national_rate = national_elderly_rate

    # -----------------------------------------------------
    # 고령화율 색 구간
    # 모든 연도에서 반드시 동일하게 사용
    # -----------------------------------------------------
    BINS = [
        0,
        19,
        23,
        28,
        38,
        float("inf")
    ]

    LABELS = [
        "19% 미만",
        "19~23%",
        "23~28%",
        "28~38%",
        "38% 이상"
    ]

    COLORS = {
        "19% 미만": "#fee6ce",
        "19~23%": "#fdc086",
        "23~28%": "#f79646",
        "28~38%": "#e8590c",
        "38% 이상": "#a63603",
        "자료 없음": "#d9d9d9"
    }


else:

    rate_column = "유소년율"

    population_column = "유소년인구"

    metric_name = "유소년율"

    national_rate = national_youth_rate

    # -----------------------------------------------------
    # 유소년율 전용 색 구간
    #
    # 고령화율보다 값이 작기 때문에
    # 별도의 구간 사용
    #
    # 이 경계값 역시 연도가 변해도 유지됨
    # -----------------------------------------------------
    BINS = [
        0,
        8,
        10,
        12,
        14,
        float("inf")
    ]

    LABELS = [
        "8% 미만",
        "8~10%",
        "10~12%",
        "12~14%",
        "14% 이상"
    ]

    COLORS = {
        "8% 미만": "#edf8fb",
        "8~10%": "#b3cde3",
        "10~12%": "#8c96c6",
        "12~14%": "#8856a7",
        "14% 이상": "#810f7c",
        "자료 없음": "#d9d9d9"
    }


# =========================================================
# 16. 색상 단계 생성
# =========================================================

map_df["단계"] = pd.cut(
    map_df[rate_column],
    bins=BINS,
    labels=LABELS,
    right=False
)


# 자료가 없는 지역은 회색
map_df["단계"] = (
    map_df["단계"]
    .astype("object")
)


map_df.loc[
    map_df[rate_column].isna(),
    "단계"
] = "자료 없음"


# =========================================================
# 17. 최고 / 최저 지역 계산
# =========================================================

# 현재 지도 경계와 실제로 연결된 지역 중에서 계산
valid_regions = map_df.dropna(
    subset=[rate_column]
).copy()


highest_region = valid_regions.loc[
    valid_regions[rate_column].idxmax()
]


lowest_region = valid_regions.loc[
    valid_regions[rate_column].idxmin()
]


# =========================================================
# 18. 지도 위 지표 카드 3개
# =========================================================

st.markdown("---")

metric1, metric2, metric3 = st.columns(3)


with metric1:

    st.metric(
        label=f"🇰🇷 전국 {metric_name}",
        value=f"{national_rate:.2f}%"
    )


with metric2:

    st.metric(
        label=f"🔴 {metric_name} 가장 높은 시군구",
        value=(
            f"{highest_region['시군구']} "
            f"{highest_region[rate_column]:.2f}%"
        ),
        help=highest_region["시도"]
    )


with metric3:

    st.metric(
        label=f"🟢 {metric_name} 가장 낮은 시군구",
        value=(
            f"{lowest_region['시군구']} "
            f"{lowest_region[rate_column]:.2f}%"
        ),
        help=lowest_region["시도"]
    )


# =========================================================
# 19. 시도 선택 적용
# =========================================================

if selected_province == "전국":

    display_df = map_df.copy()

else:

    display_df = map_df[
        map_df["시도"]
        == selected_province
    ].copy()


# =========================================================
# 20. 지도 제목
# =========================================================

if selected_province == "전국":

    st.subheader(
        f"🗺️ 전국 {metric_name} · {selected_year}년"
    )

else:

    st.subheader(
        f"🗺️ {selected_province} {metric_name} · {selected_year}년"
    )


# =========================================================
# 21. 단계구분도 생성
# =========================================================

fig = px.choropleth(
    display_df,

    geojson=geojson,

    locations="시군구코드",

    featureidkey="properties.코드",

    color="단계",

    category_orders={
        "단계": LABELS + ["자료 없음"]
    },

    color_discrete_map=COLORS,

    hover_name="시군구",

    hover_data={
        rate_column: ":.2f",
        "시도": True,
        "시군구코드": False,
        "단계": False
    },

    labels={
        rate_column: f"{metric_name}(%)",
        "시도": "시도"
    }
)


# 선택 지역 기준으로 자동 확대
fig.update_geos(
    fitbounds="locations",
    visible=False
)


fig.update_traces(
    marker_line_width=0.5,
    marker_line_color="white"
)


fig.update_layout(

    margin=dict(
        l=0,
        r=0,
        t=10,
        b=0
    ),

    height=720,

    legend_title_text=(
        f"{metric_name} ({selected_year}년)"
    )
)


st.plotly_chart(
    fig,
    width="stretch"
)


# =========================================================
# 22. 행정구역 불일치 안내
# =========================================================

if unmatched_codes:

    preview_codes = ", ".join(
        unmatched_codes[:15]
    )

    if len(unmatched_codes) > 15:
        preview_codes += " ..."

    st.info(
        "ℹ️ 이 연도에는 현재 지도 경계와 일치하지 않는 "
        "옛 행정구역 코드가 일부 존재합니다. "
        "강원·전북의 옛 시도 코드와 군위군 코드는 현재 코드로 "
        "변환했으며, 그 밖에 경계와 연결되지 않는 지역은 "
        "지도에서 회색 또는 미표시될 수 있습니다.\n\n"
        f"현재 확인된 불일치 코드: {preview_codes}"
    )

else:

    st.caption(
        "✅ 선택한 연도의 시군구 코드가 현재 지도 경계와 모두 연결되었습니다."
    )


# =========================================================
# 23. 현재 지도에서 자료가 없는 지역 안내
# =========================================================

no_data_regions = display_df[
    display_df[rate_column].isna()
]


if not no_data_regions.empty:

    st.caption(
        "⬜ 회색 지역은 선택한 연도에 현재 행정구역과 "
        "직접 연결되는 데이터가 없는 지역입니다."
    )


# =========================================================
# 24. 순위 표
# =========================================================

st.markdown("---")


# 선택한 시도 기준으로 순위 표시
ranking_df = display_df.dropna(
    subset=[rate_column]
).copy()


c1, c2 = st.columns(2)


table_columns = [
    "시도",
    "시군구",
    rate_column
]


with c1:

    st.subheader(
        f"🔴 {metric_name} 높은 곳 10"
    )

    high_table = (
        ranking_df
        .nlargest(
            10,
            rate_column
        )[table_columns]
        .reset_index(drop=True)
    )

    high_table.index += 1

    st.dataframe(
        high_table,
        width="stretch"
    )


with c2:

    st.subheader(
        f"🟢 {metric_name} 낮은 곳 10"
    )

    low_table = (
        ranking_df
        .nsmallest(
            10,
            rate_column
        )[table_columns]
        .reset_index(drop=True)
    )

    low_table.index += 1

    st.dataframe(
        low_table,
        width="stretch"
    )


# =========================================================
# 25. 하단 설명
# =========================================================

st.markdown("---")

st.caption(
    "※ 고령화율 = 65세 이상 인구 ÷ 전체 인구 × 100"
)

st.caption(
    "※ 유소년율 = 0~14세 인구 ÷ 전체 인구 × 100"
)

st.caption(
    "※ 연도별 변화를 정확하게 비교하기 위해 "
    "각 지표의 색 구간 경계값은 연도가 바뀌어도 고정됩니다."
)
