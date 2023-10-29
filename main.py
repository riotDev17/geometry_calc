import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        "Main Menu", [
            'Persegi', 'Persegi Panjang', 'Jajar Genjang', 'Segitiga', 'Belah Ketupat'
        ], menu_icon="cast"
    )


# * ======================keliling dan luas persegi======================
if selected == 'Persegi':
    st.title('Selamat Datang')
    st.write(
        'Ini Adalah Aplikasi Untuk Menghitung Keliling Dan Luas Persegi')
    st.image("images/rumus.jpg")

    # * Kolom untuk persegi
    col1, col2 = st.columns(2)

    # ? Kolom 1
    with col1:
        st.header('Luas Persegi')
        sisi = st.number_input('Masukkan Nilai S (Sisi)', 0, key=1)

        #  Rumus luas persegi
        luas_persegi = sisi * sisi

        # Tombol luas persegi
        button_luasPersegi = st.button('Totalkan', key=2)
        if button_luasPersegi:
            st.success('Luas Persegi Nya Adalah ' +
                       str(luas_persegi) + ' Cm')

    # ? Kolom 2
    with col2:
        st.header('Keliling Persegi')
        sisi = st.number_input(
            'Masukkan Nilai S (Sisi)', 0, key=3)

        #  Rumus keliling persegi
        keliling_persegi = sisi * 4

        # Tombol keliling persegi
        button_kelilingPersegi = st.button('Totalkan', key=4)
        if button_kelilingPersegi:
            st.success('Keliling Persegi Nya Adalah ' +
                       str(keliling_persegi) + ' Cm')


# * =====================keliling dan luas persegi panjang==========================
if selected == 'Persegi Panjang':
    st.title('Selamat Datang')
    st.write(
        'Ini Adalah Aplikasi Untuk Menghitung Keliling Dan Luas Persegi panjang')
    st.image("images/rumus.jpg")

    # * Kolom untuk persegi panjang
    col1, col2 = st.columns(2)

    # ? kolom 1
    with col1:
        st.header('Luas Persegi Panjang')
        panjang = st.number_input('Masukkan Nilai P (Panjang) ', 0, key=1)
        lebar = st.number_input('Masukkan Nilai L (Lebar) ', 0, key=2)

        # Rumus luas persegi panjang
        luas_persegiPanjang = panjang * lebar

        # Tombol luas persegi panjang
        buttton_luasPersegiPanjang = st.button('Totalkan ', key=3)
        if buttton_luasPersegiPanjang:
            st.success('Luas Persegi Panjang Nya Adalah ' +
                       str(luas_persegiPanjang) + ' Cm2')

    # ? kolom2
    with col2:
        st.header('Keliling Persegi Panjang')
        panjang = st.number_input('Masukkan Nilai P (Panjang) ', 0, key=4)
        lebar = st.number_input('Masukkan Nilai L (Lebar) ', 0, key=5)

        # Rumus keliling persegi panjang
        keliling_persegiPanjang = 2 * (panjang + lebar)

        # Tombol keliling persegi panjang
        button_kelilingPersegiPanjang = st.button('Totalkan ', key=6)
        if button_kelilingPersegiPanjang:
            st.success('Keliling Persegi Panjang Nya Adalah ' +
                       str(keliling_persegiPanjang) + ' Cm')


