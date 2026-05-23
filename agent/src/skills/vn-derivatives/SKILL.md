---
name: vn-derivatives
description: "Vietnam derivatives market: VN30 Futures (VN30F) contract specs, basis and hedging, covered warrants (chứng quyền có đảm bảo) pricing and Greeks, VN30-linked ETFs for indirect exposure, and trading conventions specific to the Vietnamese derivatives ecosystem."
category: analysis
---

# Vietnam Derivatives Market

## Overview

Vietnam's derivatives universe is narrow but tradeable: VN30 Index Futures (launched 2017) plus covered warrants (CW, launched 2019). There are no listed equity options, no put warrants, no bond futures, and no FX derivatives accessible to retail. Despite these limits, VN30F is the most important risk-transfer instrument in Vietnam — it carries 5x–10x the daily notional of cash VN30 turnover. This skill encodes contract specs, basis behavior, CW pricing nuances, and the ETF channels that round out the exposure toolkit.

Applicable scenarios:
- Hedging long VN equity exposure (only true short channel in the market)
- Directional intraday or swing trading via futures leverage
- Basis trading (cash-and-carry / reverse) between VN30F and constituents
- Covered warrant directional bets on single VN30 names with embedded leverage
- ETF arbitrage between VN30 cash basket and listed ETFs

## Core Concepts

### VN30 Index Futures (VN30F)

```
Listing venue:        HNX (cleared by VSDC)
Underlying:           VN30 Index
Launch:               10-Aug-2017
Contract size:        VND 100,000 × index points
                        e.g. VN30 at 1,300 -> contract notional = 1,300 × 100,000 = VND 130,000,000 (~USD 5,100)
Tick size:            0.1 index point = VND 10,000 per contract
Daily price limit:    ±7% from reference price (matches HoSE limit on VN30 underlying)
Settlement:           Cash-settled, T+1
Trading hours:        08:45 – 11:30 and 13:00 – 14:30 (HoSE same-day cash close at 14:45 print)
Last trading day:     3rd Thursday of contract month
Final settlement:     Average of VN30 spot during last 30 minutes of last trading day
```

Contract months (4 simultaneously listed):
- Near month
- Next month
- Two nearest quarterly months from {March, June, September, December}

```
Ticker format: VN30FYYMM
  VN30F2403  = March 2024 contract
  VN30F2406  = June 2024 contract
  VN30F2412  = December 2024 contract

Front-month (VN30F1M) carries 90%+ of total derivatives volume in Vietnam.
```

Margin:
```
Initial margin:       ~10% of contract value (broker-specific, can be 13–17%)
Maintenance margin:   ~8% of contract value
Mark-to-market:       Daily, with same-day cash variation margin call

Implication: VN30 dropping 7% in a day = full margin wipe + call for additional cash.
              Holders without spare cash face forced close ("đóng vị thế bắt buộc").
```

### VN30F Basis (Futures vs Spot)

```
Basis = F - S
Annualized basis = (F - S)/S × (365 / days_to_expiry)

Typical basis behavior:
  Bull market sentiment:    Front-month F > S (contango, positive basis)
  Bear / hedge demand:      Front-month F < S (backwardation, negative basis)
  Pre-event uncertainty:    Wide basis swings
  Last week to expiry:      Basis converges to zero

Cost-of-carry decomposition:
  F = S × (1 + r × t) - PV(dividends until expiry)
  Where r is risk-free, but in VN the basis often deviates from theoretical due to:
    - Short selling impossible in cash market -> no easy cash-and-carry reverse arbitrage
    - Margin demand spikes during sell-offs -> basis goes deeply negative
    - Retail speculative positioning amplifies basis moves
```

Trading uses of basis:
- **Hedging**: long-only VN equity book hedges via short VN30F (note: tracking error vs non-VN30 names)
- **Directional**: positive view -> long VN30F (10x leverage on capital)
- **Basis trade**: when basis goes deeply negative pre-expiry, long VN30F + short basket (if institutional) or simply long futures expecting convergence
- **Calendar spread**: long front / short next-month or vice versa, tracks roll yield

