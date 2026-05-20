# Hướng Dẫn Vibe-Trading

## 📌 Mục Đích của Dự Án

**Vibe-Trading** là một nền tảng nghiên cứu tài chính mã nguồn mở được thiết kế để giúp các nhà phân tích, nhà đầu tư và các nhà giao dịch chuyên nghiệp chuyển đổi các câu hỏi tài chính thành phân tích và kiểm thử chiến lược có thể chạy được.

### Mục Tiêu Chính:
1. **Tự động hóa nghiên cứu tài chính** - Sử dụng AI để phân tích dữ liệu thị trường và tạo chiến lược giao dịch
2. **Cung cấp công cụ backtesting mạnh mẽ** - Kiểm thử chiến lược trên dữ liệu lịch sử từ nhiều thị trường
3. **Phân tích hành vi giao dịch** - Phân tích nhật ký giao dịch của bạn để tìm ra những thiên vị và cơ hội cải thiện
4. **Tích hợp trí tuệ nhân tạo với giao dịch** - Kết hợp LLM với dữ liệu thị trường, kỹ năng tài chính và công cụ backtesting

### Điểm Khác Biệt:
- ✨ **Không thực hiện giao dịch trực tiếp** - Chỉ dùng cho nghiên cứu, mô phỏng và backtesting
- 🤖 **Nền tảng dựa trên AI** - Sử dụng các mô hình ngôn ngữ lớn (LLM) từ nhiều nhà cung cấp
- 📊 **Hỗ trợ đa thị trường** - A-shares (cổ phiếu TQ), HK/US equities, crypto, futures, forex
- 💾 **Bộ nhớ bền vững** - Lưu trữ các ghi chú, cấu hình và kết quả kiểm thử giữa các phiên làm việc
- 🐝 **Swarm Intelligence** - Chạy các nhóm agent đa tác nhân để phân tích phức tạp

---

## 🎯 Ứng Dụng của Dự Án

### 1. **Nghiên Cứu & Phân Tích Thị Trường**
- Phân tích sâu về cổ phiếu (xu hướng lợi nhuận, sự đồng thuận của nhà phân tích, dòng chảy tùy chọn)
- Phân tích vĩ mô (đường lãi suất Fed, sức mạnh USD, tác động lên chứng chỉ tài chính)
- Phân tích on-chain cho crypto (dòng chảy cá voi, số dư sàn giao dịch, hoạt động của người đào)

### 2. **Phát Triển & Backtesting Chiến Lược**
- Tạo chiến lược giao dịch dựa trên mô tả tự nhiên
- Kiểm thử chiến lược trên dữ liệu lịch sử từ 5+ năm
- So sánh hiệu suất với benchmark (SPY, CSI 300, v.v.)
- Xuất sang TradingView (Pine Script), TDX, MetaTrader 5

### 3. **Phân Tích Ghi Chép Giao Dịch của Bạn**
- Tải lên tập tin xuất từ sàn giao dịch (Thinkorswim, IB, Futu, etc.)
- Phân tích hành vi giao dịch của bạn:
  - Thống kê: ngày giữ, tỷ lệ chiến thắng, tỷ lệ P&L, drawdown
  - Độ lệch: hiệu ứng xử lý, giao dịch quá mức, đuổi theo momentum, fixation
- Trích xuất quy tắc từ các giao dịch của bạn
- So sánh tài khoản "bóng" (chiến lược quy tắc) với giao dịch thực tế

### 4. **Sử Dụng Alpha Zoo (452 Alphas Được Xây Dựng Sẵn)**
- Kiểm tra 452 công thức alpha được xây dựng sẵn từ 4 thư viện:
  - **qlib158** - Microsoft Qlib (154 alphas)
  - **alpha101** - Kakushadze 101 Formulaic Alphas (101 alphas)
  - **gtja191** - Guotai Junan Factors (191 alphas)
  - **academic** - Fama-French 5 + Carhart (6 alphas)
- Lọc, xếp hạng và so sánh hiệu suất