# * ========================keliling dan luas jajar genjang==================================
if selected == 'Jajar Genjang':
    st.title('Selamat Datang')
    st.write(
        'Ini Adalah Aplikasi Untuk Menghitung Keliling Dan Luas jajar Genjang')
    st.image("images/rumus.jpg")

    # * Kolom untuk jajar genjang
    col1, col2 = st.columns(2)

    # ? kolom 1
    with col1:
        st.header('Luas Jajar Genjang')
        alas = st.number_input('Masukkan Nilai a(Alas) ', 0, key=1)
        tinggi = st.number_input('Masukkan Nilai t (Tinggi)', 0, key=2)

        # rumus luas jajar genjang
        luasJajarGenjang = alas * tinggi

        # Tombol luas persegi panjang
        button_luasJajarGenjang = st.button('Totalkan', key=3)
        if button_luasJajarGenjang:
            st.success('Luas Jajar Genjang Nya Adalah ' +
                       str(luasJajarGenjang) + ' Cm2')

    # ? kolom 2
    with col2:
        st.header('Keliling Jajar Genjang')
        alas = st.number_input('Masukkan Nilai Sisi a dan b', 0, key=4)
        sisi = st.number_input('Masukkan Nilai Sisi c dan d', 0, key=5)

        # rumus keliling jajar  genjang
        kelilingJajarGenjang = 2 * (alas + sisi)

        # Tombol keliling persegi panjang
        button_kelilingJajarGenjang = st.button('Totalkan', key=6)
        if button_kelilingJajarGenjang:
            st.success('Keliling Jajar Genjang Nya Adalah ' +
                       str(kelilingJajarGenjang) + ' Cm')


# * ======================keliling dan luas segitiga===============================
if selected == 'Segitiga':
    st.title('Selamat Datang')
    st.write(
        'Ini Adalah Aplikasi Untuk Menghitung Keliling Dan Luas Segitiga Sama Kaki')
    st.image("images/rumus.jpg")

    # *  kolom untuk segitiga
    col1, col2 = st.columns(2)

    # ? kolom 1
    with col1:
        st.header('Luas Segitiga Sama Kaki')
        alas = st.number_input('Masukkan Nilai a(Alas) ', 0, key=1)
        tinggi = st.number_input('Masukkan Nilai t (Tinggi)', 0, key=2)

        # rumus luas segitiga
        luas_segitiga = (alas * tinggi) / 2

        # Tombol luas segitiga
        button_luasSegitiga = st.button('Totalkan', key=3)
        if button_luasSegitiga:
            st.success('Luas Segitiga Nya Adalah ' +
                       str(luas_segitiga) + ' Cm2')

    # ? kolom 2
    with col2:
        st.header('Keliling Segitiga Sama Kaki')
        alas = st.number_input('Masukkan Nilai a (Sisi a) ', 0, key=4)
        sisi = st.number_input('Masukkan Nilai b (Sisi b dan c) ', 0, key=5)

        # rumus keliling segitiga
        keliling_segitiga = alas + (2 * sisi)

        # Tombol keliling segitiga
        button_kelilingSegitiga = st.button('Totalkan', key=6)
        if button_kelilingSegitiga:
            st.success('Keliling Segitiga Nya Adalah ' +
                       str(keliling_segitiga)  + ' Cm')


# * =======================keliling dan luas belah ketupat================================
if selected == 'Belah Ketupat':
    st.title('Selamat Datang')
    st.write(
        'Ini Adalah Aplikasi Untuk Menghitung Keliling Dan Luas Belah Ketupat')
    st.image("images/rumus.jpg")

    # *  kolom untuk belah ketupat
    col1, col2 = st.columns(2)

    # ? kolom 1
    with col1:
        st.header('Luas Belah Ketupat')
        diagonal_1 = st.number_input(
            'Masukkan Nilai d1(Diagonal 1) ', 0, key=1)
        diagonal_2 = st.number_input(
            'Masukkan Nilai d2 (Diagonal 2)', 0, key=2)

        # rumus luas belah ketupat
        luas_BelahKetupat = (diagonal_1 * diagonal_2) / 2

        # Tombol luas belah ketupat
        button_luasBelahKetupat = st.button('Totalkan', key=3)
        if button_luasBelahKetupat:
            st.success('Luas Belah Ketupat Nya Adalah ' +
                       str(luas_BelahKetupat) + ' Cm2')

    # ? kolom 2
    with col2:
        st.header('Keliling Belah Ketupat')
        sisi = st.number_input('Masukkan Nilai a , b , c , d ', 0, key=4)

        # rumus keliling belah ketupat
        keliling_BelahKetupat = 4 * sisi

        # Tombol keliling belah ketupat
        button_kelilingBelahKetupat = st.button('Totalkan', key=6)
        if button_kelilingBelahKetupat:
            st.success('Keliling Belah Ketupat Nya Adalah ' +
                       str(keliling_BelahKetupat) + ' Cm')
