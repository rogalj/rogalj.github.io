import streamlit as st


st.write("# Training dataset checkerboard")
st.markdown("""---""")

#path = "/Users/jrogal/work/NYU/dmref/outreach/mlforkids/patterns/train_checker/"
#path = "https://github.com/rogalj/rogalj.github.io/tree/main/patterns/train_checker/"
path = "https://raw.githubusercontent.com/rogalj/rogalj.github.io/main/patterns/train_checker/"

#imgs = ["img_checker-000.png", "img_checker-001.png", "img_checker-002.png",
#        "img_checker-003.png", "img_checker-004.png", "img_checker-005.png",
#        "img_checker-006.png", "img_checker-007.png", "img_checker-008.png"]


#for img in imgs:
#    capt = "Training image " + img
#    st.image(path+img, caption=capt)


#img1 = path+imgs[0]
#img2 = path+imgs[1]

#img1 = [path+imgs[0], path+imgs[1], path+imgs[2],
#        path+imgs[3], path+imgs[4], path+imgs[5],
#        path+imgs[6], path+imgs[7], path+imgs[8]]

caps = []
imgs = []
for i in range(50):
    k = f'{i:03d}'
    name = "img_checker-" + k + ".png"
    caps.append("checkerboard " + k)
    imgs.append(path + name)



#st.image([img1,img2], caption=[imgs[0],imgs[1]])

col=st.columns(5, gap="medium")

nimg = len(imgs)
ncol = len(col)
nimgcol = int(nimg/ncol)
nleftover = nimg % ncol
#st.write(nimgcol)
#st.write(nleftover)


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


#with col[1]:
#    st.image(img1, caption=imgs)
