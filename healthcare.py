def render_yes_no_buttons(key_prefix):
    col1, col2 = st.columns([1, 1])

    # カスタムボタン用CSS（ボタンの親divに幅指定）
    st.markdown("""
    <style>
    .custom-button-wrapper {
        width: 60%;
        margin: auto;
    }
    .custom-button-wrapper > div {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

    selected = None
    with col1:
        with st.container():
            st.markdown('<div class="custom-button-wrapper">', unsafe_allow_html=True)
            if st.button("yes", key=f"{key_prefix}_yes"):
                selected = "yes"
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="custom-button-wrapper">', unsafe_allow_html=True)
            if st.button("no", key=f"{key_prefix}_no"):
                selected = "no"
            st.markdown('</div>', unsafe_allow_html=True)

    return selected
