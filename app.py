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

# กำหนดสถานะเริ่มต้น (Session State) เพื่อจำค่า
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'is_accepted' not in st.session_state:
    st.session_state.is_accepted = False

# คำนวณขนาดปุ่ม "เป็นแน่นอน" (เริ่มที่ 18px และใหญ่ขึ้นครั้งละ 12px)
yes_button_size = 18 + (st.session_state.no_count * 12)

# ฟังก์ชันคำนวณการเปลี่ยนสีพื้นหลังจาก ดำ (#000000) ไปเป็น #D4BAB0
def get_background_color(count):
    if count >= 9:
        return "#D4BAB0"
    r = int((212 / 9) * count)
    g = int((186 / 9) * count)
    b = int((176 / 9) * count)
    return f"rgb({r}, {g}, {b})"

bg_color = get_background_color(st.session_state.no_count)

# ใช้ st.html แทน st.markdown เพื่อความเสถียรในการฉีด CSS 
# ใช้ สัญลักษณ์ {{ }} สองชั้นครอบ CSS ปกติ เพื่อป้องกันการชนกับระบบ f-string
st.html(f"""
    <style>
    /* เปลี่ยนสีพื้นหลังของ App */
    .stApp {{
        background-color: {bg_color} !important;
        transition: background-color 0.5s ease-in-out;
    }}
    
    /* ปรับแต่งข้อความคำถามตรงกลาง */
    .question-text {{
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
        margin-bottom: 50px;
        padding-top: 120px;
        line-height: 1.5;
    }}
    
    /* ปรับแต่งปุ่มเจาะจงด้วย Key [yes_btn] ให้ขยายใหญ่ขึ้นเรื่อยๆ */
    div[data-testid="stBaseButton-elementHlsYes"] {{
        font-size: {yes_button_size}px !important;
        padding: 15px 25px !important;
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        transition: all 0.2s ease;
        width: 100%;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }}
    
    /* ปรับแต่งปุ่มเจาะจงด้วย Key [no_btn] ให้คงที่คงวา */
    div[data-testid="stBaseButton-elementHlsNo"] {{
        font-size: 14px !important;
        padding: 10px 15px !important;
        background-color: #444444 !important;
        color: #bbbbbb !important;
        border-radius: 30px !important;
        border: none !important;
        width: 100%;
        margin-top: 5px;
    }}
    </style>
""")

# --- ส่วนของการแสดงผลบนหน้าเว็บ ---

if st.session_state.is_accepted:
    st.markdown("<div class='question-text'>เย้! งั้นเป็นแฟนกันแล้วนะค้าบ รักที่สุดเลยยย ❤️🥰</div>", unsafe_allowed_html=True)
    st.balloons()

else:
    # เลือกคำตามจำนวนครั้งที่กดปฏิเสธ
    current_word_index = min(st.session_state.no_count, len(sweet_words) - 1)
    st.markdown(f"<div class='question-text'>{sweet_words[current_word_index]}</div>", unsafe_allowed_html=True)
    
    # แบ่งคอลัมน์ซ้ายขวาบนหน้าจอมือถือ
    col1, col2 = st.columns(2)
    
    with col1:
        # กำหนด key='elementHlsYes' เพื่อให้ CSS ค้นหาเจอและจัดสไตล์ได้ถูกต้อง
        if st.button("เป็นแน่นอน", key="elementHlsYes"):
            st.session_state.is_accepted = True
            st.rerun()
            
    with col2:
        # กำหนด key='elementHlsNo' เพื่อระบุตัวตนของปุ่มปฏิเสธ
        if st.button("ไม่เป็นอะ ไม่เอาาา", key="elementHlsNo"):
            st.session_state.no_count += 1
            st.rerun()
