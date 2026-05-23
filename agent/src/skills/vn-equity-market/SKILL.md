---
name: vn-equity-market
description: "Vietnam equity market microstructure: exchange structure (HoSE / HNX / UPCoM), price limits, T+2.5 settlement, lot sizes, foreign ownership limits (room), trading sessions and ATC, VN-Index / VN30 construction, margin and short-sale rules, common VN30 constituents, fees and taxes, state-owned enterprise dynamics."
category: analysis
---

# Vietnam Equity Market Microstructure

## Overview

The Vietnamese equity market is a frontier-to-emerging market with three trading venues, daily price limits, a managed float currency, and structural foreign ownership constraints. Compared to A-shares or US markets, the VN market is smaller (USD ~250bn market cap), more retail-driven (>85% of volume), and has unique rules (T+2.5 settlement, FOL room, no retail short selling). This skill encodes the trading mechanics needed before running any quantitative or fundamental analysis on Vietnamese stocks.

Applicable scenarios:
- Sizing positions against effective liquidity (price limit gap risk)
- Modeling realistic execution costs (fees + tax + spread + foreign room scarcity premium)
- Filtering universe by exchange listing tier (HoSE / HNX / UPCoM)
- Adjusting backtests for T+2.5 settlement and ATC session dynamics
- Mapping FOL (foreign ownership limit / "room") availability before buying VN30 names

## Core Concepts

### Exchange Structure

Three trading venues, each with its own rules:

| Exchange | Full Name | Listing Tier | Price Limit (Daily) | Lot Size | Notes |
|----------|-----------|--------------|---------------------|----------|-------|
| HoSE | Ho Chi Minh Stock Exchange | Main board | ±7% | 100 shares | Largest, hosts VN-Index and VN30 |
| HNX | Hanoi Stock Exchange | Secondary | ±10% | 100 shares | Smaller caps, HNX-Index |
| UPCoM | Unlisted Public Company Market | OTC-style | ±15% | 1 share | Pre-listing / declassified, lowest liquidity |
| IPO day | (first trading day) | — | ±20% | per exchange | Wider band only on debut |

```
Practical implications:
  - HoSE price limits cap daily moves more tightly than HNX/UPCoM
  - A locked-limit ("kịch trần" up / "kịch sàn" down) means no fills today
  - UPCoM is illiquid; many state-owned firms divest here before HoSE migration
```

### Settlement: T+2.5

```
Vietnam settlement is T+2.5 (settlement on T+2 afternoon, ~13:30):
  Buy on Monday morning -> shares available to sell Wednesday afternoon
  Buy on Friday        -> shares available to sell Tuesday afternoon (next week)
  Sell proceeds clear T+2.5 -> cash usable on T+2 afternoon

Pre-2022 it was T+3 cash; the 2022 cycle compression to T+2.5 was a notable liquidity event.
Implication for quants: cannot day-trade the same share with intraday cash unless using margin.
```

### Lot Size and Odd Lots

- HoSE / HNX board lot: 100 shares (round lot)
- UPCoM: 1 share
- Odd lots (1–99 shares) can only trade via odd-lot board (separate price, large discount, low liquidity)
- Block trade ("giao dịch thỏa thuận"): manually negotiated, min 20,000 shares or VND 3bn notional on HoSE; reported separately

### Trading Hours (HoSE / HNX, Vietnam time, UTC+7)

```
09:00 – 09:15   ATO (opening call auction)
09:15 – 11:30   Continuous morning session
11:30 – 13:00   Lunch break (markets closed)
13:00 – 14:30   Continuous afternoon session
14:30 – 14:45   ATC (closing call auction) — defines daily closing reference
14:45 – 15:00   Putthrough / block trade window (HoSE)
```

ATC is critical: index closing price is set here, ETF arbitrage and NAV pricing concentrate around 14:30, and many large orders queue for the closing print. Quant models that rely on closing price must account for ATC volume bulge (often 10–20% of daily turnover in one 15-min window).

### Price Limits ("Biên độ dao động")

Reference price ("giá tham chiếu") = previous day close (HoSE) or previous day VWAP / close depending on exchange rules.

