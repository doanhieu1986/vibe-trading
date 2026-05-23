# Vibe Trading — Tài Liệu Cho Nhà Đầu Tư Việt Nam

> Tài liệu này giúp một trader/dev người Việt hiểu nhanh dự án **Vibe-Trading** (`vibe-trading-ai` trên PyPI) — gồm lý do tác giả tạo ra, các tính năng đã xây theo dòng thời gian, kiến trúc tổng quan, và quan trọng nhất: **làm sao áp dụng cho thị trường chứng khoán Việt Nam** (VN-Index, VN30, HoSE, HNX, UPCoM).

---

## 1. Dự Án Là Gì & Mục Đích Của Tác Giả

**Vibe-Trading** là một **AI agent dành cho nghiên cứu tài chính**. Hiểu đơn giản: bạn gõ câu hỏi bằng ngôn ngữ tự nhiên (tiếng Việt, tiếng Anh, tiếng Trung…), một LLM (DeepSeek, GPT, Gemini, Qwen, Kimi, hoặc Ollama chạy local…) sẽ tự lên kế hoạch, gọi các tool có sẵn (lấy giá, chạy backtest, đọc PDF, search web, phân tích option Greeks…) và trả ra kết quả có thể tái lập (run card).

**Tác giả:** Nhóm **HKUDS** (Hong Kong University Data Science Lab) tại Đại học Hong Kong (email: `hkuds@connect.hku.hk`). Đây là nhóm nghiên cứu học thuật, không phải công ty môi giới. License **MIT**, mã nguồn mở hoàn toàn.

**Ý đồ thiết kế:**

| Mục đích | Cách triển khai trong code |
|---|---|
| Biến câu hỏi tài chính thành **phân tích có thể chạy được** | Agent loop + 22 MCP tools + 75 skill |
| **Không** giao dịch tự động (không kết nối broker) | Chỉ làm research/backtest/báo cáo |
| Đa thị trường, đa nguồn dữ liệu, **auto fallback** khi nguồn lỗi | 6 data loader + 7 backtest engine |
| Cho phép **agent học theo người dùng** qua bộ nhớ bền vững | `~/.vibe-trading/memory/*.md` với FTS5 |
| Có thể chạy **đội nhiều agent** (debate Bull/Bear, risk review…) | Swarm engine với 29 preset |
| Tái lập được 100% mọi kết quả backtest | Run card JSON + Markdown |

> Tóm lại: tác giả muốn xây một **"Claude Code dành riêng cho tài chính"** — bạn vibe (gõ tự nhiên), nó trade research (chứ không phải vibe trade tiền thật).

---

## 2. Hành Trình Xây Dựng (Theo Thời Gian)

Dữ liệu từ `git log` và `CHANGELOG.md`. Bản gốc commit đầu tiên ngày **2026-04-01**, đến nay đã 0.1.8.

