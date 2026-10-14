import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Quản lý điểm sinh viên', page_icon='🎓', layout='wide')
st.title('QUẢN LÝ ĐIỂM SINH VIÊN')

# 1. Tạo DataFrame gồm 10 sinh viên
DATA = {
    'Họ tên': ['Nguyễn Văn An', 'Trần Thị Bình', 'Lê Minh Châu', 'Phạm Quốc Dũng',
               'Hoàng Thị Hà', 'Võ Minh Khang', 'Đặng Ngọc Lan', 'Bùi Thanh Mai',
               'Phan Anh Nam', 'Đỗ Thị Phương'],
    'Chuyên cần': [9, 8, 10, 7, 9, 6, 8, 10, 5, 7],
    'Giữa kỳ': [8, 7, 9, 6, 8, 5, 7, 9, 4, 6],
    'Cuối kỳ': [9, 8, 9, 7, 8, 4, 7, 10, 3, 6],
}
df = pd.DataFrame(DATA)
df.index = range(1, len(df) + 1)
df.index.name = 'STT'

# 2. Tính điểm tổng kết
df['Tổng kết'] = (df['Chuyên cần'] * 0.2 + df['Giữa kỳ'] * 0.3 + df['Cuối kỳ'] * 0.5).round(2)

# 3. Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    if diem >= 7:
        return 'Khá'
    if diem >= 5:
        return 'Trung bình'
    return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 4. Bảng điểm
st.subheader('1. Bảng điểm của 10 sinh viên')
st.dataframe(df, use_container_width=True)

# 5. Thống kê
st.subheader('2. Thống kê kết quả học tập')
diem_tb = df['Tổng kết'].mean()
sv_cao = df.loc[df['Tổng kết'].idxmax()]
sv_thap = df.loc[df['Tổng kết'].idxmin()]
so_dat = int((df['Tổng kết'] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric('Điểm trung bình lớp', f'{diem_tb:.2f}')
c2.metric('Sinh viên đạt', f'{so_dat}/{len(df)}')
c3.metric('Điểm cao nhất', f'{sv_cao["Tổng kết"]:.2f}')
c4.metric('Điểm thấp nhất', f'{sv_thap["Tổng kết"]:.2f}')
st.write(f'**Sinh viên cao nhất:** {sv_cao["Họ tên"]} ({sv_cao["Tổng kết"]:.2f} điểm)')
st.write(f'**Sinh viên thấp nhất:** {sv_thap["Họ tên"]} ({sv_thap["Tổng kết"]:.2f} điểm)')

# 6. Chọn sinh viên
st.subheader('3. Tra cứu điểm sinh viên')
ten = st.selectbox('Chọn sinh viên:', df['Họ tên'].tolist())
sv = df.loc[df['Họ tên'] == ten].iloc[0]
st.write(f'**Họ tên:** {ten}')
st.write(f'**Điểm chuyên cần:** {sv["Chuyên cần"]}')
st.write(f'**Điểm giữa kỳ:** {sv["Giữa kỳ"]}')
st.write(f'**Điểm cuối kỳ:** {sv["Cuối kỳ"]}')
st.write(f'**Điểm tổng kết:** {sv["Tổng kết"]:.2f}')
st.write(f'**Xếp loại:** {sv["Xếp loại"]}')

# 7. Biểu đồ
st.subheader('4. Biểu đồ điểm tổng kết')
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df['Họ tên'], df['Tổng kết'])
ax.set_title('Diem tong ket cua 10 sinh vien')
ax.set_xlabel('Sinh vien')
ax.set_ylabel('Diem tong ket')
ax.set_ylim(0, 10)
ax.tick_params(axis='x', labelrotation=45)
for label in ax.get_xticklabels():
    label.set_horizontalalignment('right')
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 8. Thông tin tác giả: 
st.divider()
st.caption('Người tạo ứng dụng: [Lê Diên Hồng Vân] | MSSV: [025308003954]')
