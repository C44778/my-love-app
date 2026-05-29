import streamlit as st

# ตั้งค่าหน้าเว็บให้รองรับการเปิดบนมือถือได้สวยงาม
st.set_page_config(page_title="Question...", page_icon="❤️", layout="centered")

# ลิสต์คำอ้อน 10 แบบตามที่ขอครับ
sweet_words = [    "เป็นแฟนกันไหม",
    "เป็นเถอะนะ 🥺",
    "ขอจนเขินแล้วเนี้ยยย บ้าจริงงง",
    "ใจร้ายจัง... ยอมเป็นซะดีๆ ❤️",
    "กดผิดหรือเปล่า? ปุ่มขวาต่างหากที่ต้องกด!",
    "นะน้าาาาา คุกเข่าอ้อนวอนแล้วนะ 🙏",
    "คิดดูอีกทีสิค้าบ ไม่อยากมีคนคอยตามใจหรอ?",
    "ไม่ให้ปฏิเสธหรอกนะ! (😜)",
    "ง่าาาา นอยด์แล้วนะ ตื้อจนกว่าจะยอม!",
    "อย่าให้มีครั้งที่ 2!",
    "อย่าให้มีครั้งที่ 3!",
    "อย่าให้มีครั้งที่ 4 นิไม่ควรละนะ!",
    "รักขนาดนี้ ไม่เป็นแฟนกันไหวหรออออ 🥰"
    "หมดแล้วเตรียมมาแค่นี้คบเถอะะะ!",
]

# Session State
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'is_accepted' not in st.session_state:
    st.session_state.is_accepted = False

# คำนวณขนาดปุ่มและสี
yes_button_size = 18 + (st.session_state.no_count * 12)

def get_background_color(count):
    if count >= 9: return "#D4BAB0"
    r = int((212 / 9) * count)
    g = int((186 / 9) * count)
    b = int((176 / 9) * count)
    return f"rgb({r}, {g}, {b})"

bg_color = get_background_color(st.session_state.no_count)

# ใช้ CSS แบบปลอดภัย (ไม่ใช้ f-string ซ้อน Quote เยอะๆ)
css_code = f"""
    <style>
    .stApp {{
        background-color: {bg_color} !important;
        transition: background-color 0.5s ease;
    }}
    .question-text {{
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 50px;
        padding-top: 100px;
    }}
    div[data-testid="stBaseButton-elementHlsYes"] {{
        font-size: {yes_button_size}px !important;
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 30px !important;
        width: 100%;
    }}
    div[data-testid="stBaseButton-elementHlsNo"] {{
        font-size: 14px !important;
        background-color: #444444 !important;
        color: #bbbbbb !important;
        border-radius: 30px !important;
        width: 100%;
    }}
    </style>
"""
st.markdown(css_code, unsafe_allowed_html=True)

# ส่วนการแสดงผล
if st.session_state.is_accepted:
    st.markdown("<h1 style='text-align: center; color: white;'>เย้! เป็นแฟนกันแล้วนะ ❤️</h1>", unsafe_allowed_html=True)
    st.balloons()
else:
    # ดึงคำอ้อนมาเก็บในตัวแปรก่อน เพื่อไม่ให้ f-string ใน markdown ทำงานซับซ้อนเกินไป
    idx = min(st.session_state.no_count, len(sweet_words) - 1)
    display_text = sweet_words[idx]
    
    # แสดงข้อความ
    st.markdown(f"<div class='question-text'>{display_text}</div>", unsafe_allowed_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("เป็นแน่นอน", key="elementHlsYes"):
            st.session_state.is_accepted = True
            st.rerun()
    with col2:
        if st.button("ไม่เป็นอะ ไม่เอาาา", key="elementHlsNo"):
            st.session_state.no_count += 1
            st.rerun()
