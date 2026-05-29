import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเว็บให้เต็มจอและเหมาะกับมือถือ
st.set_page_config(page_title="❤️ Question...", layout="centered", initial_sidebar_state="collapsed")

# โค้ดทั้งหมดจะรันบนหน้าบ้าน (Frontend) เพื่อความลื่นไหลสูงสุดบนมือถือ
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Do you love me?</title>
    <style>
        body {
            background-color: #000000;
            color: white;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            transition: background-color 0.6s ease;
            overflow: hidden;
            padding: 20px;
            box-sizing: border-box;
        }
        .container {
            text-align: center;
            width: 100%;
            max-width: 500px;
        }
        .question {
            font-size: 2.2rem;
            font-weight: bold;
            margin-bottom: 50px;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
            min-height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            line-height: 1.4;
        }
        .buttons {
            display: flex;
            flex-direction: column;
            gap: 15px;
            align-items: center;
            justify-content: center;
            width: 100%;
        }
        @media (min-width: 480px) {
            .buttons {
                flex-direction: row;
                gap: 20px;
            }
        }
        button {
            padding: 15px 30px;
            border: none;
            border-radius: 50px;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            font-weight: bold;
            touch-action: manipulation;
        }
        #yesBtn {
            background-color: #ff4b4b;
            color: white;
            box-shadow: 0 4px 15px rgba(255,75,75,0.4);
            z-index: 10;
        }
        #noBtn {
            background-color: #333333;
            color: #bbbbbb;
            font-size: 14px;
            padding: 10px 20px;
        }
        .success-text {
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
            animation: popUp 0.5s ease forwards;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .balloons {
            font-size: 4rem;
            margin-top: 20px;
            animation: floatUp 3s ease infinite;
        }
        @keyframes popUp {
            0% { transform: scale(0.5); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body>

    <div class="container" id="mainApp">
        <div class="question" id="textDisplay">เป็นแฟนกันไหม</div>
        <div class="buttons">
            <button id="yesBtn" onclick="clickedYes()">เป็นแน่นอน</button>
            <button id="noBtn" onclick="clickedNo()">ไม่เป็นอะ ไม่เอาาา</button>
        </div>
    </div>

    <script>
        // รายชื่อคำอ้อน 10 แบบ
        const sweet_words = [    "เป็นแฟนกันไหม",
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
];

        let noCount = 0;
        let yesFontSize = 18;
        let yesPaddingX = 30;
        let yesPaddingY = 15;

        function clickedNo() {
            noCount++;
            
            // 1. เปลี่ยนคำอ้อนไปเรื่อยๆ สูงสุด 10 แบบ
            let wordIndex = Math.min(noCount, sweetWords.length - 1);
            document.getElementById("textDisplay").innerText = sweetWords[wordIndex];
            
            // 2. ขยายขนาดปุ่ม "เป็นแน่นอน" ให้ใหญ่ขึ้นเรื่อยๆ
            yesFontSize += 12;
            yesPaddingX += 15;
            yesPaddingY += 8;
            
            const yesBtn = document.getElementById("yesBtn");
            yesBtn.style.fontSize = yesFontSize + "px";
            yesBtn.style.padding = yesPaddingY + "px " + yesPaddingX + "px";
            
            // ถ้าใหญ่เกินหน้าจอให้เต็มจอไปเลย
            if (yesFontSize > 150) {
                yesBtn.style.position = "fixed";
                yesBtn.style.top = "0";
                yesBtn.style.left = "0";
                yesBtn.style.width = "100vw";
                yesBtn.style.height = "100vh";
                yesBtn.style.borderRadius = "0";
                yesBtn.style.display = "flex";
                yesBtn.style.alignItems = "center";
                yesBtn.style.justifyContent = "center";
            }

            // 3. ค่อยๆ เปลี่ยนสีพื้นหลังจาก ดำ (#000000) ไปเป็น #D4BAB0
            // เป้าหมาย RGB ของ #D4BAB0 คือ (212, 186, 176)
            let step = Math.min(noCount, 9);
            let r = Math.floor((212 / 9) * step);
            let g = Math.floor((186 / 9) * step);
            let b = Math.floor((176 / 9) * step);
            
            document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
        }

        function clickedYes() {
            // เมื่อกดตกลง
            document.body.style.backgroundColor = "#D4BAB0";
            document.getElementById("mainApp").innerHTML = `
                <div class="success-text">เย้! งั้นเป็นแฟนกันแล้วนะค้าบ รักที่สุดเลยยย ❤️🥰</div>
                <div class="balloons">🎈🎈🎉🎈🎈</div>
            `;
        }
    </script>
</body>
</html>
"""

# ส่งโค้ด HTML ให้แสดงผลเต็มหน้าจอ
components.html(html_code, height=750, scrolling=False)