### Position Limits and Margin Mechanics

- Maximum open positions per retail account: 5,000 contracts (broker-specific, often lower)
- Position is per contract month
- Mandatory clearing through VSDC
- Realized P&L credited / debited daily (no equity-style T+2.5 lag)
- Tax on futures: 0.1% × notional on each side (~equivalent to capital gains tax for stocks but on every leg)

### Covered Warrants (CW / Chứng Quyền Có Đảm Bảo)

```
Issuer:               Licensed securities companies (SSI, VPS, HSC, MBS, VCSC, KIS, ACBS, ...)
Listing venue:        HoSE
Type:                 European-style CALL warrants only (no puts as of 2024–2026)
Underlying:           VN30 constituent stocks (each issuer chooses)
Tenor:                Typically 3 – 24 months
Settlement:           Cash-settled at expiry (no physical delivery)
                        Payoff = max(S_settle - K, 0) / conversion ratio
                        Where S_settle = average of underlying closing price over last 5 sessions
```

Ticker format: `C<UND><YY><MM><STRIKE><ISSUER>`
- C = Call
- UND = underlying ticker
- YYMM = expiry year/month
- STRIKE = strike price (sometimes encoded)
- ISSUER = SSI / VPS / MBS / etc.

```
Example: CVNM2404C24000SSI
  C       = Call warrant
  VNM     = underlying (Vinamilk)
  2404    = expires April 2024
  C24000  = strike 24,000 VND (and Call type marker)
  SSI     = issued by SSI

In practice, ticker conventions vary slightly by issuer; always verify on issuer prospectus.
```

CW Pricing (Black-Scholes):
```
CW price = (1/k) × BS_Call(S, K, T, r, σ, q)
  k   = conversion ratio (e.g., 5:1 means 5 warrants needed for 1 share equivalent payoff)
  S   = spot of underlying
  K   = strike
  T   = time to expiry in years
  r   = risk-free rate (~3–5%, VND short rate)
  σ   = implied volatility (often 25–60% for VN30 names)
  q   = expected dividend yield until expiry

Greeks to monitor:
  Delta:    sensitivity to spot (typically 0.3–0.8 for at-the-money near expiry)
  Gamma:    delta acceleration; high near at-the-money near expiry
  Theta:    time decay; aggressive in last 30 days
  Vega:     IV sensitivity; matters in 3-6 month CWs
  Rho:      negligible in VN context
```

Conversion ratio (`k`) is critical:
```
Underlying share at VND 90,000
Strike VND 100,000
CW market price 1,000 VND
Conversion ratio 10:1 (10 warrants per 1 share equivalent)

Effective premium = (10 × 1,000 + 100,000 - 90,000) / 90,000 = 22.2%
Effective leverage = (Spot / CW price) × Delta = (90,000/1,000) × 0.5 = 45x notional × delta
                   ≈ 5–10x effective directional leverage on capital deployed
```

CW Risks (all bear-trap territory for retail):
1. **Theta decay**: out-of-the-money CWs lose ~1–3% per day in last month -> holding period must be days-to-weeks, not months
2. **Issuer credit risk**: payoff depends on issuer solvency; in practice low risk in VN (large securities firms) but non-zero
3. **Wide bid-ask spreads**: market-maker monopoly by issuer; spread can be 5–10% of CW price
4. **Implied vol mark-down**: issuer can quote lower IV when retail wants to sell -> compounds losses
5. **No put CW**: cannot express bearish view on single names via CW; must use VN30F for index shorts

CW market-making mechanics:
```
Issuer hedges its short CW position by delta-hedging the underlying.
Issuer's hedging buy/sell flow in the underlying can amplify moves in underlying near expiry.
When a name has very large CW open interest near at-the-money, expect higher gamma-induced volatility.
```

### No Options Market