| Ngày | Sự kiện lớn | Ý nghĩa |
|---|---|---|
| 2026-04-01 | Initial commit | Khởi tạo repo |
| 2026-04-08 | Multi-market backtest engine + Pine Script v6 export + 5 data sources auto-fallback | Nền móng đầu tiên: backtest đa thị trường |
| 2026-04-09 | **Wave 2**: ChinaFutures, GlobalFutures, Forex, Options v2 engine + Monte Carlo, Bootstrap CI, Walk-Forward | Thêm validation thống kê |
| 2026-04-10 | **v0.1.4** lên PyPI; multi-provider (12 LLM); Docker fix; thêm `akshare`/`ccxt` | Phát hành chính thức |
| 2026-04-11 | `vibe-trading init` (bootstrap .env), preflight check, fallback runtime; README đa ngôn ngữ (zh, ja, ko) | Đầu vào dễ dùng cho người mới |
| 2026-04-12 | `/pine` export ra **TradingView (Pine v6) + TDX (通达信/同花顺/东方财富) + MetaTrader 5 (MQL5)** | Một lệnh xuất ra 3 nền tảng |
| 2026-04-13 | `CompositeEngine` — backtest **danh mục pha trộn** (A-share + crypto trong một capital pool) | Cross-market portfolio |
| 2026-04-15 | Thêm provider **Z.ai** + **MiniMax** → 13 LLM provider | Đa dạng provider |
| 2026-04-16 | **Agent Harness**: bộ nhớ bền vững xuyên session, FTS5 search, skill CRUD, **5-layer context compression**, tool batching | Agent "có não", nhớ giữa các phiên |
| 2026-04-17 | **Trade Journal Analyzer** + Universal File Reader (PDF/Word/Excel/PPT/ảnh OCR) | Đọc được mọi file người dùng upload |
| 2026-04-18 | **Shadow Account** — trích chiến lược ngầm từ nhật ký giao dịch → backtest → so sánh với thực tế | Tính năng đặc trưng "soi bóng" hành vi của bạn |
| 2026-04-19 | v0.1.5 + bảo toàn `reasoning_content` qua Kimi/DeepSeek/Qwen thinking | Hỗ trợ chế độ "suy nghĩ" của LLM |
| 2026-04-21 | **Futu loader** (HK + A-share); skill **vnpy export** cho CtaTemplate | Tích hợp broker HK + framework giao dịch tiếng Trung |
| 2026-04-27 | Benchmark comparison panel (so với SPY, CSI300…), upload streaming với size limit | Báo cáo chuyên nghiệp hơn |
| 2026-04-28 | **v0.1.6**; AKShare route đúng cho ETF và forex | Hoàn thiện loader |
| 2026-04-30 | Web UI **Settings page** + CLI validation hardening | UI cấu hình thân thiện |
| 2026-05-01 | **Correlation heatmap** dashboard, OpenAI Codex OAuth, `ashare-pre-st-filter` (lọc cổ phiếu ST của TQ) | Phân tích tương quan + risk screening |
| 2026-05-02 | Skill `dividend-analysis`; cập nhật roadmap (Autopilot, Data Bridge, Options Lab, Portfolio Studio, Alpha Zoo, Trust Layer) | Mở rộng chiến lược cổ tức |
| 2026-05-03 → 05 | **Security hardening**: auth cho remote API, sandbox upload/file, tắt shell tool mặc định khi remote | Production-grade |
| 2026-05-06 | **v0.1.7** | Bản release security |
| 2026-05-07 → 08 | **Tushare fundamentals**: lọc theo `income_total_revenue`, `roe`, `total_revenue`… point-in-time | Backtest cơ bản (fundamental) chuẩn PIT |
| 2026-05-10 → 11 | Memory recall improvements (CJK, underscore boundary), Swarm token accounting | Bộ nhớ chính xác hơn |
| 2026-05-12 → 15 | **Trust Layer run card** (run_card.json/.md) hiển thị trên Web UI | Mọi backtest đều có "thẻ tin cậy" |
| 2026-05-14 | Wiki công khai tại **vibetrading.wiki**; memory hỗ trợ Thái/Ả-Rập/Hebrew/Cyrillic | Quốc tế hóa bộ nhớ |
| 2026-05-16 | Hypothesis Registry (đăng ký giả thuyết research), MCP client integration | Quản lý chu trình research |
| 2026-05-17 | **v0.1.8 — Alpha Zoo**: 452 alpha pre-built (qlib158 + alpha101 + gtja191 + academic), CLI `alpha bench`, Web UI `/alpha-zoo`, REST API, blog "Which of the 191 GTJA alphas still work in 2026" | **Bước nhảy lớn nhất**: thư viện factor có sẵn |
| 2026-05-18 | Cleanup pass (-918 LOC), sửa 3 bug latent | Dọn dẹp |
| 2026-05-19 | **Live tool feedback** (heartbeat 3s + progress bar) + graceful Ctrl+C | UX khi chạy lâu |
| 2026-05-20 | description.md + instruction.md với Mermaid diagram | Bản thân tài liệu bạn đang xem được tạo ngay sau đó |

