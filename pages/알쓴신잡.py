
# 수정👉 내부 임베딩 (로컬 HTML)
with open("geo_sub_thm.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")    
components.html(html, height=950, scrolling=True)
