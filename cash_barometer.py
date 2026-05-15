import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# 基本設定
# =========================
APP_DIR = Path(".")
USERS_FILE = APP_DIR / "pro_users.json"
USER_DATA_DIR = APP_DIR / "user_data"
USER_DATA_DIR.mkdir(exist_ok=True)

DEMO_LIMIT = 6
LINE_URL = "https://lin.ee/7m28VAs"

DEFAULT_STATE = {
    "company_name": "株式会社○○",
    "cash": 500,
    "revenue": 500,
    "cost": 250,
    "fixed_cost": 130,
    "loan_pay": 50,
    "tax_rate": 0.30,
    "plan": "デモ（無料）",
    "calc_count": 0
}
