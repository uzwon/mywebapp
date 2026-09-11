import streamlit as st


# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="MBTI Trip Pick",
    page_icon="✈️",
    layout="centered"
)


# =========================
# 디자인
# =========================
st.markdown(
    """
<style>

/* 전체 배경 */
.stApp {
    background: linear-gradient(
        135deg,
        #fffafc 0%,
        #f8f6ff 100%
    );
}

/* 화면 폭 */
.block-container {
    max-width: 700px;
    padding-top: 3.5rem;
    padding-bottom: 3rem;
}

/* 작은 상단 텍스트 */
.label {
    text-align: center;
    color: #c98da4;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

/* 메인 제목 */
.title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #4e4453;
    margin-bottom: 8px;
}

/* 부제목 */
.subtitle {
    text-align: center;
    color: #9c8f9f;
    font-size: 16px;
    margin-bottom: 35px;
}

/* selectbox */
div[data-baseweb="select"] > div {
    border-radius: 14px;
    border: 1px solid #eadde5;
    background-color: white;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    height: 52px;
    border: none;
    border-radius: 14px;
    background: linear-gradient(
        90deg,
        #f5b8c7,
        #d7c5f5
    );
    color: white;
    font-weight: 700;
    font-size: 16px;
    margin-top: 12px;
}

.stButton > button:hover {
    color: white;
    border: none;
    opacity: 0.92;
}

/* 결과 카드 */
.result-card {
    margin-top: 28px;
    padding: 32px 28px;
    background: white;
    border-radius: 24px;
    border: 1px solid #f0e2e8;
    box-shadow: 0 10px 30px rgba(120, 90, 110, 0.08);
    text-align: center;
}

/* 이모지 */
.emoji {
    font-size: 52px;
    margin-bottom: 10px;
}

/* MBTI */
.mbti {
    color: #c58aa1;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
}

/* 여행지 */
.place {
    font-size: 34px;
    font-weight: 800;
    color: #4e4453;
    margin-top: 8px;
}

/* 국가 */
.country {
    color: #a699a8;
    font-size: 14px;
    margin-top: 3px;
}

/* 한줄 설명 */
.reason {
    margin-top: 20px;
    background-color: #fff7fa;
    padding: 17px 18px;
    border-radius: 16px;
    color: #665d69;
    line-height: 1.7;
    text-align: left;
}

/* 태그 */
.tag {
    display: inline-block;
    margin: 4px 2px;
    padding: 6px 11px;
    border-radius: 18px;
    background-color: #f7e8ee;
    color: #b77690;
    font-size: 12px;
    font-weight: 600;
}

/* 하단 */
.footer {
    text-align: center;
    margin-top: 40px;
    color: #c1b6c1;
    font-size: 12px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================
# MBTI별 여행지 데이터
# =========================
travel_data = {

    "INTJ": {
        "emoji": "🏛️",
        "place": "빈",
        "country": "오스트리아",
        "tags": ["예술", "사색", "역사"],
        "reason":
            "차분하게 혼자만의 시간을 즐기며 깊이 있게 여행하기 좋은 도시예요. "
            "고전적인 건축과 미술관을 천천히 둘러보는 여행이 잘 어울려요."
    },

    "INTP": {
        "emoji": "🔭",
        "place": "런던",
        "country": "영국",
        "tags": ["박물관", "과학", "탐구"],
        "reason":
            "호기심을 자극하는 박물관과 문화 공간이 많아 "
            "관심 가는 곳을 자유롭게 탐험하기 좋아요."
    },

    "ENTJ": {
        "emoji": "🌆",
        "place": "뉴욕",
        "country": "미국",
        "tags": ["도시", "도전", "에너지"],
        "reason":
            "빠르게 움직이는 도시의 에너지와 다양한 경험을 즐기기 좋아요. "
            "계획적으로 여러 장소를 돌아보기에도 잘 맞아요."
    },

    "ENTP": {
        "emoji": "🎨",
        "place": "바르셀로나",
        "country": "스페인",
        "tags": ["개성", "자유", "건축"],
        "reason":
            "독특한 건축물과 자유로운 분위기가 가득해 "
            "새로운 경험을 좋아하는 성향과 잘 어울려요."
    },

    "INFJ": {
        "emoji": "🌿",
        "place": "교토",
        "country": "일본",
        "tags": ["고요함", "전통", "산책"],
        "reason":
            "조용한 거리와 자연, 전통적인 분위기 속에서 "
            "천천히 생각을 정리하며 여행하기 좋아요."
    },

    "INFP": {
        "emoji": "🌷",
        "place": "프라하",
        "country": "체코",
        "tags": ["낭만", "감성", "야경"],
        "reason":
            "동화 같은 거리와 아름다운 야경이 있어 "
            "감성적이고 낭만적인 여행을 좋아하는 사람에게 잘 어울려요."
    },

    "ENFJ": {
        "emoji": "🌺",
        "place": "하와이",
        "country": "미국",
        "tags": ["힐링", "바다", "사람"],
        "reason":
            "따뜻한 분위기와 다양한 활동을 함께 즐길 수 있어 "
            "사람들과 좋은 추억을 만들기 좋아요."
    },

    "ENFP": {
        "emoji": "✨",
        "place": "방콕",
        "country": "태국",
        "tags": ["활기", "먹거리", "즉흥"],
        "reason":
            "먹거리와 시장, 야경 등 새로운 경험이 가득해 "
            "즉흥적이고 활기찬 여행을 즐기기 좋아요."
    },

    "ISTJ": {
        "emoji": "🏰",
        "place": "뮌헨",
        "country": "독일",
        "tags": ["질서", "역사", "안정"],
        "reason":
            "정돈된 도시와 역사적인 건축물이 많아 "
            "계획적으로 여행하는 사람에게 잘 어울려요."
    },

    "ISFJ": {
        "emoji": "🫖",
        "place": "코펜하겐",
        "country": "덴마크",
        "tags": ["편안함", "여유", "감성"],
        "reason":
            "아기자기한 거리와 차분한 분위기가 있어 "
            "편안하고 따뜻한 여행을 즐기기 좋아요."
    },

    "ESTJ": {
        "emoji": "🗼",
        "place": "도쿄",
        "country": "일본",
        "tags": ["효율", "도시", "쇼핑"],
        "reason":
            "교통이 편리하고 볼거리가 다양해서 "
            "효율적으로 일정을 짜서 여행하기 좋아요."
    },

    "ESFJ": {
        "emoji": "🥐",
        "place": "파리",
        "country": "프랑스",
        "tags": ["문화", "사진", "맛집"],
        "reason":
            "예쁜 거리와 카페, 문화 공간이 많아 "
            "함께 여행하며 추억을 남기기 좋아요."
    },

    "ISTP": {
        "emoji": "🏔️",
        "place": "인터라켄",
        "country": "스위스",
        "tags": ["자연", "모험", "액티비티"],
        "reason":
            "아름다운 자연 속에서 직접 몸으로 체험하는 활동이 많아 "
            "액티브한 여행을 즐기기 좋아요."
    },

    "ISFP": {
        "emoji": "🌊",
        "place": "제주",
        "country": "대한민국",
        "tags": ["자연", "휴식", "사진"],
        "reason":
            "바다와 숲, 감성적인 장소가 많아 "
            "여유롭게 풍경을 즐기며 여행하기 좋아요."
    },

    "ESTP": {
        "emoji": "🏄",
        "place": "시드니",
        "country": "호주",
        "tags": ["활동", "바다", "도전"],
        "reason":
            "도시와 해변을 동시에 즐길 수 있어 "
            "활동적이고 새로운 경험을 좋아하는 사람에게 잘 어울려요."
    },

    "ESFP": {
        "emoji": "🍹",
        "place": "발리",
        "country": "인도네시아",
        "tags": ["휴양", "바다", "즐거움"],
        "reason":
            "아름다운 자연과 휴양지를 함께 즐길 수 있어 "
            "밝고 즐거운 분위기의 여행을 좋아하는 사람에게 잘 어울려요."
    }
}


# =========================
# 메인 화면
# =========================
st.markdown(
    '<div class="label">MBTI TRAVEL PICK</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">Where should I go? ✈️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">MBTI로 나에게 어울리는 여행지를 찾아보세요.</div>',
    unsafe_allow_html=True
)


# =========================
# MBTI 선택
# =========================
mbti = st.selectbox(
    "MBTI를 선택해 주세요 💗",
    [
        "선택하기",
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)


# =========================
# 버튼
# =========================
button = st.button("나의 여행지 찾기 ✨")


# =========================
# 결과
# =========================
if button:

    if mbti == "선택하기":
        st.warning("MBTI를 먼저 선택해 주세요.")

    else:

        data = travel_data[mbti]

        tags_html = ""

        for tag in data["tags"]:
            tags_html += f'<span class="tag">#{tag}</span>'

        result_html = f"""
<div class="result-card">
<div class="emoji">{data["emoji"]}</div>
<div class="mbti">{mbti} TRAVEL PICK</div>
<div class="place">{data["place"]}</div>
<div class="country">{data["country"]}</div>

<div style="margin-top: 16px;">
{tags_html}
</div>

<div class="reason">
💌 <b>추천 이유</b><br><br>
{data["reason"]}
</div>
</div>
"""

        st.markdown(
            result_html,
            unsafe_allow_html=True
        )


# =========================
# Footer
# =========================
st.markdown(
    """
<div class="footer">
MBTI TRAVEL PICK · simple travel recommendation
</div>
""",
    unsafe_allow_html=True
)