> **Tốc độ phát triển:** chỉ trong **~7 tuần** (1/4 → 20/5) dự án đi từ commit đầu đến 0.1.8 với 452 alpha pre-built, 75 skill, 7 backtest engine, 29 swarm team, 6 nguồn dữ liệu, 13 LLM provider. Đây là dự án phát triển cực nhanh.

---

## 3. Kiến Trúc Đơn Giản

```
Bạn (CLI / Web UI / API / MCP client)
            │
            ▼
   FastAPI server (route, session)
            │
            ▼
        Agent Loop
   (LLM lập kế hoạch, chọn tool, suy nghĩ)
            │
            ▼
       22 Tools sẵn sàng
   (run_backtest, get_market_data, web_search,
    read_document, analyze_trade_journal,
    extract_shadow_strategy, run_swarm, …)
            │
   ┌────────┼────────┐
   ▼        ▼        ▼
 Data    Backtest  Memory
 Loaders  Engines   & Skills
 (6)      (7)       (75)
```

**Vòng đời 1 yêu cầu:**

1. Bạn gõ prompt → API server nhận
2. Agent gắn context (lịch sử + memory + 75 skill + 22 tool)
3. LLM lập kế hoạch: nên gọi tool nào?
4. Tool chạy (có heartbeat 3s + progress bar)
5. Kết quả → LLM tóm tắt → trả về bạn
6. Mọi run đều lưu vào `~/.vibe-trading/runs/<run_id>/` (gồm `metrics.json`, `strategy.py`, `backtest.csv`, `run_card.json`)

**Hai loại bộ nhớ:**

| Loại | Vị trí | Mục đích |
|---|---|---|
| Session memory | `~/.vibe-trading/sessions/*.db` (SQLite, FTS5) | Lịch sử chat trong phiên, có compression 5 lớp |
| Persistent memory | `~/.vibe-trading/memory/*.md` (frontmatter YAML) | Sở thích, rule, insight — tự gọi lại giữa các phiên |

---

## 4. Các Tính Năng Chính

### 4.1. Backtest đa thị trường (7 engine)

- `ChinaAShareEngine` — cổ phiếu Trung Quốc (CSI300)
- `GlobalEquityEngine` — Mỹ + HK
- `CryptoEngine` — Bitcoin và phái sinh
- `ChinaFuturesEngine` + `GlobalFuturesEngine` — futures
- `ForexEngine` — ngoại hối
- `OptionsPortfolioEngine` — quyền chọn
- `CompositeEngine` — **danh mục pha trộn** (vd: A-share + crypto chung capital pool)

Mọi engine có **validation thống kê**: Monte Carlo 1000 path, Bootstrap CI, Walk-Forward analysis.

**Ví dụ prompt:**
```
Backtest chiến lược MA 20/50 trên AAPL trong 1 năm qua,
hiển thị Sharpe, max drawdown, win rate.
```

### 4.2. Alpha Zoo — 452 alpha pre-built

Đây là tính năng "bom tấn" của v0.1.8. Bạn có 4 thư viện factor sẵn sàng:

| Zoo | Số alpha | Nguồn |
|---|---|---|
| `qlib158` | 154 | Microsoft Qlib (Apache-2.0) |
| `alpha101` | 101 | Kakushadze 2015 — 101 Formulaic Alphas |
| `gtja191` | 191 | Guotai Junan 2014 — 191 short-period factors |
| `academic` | 6 | Fama-French 5 + Carhart momentum |

CLI:
```bash
vibe-trading alpha list --zoo gtja191 --limit 20
vibe-trading alpha show gtja191_171
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

Mỗi alpha có AST purity gate (cấm import bậy, cấm look-ahead), test sentinel 300 dòng đảm bảo không "peek future".

### 4.3. Swarm — đội agent đa tác nhân (29 preset)

Một số preset hay:

| Preset | Mô tả |
|---|---|
| `investment_committee` | Bull case → Bear case → Risk review → PM quyết định |
| `quant_strategy_desk` | Screen → factor research → backtest → risk audit |
| `crypto_trading_desk` | Funding/basis + liquidation heatmap + flow → risk manager |
| `macro_rates_fx_desk` | Lãi suất + FX + commodity → macro PM |
| `technical_analysis_panel` | TA cơ bản + Ichimoku + Elliott + SMC → đồng thuận |
| `earnings_research_desk` | Fundamentals + revision + option → earnings strategist |
| `factor_research_committee` | Factor IC/IR + economic interpretation |
| `risk_committee` | Drawdown + tail risk + regime |

```bash
vibe-trading --swarm-run investment_committee \
  '{"topic": "Nên mua VCB ở mức giá hiện tại?"}'
