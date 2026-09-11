import streamlit as st


# ==================================================
# 페이지 기본 설정
# ==================================================
st.set_page_config(
    page_title="MBTI Travel",
    page_icon="🎀",
    layout="centered"
)


# ==================================================
# CSS 디자인
# ==================================================
st.markdown(
    """
<style>

/* 전체 배경 */
.stApp {
    background: linear-gradient(
        135deg,
        #fff8fb 0%,
        #fff4f7 45%,
        #f6f4ff 100%
    );
}

/* 메인 콘텐츠 */
.block-container {
    max-width: 760px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* 상단 작은 글씨 */
.mini-label {
    text-align: center;
    color: #d18fa5;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 13px;
    margin-bottom: 7px;
}

/* 제목 */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #4d4057;
    margin-bottom: 5px;
    letter-spacing: -2px;
}

/* 부제목 */
.sub-title {
    text-align: center;
    color: #9b879e;
    font-size: 17px;
    margin-bottom: 35px;
}

/* selectbox 라벨 */
.stSelectbox label {
    color: #775f72;
    font-weight: 700;
    font-size: 16px;
}

/* selectbox */
div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.92);
    border-radius: 16px;
    border: 1px solid #eddbe4;
    min-height: 52px;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    height: 56px;
    border: none;
    border-radius: 18px;
    background: linear-gradient(
        90deg,
        #f7b7c8,
        #d9c4f7
    );
    color: white;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0px 8px 20px rgba(211, 158, 185, 0.25);
    transition: 0.2s;
    margin-top: 12px;
}

.stButton > button:hover {
    transform: translateY(-2px);
    color: white;
    border: none;
}

/* 결과 카드 */
.result-card {
    margin-top: 30px;
    padding: 35px 30px;
    border-radius: 28px;
    background: rgba(255,255,255,0.92);
    border: 1px solid #f1dce4;
    box-shadow: 0px 12px 35px rgba(126, 92, 118, 0.12);
    text-align: center;
}

/* 결과 이모지 */
.result-emoji {
    font-size: 65px;
    margin-bottom: 8px;
}

/* MBTI 표시 */
.result-mbti {
    color: #c2849d;
    font-weight: 800;
    letter-spacing: 3px;
    font-size: 14px;
}

/* 도시 이름 */
.result-city {
    color: #4d4057;
    font-size: 36px;
    font-weight: 800;
    margin-top: 8px;
    margin-bottom: 5px;
}

/* 국가명 */
.result-country {
    color: #ab9aae;
    font-size: 15px;
    margin-bottom: 22px;
}

/* 키워드 */
.keyword {
    display: inline-block;
    background-color: #fbe5ed;
    color: #b87590;
    padding: 7px 12px;
    border-radius: 20px;
    font-size: 13px;
    margin: 4px 2px;
    font-weight: 600;
}

/* 추천 이유 */
.result-description {
    text-align: left;
    color: #655a69;
    line-height: 1.8;
    background-color: #fff8fa;
    border-radius: 18px;
    padding: 20px 22px;
    margin-top: 22px;
}

/* 팁 */
.tip-box {
    text-align: left;
    margin-top: 17px;
    background-color: #f7f3ff;
    color: #70657a;
    padding: 17px 20px;
    border-radius: 17px;
    line-height: 1.7;
}

/* 안내 문구 */
.guide-box {
    margin-top: 25px;
    background: rgba(255,255,255,0.7);
    border-radius: 18px;
    padding: 17px;
    text-align: center;
    color: #9b879e;
    font-size: 14px;
}

/* 하단 */
.footer {
    margin-top: 45px;
    text-align: center;
    color: #c0b0bd;
    font-size: 12px;
    line-height: 1.7;
}

</style>
""",
    unsafe_allow_html=True
)