```
As of 2024–2026, Vietnam has NO listed:
  - American-style options
  - Put options (only European call CWs)
  - Single-stock futures
  - Currency or interest rate futures (for retail / standard channels)
  - Bond futures (G-bond futures planned but not yet launched)

Implications:
  - Cannot hedge specific single-stock long exposure with puts
  - Vol surface / skew analysis limited to whatever CW IVs reveal
  - Tail-risk hedging at portfolio level = VN30F short only (basis risk vs non-VN30 holdings)
```

### VN30-Linked ETFs

Three primary VN30-tracking ETFs (HoSE-listed):

| Ticker | Issuer | Notes |
|--------|--------|-------|
| E1VFVN30 | Vietfund Management (VFM, originally) | First Vietnamese ETF, launched 2014 |
| FUEVFVND | VinaCapital | "Diamond ETF" — tracks Diamond Index (room-full names focus) |
| VFMVN30 | DragonCapital VFM | VN30 tracker |
| FUESSV50 | SSI Asset Management | Tracks SSIAM VN50 |
| FUEVN100 | Various | VN100 broader tracker (not always available) |

Use cases:
- Foreign investors use Diamond ETF (FUEVFVND) to gain exposure to room-full names (VNM, FPT, MWG, ACB, ...)
- Domestic investors use VN30 ETFs as low-fee market-beta vehicles
- ETF arbitrage: NAV vs market price gap, primary creation/redemption by APs

### Comparison: VN30F vs CW vs ETF

| Dimension | VN30F | CW (Call) | ETF (e.g., E1VFVN30) |
|-----------|-------|-----------|----------------------|
| Direction | Long or short | Long only | Long only |
| Leverage | ~10x | 5–10x effective | 1x |
| Settlement | Cash, T+1 | Cash, at expiry only | T+2.5 like stock |
| Margin | Required | Full premium upfront | Full premium upfront |
| Time decay | None (futures) | Strong (theta) | None |
| Issuer credit risk | None (cleared) | Yes (issuer-specific) | None (cash basket) |
| Trading hours | 08:45–14:30 | HoSE hours | HoSE hours |
| Tax | 0.1% notional × 2 | Standard equity | Standard equity |

### Bond Market and G-Bond Futures

```
Government bond market:
  - VST (Vietnam State Treasury) auctions weekly
  - 5Y, 10Y, 15Y, 20Y, 30Y tenors
  - Secondary trading thin; quotes via primary dealers
  - 10Y yield range 2024–2026: ~2.5–4.5%
  - Used by banks and insurers for HTM book; limited speculative use

G-bond futures:
  - Planned for launch but not yet live as of 2024–2026
  - When launched, would enable duration hedging for institutional
```

## Analysis Framework

### 1. When to Use VN30F vs CW vs Cash

```
Use VN30F when:
  □ Want directional exposure to broad market (long or short)
  □ Need hedge for long VN equity book
  □ Capital efficient (10x leverage)
  □ Holding period: minutes to days
  □ Want T+1 P&L (no settlement lag)

Use Covered Warrants when:
  □ Have directional view on single VN30 stock (long only)
  □ Want defined max loss (premium paid)
  □ Comfortable with theta decay
  □ Holding period: 1 week to 2 months max
  □ Stock has actively traded CW (verify open interest > 500k units)

Use Cash equity / ETF when:
  □ Long-term holding (>3 months)
  □ Need dividend entitlement
  □ Building portfolio for income / wealth accumulation
  □ Foreign with room constraint on direct names -> use Diamond ETF
```

### 2. VN30F Basis Trading Setup

```
Pre-conditions:
  - Identify basis at >2% (absolute) annualized away from theoretical
  - Days to expiry < 30 (convergence pressure)
  - Adequate liquidity in front-month (>50,000 contracts daily volume)

Long-basis trade (basis negative, futures cheap):
  Long VN30F1M (front month)
  Hedge: short next-month VN30F2M (calendar spread) to isolate basis
        OR short VN30 ETF (basket proxy, retail can do this)

Track basis convergence; exit at zero basis or 50% of original gap.
Risk: ETF tracking error vs index; calendar spread basis can move further apart.
```

### 3. Covered Warrant Filter

