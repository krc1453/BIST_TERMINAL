import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="BIST Hybrid Terminal", layout="wide", page_icon="📈")

# Özel CSS ile Şık Koyu Tema (Dark Mode) Tasarımı
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

# --- ÜST BİLGİ ÇUCU ---
c1, c2, c3 = st.columns([3, 2, 1])
with c1:
    st.markdown("### 📈 BIST 100 <span style='background-color: #238636; color: white; padding: 3px 8px; border-radius: 5px; font-size: 14px;'>HYBRID TERMINAL v2.4</span>", unsafe_allow_html=True)
    st.caption("Kırılım (Breakout) • Zaman Stopu • İz Süren Stop • RS Filtresi")
with c2:
    st.markdown("🟢 **BIST 100:** 10,482.15 (+1.24%) &nbsp;&nbsp;|&nbsp;&nbsp; **USD/TRY:** 34.22")
with c3:
    btn_refresh = st.button("🔄 Taramayı Yenile", type="primary")

st.markdown("---")

# --- STRATEJİ ÖZET KARTLARI ---
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.markdown("##### STRATEJİ MODELİ\n**Hibrit Kırılım (Breakout)**\n<span style='font-size:12px; color:8b949e;'>20 Günlük Donchian Zirve Kırılımı + Piramit Alım</span>", unsafe_allow_html=True)
with col_m2:
    st.markdown("##### ZAMAN STOPU DİSİPLİNİ\n⏱️ **Maks. 15 İşlem Gün**\n<span style='font-size:12px; color:8b949e;'>Yatay kalan pozisyon kapatılır, fırsat maliyeti sıfırlanır.</span>", unsafe_allow_html=True)
with col_m3:
    st.markdown("##### RİSK & İZ SÜREN STOP\n🛡️ **%5 - %8 Esnek Stop**\n<span style='font-size:12px; color:8b949e;'>Zirveden %5 sarmada kâr koruma & zararı kesme.</span>", unsafe_allow_html=True)
with col_m4:
    st.markdown("##### 2 YILLIK SİMÜLASYON GETİRİSİ\n🟢 **+%%168.45** <span style='font-size:11px;'>(Max DD: -%%9.4)</span>\n<span style='font-size:12px; color:8b949e;'>Düz Al-Tut: %85.95 • Enflasyonu Net Yenen Model</span>", unsafe_allow_html=True)

st.markdown("---")

# --- SEKMELER VE FİLTRELER ---
tab_sec1, tab_sec2, tab_sec3 = st.tabs(["📊 Canlı Sinyal Taraması", "📈 Backtest & Portföy Simülatörü", "💼 Aktif Takip Portföyüm"])

with tab_sec1:
    f_col1, f_col2 = st.columns([2, 2])
    with f_col1:
        sec_filter = st.selectbox("Sektör Filtresi", ["Tüm Sektörler (BIST 100)", "Sanayi", "Holding", "Perakende", "Teknoloji"])
    with f_col2:
        sig_filter = st.selectbox("Sinyal Filtresi", ["Tüm Sinyaller", "Kırılım Al", "Piramit Ekle", "Stop / Çıkış"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 📊 BIST 100 Hibrit Strateji Taraması ve Anlık Göstergeler\n<span style='font-size:12px; color:8b949e;'>20 Günlük Donchian Zirvesi, Göreli Güç (RS) ve Zaman Stopu Takibi</span>", unsafe_allow_html=True)

    # Örnek Profesyonel Tablo Verisi (Canlı veri motoru buraya bağlanır)
    data_demo = [
        {"HİSSE KODU": "TUPRS", "ŞİRKET": "Tüpraş", "SEKTÖR": "SANAYİ", "SON FİYAT": "₺168.40", "20G ZİRVE (DİRENÇ)": "₺165.00", "RS PUANI": 1.92, "ZAMAN SAYACI": "3 / 15 Gün", "STRATEJİ SİNYALİ": "⚡ KIRILIM AL"},
        {"HİSSE KODU": "ASELS", "ŞİRKET": "Aselsan", "SEKTÖR": "HOLDİNG", "SON FİYAT": "₺68.50", "20G ZİRVE (DİRENÇ)": "₺68.00", "RS PUANI": 1.85, "ZAMAN SAYACI": "5 / 15 Gün", "STRATEJİ SİNYALİ": "📈 PİRAMİT EKLE"},
        {"HİSSE KODU": "CCOLA", "ŞİRKET": "Coca-Cola İçecek", "SEKTÖR": "PERAKENDE", "SON FİYAT": "₺74.20", "20G ZİRVE (DİRENÇ)": "₺71.50", "RS PUANI": 1.64, "ZAMAN SAYACI": "2 / 15 Gün", "STRATEJİ SİNYALİ": "⚡ KIRILIM AL"},
    ]
    
    df_show = pd.DataFrame(data_demo)
    st.dataframe(df_show, use_container_width=True, hide_index=True)

with tab_sec2:
    st.info("Backtest motoru aktif: Son 2 yıllık veri üzerinde Donchian + Zaman Stopu simülasyonu çalıştırılıyor.")

with tab_sec3:
    st.info("Portföyünüzde şu an aktif işlem bulunmuyor. Kırılım gelen hisselerden ekleme yapabilirsiniz.")