```
Ceiling ("giá trần") = ref × (1 + limit)
Floor   ("giá sàn") = ref × (1 - limit)

If a name locks ceiling on news, you cannot buy at any price until next day (or until a seller appears).
If a name locks floor on panic, you cannot exit until next day.
```

Gap risk: a stock can lose 7% on HoSE every day with no fills available -> a -30% move over 5 sessions is possible (consecutive floor closes). This was repeatedly seen in the 2022 NVL / PDR / HPX real-estate distress cycle.

### Foreign Ownership Limit (FOL) / "Room"

Each listed company has a maximum foreign ownership cap. "Room còn lại" ("remaining room") is the bandwidth before foreign investors can no longer buy on-exchange.

| Sector | Standard FOL |
|--------|--------------|
| Most listed equities (default) | 49% |
| Banks ("ngân hàng") | 30% |
| Restricted strategic sectors (oil & gas distribution, defense, certain telecom) | 0% – varies |
| Some firms with NVDR-like instruments | 100% effective |

```
Room dynamics:
  - VCB, VNM, FPT, MWG are chronically at or near room cap -> foreign buyers pay a "premium" via foreign board ("giao dịch ngoại")
  - Premium to local price can be 5–15% for room-constrained names
  - Diamond ETF (FUEVFVND) was built to give foreigners exposure to room-full names
  - When a company increases its FOL (regulatory approval), foreign inflow surges -> short-term tailwind
```

### Index Construction

```
VN-Index:
  Constituents: all HoSE-listed common shares
  Weighting:    free-float adjusted market cap
  Base:         100 on 28-Jul-2000
  Today (2024–26 range): typically 1,100–1,500

VN30:
  Constituents: 30 largest HoSE stocks by market cap + liquidity
  Weighting:    free-float adjusted with 10% individual weight cap
  Rebalanced:   semiannually (Jan & Jul)
  Used for:     ETFs (E1VFVN30, FUEVFVND, VFMVN30), VN30 Futures (VN30F), Covered Warrants
  Notable:      8–10 names typically dominate >60% of VN30 weight

HNX-Index:
  All HNX stocks, market-cap weighted

UPCOM-Index:
  All UPCoM stocks, market-cap weighted

VN30F:
  VN30 Futures (HNX-listed), cash-settled, see vn-derivatives skill
```

### Common VN30 Constituents (illustrative, subject to rebalancing)

| Sector | Tickers | Notes |
|--------|---------|-------|
| Banking | VCB, BID, CTG, VPB, MBB, TCB, ACB, STB, HDB | Largest VN-Index weight bucket |
| Real estate | VIC, VHM, VRE, KDH, NVL, PDR | Vingroup ecosystem dominant |
| Steel | HPG, HSG | HPG alone ~40% of domestic steel |
| Tech | FPT, CMG | FPT is rare 100% foreign-room-open large cap |
| Retail / Consumer | MWG, FRT, PNJ, VNM, MSN, SAB | MWG = Mobile World + Bach Hoa Xanh |
| Energy | GAS, PLX, POW | Mostly SOE-controlled |
| Aviation | VJC, HVN | VJC private LCC; HVN SOE flag carrier |

### Margin Trading

- Only stocks on the "approved margin list" can be margined (refreshed quarterly by SSC)
- Maximum margin ratio: 50% (initial); brokers offer 40–50% in practice
- Margin call ("call margin") triggers if equity ratio falls below ~30%
- Forced sell ("force sell" / "bán giải chấp") cascades created the 2022 real-estate flash sell-offs
- Margin balance is a key sentiment indicator: monthly broker margin balance growth >15% YoY is a leading top signal

### Short Selling

- Retail short selling: not permitted (as of 2024–2026)
- Stock lending / SBL: very limited, institutional only via approved bilateral structures
- ETF shorting: only via VN30F (futures) for directional shorts on the index
- Implication: cash equity strategies are long-only; bearish views must use VN30F or covered puts (which do not exist in CW market – only call CWs available)

### Fees and Taxes