```

### 4.4. Shadow Account — "soi bóng" hành vi giao dịch

Đây là tính năng độc đáo nhất. Bạn upload nhật ký giao dịch (export CSV từ broker), agent sẽ:

1. `analyze_trade_journal` — profile bạn: holding days, win rate, profit factor, drawdown
2. Phát hiện **4 bias hành vi**: disposition effect (bán thắng giữ thua), overtrading, chasing momentum, anchoring
3. `extract_shadow_strategy` — chiết xuất 3-5 luật "nếu-thì" từ các giao dịch có lời
4. `run_shadow_backtest` — backtest các luật đó như thể bạn đã tuân thủ kỷ luật
5. `render_shadow_report` — báo cáo HTML/PDF 8 mục với delta-PnL: **"nếu giữ kỷ luật bạn đã kiếm thêm X% hoặc tránh được Y% thua lỗ"**

Hỗ trợ format export của: 同花顺 (Tonghuashun), 东财 (DongCai), 富途 (Futu), generic CSV.

### 4.5. 75 Skill (kiến thức chuyên ngành)

Skill = file markdown + metadata, agent có thể tự `load_skill("ichimoku")` khi cần. Một số nhóm:

- **Kỹ thuật**: candlestick, ichimoku, elliott-wave, smc (Smart Money Concepts), chanlun (缠论), harmonic, technical-basic
- **Định lượng**: factor-research, ml-strategy, multi-factor, pair-trading, quant-statistics
- **Phái sinh**: options-advanced, options-payoff, options-strategy, volatility, convertible-bond
- **Crypto**: perp-funding-basis, liquidation-heatmap, defi-yield, stablecoin-flow, onchain-analysis, token-unlock-treasury
- **Vĩ mô**: macro-analysis, global-macro, sector-rotation, commodity-analysis, geopolitical-risk
- **Cơ bản**: financial-statement, valuation-model, fundamental-filter, earnings-forecast, earnings-revision, dividend-analysis
- **Rủi ro & hành vi**: risk-analysis, behavioral-finance, trade-journal, shadow-account, hedging-strategy
- **Khác**: hk-connect-flow, edgar-sec-filings, etf-analysis, fund-analysis, market-microstructure, vnpy-export, pine-script…

### 4.6. Xuất chiến lược ra 3 nền tảng

Sau khi backtest xong, lệnh `/pine <run_id>` tạo ra:

- **Pine Script v6** cho TradingView
- **TDX** cho 通达信/同花顺/东方财富 (TQ)
- **MQL5** cho MetaTrader 5

Đáng tiếc: **chưa có export cho AmiBroker AFL** — đây là cơ hội nếu bạn muốn đóng góp.

### 4.7. MCP server

Có thể plug vào **Claude Desktop, Cursor, Windsurf** như một tool external. Cấu hình:
```json
{ "mcpServers": { "vibe-trading": { "command": "vibe-trading-mcp" } } }
```

---

## 5. Hỗ Trợ Thị Trường Việt Nam Hiện Tại

**Câu trả lời thẳng: Vibe-Trading hiện tại KHÔNG hỗ trợ VN-Index/HoSE/HNX/UPCoM một cách native.** Đây là thực tế quan trọng cần biết:

### 5.1. Những gì đã kiểm tra

| Khía cạnh | Tình trạng |
|---|---|
| Loader `tushare` | Chỉ A-share Trung Quốc (cần `TUSHARE_TOKEN`) |
| Loader `akshare` | A-share, ETF, forex, futures TQ, macro TQ — **không** có VN |
| Loader `yfinance` | US (`AAPL`) + HK (`0700.HK`); **về mặt kỹ thuật** Yahoo có `VCB.VN` nhưng `_to_yfinance_symbol()` không có mapping cho đuôi `.VN` |
| Loader `okx` / `ccxt` | Crypto — không liên quan VN equities |
| Loader `futu` | HK + A-share, không có VN |
| `_detect_market()` regex | Chỉ có A-share, US, HK, crypto, futures, forex — symbol VN sẽ bị **mặc định route vào A-share** |
| Skill | 0/75 skill nhắc đến VN cụ thể (chỉ 2 nhắc gián tiếp ở `geopolitical-risk` và `correlation-analysis`) |
| Engine backtest | Không có `VNEquityEngine`; gần nhất là `GlobalEquityEngine` (rule: T+0 settle, không price limit) — không khớp với rule HoSE/HNX (T+2.5, biên độ ±7% HoSE, ±10% HNX, ±15% UPCoM, lot 100) |

### 5.2. Yahoo Finance có dữ liệu VN không?

**Có một phần**: Yahoo Finance ký hiệu cổ phiếu VN bằng đuôi `.VN`, ví dụ `VCB.VN`, `VIC.VN`, `VNM.VN`, `HPG.VN`, `FPT.VN`. Tuy nhiên:
- Dữ liệu thường **trễ, thiếu volume chính xác, không đầy đủ corporate action**
- Index `^VNINDEX` đôi khi có, đôi khi không — không đáng tin cậy
- Adjusted close không khớp với cách Việt Nam điều chỉnh sau cổ tức/chia tách

### 5.3. Mức độ "khả dụng" hiện tại

| Trường hợp dùng | Khả dụng cho VN? |
|---|---|
| Phân tích cơ bản, đọc báo cáo PDF tiếng Việt | ✅ Có (`read_document` + LLM hiểu tiếng Việt) |
| Search tin tức + tóm tắt | ✅ Có (`web_search` + `read_url`) |
| Backtest VCB.VN bằng yfinance | ⚠️ Patch nhẹ là chạy được, chất lượng dữ liệu kém |
| Backtest đúng rule HoSE (T+2.5, biên độ giá, lot 100) | ❌ Cần viết engine mới |
| Phân tích nhật ký giao dịch từ SSI/VPS/VND CSV | ⚠️ Cần thêm parser cho format VN trong `trade_journal_parsers.py` |
| Áp dụng 452 alpha của Alpha Zoo lên VN30 | ✅ Code-wise OK (alpha là công thức trên OHLCV), chỉ cần universe VN30 và data tốt |
| Multi-agent swarm phân tích VCB | ✅ Hoạt động — LLM hiểu cổ phiếu VN, chỉ là không có data ground-truth |
| Xuất Pine Script cho TradingView VN | ✅ Pine Script chạy được trên TradingView với mã `HOSE:VCB`, `HOSE:VN30` |

---

## 6. Lộ Trình Áp Dụng Cho Thị Trường Việt Nam

Dưới đây là **lộ trình thực tế** theo 3 cấp độ: nhanh, vừa, sâu.

### 6.1. Cấp 1 — Dùng ngay (không sửa code)

**Mục tiêu:** Tận dụng phần "agent + skill + swarm" để **research** cổ phiếu VN, không backtest.

| Việc | Cách làm |
|---|---|
| Cài đặt | `pip install vibe-trading-ai` → `vibe-trading init` → chọn DeepSeek hoặc Qwen (rẻ, hiểu tiếng Việt tốt) |
| Đọc báo cáo BCTC PDF tiếng Việt | Upload `vibe-trading --upload bao_cao_VCB_Q3_2025.pdf` rồi hỏi "Tóm tắt 3 rủi ro lớn nhất và đánh giá ROE qua các quý" |
| Phân tích tin tức | `vibe-trading run -p "Search tin tức về HPG tuần qua và đánh giá tác động lên giá cổ phiếu"` |
| Swarm investment committee | `vibe-trading --swarm-run investment_committee '{"topic":"Nên mua VCB ở giá hiện tại không?"}'` — LLM sẽ debate Bull/Bear với kiến thức nó có |
| Lưu sở thích | `vibe-trading run -p "Ghi nhớ: tôi giao dịch VN30, ưa chiến lược momentum, max drawdown 15%, holding 5-20 ngày"` |
| Phân tích option Greeks (cho warrant VN) | `analyze_options` (Black-Scholes) — VN chỉ có CW (covered warrant), công thức tương tự |

### 6.2. Cấp 2 — Patch nhỏ (1-2 ngày code)

**Mục tiêu:** Backtest được trên dữ liệu Yahoo VN.

#### Patch A: Cho yfinance loader nhận đuôi `.VN`

Sửa `agent/backtest/loaders/yfinance_loader.py` hàm `_to_yfinance_symbol`:
```python
if upper.endswith(".VN"):
    return upper  # Yahoo dùng nguyên dạng VCB.VN, VIC.VN