### 5. **Chạy Các Nhóm Phân Tích Đa Tác Nhân**
- Nhóm đầu tư: Tranh luận Bull/Bear → xem xét rủi ro → quyết định cuối cùng
- Nhóm giao dịch crypto: Quỹ + liquidation heatmap + dòng chảy → quản lý rủi ro
- Nhóm phân tích kỹ thuật: TA cơ bản + Ichimoku + Elliott Wave + SMC → đồng thuận
- Nhóm macro: Lãi suất + FX + hàng hóa → phân bổ danh mục

### 6. **Tạo & Chia Sẻ Kỹ Năng Tùy Chỉnh**
- Tạo quy trình tái sử dụng (kỹ năng) từ các quy trình thường lặp lại
- Lưu trữ và gọi lại từ các phiên làm việc trong tương lai
- Chia sẻ với cộng đồng hoặc lưu giữ riêng

---

## 📖 Hướng Dẫn Sử Dụng

### **Bước 0: Chuẩn Bị Tiên Quyết**

Trước khi bắt đầu, bạn cần:

1. **Python 3.11+** (cho cài đặt cục bộ)
2. **Khóa API từ nhà cung cấp LLM** - chọn một trong những tùy chọn:
   - OpenAI, DeepSeek, Gemini, Groq, Qwen, Kimi, MiniMax, Ollama (cục bộ - không cần khóa)
   - [Xem danh sách đầy đủ](https://github.com/HKUDS/Vibe-Trading#-environment-variables)
3. **(Tùy chọn) Token Tushare** - cho dữ liệu A-share nâng cao

> 💡 **Lưu ý:** Hầu hết các thị trường hoạt động miễn phí (yfinance, OKX, AKShare). Chỉ cần LLM API.

---

### **Phương Pháp A: Cài Đặt Cục Bộ (Được Đề Xuất)**

#### Bước 1: Cài Đặt Vibe-Trading từ PyPI

```bash
pip install vibe-trading-ai
```

#### Bước 2: Khởi Tạo Biến Môi Trường

```bash
vibe-trading init
```

Lệnh này sẽ:
- Tạo thư mục `~/.vibe-trading/`
- Hỏi bạn chọn nhà cung cấp LLM và nhập khóa API
- Tạo tệp `.env` tại `~/.vibe-trading/.env`

#### Bước 3: Chạy Ứng Dụng

**Chế độ tương tác (CLI):**
```bash
vibe-trading
```

**Giao diện web (cùng lúc):**
```bash
# Terminal 1: Chạy API server
vibe-trading serve --port 8899

# Terminal 2: Chạy frontend (nếu muốn phát triển)
cd frontend && npm install && npm run dev
# Truy cập: http://localhost:5899
```

---

### **Phương Pháp B: Docker (Thiết Lập Bằng Không)**

```bash
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading

# Sao chép tệp ví dụ biến môi trường
cp agent/.env.example agent/.env

# Chỉnh sửa agent/.env - thêm khóa API LLM của bạn
# Ví dụ, với DeepSeek:
#   LANGCHAIN_PROVIDER=deepseek
#   DEEPSEEK_API_KEY=sk-...
#   LANGCHAIN_MODEL_NAME=deepseek-v3

docker compose up --build
```

Truy cập: `http://localhost:8899`

---

### **Phương Pháp C: Plugin MCP (Cho Claude Desktop, Cursor, v.v.)**

Thêm vào cấu hình:

**Claude Desktop:**
```json
{
  "mcpServers": {
    "vibe-trading": {
      "command": "vibe-trading-mcp"
    }
  }
}
```

**Cursor / Windsurf:**
```bash
vibe-trading-mcp --transport sse
```

---

## 🚀 Các Ví Dụ Sử Dụng Nhanh

### **1. Backtesting Một Chiến Lược Đơn Giản**

```bash
vibe-trading run -p "Backtest chiến lược crossover trung bình động 20/50 ngày trên AAPL trong 1 năm qua, hiển thị Sharpe ratio và max drawdown"
```

Hoặc từ CLI tương tác:
```bash
vibe-trading
# Nhập: Backtest chiến lược crossover trung bình động 20/50 ngày trên AAPL trong 1 năm qua
```

### **2. Kiểm Tra Một Alpha Từ Zoo**

```bash
# Liệt kê các alphas từ thư viện GTJA 191
vibe-trading alpha list --zoo gtja191 --limit 10

# Xem chi tiết một alpha cụ thể
vibe-trading alpha show gtja191_171

# Kiểm tra hiệu suất toàn bộ thư viện
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

### **3. Phân Tích Hành Vi Giao Dịch của Bạn**

```bash
# Tải lên tệp xuất từ sàn giao dịch
vibe-trading --upload trades_export.csv

# Phân tích hành vi
vibe-trading run -p "Phân tích hành vi giao dịch của tôi, trích xuất chiến lược bóng của tôi và so sánh với giao dịch thực tế"
```

### **4. Chạy Một Nhóm Phân Tích (Swarm)**

```bash
vibe-trading --swarm-run investment_committee '{"topic": "Nên mua TSLA ở mức giá hiện tại không?"}'
```

### **5. Xuất Chiến Lược sang TradingView**

```bash
# Sau khi chạy một backtest, lấy run_id
vibe-trading --pine <run_id>
```

Lệnh này tạo các tệp:
- Pine Script v6 (TradingView)
- TDX (通达信 / 同花顺 / 东方财富)
- MQL5 (MetaTrader 5)

---

## 💬 Chế Độ CLI Tương Tác

Khi chạy `vibe-trading`, bạn vào chế độ TUI (Terminal UI) tương tác với các lệnh sau:

| Lệnh | Mô Tả |
|------|-------|
| `/help` | Hiển thị tất cả các lệnh |
| `/skills` | Liệt kê 75 kỹ năng tài chính |
| `/swarm` | Liệt kê 29 cài đặt trước nhóm |
| `/list` | Các lần chạy gần đây |
| `/show <run_id>` | Chi tiết lần chạy |
| `/code <run_id>` | Mã chiến lược được tạo |
| `/pine <run_id>` | Xuất chỉ báo |
| `/trace <run_id>` | Phát lại toàn bộ quá trình thực hiện |
| `/settings` | Hiển thị cấu hình |
| `/quit` | Thoát |

---

## 🧠 Các Kỹ Năng & Chức Năng Có Sẵn

### **75 Kỹ Năng Tài Chính** (xem `/skills`)

**Danh Mục:**
- 📊 **Dữ liệu** (6): tushare, yfinance, okx, akshare, ccxt
- 📈 **Chiến Lược** (17): technical-basic, candlestick, ichimoku, multi-factor, ml-strategy
- 🔬 **Phân Tích** (17): factor-research, macro-analysis, valuation-model
- 🎯 **Lớp Tài Sản** (9): options, convertible-bond, etf-analysis
- 🪙 **Crypto** (7): perp-funding, liquidation-heatmap, defi-yield
- 💰 **Dòng Chảy** (7): hk-connect-flow, edgar-sec-filings
- 🔧 **Công Cụ** (11): backtest-diagnose, report-generate, doc-reader
- ⚠️ **Rủi Ro** (1): ashare-pre-st-filter

### **29 Cài Đặt Trước Nhóm** (xem `/swarm`)

Ví dụ:
- `investment_committee` - Tranh luận Bull/Bear
- `quant_strategy_desk` - Lọc → Nghiên cứu nhân tố → Backtest
- `crypto_trading_desk` - Quỹ + Liquidation + Dòng chảy
- `macro_rates_fx_desk` - Lãi suất + FX + Hàng hóa

---

## 📁 Cấu Trúc Dữ Liệu

```
~/.vibe-trading/
├── .env                    # Cấu hình (khóa API, mô hình)
├── memory/                 # Bộ nhớ bền vững (ghi chú, kỹ năng)
├── uploads/                # Tệp tải lên (nhật ký giao dịch, PDF)
└── agent.json             # Cấu hình MCP server tùy chỉnh (tùy chọn)

~/.vibe-trading/runs/
└── <run_id>/              # Kết quả lần chạy
    ├── metrics.json       # Chỉ số hiệu suất
    ├── strategy.py        # Mã chiến lược
    ├── backtest.csv       # Chi tiết giao dịch
    └── report.html        # Báo cáo HTML
```

---

## ⚙️ Cấu Hình Môi Trường

Sửa `~/.vibe-trading/.env`:

```bash
# Nhà cung cấp LLM (chọn một)
LANGCHAIN_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-...
LANGCHAIN_MODEL_NAME=deepseek-v4-pro

# Hoặc OpenRouter
LANGCHAIN_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-...
LANGCHAIN_MODEL_NAME=deepseek/deepseek-v4-pro

# Tushare (tùy chọn, cho dữ liệu A-share)
TUSHARE_TOKEN=your_token_here

# Cài đặt API từ xa (bảo mật)
API_AUTH_KEY=strong_secret_key_here
```

---

## 🛠️ Các Mẹo & Thủ Thuật

### **1. Lưu Tùy Chọn Ưu Tiên của Bạn**

```bash
vibe-trading run -p "Ghi nhớ: Tôi thích chiến lược dựa trên RSI, max 10% drawdown, khoảng thời gian giữ 5-20 ngày"
```

Agent sẽ nhớ điều này cho các phiên làm việc trong tương lai.

### **2. Sử Dụng Dữ Liệu Miễn Phí**

- ✅ A-shares: AKShare (miễn phí)
- ✅ HK/US: yfinance (miễn phí)
- ✅ Crypto: OKX (miễn phí)
- ✅ 100+ sàn crypto: CCXT (miễn phí)

Không cần API key để chạy backtests!

### **3. Xuất Chiến Lược của Bạn**

Sau khi backtest:
```bash
vibe-trading --pine <run_id>
# Tạo: Pine Script, TDX, MQL5
```

### **4. Đọc PDF & Tệp**

```bash
vibe-trading --upload quarterly_report.pdf
vibe-trading run -p "Tóm tắt những rủi ro chính từ báo cáo này"
```

---

## 🔒 Bảo Mật

### Localhost (Phát Triển)
- ✅ Miễn phí truy cập, không cần xác thực
- ✅ Có thể đọc/ghi tệp cục bộ
- ✅ Shell tools có sẵn

### Triển Khai Từ Xa
- ⚠️ Đặt `API_AUTH_KEY` mạnh
- ⚠️ Giới hạn CORS origins
- ⚠️ Shell tools bị tắt theo mặc định
- ⚠️ Tệp & Upload bị giới hạn trong các thư mục an toàn

```bash
export API_AUTH_KEY="your_strong_secret_here"
vibe-trading serve --port 8899
```

Khách hàng phải gửi:
```
Authorization: Bearer your_strong_secret_here
```

---

## 📚 Tài Nguyên Thêm

- 📖 [Tài liệu chính thức](https://vibetrading.wiki/)
- 🐛 [Báo cáo lỗi / yêu cầu](https://github.com/HKUDS/Vibe-Trading/issues)
- 💬 [Cộng đồng Discord](https://discord.gg/2vDYc2w5)
- 📊 [Alpha Library](https://vibetrading.wiki/alpha-library/)

---

## ❓ Câu Hỏi Thường Gặp

### **P: Tôi có thể sử dụng Vibe-Trading mà không có khóa API LLM không?**
**Đ:** Có, sử dụng Ollama (chạy cục bộ):
```bash
ollama pull deepseek-r1
# Sửa .env: LANGCHAIN_PROVIDER=ollama
vibe-trading run -p "..."
```

### **P: Vibe-Trading có thực hiện giao dịch trực tiếp không?**
**Đ:** Không. Nó chỉ dùng cho nghiên cứu, mô phỏng và backtesting.

### **P: Tôi có thể sử dụng Vibe-Trading với các mô hình cục bộ không?**
**Đ:** Có, Ollama được hỗ trợ. Các mô hình khác không thể vì chúng cần API chuyên biệt.

### **P: Các kỹ năng có được tùy chỉnh không?**
**Đ:** Có, lệnh `/skills` cho phép CRUD (tạo, chỉnh sửa, xóa, lưu).

---

## 🎯 Bước Tiếp Theo

1. **Cài đặt** từ PyPI hoặc Docker
2. **Chạy một lệnh đơn giản** để kiểm tra:
   ```bash
   vibe-trading run -p "Backtest chiến lược 20/50 MA trên BTC-USDT trong tháng qua"
   ```
3. **Khám phá kỹ năng**: `/skills`
4. **Chạy một nhóm**: `/swarm`
5. **Phân tích thị trường của bạn**: Sử dụng các câu hỏi tự nhiên

---

**Chúc bạn thành công với Vibe-Trading! 🚀**