```
Brokerage fee (per side):      0.15% – 0.25% (varies by broker; large clients ~0.08%)
Capital gains tax (sell only): 0.10% of sell proceeds (flat, not on profit)
Stock dividend tax:            5% on declared par value (income tax on individuals)
Cash dividend tax:             5% on cash received
VAT / stamp duty:              none on listed equity trades

Round-trip cost estimate for retail: 30–60 bps + spread.
```

### Corporate Actions

Key Vietnamese terms:

| Vietnamese | English | Implication |
|------------|---------|-------------|
| Cổ tức bằng tiền | Cash dividend | Ex-date price adjusted down by gross dividend |
| Cổ tức bằng cổ phiếu | Stock dividend (bonus shares) | Float increases; price adjusted by ratio |
| Phát hành thêm | Rights issue / follow-on issuance | Dilutive; subscription rights tradable |
| Chia tách / tách cổ phiếu | Stock split | Adjustment ratio applied |
| Chốt quyền | Record date | Last day to hold for entitlement |

Ex-rights date ("ngày giao dịch không hưởng quyền") = T-1 from record date (because T+2.5 settlement minus 1 because new entitlement rule is "T+1 from record date is the entitlement date" — practical effect: trade before this date to be entitled).

### State Ownership

Many large caps are state-owned enterprises (SOEs) where the government (via SCIC, MOF, or line ministries) holds >50%:

- VCB, BID, CTG (banks): MOF / SBV ~65–75% stake
- GAS, PLX (energy): PetroVietnam / MOF majority
- SAB (Sabeco beer): MOIT remaining stake post-ThaiBev sale
- HVN (Vietnam Airlines): MOF majority
- VNM, FPT, MWG: privatized / private-controlled (lower government stake)

Implications:
- Free float is often much smaller than market cap suggests
- Government divestment ("thoái vốn") events can be significant liquidity shocks
- Dividend policy partly driven by state budget needs
- Strategic decisions slower; M&A activity restricted

## Analysis Framework

### 1. Pre-Trade Checklist for a VN Equity Position

```
□ Exchange (HoSE / HNX / UPCoM)? -> sets price limit and lot size
□ Daily price limit -> max single-day adverse move
□ Foreign room remaining? -> can I buy on-exchange at local price?
□ ADV (20-day average daily volume) -> liquidity score
□ Position size vs 10% of ADV -> estimated days-to-exit
□ State ownership % -> effective float
□ Margin-eligible? -> can institutional clients leverage
□ Upcoming corporate action (ex-date within 30 days)?
□ Estimated all-in round-trip cost: fees 0.4% + tax 0.1% + spread X bps
```

### 2. Liquidity Scoring

```
ADV bucket (USD-equivalent daily turnover):
  Tier 1: > USD 10M     -> VCB, HPG, VHM, FPT, MWG class
  Tier 2: USD 2M – 10M  -> most VN30 constituents
  Tier 3: USD 0.5M – 2M -> mid-caps, some HNX leaders
  Tier 4: < USD 0.5M    -> small / UPCoM (most institutional capital cannot trade)

Effective tradeable size = min(20% of ADV per day, foreign room remaining if foreign).
```

### 3. ATC Volume Concentration

```
Typical HoSE intraday volume distribution:
  ATO (09:00–09:15):      ~5–8%
  Morning continuous:     ~35–40%
  Afternoon continuous:   ~35–40%
  ATC (14:30–14:45):      ~10–20%  <- index print, ETF rebalance, large order finalization

Quant impact:
  - VWAP execution must oversample ATC slot
  - Closing price has more institutional weight than midday print
  - ATC-only orders ("ATC order type") fill at the call auction equilibrium price only
```

### 4. Price-Limit Gap Risk Estimation

```
For position with concentrated bear-case downside:
  Max daily loss (HoSE name): 7%
  5-day cumulative if locked floor: 1 - 0.93^5 = -30%
  10-day: 1 - 0.93^10 = -52%

Use this as the hard scenario for VaR; historical max drawdowns of 2022 distressed names hit -70%+ over <20 sessions.
```

## Output Format