```
Và thêm vào `markets = {"us_equity", "hk_equity", "vn_equity"}`.

#### Patch B: Thêm pattern `vn_equity` vào market detection

Sửa `agent/backtest/engines/_market_hooks.py`:
```python
(re.compile(r"^[A-Z]{2,4}\.VN$", re.I), "vn_equity"),
```

#### Patch C: Thêm fallback chain

Sửa `agent/backtest/loaders/registry.py`:
```python
"vn_equity": ["yfinance"],   # tạm thời chỉ yfinance
```

Với 3 patch này bạn có thể chạy:
```bash
vibe-trading run -p "Backtest chiến lược MA 20/50 trên VCB.VN, VIC.VN, VNM.VN, HPG.VN, FPT.VN từ 2020 đến nay"
```

Engine sẽ tạm dùng `GlobalEquityEngine` — chấp nhận sai lệch nhỏ (không có price limit, T+0 thay vì T+2.5).

### 6.3. Cấp 3 — Tích hợp đầy đủ (1-2 tuần code)

**Mục tiêu:** Có dữ liệu VN chất lượng cao và backtest đúng rule HoSE/HNX/UPCoM.

#### Bước 1 — Chọn nguồn dữ liệu VN

| Nguồn | Loại | Cách dùng | Giá |
|---|---|---|---|
| **vnstock** (PyPI) | Python lib | `pip install vnstock`, có lịch sử OHLCV, BCTC, holder data | Free |
| **vnquant** | Python lib | Wrap CafeF + VnDirect | Free |
| **SSI iBoard API** | Broker API | Token từ tài khoản SSI | Free cho khách SSI |
| **VnDirect DataFeed** | Broker API | Token VND | Free cho khách VND |
| **Fireant** | Web/API ngầm | Scrape hoặc dùng thư viện cộng đồng | Free |
| **CafeF** | Web | Scrape (rủi ro) | Free |
| **FiinPro / FiinTrade** | Trả phí | API thương mại, chuẩn institutional | Trả phí |
| **TCBS Open API** | Broker API | Khách TCBS | Free |

→ Khuyến nghị: **vnstock** (community-maintained, ổn định nhất) làm primary, **FiinPro** nếu có ngân sách.

#### Bước 2 — Viết VnstockLoader

Tạo file `agent/backtest/loaders/vnstock_loader.py` theo template `yfinance_loader.py`:
```python
@register
class DataLoader:
    name = "vnstock"
    markets = {"vn_equity"}
    requires_auth = False
    
    def fetch(self, codes, start_date, end_date, fields=None, interval="1D"):
        from vnstock import stock_historical_data
        # Trả về dict[code -> DataFrame OHLCV]
