import streamlit as st
from PIL import Image
import io

# ปรับหน้าตาให้เหมาะกับมือถือ
st.set_page_config(page_title="ตัวแปลงไฟล์มือถือ", layout="centered")

st.title("📸 เครื่องมือแปลงไฟล์ภาพ")
st.write("ใช้งานง่ายๆ แค่อัปโหลดแล้วดาวน์โหลด")

# ส่วนรับไฟล์
uploaded_files = st.file_uploader("เลือกรูปภาพ (PNG, WebP, BMP)", type=["png", "webp", "bmp"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        
        # แสดงรูปตัวอย่าง
        st.image(image, caption=f'ไฟล์ที่อัปโหลด: {uploaded_file.name}', use_container_width=True)
        
        # เลือกนามสกุลที่ต้องการแปลง
        option = st.selectbox(f"แปลง {uploaded_file.name} เป็น:", ("JPG", "PNG", "WebP"), key=uploaded_file.name)
        
        # สร้างบัฟเฟอร์เก็บข้อมูลภาพ
        buf = io.BytesIO()
        
        if option == "JPG":
            image.convert('RGB').save(buf, format="JPEG")
            mime_type = "image/jpeg"
            file_ext = ".jpg"
        elif option == "PNG":
            image.save(buf, format="PNG")
            mime_type = "image/png"
            file_ext = ".png"
        else:
            image.save(buf, format="WEBP")
            mime_type = "image/webp"
            file_ext = ".webp"
            
        btn = st.download_button(
            label=f"ดาวน์โหลด {option}",
            data=buf.getvalue(),
            file_name=f"converted_{uploaded_file.name}{file_ext}",
            mime=mime_type
        )
        st.divider()