# ==================================================
# MBTI별 여행지 데이터
# ==================================================
travel_data = {

    "INTJ": {
        "emoji": "🏛️",
        "city": "빈",
        "country": "오스트리아 · Vienna",
        "keywords": ["고전", "예술", "사색", "도시 탐방"],
        "description":
            "혼자서도 깊이 있게 여행하는 것을 좋아하는 INTJ에게 "
            "빈의 차분한 분위기와 풍부한 역사·예술 공간이 잘 어울려요. "
            "박물관과 오래된 건축물을 천천히 둘러보며 자신만의 여행을 만들어 보세요.",
        "tip":
            "쇤브룬 궁전과 미술사 박물관을 둘러본 뒤 "
            "조용한 카페에서 하루를 마무리해 보세요."
    },

    "INTP": {
        "emoji": "🔭",
        "city": "런던",
        "country": "영국 · London",
        "keywords": ["박물관", "과학", "탐구", "자유여행"],
        "description":
            "호기심이 많고 새로운 지식을 발견하는 것을 좋아하는 INTP에게 "
            "다양한 박물관과 문화가 모인 런던을 추천해요. "
            "계획에 얽매이지 않고 관심 가는 곳을 자유롭게 탐험하기 좋은 도시예요.",
        "tip":
            "자연사박물관이나 과학박물관처럼 흥미로운 장소를 중심으로 "
            "자유롭게 동선을 짜보세요."
    },

    "ENTJ": {
        "emoji": "🌆",
        "city": "뉴욕",
        "country": "미국 · New York",
        "keywords": ["도전", "도시", "트렌드", "에너지"],
        "description":
            "목표가 뚜렷하고 에너지가 넘치는 ENTJ에게는 "
            "빠르게 움직이는 뉴욕이 잘 어울려요. "
            "문화, 예술, 쇼핑 등 다양한 경험을 한 번에 즐길 수 있어요.",
        "tip":
            "맨해튼의 대표 명소들을 테마별로 묶어 "
            "효율적인 여행 코스를 만들어 보세요."
    },

    "ENTP": {
        "emoji": "🎡",
        "city": "바르셀로나",
        "country": "스페인 · Barcelona",
        "keywords": ["개성", "자유", "건축", "활기"],
        "description":
            "새롭고 독특한 경험을 좋아하는 ENTP에게 "
            "바르셀로나의 자유로운 분위기를 추천해요. "
            "개성 강한 건축과 활기찬 거리 곳곳에서 예상하지 못한 재미를 발견할 수 있어요.",
        "tip":
            "유명 관광지만 보기보다 골목길과 현지 시장까지 "
            "함께 탐방해 보세요."
    },

    "INFJ": {
        "emoji": "🌿",
        "city": "교토",
        "country": "일본 · Kyoto",
        "keywords": ["고요함", "감성", "전통", "산책"],
        "description":
            "깊은 감성과 차분한 시간을 중요하게 생각하는 INFJ에게 "
            "교토를 추천해요. "
            "고즈넉한 거리와 사찰, 자연 속에서 여유롭게 생각을 정리할 수 있어요.",
        "tip":
            "이른 아침 조용한 사찰이나 대나무 숲을 산책하며 "
            "한적한 교토를 느껴보세요."
    },

    "INFP": {
        "emoji": "🌷",
        "city": "프라하",
        "country": "체코 · Prague",
        "keywords": ["낭만", "동화", "감성", "야경"],
        "description":
            "상상력이 풍부하고 감성적인 INFP에게는 "
            "동화 속 장면 같은 프라하가 잘 어울려요. "
            "오래된 거리와 아름다운 야경을 걷는 것만으로도 특별한 이야기가 만들어져요.",
        "tip":
            "해 질 무렵 카를교를 걸으며 "
            "프라하의 야경을 천천히 감상해 보세요."
    },

    "ENFJ": {
        "emoji": "🌺",
        "city": "하와이",
        "country": "미국 · Hawaii",
        "keywords": ["힐링", "사람", "바다", "활동"],
        "description":
            "사람들과 함께하는 시간을 좋아하고 따뜻한 분위기를 사랑하는 ENFJ에게 "
            "하와이를 추천해요. 아름다운 자연과 다양한 체험을 함께 즐기기 좋아요.",
        "tip":
            "낮에는 자연을 즐기고 저녁에는 함께 여행한 사람들과 "
            "여유로운 시간을 보내보세요."
    },

    "ENFP": {
        "emoji": "🪩",
        "city": "방콕",
        "country": "태국 · Bangkok",
        "keywords": ["활기", "먹거리", "새로움", "즉흥여행"],
        "description":
            "호기심과 에너지가 가득한 ENFP에게는 "
            "매 순간 새로운 경험이 기다리는 방콕을 추천해요. "
            "먹거리부터 시장, 야경까지 즉흥적으로 즐길 거리가 가득해요.",
        "tip":
            "세세한 계획을 모두 정하기보다 "
            "하루 정도는 마음 가는 대로 움직여 보세요."
    },

    "ISTJ": {
        "emoji": "🏰",
        "city": "뮌헨",
        "country": "독일 · Munich",
        "keywords": ["질서", "역사", "안정", "문화"],
        "description":
            "체계적이고 안정적인 여행을 선호하는 ISTJ에게 "
            "뮌헨을 추천해요. "
            "정돈된 도시와 역사적인 건축물을 계획적으로 둘러보기 좋아요.",
        "tip":
            "방문 장소와 이동 경로를 미리 정리하면 "
            "더욱 만족스러운 여행이 될 거예요."
    },

    "ISFJ": {
        "emoji": "🫖",
        "city": "코펜하겐",
        "country": "덴마크 · Copenhagen",
        "keywords": ["편안함", "여유", "감성", "힐링"],
        "description":
            "따뜻하고 편안한 분위기를 좋아하는 ISFJ에게 "
            "코펜하겐을 추천해요. "
            "아기자기한 거리와 여유로운 일상 속에서 편안한 여행을 즐길 수 있어요.",
        "tip":
            "예쁜 카페와 작은 상점을 천천히 둘러보는 "
            "여유로운 일정이 잘 어울려요."
    },

    "ESTJ": {
        "emoji": "🗼",
        "city": "도쿄",
        "country": "일본 · Tokyo",
        "keywords": ["효율", "도시", "쇼핑", "다양성"],
        "description":
            "효율적인 일정과 다양한 경험을 좋아하는 ESTJ에게 "
            "도쿄를 추천해요. "
            "교통이 편리하고 각 지역의 분위기가 달라 계획적인 도시 여행을 즐기기 좋아요.",
        "tip":
            "지역별로 일정을 묶어 이동 시간을 줄이는 방식으로 "
            "여행 계획을 세워보세요."
    },

    "ESFJ": {
        "emoji": "🥐",
        "city": "파리",
        "country": "프랑스 · Paris",
        "keywords": ["문화", "사진", "맛집", "분위기"],
        "description":
            "사람들과 좋은 추억을 만드는 것을 중요하게 생각하는 ESFJ에게 "
            "파리의 아름다운 거리와 풍부한 문화를 추천해요.",
        "tip":
            "친구와 예쁜 사진을 남기고 "
            "현지 디저트와 카페를 함께 즐겨보세요."
    },

    "ISTP": {
        "emoji": "🏔️",
        "city": "인터라켄",
        "country": "스위스 · Interlaken",
        "keywords": ["자연", "모험", "액티비티", "자유"],
        "description":
            "직접 몸으로 경험하는 것을 좋아하는 ISTP에게 "
            "알프스의 자연을 느낄 수 있는 인터라켄을 추천해요. "
            "도시 관광보다 활동적인 여행을 즐기기에 좋아요.",
        "tip":
            "자연 경관을 감상할 수 있는 하이킹이나 "
            "다양한 야외 체험을 일정에 넣어보세요."
    },

    "ISFP": {
        "emoji": "🌊",
        "city": "제주",
        "country": "대한민국 · Jeju",
        "keywords": ["자연", "감성", "사진", "휴식"],
        "description":
            "아름다운 풍경과 순간의 감정을 중요하게 생각하는 ISFP에게 "
            "제주를 추천해요. "
            "바다와 숲, 감성적인 공간을 천천히 돌아다니며 편안하게 여행할 수 있어요.",
        "tip":
            "일정을 빽빽하게 채우기보다 "
            "마음에 드는 장소에서 충분히 머물러 보세요."
    },

    "ESTP": {
        "emoji": "🏄",
        "city": "시드니",
        "country": "호주 · Sydney",
        "keywords": ["활동", "바다", "도전", "도시"],
        "description":
            "활동적이고 새로운 경험을 즐기는 ESTP에게 "
            "시드니를 추천해요. "
            "도시와 바다를 동시에 즐기면서 다양한 체험을 할 수 있어요.",
        "tip":
            "도시 관광과 해변 활동을 하루 일정에 함께 넣어 "
            "역동적으로 즐겨보세요."
    },

    "ESFP": {
        "emoji": "🍹",
        "city": "발리",
        "country": "인도네시아 · Bali",
        "keywords": ["휴양", "사진", "즐거움", "바다"],
        "description":
            "즐거운 분위기와 특별한 순간을 사랑하는 ESFP에게 "
            "발리를 추천해요. "
            "아름다운 자연과 감각적인 공간이 많아 매일 새로운 추억을 만들기 좋아요.",
        "tip":
            "낮에는 자연을 즐기고 저녁에는 멋진 노을을 감상하며 "
            "하루를 마무리해 보세요."
    }
}