```

Đăng ký vào `registry.py`:
```python
"vn_equity": ["vnstock", "yfinance"],
```

#### Bước 3 — Viết VnEquityEngine

Tạo `agent/backtest/engines/vn_equity.py` clone từ `china_a.py` nhưng:
- **T+2.5 settle** (mua thứ Hai → bán được thứ Năm chiều)
- **Biên độ giá**: HoSE ±7%, HNX ±10%, UPCoM ±15%, ngày chào sàn ±20%
- **Lot 100**: lệnh ≥100 cổ phiếu trên HoSE
- **Phí**: 0.15-0.25% mỗi lượt + thuế bán 0.1%
- **Skip ngày limit-up/down**: như engine A-share đã làm

#### Bước 4 — Parser nhật ký giao dịch VN

Sửa `agent/src/tools/trade_journal_parsers.py` thêm các format export:
- SSI iBoard CSV (cột: `Mã CK`, `Ngày`, `Khối lượng`, `Giá`, `Loại lệnh`)
- VPS SmartOne
- VND DStock
- TCBS

#### Bước 5 — Skill VN-specific

Thêm vào `agent/src/skills/`:
- `vn-equity-microstructure/SKILL.md` — giải thích lot 100, foreign ownership cap, biên độ giá
- `vn-cw-warrant/SKILL.md` — chứng quyền có đảm bảo (covered warrant) Việt Nam
- `vn-derivatives/SKILL.md` — VN30F1M, VN30F2M futures
- `vn30-universe/SKILL.md` — danh sách thành phần VN30 + cách rebalance

#### Bước 6 — Universe presets

Thêm `vn30`, `hose100`, `vnall` làm universe cho Alpha Zoo:
```bash
vibe-trading alpha bench --zoo gtja191 --universe vn30 --period 2020-2025
```

#### Bước 7 — Swarm preset VN

Tạo `agent/src/swarm/presets/vn_equity_desk.yaml` — đội phân tích VN gồm: macro VN, sector VN, technical VN30, risk control.

> Nếu bạn làm xong cấp 3, đó sẽ là một **PR rất giá trị** cho upstream. Tác giả HKUDS có lịch sử merge PR cộng đồng nhanh (xem `CONTRIBUTING.md` — chỉ cần DCO sign-off).

---

## 7. Ví Dụ Prompt Thực Tế

Các prompt dưới đây dùng ngay được, viết bằng tiếng Việt — LLM hiểu tốt.

### 7.1. Research cơ bản (Cấp 1, không cần patch)

```
Search tin tức về VCB trong 2 tuần qua, tóm tắt 5 điểm chính,
và đánh giá tác động ngắn hạn lên giá cổ phiếu.
```

```
Đọc PDF báo cáo Q3/2025 của HPG (tôi vừa upload), liệt kê:
1. Doanh thu, lợi nhuận so với cùng kỳ
2. 3 rủi ro lớn nhất
3. So sánh với DBC, NKG cùng ngành thép
```

```
Phân tích option Greeks cho CW VRE (covered warrant): 
spot=27000, strike=25000, 60 ngày, vol=35%, lãi suất 4.5%.
Tính delta, gamma, theta và breakeven.
```

### 7.2. Swarm (Cấp 1)

```
vibe-trading --swarm-run investment_committee '{
  "topic": "Đánh giá VHM ở mức 42,000 VND — có nên mua dài hạn?",
  "market": "VN",
  "horizon": "12 months"
}'
```

```
vibe-trading --swarm-run technical_analysis_panel '{
  "topic": "VN30 đang ở vùng kháng cự 1340, phân tích đa khung TA"
}'
```

```
vibe-trading --swarm-run risk_committee '{
  "topic": "Danh mục: 30% VCB, 25% HPG, 20% FPT, 15% MWG, 10% VRE.
            Đánh giá tail risk, correlation, sector concentration."
}'
```

### 7.3. Sau khi patch yfinance (Cấp 2)

```
Backtest chiến lược MA 20/50 crossover trên rổ:
VCB.VN, VIC.VN, VNM.VN, HPG.VN, FPT.VN, MWG.VN, MSN.VN, VHM.VN
từ 2020-01-01 đến nay. So sánh với benchmark ^VNINDEX.
Hiển thị Sharpe, max DD, win rate, profit factor.
```

```
Backtest momentum strategy: mua top 5 cổ phiếu VN30 có
return 60 ngày cao nhất, rebalance hàng tháng,
từ 2021 đến nay. Áp dụng stop loss 8%.
```

```
Chạy factor_analysis với factor "RSI(14)" trên rổ VN30
từ 2022 đến nay. Tính IC, IR, layered backtest top/bottom quintile.
```

### 7.4. Sau khi tích hợp đầy đủ (Cấp 3)

```
vibe-trading alpha bench --zoo gtja191 --universe vn30 \
  --period 2020-2025 --top 30

