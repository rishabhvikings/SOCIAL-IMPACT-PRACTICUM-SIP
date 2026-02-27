import streamlit as st

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Govt Schemes | सरकारी योजनाएं",
    page_icon="🏛️",
    layout="wide",
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;800&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Baloo 2', 'Noto Sans Devanagari', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #e8f4fd 0%, #fef9e7 35%, #fde8f0 65%, #e8f8f0 100%);
    color: #2c3e50;
}

/* Header banner */
.header-banner {
    background: linear-gradient(90deg, #e74c3c, #e67e22, #f1c40f, #27ae60, #2980b9, #8e44ad);
    background-size: 300% 100%;
    animation: rainbowShift 6s ease infinite;
    border-radius: 18px;
    padding: 30px 32px;
    text-align: center;
    margin-bottom: 28px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
}
@keyframes rainbowShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.header-banner h1 {
    font-size: 2.5rem;
    font-weight: 800;
    color: #fff;
    margin: 0;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    letter-spacing: 1px;
}
.header-banner p {
    font-size: 1.05rem;
    color: #fff;
    margin: 8px 0 0 0;
    opacity: 0.92;
}

/* Category header */
.category-header {
    font-size: 1.2rem;
    font-weight: 700;
    color: #fff;
    border-radius: 8px;
    padding: 8px 16px;
    margin: 28px 0 16px 0;
    letter-spacing: 0.5px;
    display: inline-block;
}
.cat-health    { background: linear-gradient(90deg, #e74c3c, #c0392b); }
.cat-housing   { background: linear-gradient(90deg, #e67e22, #d35400); }
.cat-women     { background: linear-gradient(90deg, #8e44ad, #6c3483); }
.cat-education { background: linear-gradient(90deg, #2980b9, #1a5276); }
.cat-pension   { background: linear-gradient(90deg, #16a085, #1abc9c); }
.cat-farmer    { background: linear-gradient(90deg, #27ae60, #1e8449); }
.cat-food      { background: linear-gradient(90deg, #f39c12, #d68910); }
.cat-finance   { background: linear-gradient(90deg, #2471a3, #1a5276); }

/* Scheme card — alternating accent colours per category */
.scheme-card {
    background: #ffffff;
    border-left: 5px solid #3498db;
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 14px;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 3px 14px rgba(0,0,0,0.08);
}
.scheme-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(0,0,0,0.14);
}
.scheme-card.health    { border-left-color: #e74c3c; background: linear-gradient(135deg, #fff5f5, #ffffff); }
.scheme-card.housing   { border-left-color: #e67e22; background: linear-gradient(135deg, #fff8f0, #ffffff); }
.scheme-card.women     { border-left-color: #8e44ad; background: linear-gradient(135deg, #fdf2ff, #ffffff); }
.scheme-card.education { border-left-color: #2980b9; background: linear-gradient(135deg, #f0f8ff, #ffffff); }
.scheme-card.pension   { border-left-color: #16a085; background: linear-gradient(135deg, #f0fffe, #ffffff); }
.scheme-card.farmer    { border-left-color: #27ae60; background: linear-gradient(135deg, #f0fff5, #ffffff); }
.scheme-card.food      { border-left-color: #f39c12; background: linear-gradient(135deg, #fffbf0, #ffffff); }
.scheme-card.finance   { border-left-color: #2471a3; background: linear-gradient(135deg, #f0f6ff, #ffffff); }

.scheme-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 5px;
}
.scheme-desc {
    font-size: 0.88rem;
    color: #5d6d7e;
    margin-bottom: 12px;
}

/* Button colours per category */
.scheme-link a {
    display: inline-block;
    color: #fff !important;
    text-decoration: none !important;
    padding: 7px 20px;
    border-radius: 20px;
    font-size: 0.88rem;
    font-weight: 600;
    box-shadow: 0 3px 10px rgba(0,0,0,0.15);
    transition: opacity 0.2s, transform 0.2s;
}
.scheme-link a:hover { opacity: 0.88; transform: scale(1.03); }
.health    .scheme-link a { background: linear-gradient(90deg,#e74c3c,#c0392b); }
.housing   .scheme-link a { background: linear-gradient(90deg,#e67e22,#d35400); }
.women     .scheme-link a { background: linear-gradient(90deg,#8e44ad,#6c3483); }
.education .scheme-link a { background: linear-gradient(90deg,#2980b9,#1a5276); }
.pension   .scheme-link a { background: linear-gradient(90deg,#16a085,#1abc9c); }
.farmer    .scheme-link a { background: linear-gradient(90deg,#27ae60,#1e8449); }
.food      .scheme-link a { background: linear-gradient(90deg,#f39c12,#d68910); }
.finance   .scheme-link a { background: linear-gradient(90deg,#2471a3,#1a5276); }

/* Info footer */
.info-box {
    background: linear-gradient(135deg, #fff9e6, #fff3cd);
    border: 2px solid #f1c40f;
    border-radius: 14px;
    padding: 20px 24px;
    margin-top: 32px;
    font-size: 0.93rem;
    color: #4a4a4a;
    line-height: 1.9;
    box-shadow: 0 4px 16px rgba(241,196,15,0.2);
}

/* Divider */
hr {
    border: none;
    border-top: 2px dashed rgba(0,0,0,0.1);
    margin: 24px 0;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fdebd0 0%, #d5f5e3 50%, #d6eaf8 100%);
    border-right: 2px solid rgba(0,0,0,0.07);
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stRadio label {
    color: #2c3e50 !important;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA  — schemes by category
# ─────────────────────────────────────────────
SCHEMES = {
    "en": {
        "🏥 Health & Medical": [
            {"name": "Ayushman Bharat (PM-JAY)",          "desc": "₹5 lakh free treatment per family per year",               "link": "https://pmjay.gov.in"},
            {"name": "Mukhyamantri Swasthya Sahayata",    "desc": "Medical financial support (Jharkhand)",                    "link": "https://sha.jharkhand.gov.in"},
            {"name": "PM Matru Vandana Yojana",           "desc": "Cash support for pregnant & lactating women",              "link": "https://pmmvy.wcd.gov.in"},
        ],
        "🏠 Housing": [
            {"name": "PM Awas Yojana (Gramin)",           "desc": "Financial help to build pucca house",                      "link": "https://pmayg.nic.in"},
            {"name": "Abua Awas Yojana",                  "desc": "Jharkhand state housing support scheme",                   "link": "https://jharkhand.gov.in"},
        ],
        "👩 Women & Girl Child": [
            {"name": "Sukanya Samriddhi Yojana",          "desc": "High-interest savings scheme for girl child",              "link": "https://www.nsiindia.gov.in"},
            {"name": "Maiya Samman Yojana",               "desc": "Monthly financial support for women (Jharkhand)",          "link": "https://jharkhand.gov.in"},
            {"name": "Savitribai Phule Kishori Yojana",   "desc": "Support for girl child education",                         "link": "https://jharkhand.gov.in"},
            {"name": "Phulo Jhano Ashirwad Yojana",       "desc": "Support for women Self Help Groups",                       "link": "https://jharkhand.gov.in"},
        ],
        "🎓 Education": [
            {"name": "Guruji Student Credit Card",        "desc": "Education loan up to ₹15 lakh for higher studies",        "link": "https://jharkhand.gov.in"},
            {"name": "PM Poshan (Mid-Day Meal)",          "desc": "Free nutritious meals in government schools",              "link": "https://pmposhan.education.gov.in"},
        ],
        "👴 Pension & Social Security": [
            {"name": "Atal Pension Yojana",               "desc": "Guaranteed monthly pension after age 60",                  "link": "https://www.npscra.nsdl.co.in"},
            {"name": "Sarvajan Pension Yojana",           "desc": "Monthly pension for elderly (Jharkhand)",                  "link": "https://jharkhand.gov.in"},
            {"name": "National Social Assistance (NSAP)", "desc": "Pension for elderly, widows & disabled persons",           "link": "https://nsap.nic.in"},
            {"name": "PM Suraksha Bima Yojana",           "desc": "₹2 lakh accident insurance at ₹20/year",                  "link": "https://jansuraksha.gov.in"},
        ],
        "🌾 Farmer & Livelihood": [
            {"name": "Mukhyamantri Sukhad Rahat Yojana", "desc": "Relief for farmers affected by natural calamities",        "link": "https://aahar.jharkhand.gov.in"},
            {"name": "Birsa Harit Gram Yojana",           "desc": "Employment & livelihood through plantation",               "link": "https://jharkhand.gov.in"},
        ],
        "🍚 Food & Basic Needs": [
            {"name": "Food Security Scheme (NFSA/PDS)",  "desc": "Subsidized ration through fair price shops",               "link": "https://aahar.jharkhand.gov.in"},
            {"name": "PM Ujjwala Yojana",                 "desc": "Free LPG connection for BPL families",                    "link": "https://www.pmuy.gov.in"},
        ],
        "🏦 Financial Inclusion": [
            {"name": "PM Jan Dhan Yojana",               "desc": "Free zero-balance bank account with RuPay card",           "link": "https://pmjdy.gov.in"},
        ],
    },
    "hi": {
        "🏥 स्वास्थ्य एवं चिकित्सा": [
            {"name": "आयुष्मान भारत (PM-JAY)",           "desc": "₹5 लाख तक मुफ्त इलाज प्रति परिवार प्रति वर्ष",          "link": "https://pmjay.gov.in"},
            {"name": "मुख्यमंत्री स्वास्थ्य सहायता",    "desc": "इलाज हेतु आर्थिक सहायता (झारखंड)",                       "link": "https://sha.jharkhand.gov.in"},
            {"name": "PM मातृ वंदना योजना",              "desc": "गर्भवती एवं स्तनपान कराने वाली महिलाओं को सहायता",       "link": "https://pmmvy.wcd.gov.in"},
        ],
        "🏠 आवास": [
            {"name": "PM आवास योजना (ग्रामीण)",          "desc": "पक्का घर बनाने हेतु आर्थिक सहायता",                      "link": "https://pmayg.nic.in"},
            {"name": "अबुआ आवास योजना",                  "desc": "झारखंड राज्य आवास सहायता योजना",                         "link": "https://jharkhand.gov.in"},
        ],
        "👩 महिला एवं बालिका": [
            {"name": "सुकन्या समृद्धि योजना",            "desc": "बेटी के लिए उच्च ब्याज बचत योजना",                       "link": "https://www.nsiindia.gov.in"},
            {"name": "मैया सम्मान योजना",                "desc": "महिलाओं को मासिक आर्थिक सहायता (झारखंड)",                "link": "https://jharkhand.gov.in"},
            {"name": "सावित्रीबाई फुले किशोरी योजना",   "desc": "बालिका शिक्षा हेतु सहायता",                               "link": "https://jharkhand.gov.in"},
            {"name": "फूलो झानो आशीर्वाद योजना",        "desc": "महिला स्वयं सहायता समूहों को सहायता",                     "link": "https://jharkhand.gov.in"},
        ],
        "🎓 शिक्षा": [
            {"name": "गुरुजी स्टूडेंट क्रेडिट कार्ड",  "desc": "उच्च शिक्षा हेतु ₹15 लाख तक ऋण",                        "link": "https://jharkhand.gov.in"},
            {"name": "PM पोषण (मध्याह्न भोजन)",         "desc": "सरकारी स्कूलों में मुफ्त पौष्टिक भोजन",                   "link": "https://pmposhan.education.gov.in"},
        ],
        "👴 पेंशन एवं सामाजिक सुरक्षा": [
            {"name": "अटल पेंशन योजना",                  "desc": "60 वर्ष की आयु के बाद मासिक पेंशन की गारंटी",           "link": "https://www.npscra.nsdl.co.in"},
            {"name": "सर्वजन पेंशन योजना",               "desc": "बुजुर्गों के लिए मासिक पेंशन (झारखंड)",                  "link": "https://jharkhand.gov.in"},
            {"name": "राष्ट्रीय सामाजिक सहायता (NSAP)", "desc": "वृद्ध, विधवा एवं दिव्यांग व्यक्तियों को पेंशन",          "link": "https://nsap.nic.in"},
            {"name": "PM सुरक्षा बीमा योजना",            "desc": "₹20/वर्ष में ₹2 लाख दुर्घटना बीमा",                      "link": "https://jansuraksha.gov.in"},
        ],
        "🌾 किसान एवं आजीविका": [
            {"name": "मुख्यमंत्री सुखाड़ राहत योजना",   "desc": "प्राकृतिक आपदाओं से प्रभावित किसानों को राहत",           "link": "https://aahar.jharkhand.gov.in"},
            {"name": "बिरसा हरित ग्राम योजना",           "desc": "वृक्षारोपण के माध्यम से रोजगार एवं आजीविका",              "link": "https://jharkhand.gov.in"},
        ],
        "🍚 खाद्य एवं मूलभूत आवश्यकताएं": [
            {"name": "खाद्य सुरक्षा योजना (NFSA/PDS)",  "desc": "उचित मूल्य की दुकानों से सस्ता राशन",                    "link": "https://aahar.jharkhand.gov.in"},
            {"name": "PM उज्ज्वला योजना",                "desc": "BPL परिवारों को मुफ्त LPG कनेक्शन",                      "link": "https://www.pmuy.gov.in"},
        ],
        "🏦 वित्तीय समावेशन": [
            {"name": "PM जन धन योजना",                  "desc": "RuPay कार्ड के साथ मुफ्त जीरो बैलेंस बैंक खाता",         "link": "https://pmjdy.gov.in"},
        ],
    },
}

# ─────────────────────────────────────────────
# CATEGORY → CSS CLASS MAPPING
# ─────────────────────────────────────────────
CAT_CLASS_EN = {
    "🏥 Health & Medical":          "health",
    "🏠 Housing":                   "housing",
    "👩 Women & Girl Child":        "women",
    "🎓 Education":                 "education",
    "👴 Pension & Social Security": "pension",
    "🌾 Farmer & Livelihood":       "farmer",
    "🍚 Food & Basic Needs":        "food",
    "🏦 Financial Inclusion":       "finance",
}
CAT_CLASS_HI = {
    "🏥 स्वास्थ्य एवं चिकित्सा":      "health",
    "🏠 आवास":                         "housing",
    "👩 महिला एवं बालिका":             "women",
    "🎓 शिक्षा":                       "education",
    "👴 पेंशन एवं सामाजिक सुरक्षा":   "pension",
    "🌾 किसान एवं आजीविका":            "farmer",
    "🍚 खाद्य एवं मूलभूत आवश्यकताएं": "food",
    "🏦 वित्तीय समावेशन":              "finance",
}

LABELS = {
    "en": {
        "title": "Know Your Government Schemes",
        "subtitle": "For Poor Families • Women • Children • Elderly | Ranchi & Nearby Areas",
        "lang_label": "🌐 Language",
        "filter_label": "🔍 Search Scheme",
        "filter_placeholder": "Type to search...",
        "cat_label": "📂 Filter by Category",
        "all_cats": "All Categories",
        "visit_btn": "Visit Website →",
        "important_title": "⚠️ Important Reminders",
        "important_body": (
            "🚫 Do NOT pay extra money to agents or middlemen\n"
            "📄 Always carry: Aadhaar Card, Bank Passbook, Ration Card\n"
            "🧾 Always collect an official receipt after applying\n"
            "📍 Apply at: Nearest CSC Centre | Block Office | Government Bank"
        ),
        "apply_link": "https://csc.gov.in",
        "apply_text": "Find Nearest CSC Centre →",
    },
    "hi": {
        "title": "सरकारी योजनाओं की जानकारी लें",
        "subtitle": "गरीब परिवार • महिलाएं • बच्चे • बुजुर्ग | रांची एवं आसपास के क्षेत्र",
        "lang_label": "🌐 भाषा",
        "filter_label": "🔍 योजना खोजें",
        "filter_placeholder": "यहाँ टाइप करें...",
        "cat_label": "📂 श्रेणी से फ़िल्टर करें",
        "all_cats": "सभी श्रेणियां",
        "visit_btn": "वेबसाइट देखें →",
        "important_title": "⚠️ महत्वपूर्ण जानकारी",
        "important_body": (
            "🚫 किसी दलाल या बिचौलिए को पैसे न दें\n"
            "📄 साथ रखें: आधार कार्ड, बैंक पासबुक, राशन कार्ड\n"
            "🧾 आवेदन के बाद हमेशा रसीद अवश्य लें\n"
            "📍 यहाँ आवेदन करें: नजदीकी CSC केंद्र | प्रखंड कार्यालय | सरकारी बैंक"
        ),
        "apply_link": "https://csc.gov.in",
        "apply_text": "नजदीकी CSC केंद्र खोजें →",
    },
}

# ─────────────────────────────────────────────
# SIDEBAR  — controls
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    lang = st.radio("🌐 Language / भाषा", options=["English", "हिंदी"], index=0)
    lang_key = "en" if lang == "English" else "hi"
    lbl = LABELS[lang_key]
    data = SCHEMES[lang_key]
    CAT_CLASS = CAT_CLASS_EN if lang_key == "en" else CAT_CLASS_HI  # noqa

    st.markdown("<hr>", unsafe_allow_html=True)

    # Category filter
    all_cats = [lbl["all_cats"]] + list(data.keys())
    selected_cat = st.selectbox(lbl["cat_label"], all_cats)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Search
    search_query = st.text_input(lbl["filter_label"], placeholder=lbl["filter_placeholder"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"[{lbl['apply_text']}]({lbl['apply_link']})")

# ─────────────────────────────────────────────
# MAIN — Header
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="header-banner">
    <h1>🏛️ {lbl['title']}</h1>
    <p>{lbl['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# MAIN — Scheme cards
# ─────────────────────────────────────────────
def render_scheme(scheme, css_class=""):
    st.markdown(f"""
    <div class="scheme-card {css_class}">
        <div class="scheme-name">{scheme['name']}</div>
        <div class="scheme-desc">{scheme['desc']}</div>
        <div class="scheme-link"><a href="{scheme['link']}" target="_blank">{lbl['visit_btn']}</a></div>
    </div>
    """, unsafe_allow_html=True)

shown_any = False

for category, schemes in data.items():
    # Category filter
    if selected_cat != lbl["all_cats"] and category != selected_cat:
        continue

    # Search filter
    filtered = schemes
    if search_query:
        q = search_query.lower()
        filtered = [s for s in schemes if q in s["name"].lower() or q in s["desc"].lower()]
    if not filtered:
        continue

    css_class = CAT_CLASS.get(category, "")
    shown_any = True
    st.markdown(f'<div class="category-header cat-{css_class}">{category}</div>', unsafe_allow_html=True)

    # Responsive 2-column grid
    cols = st.columns(2, gap="medium")
    for i, scheme in enumerate(filtered):
        with cols[i % 2]:
            render_scheme(scheme, css_class)

if not shown_any:
    st.info("No schemes found. Try a different search term." if lang_key == "en" else "कोई योजना नहीं मिली। कृपया अलग शब्द खोजें।")

# ─────────────────────────────────────────────
# MAIN — Important info box
# ─────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
important_lines = lbl["important_body"].strip().split("\n")
important_html = "".join(f"<div>{line}</div>" for line in important_lines)
st.markdown(f"""
<div class="info-box">
    <strong style="font-size:1.05rem; color:#FFD700;">{lbl['important_title']}</strong><br><br>
    {important_html}
    <br>
    <a href="{lbl['apply_link']}" target="_blank" style="color:#FF6B35; font-weight:700;">{lbl['apply_text']}</a>
</div>
""", unsafe_allow_html=True)
