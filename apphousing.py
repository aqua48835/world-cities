import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 绘图样式
plt.style.use('seaborn-v0_8')

# 1. 页面标题
st.title("California Housing Data (1990) by [Xia Jingying]")

# 读取加州房价数据集
df_raw = pd.read_csv("housing.csv")
df = df_raw.copy()

# 2. 主页面滑块：最小房屋中位价
price_min = st.slider("Minimal Median House Value", min_value=0, max_value=500001, value=200000)
# 过滤房价 >= 滑块值
df = df[df["median_house_value"] >= price_min]

# 3. 子标题
st.subheader("See more filters in the sidebar:")

# ========== 侧边栏筛选器 ==========
with st.sidebar:
    # 4. 多选：近海类型，默认全选
    location_options = df_raw["ocean_proximity"].unique()
    location_select = st.multiselect("Choose the location type", options=location_options, default=location_options)
    df = df[df["ocean_proximity"].isin(location_select)]

    # 5. 单选：收入等级
    income_level = st.radio("Choose income level", ["Low", "Medium", "High"])
    # 根据单选筛选收入
    if income_level == "Low":
        df = df[df["median_income"] <= 2.5]
    elif income_level == "Medium":
        df = df[(df["median_income"] > 2.5) & (df["median_income"] < 4.5)]
    elif income_level == "High":
        df = df[df["median_income"] >= 4.5]

# 6. 绘制过滤后区域地图
st.map(df)

# 7. 房价直方图，30个区间
st.subheader("Median House Value Histogram")
fig, ax = plt.subplots()
ax.hist(df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value ($)")
ax.set_ylabel("District Count")
st.pyplot(fig)