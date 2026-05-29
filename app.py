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
# โดยแบ่งเป็น 10 ระดับตามจำนวนครั้งที่กดปฏิเสธ
def get_background_color(count):
    if count >= 9:
        return "#D4BAB0"
    
    # เป้าหมายสี #D4BAB0 แปลงเป็น RGB คือ (212, 186, 176)
    # ค่อยๆ เพิ่มค่า RGB จาก 0 ไปหาเป้าหมาย
    r = int((212 / 9) * count)
    g = int((186 / 9) * count)
    b = int((176 / 9) * count)
    return f"rgb({r}, {g}, {b})"

bg_color = get_background_color(st.session_state.no_count)

# แทรก CSS เพื่อปรับแต่งหน้าตา สีพื้นหลัง และขนาดปุ่มแบบ Dynamic
st.markdown(f"""
    <style>
    /* เปลี่ยนสีพื้นหลังของ App */
    .stApp {{
        background-color: {bg_color} !important;
        transition: background-color 0.5s ease-in-out;
    }}
    
    /* ปรับแต่งข้อความคำถามตรงกลาง */
    .question-text {{
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 50px;
        padding-top: 100px;
    }}
    
    /* ปรับแต่งปุ่ม "เป็นแน่นอน" ให้ขยายใหญ่ขึ้นได้ */
    div.stButton > button:first-child {{
        font-size: {yes_button_size}px !important;
        padding: 10px 20px !important;
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        transition: all 0.3s ease;
        width: 100%;
    }}
    
    /* ปรับแต่งปุ่ม "ไม่เป็นอะ ไม่เอาาา" ให้ดูเล็กลงเรื่อยๆ */
    div.stButton > button:last-child {{
        font-size: 14px !important;
        background-color: #555555 !important;
        color: #cccccc !important;
        border-radius: 20px !important;
        border: none !important;
        width: 100%;
    }}
    </style>
""", unsafe_allowed_html=True)

# --- ส่วนของการแสดงผลบนหน้าเว็บ ---

# ถ้าเขากดตกลงแล้ว 🎉
if st.session_state.is_accepted:
    st.markdown("<div class='question-text'>เย้! งั้นเป็นแฟนกันแล้วนะครับ รักแบมที่สุดเลยยย❤️🥰</div>", unsafe_allowed_html=True)
    st.balloons() # เอฟเฟกต์ลูกโป่งลอยขึ้นมา

# ถ้ายังไม่กดตกลง
else:
    # แสดงคำถาม (เปลี่ยนตามจำนวนครั้งที่กดปฏิเสธ)
    current_word_index = min(st.session_state.no_count, len(sweet_words) - 1)
    st.markdown(f"<div class='question-text'>{sweet_words[current_word_index]}</div>", unsafe_allowed_html=True)
    
    # สร้างคอลัมน์ซ้าย-ขวา สำหรับวางปุ่มคู่กัน (เหมาะกับหน้าจอมือถือ)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("เป็นแน่นอน"):
            st.session_state.is_accepted = True
            st.rerun()
            
    with col2:
        if st.button("ไม่เป็นอะ ไม่เอาาา"):
            st.session_state.no_count += 1
            st.rerun()