# Xem 30 alpha hoạt động tốt nhất trên VN30 trong 5 năm
```

```
Tải lên file SSI_LSGD_2024.csv (nhật ký giao dịch SSI).
Phân tích hành vi giao dịch của tôi, tìm bias 
(disposition effect, overtrading...), trích chiến lược 
shadow, backtest và so sánh với P&L thực tế.
```

```
Run quant_strategy_desk swarm với universe = VN30, 
hypothesis = "low PE + high ROE + positive earnings revision 
sẽ outperform trong 6 tháng tới". Backtest 2018-2024,
walk-forward 6-month rebalance.
```

### 7.5. Xuất ra TradingView (Cấp 1, sau backtest)

```bash
# Sau khi backtest có run_id = run_2026_001
vibe-trading --pine run_2026_001
```

Copy Pine Script ra TradingView, gắn vào ticker `HOSE:VCB`, `HOSE:VN30`, `HNX:SHS`.

### 7.6. Lưu rule riêng (memory bền vững)

```
Ghi nhớ vào memory:
- Tôi chỉ giao dịch cổ phiếu VN30
- Max position size: 15% NAV
- Max drawdown danh mục: 12%
- Tránh các cổ phiếu trong diện cảnh báo/kiểm soát
- Holding period mục tiêu: 5-30 phiên
- Stop loss kỹ thuật: dưới MA50
- Take profit: trail stop 8%
```

Các phiên sau, khi bạn hỏi "tạo chiến lược cho tôi", agent sẽ tự áp dụng rule trên.

---

## 8. Tóm Tắt & Bước Tiếp Theo

**Vibe-Trading hiện tại** là bộ công cụ research **rất mạnh** nhưng đang **thiên về thị trường Trung Quốc + Mỹ + HK + Crypto**. Với thị trường Việt Nam:

- ✅ **Dùng được ngay** cho: research định tính, đọc PDF, search tin tức, swarm debate, option Greeks, lưu memory, viết Pine Script cho TradingView VN
- ⚠️ **Cần patch nhỏ** (~1 ngày) để: backtest cơ bản qua yfinance với mã `.VN`
- ❌ **Cần code thêm** (~1-2 tuần) để: có loader vnstock/SSI, engine VN đúng rule HoSE/HNX, parser CSV broker VN, skill và swarm preset chuyên VN

**Đề xuất bắt đầu:**

1. `pip install vibe-trading-ai` → `vibe-trading init` → chọn DeepSeek hoặc Qwen
2. Thử 3 prompt research ở mục 7.1 — không cần code gì
3. Nếu thấy giá trị, làm patch cấp 2 (yfinance `.VN`) → backtest thử trên VN30
4. Nếu nghiêm túc, contribute cấp 3 lên upstream — sẽ là PR rất có ý nghĩa cho cộng đồng VN

**Tài nguyên:**

- Repo: https://github.com/HKUDS/Vibe-Trading
- Wiki: https://vibetrading.wiki/
- Alpha Library: https://vibetrading.wiki/alpha-library/
- Discord: https://discord.gg/2vDYc2w5
- CHANGELOG đầy đủ: `/CHANGELOG.md` trong repo

---

*Tài liệu này được tạo từ research toàn bộ repo (CHANGELOG.md, README.md, description.md, instruction.md, SKILL.md, git log từ 2026-04-01 đến 2026-05-20, kiểm tra trực tiếp `agent/backtest/loaders/`, `agent/backtest/engines/`, `agent/src/skills/`, `agent/src/swarm/presets/`). Mọi mã ticker VN (VCB, VIC, VNM, HPG, FPT, MWG, MSN, VHM, VRE) là ví dụ minh họa, không phải khuyến nghị đầu tư.*
