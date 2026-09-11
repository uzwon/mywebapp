import streamlit as st


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="MBTI Style Finder",
    page_icon="🖤",
    layout="centered"
)


# =========================================================
# CSS 디자인
# =========================================================
st.markdown(
    """
<style>

/* 전체 배경 */
.stApp {
    background: #f7f7f5;
}

/* 본문 너비 */
.block-container {
    max-width: 760px;
    padding-top: 4rem;
    padding-bottom: 4rem;
}

/* 상단 작은 제목 */
.top-label {
    text-align: center;
    font-size: 12px;
    letter-spacing: 4px;
    font-weight: 700;
    color: #8b8b87;
    margin-bottom: 12px;
}

/* 메인 제목 */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #171717;
    letter-spacing: -2px;
    margin-bottom: 10px;
}

/* 부제목 */
.subtitle {
    text-align: center;
    color: #8a8a86;
    font-size: 15px;
    margin-bottom: 42px;
}

/* 구분선 */
.line {
    width: 45px;
    height: 2px;
    background-color: #171717;
    margin: 0 auto 40px auto;
}

/* selectbox 라벨 */
.stSelectbox label {
    color: #343434;
    font-size: 15px;
    font-weight: 700;
}

/* selectbox */
div[data-baseweb="select"] > div {
    background-color: #ffffff;
    border: 1px solid #dededb;
    border-radius: 8px;
    min-height: 52px;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    height: 54px;
    border-radius: 8px;
    border: none;
    background-color: #171717;
    color: white;
    font-size: 15px;
    font-weight: 700;
    margin-top: 12px;
    transition: all 0.2s ease;
}

/* 버튼 hover */
.stButton > button:hover {
    background-color: #363636;
    color: white;
    border: none;
    transform: translateY(-1px);
}

/* 결과 카드 */
.result-card {
    background-color: white;
    border: 1px solid #e4e4e0;
    border-radius: 14px;
    padding: 38px 34px;
    margin-top: 34px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.05);
}

/* 결과 상단 MBTI */
.mbti-label {
    text-align: center;
    color: #9a9a95;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* 이모지 */
.style-icon {
    text-align: center;
    font-size: 45px;
    margin-bottom: 8px;
}

/* 스타일 이름 */
.style-name {
    text-align: center;
    font-size: 32px;
    color: #191919;
    font-weight: 800;
    margin-bottom: 7px;
}

/* 영어 스타일명 */
.style-eng {
    text-align: center;
    font-size: 14px;
    color: #999994;
    margin-bottom: 24px;
}

/* 태그 영역 */
.tags {
    text-align: center;
    margin-bottom: 25px;
}

/* 태그 */
.tag {
    display: inline-block;
    padding: 7px 12px;
    margin: 3px;
    border-radius: 20px;
    background-color: #f2f2ef;
    color: #555550;
    font-size: 12px;
    font-weight: 600;
}

/* 설명 */
.description {
    background-color: #f8f8f6;
    border-radius: 10px;
    padding: 20px 22px;
    color: #555552;
    line-height: 1.8;
    font-size: 14px;
    margin-top: 20px;
}

/* 아이템 박스 */
.item-box {
    margin-top: 18px;
    padding: 20px 22px;
    border: 1px solid #e6e6e2;
    border-radius: 10px;
    color: #555552;
    line-height: 1.8;
    font-size: 14px;
}

/* 컬러 박스 */
.color-box {
    margin-top: 18px;
    padding: 20px 22px;
    border-radius: 10px;
    background-color: #202020;
    color: #f4f4f2;
    line-height: 1.8;
    font-size: 14px;
}

/* 처음 안내 */
.guide {
    margin-top: 28px;
    text-align: center;
    color: #a0a09c;
    font-size: 13px;
    line-height: 1.7;
}

/* footer */
.footer {
    margin-top: 50px;
    text-align: center;
    color: #b0b0ac;
    font-size: 11px;
    letter-spacing: 1px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# MBTI별 스타일 데이터
# =========================================================
style_data = {

    "INTJ": {
        "icon": "🖤",
        "style": "미니멀 시크",
        "eng": "Minimal Chic",
        "tags": ["미니멀", "모노톤", "구조적"],
        "description":
            "불필요한 장식보다 깔끔한 실루엣과 완성도 높은 기본 아이템이 잘 어울려요. "
            "단정하면서도 차가운 분위기의 스타일을 추천해요.",
        "items":
            "블랙 재킷 · 슬랙스 · 베이직 셔츠 · 로퍼 · 심플한 가죽 가방",
        "colors":
            "BLACK · CHARCOAL · WHITE · NAVY"
    },

    "INTP": {
        "icon": "📚",
        "style": "스마트 캐주얼",
        "eng": "Smart Casual",
        "tags": ["편안함", "베이직", "레이어드"],
        "description":
            "편안하면서도 너무 평범하지 않은 스타일이 잘 어울려요. "
            "베이직한 아이템을 자연스럽게 레이어드하는 코디를 추천해요.",
        "items":
            "니트 · 와이드 팬츠 · 오버핏 셔츠 · 스니커즈 · 크로스백",
        "colors":
            "GREY · NAVY · BEIGE · WHITE"
    },

    "ENTJ": {
        "icon": "⌚",
        "style": "모던 클래식",
        "eng": "Modern Classic",
        "tags": ["세련됨", "클래식", "정돈"],
        "description":
            "깔끔하고 자신감 있는 인상을 주는 스타일이 잘 어울려요. "
            "유행을 타지 않는 클래식 아이템을 현대적으로 활용해 보세요.",
        "items":
            "테일러드 재킷 · 셔츠 · 스트레이트 팬츠 · 시계 · 레더 슈즈",
        "colors":
            "BLACK · NAVY · CAMEL · IVORY"
    },

    "ENTP": {
        "icon": "🕶️",
        "style": "스트리트 모던",
        "eng": "Modern Street",
        "tags": ["개성", "트렌드", "포인트"],
        "description":
            "새로운 스타일을 시도하는 것을 좋아하는 성향에 맞게 "
            "베이직한 룩에 한 가지 강한 포인트를 더하는 코디가 잘 어울려요.",
        "items":
            "오버핏 재킷 · 와이드 데님 · 그래픽 티셔츠 · 볼캡 · 스니커즈",
        "colors":
            "BLACK · GREY · BLUE · SILVER"
    },

    "INFJ": {
        "icon": "🌿",
        "style": "소프트 미니멀",
        "eng": "Soft Minimal",
        "tags": ["차분함", "부드러움", "감성"],
        "description":
            "차분하고 섬세한 분위기를 살릴 수 있는 부드러운 색감과 "
            "깔끔한 디자인의 옷을 추천해요.",
        "items":
            "가디건 · 롱스커트 · 니트 · 스트레이트 팬츠 · 심플 숄더백",
        "colors":
            "IVORY · BEIGE · GREY · DUSTY BLUE"
    },

    "INFP": {
        "icon": "☁️",
        "style": "빈티지 내추럴",
        "eng": "Vintage Natural",
        "tags": ["감성", "빈티지", "자연스러움"],
        "description":
            "부드럽고 자연스러운 분위기에 빈티지한 요소를 더한 스타일이 잘 어울려요. "
            "편안하지만 개성이 느껴지는 코디를 추천해요.",
        "items":
            "빈티지 니트 · 데님 · 롱스커트 · 셔츠 · 캔버스백",
        "colors":
            "CREAM · BROWN · KHAKI · DENIM BLUE"
    },

    "ENFJ": {
        "icon": "🤎",
        "style": "컨템포러리 클래식",
        "eng": "Contemporary Classic",
        "tags": ["깔끔함", "우아함", "호감형"],
        "description":
            "부드럽고 단정한 인상을 주는 스타일이 잘 어울려요. "
            "클래식한 아이템에 자연스러운 포인트를 더해 보세요.",
        "items":
            "트렌치코트 · 니트 · 슬랙스 · 미디 스커트 · 숄더백",
        "colors":
            "CAMEL · CREAM · BLACK · BROWN"
    },

    "ENFP": {
        "icon": "✨",
        "style": "컬러 캐주얼",
        "eng": "Color Casual",
        "tags": ["활기", "컬러", "자유로움"],
        "description":
            "밝은 분위기와 개성을 살릴 수 있도록 "
            "기본 아이템에 컬러나 액세서리로 포인트를 주는 스타일을 추천해요.",
        "items":
            "컬러 니트 · 데님 · 스니커즈 · 미니백 · 포인트 액세서리",
        "colors":
            "BLUE · GREEN · WHITE · YELLOW"
    },

    "ISTJ": {
        "icon": "🧥",
        "style": "클린 클래식",
        "eng": "Clean Classic",
        "tags": ["정돈", "실용성", "클래식"],
        "description":
            "단정하고 오래 입을 수 있는 스타일이 잘 어울려요. "
            "기본에 충실하면서도 소재와 핏이 좋은 아이템을 추천해요.",
        "items":
            "셔츠 · 트렌치코트 · 스트레이트 팬츠 · 로퍼 · 토트백",
        "colors":
            "NAVY · BEIGE · WHITE · BLACK"
    },

    "ISFJ": {
        "icon": "🧸",
        "style": "소프트 클래식",
        "eng": "Soft Classic",
        "tags": ["단정함", "편안함", "부드러움"],
        "description":
            "편안하면서도 깔끔한 분위기의 코디가 잘 어울려요. "
            "부드러운 소재와 차분한 색을 활용하면 좋아요.",
        "items":
            "가디건 · 셔츠 · 코튼 팬츠 · 플랫 슈즈 · 미니백",
        "colors":
            "CREAM · BEIGE · PINK · LIGHT GREY"
    },

    "ESTJ": {
        "icon": "👜",
        "style": "시티 포멀",
        "eng": "City Formal",
        "tags": ["도시적", "정돈", "세련됨"],
        "description":
            "깔끔하고 도시적인 분위기가 잘 어울려요. "
            "각이 살아 있는 아이템으로 정돈된 실루엣을 만들어 보세요.",
        "items":
            "블레이저 · 슬랙스 · 셔츠 · 레더백 · 로퍼",
        "colors":
            "BLACK · NAVY · GREY · WHITE"
    },

    "ESFJ": {
        "icon": "🩰",
        "style": "프렌치 클래식",
        "eng": "French Classic",
        "tags": ["세련됨", "부드러움", "클래식"],
        "description":
            "친근하면서도 세련된 분위기를 살릴 수 있는 "
            "단정한 프렌치 스타일을 추천해요.",
        "items":
            "트위드 재킷 · 니트 · 데님 · 플랫 슈즈 · 숄더백",
        "colors":
            "IVORY · BLACK · NAVY · SOFT PINK"
    },

    "ISTP": {
        "icon": "🧢",
        "style": "테크 캐주얼",
        "eng": "Tech Casual",
        "tags": ["실용성", "편안함", "모던"],
        "description":
            "움직이기 편하면서도 깔끔한 스타일이 잘 어울려요. "
            "기능적인 소재와 심플한 디자인을 활용해 보세요.",
        "items":
            "윈드브레이커 · 카고 팬츠 · 기본 티셔츠 · 스니커즈 · 크로스백",
        "colors":
            "BLACK · KHAKI · GREY · WHITE"
    },

    "ISFP": {
        "icon": "🎧",
        "style": "내추럴 스트리트",
        "eng": "Natural Street",
        "tags": ["자유로움", "감각적", "편안함"],
        "description":
            "억지로 꾸민 느낌보다 자연스럽게 멋이 나는 스타일이 잘 어울려요. "
            "실루엣과 작은 디테일로 개성을 표현해 보세요.",
        "items":
            "와이드 데님 · 후드 · 니트 · 스니커즈 · 숄더백",
        "colors":
            "GREY · DENIM · BROWN · BLACK"
    },

    "ESTP": {
        "icon": "👟",
        "style": "스포티 스트리트",
        "eng": "Sporty Street",
        "tags": ["활동적", "스트리트", "트렌드"],
        "description":
            "활동적인 분위기와 트렌디한 요소가 잘 어울려요. "
            "스포티한 아이템에 스트리트 요소를 섞어 보세요.",
        "items":
            "트랙 재킷 · 카고 팬츠 · 캡 · 스니커즈 · 크로스백",
        "colors":
            "BLACK · RED · GREY · WHITE"
    },

    "ESFP": {
        "icon": "💿",
        "style": "트렌디 캐주얼",
        "eng": "Trendy Casual",
        "tags": ["트렌드", "포인트", "감각적"],
        "description":
            "밝고 눈에 띄는 분위기를 살릴 수 있는 스타일이 잘 어울려요. "
            "트렌디한 아이템이나 액세서리를 포인트로 활용해 보세요.",
        "items":
            "크롭 재킷 · 데님 · 포인트 백 · 스니커즈 · 액세서리",
        "colors":
            "BLACK · WHITE · SILVER · BLUE"
    }
}


# =========================================================
# 메인 화면
# =========================================================
st.markdown(
    '<div class="top-label">PERSONAL STYLE FINDER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Find Your Style.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">MBTI로 알아보는 나에게 어울리는 패션 스타일</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="line"></div>',
    unsafe_allow_html=True
)


# =========================================================
# MBTI 선택
# =========================================================
mbti = st.selectbox(
    "MBTI를 선택해 주세요",
    [
        "선택하기",
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)


# =========================================================
# 추천 버튼
# =========================================================
button = st.button(
    "STYLE FINDER →"
)


# =========================================================
# 결과 출력
# =========================================================
if button:

    if mbti == "선택하기":

        st.warning(
            "MBTI를 먼저 선택해 주세요."
        )

    else:

        data = style_data[mbti]

        tags_html = ""

        for tag in data["tags"]:

            tags_html += (
                f'<span class="tag">#{tag}</span>'
            )


        result_html = f"""
<div class="result-card">

<div class="mbti-label">
{mbti} STYLE PROFILE
</div>

<div class="style-icon">
{data["icon"]}
</div>

<div class="style-name">
{data["style"]}
</div>

<div class="style-eng">
{data["eng"]}
</div>

<div class="tags">
{tags_html}
</div>

<div class="description">
<b>STYLE NOTE</b><br><br>
{data["description"]}
</div>

<div class="item-box">
<b>KEY ITEMS</b><br><br>
{data["items"]}
</div>

<div class="color-box">
<b>COLOR PALETTE</b><br><br>
{data["colors"]}
</div>

</div>
"""

        st.markdown(
            result_html,
            unsafe_allow_html=True
        )


# =========================================================
# 처음 화면 안내
# =========================================================
if not button:

    st.markdown(
        """
<div class="guide">
MBTI를 선택하면<br>
추천 스타일 · 핵심 아이템 · 컬러 팔레트를 보여드립니다.
</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# 하단
# =========================================================
st.markdown(
    """
<div class="footer">
MBTI STYLE FINDER · PERSONAL FASHION GUIDE
</div>
""",
    unsafe_allow_html=True
)