```
Universe screen for tradeable CWs:
  □ Open interest > 500,000 units
  □ 20-day average volume > 50,000 units
  □ Days to expiry between 30 and 120 (avoid both gamma blow-up and excessive theta)
  □ Delta between 0.4 and 0.7 (near-the-money region)
  □ Bid-ask spread < 3% of mid price
  □ Implied vol within 1.5x of underlying realized vol (not over-marked by issuer)

Sample setup for bullish view on HPG:
  Pick a HPG call CW with:
    - 60 days to expiry
    - Delta ~0.5
    - IV not >40% (avoid overpriced)
  Compare expected return for +10% spot move:
    Cash equity: +10%
    CW (delta 0.5, ~5x leverage):  +50% × (1 - decay_in_holding_period)
```

### 4. Hedging Long VN Equity Book with VN30F

```
Portfolio beta-adjusted hedge:
  Hedge_ratio = portfolio_VN30_beta × portfolio_value / VN30F_contract_value
  Round to whole contracts

Example:
  Portfolio VND 10bn, beta 0.95 to VN30
  VN30 = 1,300; contract value = 1,300 × 100,000 = 130mn
  Number of short VN30F contracts = 0.95 × 10,000,000,000 / 130,000,000 ≈ 73 contracts

Margin required to short 73 contracts ≈ 10% × 73 × 130mn = ~950mn VND (~9.5% of portfolio)
Be sure to model variation margin top-up if VN30 moves against the short.
```

## Output Format

VN derivatives positioning summary:

```
=== VN Derivatives Snapshot — 2026-03-15 ===

VN30F1M (VN30F2603):
  Price:               1,318.5
  Spot VN30:           1,315.2
  Basis:               +3.3 pts (+0.25%, annualized +30%, contango bullish)
  Open interest:       42,500 contracts
  Daily volume:        58,000 contracts

CW spotlight (HPG):
  CHPG2406C30000SSI (strike 30,000, exp Jun 2026, SSI)
    Price 2,400 / Delta 0.55 / IV 35% / DTE 90
    Open interest 1.2mn units, 20D ADV 85,000 units, B/A spread 1.5%
    Recommendation: tradeable; size 1% of book max

Portfolio hedge recommendation:
  Short 73 VN30F2603 to neutralize VN30 beta of long book
  Margin required: ~VND 950mn (kept in derivatives sub-account)
  Roll: 3 days before expiry (Mar 18) into VN30F2604
```

## Notes

1. **VN30 rebalancing impact on VN30F**: semiannual rebalancing (Jan / Jul) shifts index composition; basis can spike around rebalance announcement (mid-Dec / mid-Jun)
2. **Single-day futures volume can exceed cash market volume**: a 7%+ VN30 day can see VN30F volume 3x larger than entire HoSE cash turnover — futures are the dominant directional vehicle
3. **Margin calls during sell-offs**: 2022 sell-off triggered cascade liquidations in retail futures accounts; risk-manage stop-loss before margin call automation kicks in
4. **No overnight gap protection**: futures close 14:30, cash market 14:45; ATC print on cash can gap vs futures last trade — not arb-able directly
5. **CW expiry mechanics**: many retail forget that European CW pays only at expiry; cannot exercise early. Some CWs have low remaining liquidity in last 2 weeks pre-expiry, so plan exit window
6. **Issuer hedging flow**: large CW open interest near expiry creates gamma-driven volatility in the underlying — watch out for the last week
7. **Tax efficiency**: VN30F tax (0.1% notional per leg) is higher than cash equity for high-frequency strategies; size accordingly

## Dependencies

```bash
# Vietnamese derivatives data sources
# - HNX (hnx.vn): VN30F tick data, daily summaries
# - HoSE (hsx.vn): CW issuance, listings
# - VSDC (vsd.vn): clearing data
# - Broker terminals: SSI iBoard, VPS SmartOne, VND Trade, TCBS
pip install pandas numpy scipy  # for BS pricing of CWs
pip install vnstock              # for cash + some derivatives data
```