# ==================================================
# 상단 화면
# ==================================================
st.markdown(
    '<div class="mini-label">TRAVEL MATCH</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Where should I go? 🎀</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">나의 MBTI와 꼭 맞는 여행지를 찾아보세요 ✈️</div>',
    unsafe_allow_html=True
)


# ==================================================
# MBTI 선택
# ==================================================
mbti = st.selectbox(
    "💗 나의 MBTI를 선택해 주세요",
    [
        "선택하기",
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)


# ==================================================
# 추천 버튼
# ==================================================
recommend = st.button("✨ 나에게 딱 맞는 여행지 찾기")


# ==================================================
# 결과 출력
# ==================================================
if recommend:

    if mbti == "선택하기":

        st.warning("MBTI를 먼저 선택해 주세요 💌")

    else:

        data = travel_data[mbti]

        keyword_html = ""

        for keyword in data["keywords"]:
            keyword_html += (
                f'<span class="keyword">#{keyword}</span>'
            )

        result_html = f"""
<div class="result-card">
<div class="result-emoji">{data["emoji"]}</div>

<div class="result-mbti">{mbti} TRAVEL PICK</div>

<div class="result-city">{data["city"]}</div>

<div class="result-country">{data["country"]}</div>

<div>{keyword_html}</div>

<div class="result-description">
💌 <b>Why this place?</b><br><br>
{data["description"]}
</div>

<div class="tip-box">
🧳 <b>TRAVEL TIP</b><br>
{data["tip"]}
</div>
</div>
"""

        st.markdown(
            result_html,
            unsafe_allow_html=True
        )

        st.balloons()


# ==================================================
# 처음 접속했을 때 안내
# ==================================================
if not recommend:

    st.markdown(
        """
<div class="guide-box">
💭 MBTI를 선택하고 버튼을 누르면<br>
나에게 어울리는 여행지를 추천해 드려요.
</div>
""",
        unsafe_allow_html=True
    )


# ==================================================
# Footer
# ==================================================
st.markdown(
    """
<div class="footer">
MBTI TRAVEL MATCH ✦<br>
나의 성격 유형으로 찾아보는 여행지 추천 서비스
</div>
""",
    unsafe_allow_html=True
)