VN equity microstructure cheat-card:

```
=== VN Equity Pre-Trade Card ===
Ticker:               VCB
Exchange:             HoSE
Price limit:          ±7% (ref: 92,500 -> trần 98,975 / sàn 86,025)
Lot size:             100
Settlement:           T+2.5 (cash D+2 PM)
FOL (sector cap):     30% (bank)
Foreign room:         ~0% remaining -> foreign premium ~6–10%
20D ADV (VND):        ~250 bn (~USD 10M)
State ownership:      MOF / SBV ~74.8% -> effective free float ~25%
Margin eligible:      Yes
Upcoming events:      Ex-cash-div 8% on 2026-06-12
Round-trip cost:      ~0.45% (fee 0.15%×2 + tax 0.10% + spread ~5 bps)

=== Execution notes ===
- ADV-implied 5-day exit at 20% participation: ~USD 10M position max
- Foreign buyer must use put-through / foreign board at premium
- ATC closes ~15% of daily turnover -> use ATC slice in VWAP
```

## Notes

1. **HoSE upgrade timeline**: market is targeting frontier-to-emerging reclassification (FTSE EM and MSCI EM watch list); reforms include pre-funding removal for foreigners, CCP central clearing, and shorter settlement to T+2 — track these milestones, they are flow events
2. **Retail dominance**: >85% of volume is domestic retail; sentiment-driven volatility is sharper than in institutional markets, behavioral-finance signals work well
3. **System outages**: HoSE has had multi-day matching engine outages historically (2020–2021); business continuity risk is real
4. **Disclosure delay**: company disclosure can be slower than HK / US standards; verify via SSC ("Ủy ban Chứng khoán Nhà nước") and FiinPro / Vietstock databases
5. **Holiday calendar**: market closes for Tet (Lunar New Year, ~5 trading days end Jan / early Feb), Reunification + Labour Day (Apr 30 + May 1), National Day (Sep 2 + 1) — these create gaps and pre-holiday volume drops
6. **Currency**: prices quoted in VND; for USD-based portfolios apply USD/VND of ~24,500–26,000 (managed float band) and track SBV intervention signals

## Vietnamese News & Data Sources

When searching for Vietnamese market news, **always use `region="vn-vi"`** in `web_search` and prefer these sources:

| Source | URL | Nội dung |
|---|---|---|
| CafeF | cafef.vn | Tin tức tài chính, phân tích cổ phiếu, BCTC |
| Vietstock | vietstock.vn | Phân tích kỹ thuật, dữ liệu giao dịch |
| VnEconomy | vneconomy.vn | Kinh tế vĩ mô, chính sách |
| Tinnhanh CK | tinnhanhchungkhoan.vn | Tin chứng khoán nhanh |
| NDH | ndh.vn | Tin doanh nghiệp, nhịp điệu thị trường |
| Fireant | fireant.vn | Cộng đồng đầu tư, tin tức real-time |
| HOSE chính thức | hsx.vn | Công bố thông tin chính thức HoSE |
| HNX chính thức | hnx.vn | Công bố thông tin chính thức HNX |
| SSI Research | ssi.com.vn/Research | Báo cáo phân tích từ SSI |
| Viet Capital | vcsc.com.vn | Báo cáo VCSC |
| FiinGroup | fiingroup.vn | Dữ liệu cơ bản, FiinPro (trả phí) |

**Search patterns for Vietnamese market:**
```
# Tin tức cổ phiếu cụ thể
web_search(query="VCB kết quả kinh doanh 2024 site:cafef.vn OR site:vietstock.vn", region="vn-vi")

# Tin vĩ mô
web_search(query="SBV lãi suất tháng 5 2025", region="vn-vi", max_results=8)

# Công bố thông tin chính thức
web_search(query="HPG công bố thông tin site:hsx.vn", region="vn-vi")

# Phân tích chuyên sâu
web_search(query="VN30 phân tích kỹ thuật site:vietstock.vn", region="vn-vi")
```

## Dependencies

```bash
pip install vnstock         # Vietnamese ticker fundamentals + OHLCV
pip install pandas numpy
```
