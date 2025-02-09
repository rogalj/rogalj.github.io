import streamlit as st


st.write("# Training dataset checkerboard")
st.markdown("""---""")

path = "https://raw.githubusercontent.com/rogalj/rogalj.github.io/main/patterns/train_checker/"

caps = []
imgs = []
for i in range(50):
    k = f'{i:03d}'
    name = "img_checker-" + k + ".png"
    caps.append("checkerboard " + k)
    imgs.append(path + name)



col=st.columns(5, gap="medium")

nimg = len(imgs)
ncol = len(col)
nimgcol = int(nimg/ncol)
nleftover = nimg % ncol


start=0
stop = start+nimgcol

for i in range(len(col)):
    if i < nleftover:
        stop = stop + 1
    with col[i]:
        if stop < nimg:
            st.image(imgs[start:stop], caption=caps[start:stop])
        else:
            st.image(imgs[start:], caption=caps[start:])
    start = stop
    stop = start + nimgcol


