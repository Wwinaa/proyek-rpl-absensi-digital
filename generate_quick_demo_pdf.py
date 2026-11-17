# -*- coding: utf-8 -*-
"""
Script to generate a concise, professional, step-by-step PDF guide and script for Winarti's Live Demo Video.
File: Panduan_dan_Naskah_Demo_Singkat_Winarti.pdf
"""

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os
import subprocess

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def style_table_header(row, col_widths, bg_color="0F172A"):
    for idx, cell in enumerate(row.cells):
        cell.width = Inches(col_widths[idx])
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=140, bottom=140, left=160, right=160)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                run.font.size = Pt(10)

def style_table_row(row, is_even, col_widths):
    bg_color = "F8FAFC" if is_even else "FFFFFF"
    for idx, cell in enumerate(row.cells):
        cell.width = Inches(col_widths[idx])
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=120, bottom=120, left=160, right=160)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

def build_demo_guide_document():
    doc = Document()

    # Set Margins (Narrow 0.7 inch for high content density & elegance)
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    # HEADER TITLE
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    r_t1 = p_title.add_run("PANDUAN LANGKAH & NASKAH DEMO LIVE APLIKASI\n")
    r_t1.bold = True
    r_t1.font.name = "Calibri"
    r_t1.font.size = Pt(16)
    r_t1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    r_t2 = p_title.add_run("Sistem Presensi Digital & Kesiswaan Terpadu SMK NU Wargabinangun\n")
    r_t2.bold = True
    r_t2.font.name = "Calibri"
    r_t2.font.size = Pt(12)
    r_t2.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

    r_t3 = p_title.add_run("Format Singkat, Jelas, & Langsung ke Intinya (Durasi Video: 5 – 7 Menit)")
    r_t3.italic = True
    r_t3.font.name = "Calibri"
    r_t3.font.size = Pt(10)
    r_t3.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

    # 1. IDENTITAS & REPO CHEAT SHEET
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    h1 = doc.add_heading("1. Identitas Pengembang & Akses Proyek", level=2)
    h1.runs[0].font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    h1.runs[0].font.size = Pt(11.5)

    tbl_id = doc.add_table(rows=5, cols=2)
    tbl_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    id_data = [
        ("Nama Mahasiswa / NIM", "Winarti (NIM: 41257168) | Kelas: TI-1C (Angkatan 2025)"),
        ("Kelompok / Tema Topik", "Kelompok Sunyaragi Nexus | Tema: E-Learning & Smart Education AI"),
        ("Dosen Pengampu", "Yudhistira Arie Wijaya, M.Kom., CDS."),
        ("Repositori GitHub Resmi", "https://github.com/Wwinaa/proyek-rpl-absensi-digital"),
        ("Prototipe Figma UI/UX", "https://www.figma.com/design/HJ3KQU3E6jYNRBvK1X99aU/Untitled?node-id=0-1")
    ]
    for idx, (k, v) in enumerate(id_data):
        row = tbl_id.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.text = k
        c1.text = v
        c0.width = Inches(2.2); c1.width = Inches(4.9)
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)
        c0.paragraphs[0].runs[0].font.bold = True
        c0.paragraphs[0].runs[0].font.size = Pt(9)
        c1.paragraphs[0].runs[0].font.size = Pt(9)

    # 2. CONTEKAN AKUN & BARCODE UNTUK DEMO
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    h2 = doc.add_heading("2. Contekan Cepat Akun Demo & Kode Barcode Siap Scan", level=2)
    h2.runs[0].font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    h2.runs[0].font.size = Pt(11.5)

    tbl_acc = doc.add_table(rows=5, cols=4)
    tbl_acc.alignment = WD_TABLE_ALIGNMENT.CENTER
    acc_headers = ["Peran (Role)", "Username", "Password", "Kode Barcode / QR (Scan)"]
    for idx, text in enumerate(acc_headers):
        tbl_acc.rows[0].cells[idx].text = text
    style_table_header(tbl_acc.rows[0], [1.8, 1.6, 1.4, 2.3], bg_color="1E3A8A")

    acc_data = [
        ("Administrator", "Winarti (atau admin)", "password", "Hak akses penuh kelola 20 tabel"),
        ("Peserta Didik (Siswa)", "cakra", "password123", "BRC1000 (Cakra Bramantyo - X TKJ 1)"),
        ("Guru Pengajar", "BudiSan", "password123", "198001012005011001 (Budi Santoso, S.Kom)"),
        ("Wali Kelas (Dual-Sync)", "iwan.wk", "password123", "WK19800000 (Iwan Setiawan - X TKJ 1)")
    ]
    for idx, (r, u, p, b) in enumerate(acc_data, start=1):
        row = tbl_acc.rows[idx]
        row.cells[0].text = r
        row.cells[1].text = u
        row.cells[2].text = p
        row.cells[3].text = b
        style_table_row(row, is_even=(idx % 2 == 1), col_widths=[1.8, 1.6, 1.4, 2.3])
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[3].paragraphs[0].runs[0].font.bold = True

    # 3. TABEL ARAHAN & NASKAH DEMO SINGKAT (7 LANGKAH TO-THE-POINT)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    h3 = doc.add_heading("3. Panduan 7 Langkah Aksi Layar & Naskah Bicara Winarti", level=2)
    h3.runs[0].font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    h3.runs[0].font.size = Pt(11.5)

    tbl_demo = doc.add_table(rows=8, cols=3)
    tbl_demo.alignment = WD_TABLE_ALIGNMENT.CENTER
    d_headers = ["Langkah & Waktu", "Arahan Aksi di Layar Komputer", "Naskah Bicara Winarti (Gaya Santai & Lugas)"]
    for idx, text in enumerate(d_headers):
        tbl_demo.rows[0].cells[idx].text = text
    style_table_header(tbl_demo.rows[0], [1.3, 2.3, 3.5], bg_color="0F172A")

    steps_data = [
        (
            "Langkah 1\n(~30 Detik)\nPembuka",
            "• Buka Google Chrome di halaman http://localhost/absen/\n• Webcam wajah aktif di pojok kanan atas layar\n• Tatap kamera sambil tersenyum ramah",
            "\"Halo semuanya, selamat datang! Nama saya Winarti, mahasiswi Teknik Informatika kelas TI-1C, NIM 41257168 dari kelompok Sunyaragi Nexus.\n\nDi video ini, saya akan mendemonstrasikan secara langsung sistem tugas proyek akhir saya, yaitu: Sistem Presensi Digital dan Kesiswaan Terpadu SMK NU Wargabinangun yang sudah terintegrasi scanner kamera, notifikasi Bot Telegram, dan Asisten AI cerdas Hadir.io. Yuk langsung kita coba aplikasinya!\""
        ),
        (
            "Langkah 2\n(~45 Detik)\nDashboard & Master Data",
            "• Di form login, ketik username: Winarti, password: password. Klik Masuk.\n• Sorot grafik statistik kehadiran hari ini.\n• Buka menu Master Data Siswa, lalu klik tombol Cetak Barcode.",
            "\"Pertama, kita login sebagai Administrator. Masukkan password, klik Masuk.\n\nNah, di dashboard utama ini admin bisa langsung melihat grafik statistik kehadiran hari ini. Di sebelah kiri, sistem ini mengelola 20 tabel database terpadu: mulai dari data jurusan, kelas, siswa, guru, jadwal pelajaran, sampai pengaturan sistem.\n\nAdmin juga bisa langsung mencetak kartu barcode atau QR Code untuk semua siswa dan guru hanya dalam satu kali klik, seperti yang terlihat pada halaman cetak ini.\""
        ),
        (
            "Langkah 3\n(~1.5 Menit)\nLive Scan & Telegram",
            "• Buka menu Scanner di http://localhost/absen/absensi/scan.\n• Ketik kode barcode siswa: BRC1000, tekan Enter. Muncul toast sukses hijau.\n• Ketik kode Wali Kelas: WK19800000, tekan Enter.",
            "\"Sekarang kita masuk ke fitur utamanya: Pemindai Presensi Cepat.\n\nHalaman ini mendukung scan kamera webcam langsung atau input barcode. Saya contohkan scan barcode siswa BRC1000 atas nama Cakra Bramantyo. Kita klik Kirim... langsung berbunyi bip dan muncul notifikasi: Presensi masuk berhasil dicatat!\n\nSaat presensi sukses, sistem otomatis mengirim notifikasi live ke Bot Telegram (@HadirioBot) langsung ke grup sekolah dan orang tua.\n\nFitur ini juga memiliki Dual-Sync Otomatis untuk wali kelas. Saat kode WK19800000 di-scan, sistem otomatis mencatat presensi guru sekaligus kehadiran wali kelas rombel binaannya.\""
        ),
        (
            "Langkah 4\n(~1 Menit)\nPortal Siswa & Izin Dokter",
            "• Logout Admin, lalu login akun siswa: cakra / password123.\n• Tunjukkan kalender kehadiran (kotak tanggal hari ini otomatis HIJAU / Hadir).\n• Buka menu Pengajuan Izin.",
            "\"Sekarang kita beralih ke portal siswa dengan login pakai akun cakra, password: password123.\n\nDi dashboard siswa, Cakra bisa langsung melihat kalender presensi pribadinya yang otomatis berwarna hijau karena tadi kita sudah scan masuk.\n\nKalau siswa berhalangan hadir karena sakit, siswa bisa mengajukan perizinan mandiri secara paperless di menu ini dengan wajib melampirkan foto surat dokter. Pengajuan ini akan langsung masuk ke dashboard wali kelas untuk diverifikasi.\""
        ),
        (
            "Langkah 5\n(~1.5 Menit)\nAsisten Cerdas AI Hadir.io",
            "• Klik balon chat robot mengambang di pojok kanan bawah.\n• Ketik: 'Berapa jumlah kelas di SMK NU Wargabinangun?' kirim.\n• Ketik: 'Siapa saja nama guru yang mengajar di sini?' kirim.",
            "\"Ini adalah fitur paling cerdas di sistem ini: Asisten AI Sekolah Hadir.io yang bisa diakses oleh seluruh 5 peran pengguna.\n\nChatbot ini menggabungkan Fast-Path SQL Extraction lokal dengan model AI NVIDIA NIM (Nemotron LLM). Jadi jawabannya keluar dalam hitungan detik, bahasanya natural, 100% akurat dari database lokal dan bebas halusinasi.\n\nMisalnya saya tanya: 'Berapa jumlah kelas di SMK NU Wargabinangun?'. Kita kirim... dan jawabannya langsung keluar lengkap dan to-the-point!\n\nAsisten ini juga sudah mendukung 4 bahasa adaptif: Bahasa Indonesia, English, Basa Sunda, dan Basa Jawa Cirebonan.\""
        ),
        (
            "Langkah 6\n(~1 Menit)\nRekapitulasi & Ekspor Laporan",
            "• Login kembali ke akun Admin / Kepsek (Winarti / password).\n• Buka menu Laporan Presensi.\n• Tunjukkan filter Senin-Jumat, lalu klik tombol Ekspor Excel (.xlsx) dan Cetak PDF.",
            "\"Terakhir untuk pelaporan, pimpinan sekolah dan wali kelas bisa membuka menu Rekapitulasi Presensi.\n\nPerhitungan persentase kehadiran di sistem ini sudah menggunakan filter hari efektif Senin sampai Jumat, jadi hari libur Sabtu dan Minggu otomatis dikecualikan agar data rekapitulasi benar-benar valid.\n\nLaporan ini bisa langsung kita ekspor satu kali klik ke format Microsoft Excel (.xlsx) maupun dicetak resmi ke format PDF untuk arsip sekolah.\""
        ),
        (
            "Langkah 7\n(~30 Detik)\nPenutup",
            "• Kembali ke halaman dashboard utama.\n• Tatap webcam wajah, tersenyum ramah.",
            "\"Secara keseluruhan, sistem presensi ini berhasil mengotomasi proses absensi harian menjadi transparan, cepat, dan bebas kecurangan dengan dukungan Bot Telegram dan AI Hadir.io.\n\nSeluruh kode program telah diunggah ke repositori GitHub proyek-rpl-absensi-digital, dan berkas laporan lengkap sudah selesai disusun.\n\nSekian demonstrasi dari saya, Winarti. Terima kasih banyak kepada Bapak Yudhistira Arie Wijaya dan teman-teman semua. Wassalamu'alaikum warahmatullahi wabarakatuh.\""
        )
    ]

    for idx, (step_time, action, speech) in enumerate(steps_data, start=1):
        row = tbl_demo.rows[idx]
        row.cells[0].text = step_time
        row.cells[1].text = action
        row.cells[2].text = speech
        style_table_row(row, is_even=(idx % 2 == 1), col_widths=[1.3, 2.3, 3.5])
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

    # 4. TIPS PENTING SEBELUM REKAMAN
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    h4 = doc.add_heading("4. Tips Teknis Perekaman Layar (Screen Recording)", level=2)
    h4.runs[0].font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    h4.runs[0].font.size = Pt(11.5)

    p_tips = doc.add_paragraph()
    p_tips.paragraph_format.line_spacing = 1.15
    tips_items = [
        ("Kamera Wajah Aktif: ", "Pastikan webcam wajah Anda selalu menyala di sudut kanan atas layar sepanjang video (kriteria wajib verifikasi tugas mandiri)."),
        ("Mode Bebas 24 Jam Aktif: ", "Sistem sudah diatur dalam mode bebas 24 jam, jadi Anda bisa melakukan scan masuk dan scan pulang kapan saja tanpa ada kendala batasan jam sekolah."),
        ("Gunakan Fitur Input Barcode Cepat: ", "Di bawah kotak kamera terdapat input teks manual barcode. Mengetik kode seperti BRC1000 atau WK19800000 jauh lebih cepat, stabil, dan minim risiko gagal baca kamera."),
        ("Studio Teleprompter Lokal: ", "Anda bisa membuka berkas teleprompter_video.html di browser Chrome dan mengaturnya berdampingan dengan layar aplikasi saat merekam video.")
    ]
    for bold_text, normal_text in tips_items:
        r_b = p_tips.add_run("• " + bold_text)
        r_b.bold = True
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        r_n = p_tips.add_run(normal_text + "\n")
        r_n.font.size = Pt(9.5)
        r_n.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    return doc

if __name__ == "__main__":
    docx_path = r"c:\xampp\htdocs\absen\Panduan_dan_Naskah_Demo_Singkat_Winarti.docx"
    pdf_path = r"c:\xampp\htdocs\absen\Panduan_dan_Naskah_Demo_Singkat_Winarti.pdf"

    print("Generating concise Demo Guide DOCX...")
    d = build_demo_guide_document()
    d.save(docx_path)
    print("[SUCCESS] DOCX generated at:", docx_path)

    print("Converting DOCX to PDF via docx2pdf...")
    try:
        from docx2pdf import convert
        convert(docx_path, pdf_path)
        print("[SUCCESS] PDF generated at:", pdf_path)
    except Exception as e:
        print("[ERROR] docx2pdf failed:", e)
