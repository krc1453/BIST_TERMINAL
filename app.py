import yfinance as yf
import pandas as pd
import numpy as np

# BIST 50 Likit Havuzu
bist50_tickers = [
    "THYAO.IS", "TUPRS.IS", "ASELS.IS", "EREGL.IS", "BIMAS.IS",
    "CCOLA.IS", "KCHOL.IS", "SAHOL.IS", "ASTOR.IS", "TCELL.IS",
    "SISE.IS", "PGSUS.IS", "GUBRF.IS", "MGROS.IS", "DOHOL.IS",
    "AKBNK.IS", "GARAN.IS", "ISCTR.IS", "YKBNK.IS",
    "ALARK.IS", "ARCLK.IS", "BRSAN.IS", "CIMSA.IS", "EKGYO.IS",
    "ENJSA.IS", "ENKAI.IS", "FROTO.IS", "HEKTS.IS", "KRDMD.IS",
    "KONTR.IS", "OYAKC.IS", "PETKM.IS", "SASA.IS", "TAVHL.IS", 
    "TKFEN.IS", "TOASO.IS", "TTKOM.IS", "ULKER.IS", "VESTL.IS", 
    "MAVI.IS", "DOAS.IS"
]

bist50_tickers = list(set(bist50_tickers))

# 1. Canlı Verileri İndir
data = yf.download(bist50_tickers, period="1y", interval="1d", progress=False)['Close'].ffill().bfill()

# 2. Göstergeleri Hesapla (20 Günlük Donchian Zirvesi)
donchian_high = data.rolling(20).max()
latest_prices = data.iloc[-1]
prev_donchian = donchian_high.iloc[-2]

results = []
for t in bist50_tickers:
    if t in latest_prices and t in prev_donchian:
        sym = t.replace(".IS", "")
        price = latest_prices.loc[t]
        resistance = prev_donchian.loc[t]
        
        # Sinyal Mantığı
        if price > resistance:
            signal = "⚡ KIRILIM AL"
        else:
            signal = "İzlemede / Beklemede"
            
        results.append({
            "HİSSE KODU": sym,
            "SON FİYAT": f"₺{price:.2f}",
            "20G DİRENÇ": f"₺{resistance:.2f}",
            "STRATEJİ SİNYALİ": signal
        })

df_live = pd.DataFrame(results)
# Sadece kırılım verenleri veya tüm listeyi filtreleyebilirsiniz
print(df_live.to_string(index=False))
