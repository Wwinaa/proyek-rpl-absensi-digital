# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Arrow
import numpy as np

def create_ai_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    # Title
    ax.text(50, 7, "ARSITEKTUR DUAL-ENGINE ASISTEN AI HADIR.IO & GUARDRAIL RBAC", color='#F8FAFC', fontsize=12, fontweight='bold', ha='center')
    ax.text(50, 12, "Integrasi Fast-Path SQL Extraction & Model NVIDIA NIM Nemotron LLM (4 Bahasa)", color='#38BDF8', fontsize=8.5, ha='center')

    # User Input Box
    ax.add_patch(FancyBboxPatch((3, 22), 20, 24, boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#38BDF8', linewidth=1.2))
    ax.text(13, 27, "INPUT PENGGUNA", color='#FFFFFF', fontsize=9, fontweight='bold', ha='center')
    ax.text(13, 33, "Siswa / Guru / Wali Kelas\nKepala Sekolah / Admin", color='#94A3B8', fontsize=7.5, ha='center')
    ax.text(13, 40, "\"Ada berapa guru aktif?\"\n\"Aya sabaraha kelas?\"", color='#FDE047', fontsize=7, ha='center', style='italic')

    # Arrow 1
    ax.annotate('', xy=(28, 34), xytext=(24, 34), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=2))

    # RBAC Guardrail Box
    ax.add_patch(FancyBboxPatch((29, 22), 18, 24, boxstyle="round,pad=0.3", facecolor='#0F172A', edgecolor='#EF4444', linewidth=1.2))
    ax.text(38, 27, "GUARDRAIL RBAC", color='#EF4444', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(38, 33, "Penyaringan Prompt\n& Firewall Privasi", color='#E2E8F0', fontsize=7.5, ha='center')
    ax.text(38, 41, "[BLOKIR]\nPassword / NIK / Tanggal Lahir", color='#FCA5A5', fontsize=6.5, ha='center')

    # Arrow 2 Split
    ax.annotate('', xy=(52, 27), xytext=(48, 32), arrowprops=dict(arrowstyle="->", color='#10B981', lw=1.8))
    ax.annotate('', xy=(52, 41), xytext=(48, 36), arrowprops=dict(arrowstyle="->", color='#A855F7', lw=1.8))

    # Engine 1: Fast-Path SQL
    ax.add_patch(FancyBboxPatch((53, 17), 24, 20, boxstyle="round,pad=0.3", facecolor='#064E3B', edgecolor='#10B981', linewidth=1.2))
    ax.text(65, 22, "ENGINE 1: FAST-PATH SQL", color='#34D399', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(65, 27, "Ekstraksi Fakta Database Lokal", color='#FFFFFF', fontsize=7.5, ha='center')
    ax.text(65, 33, "SELECT COUNT(*) FROM guru\n100% Akurat & Zero Hallucination", color='#D1FAE5', fontsize=6.8, ha='center')

    # Engine 2: NVIDIA NIM
    ax.add_patch(FancyBboxPatch((53, 41), 24, 20, boxstyle="round,pad=0.3", facecolor='#3B0764', edgecolor='#C084FC', linewidth=1.2))
    ax.text(65, 46, "ENGINE 2: NVIDIA NIM LLM", color='#E9D5FF', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(65, 51, "Nemotron-3.5-bolt-e4b REST API", color='#FFFFFF', fontsize=7.5, ha='center')
    ax.text(65, 57, "Penalaran Bahasa Alami\n& Formulasi Konteks Santun", color='#F3E8FF', fontsize=6.8, ha='center')

    # Merge Arrows
    ax.annotate('', xy=(82, 34), xytext=(78, 27), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=1.8))
    ax.annotate('', xy=(82, 34), xytext=(78, 51), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=1.8))

    # Multilingual Response Box
    ax.add_patch(FancyBboxPatch((83, 20), 15, 28, boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#0284C7', linewidth=1.2))
    ax.text(90.5, 25, "OUTPUT AI", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(90.5, 30, "4 BAHASA:", color='#FFFFFF', fontsize=7.5, fontweight='bold', ha='center')
    ax.text(90.5, 36, "• Indonesia (Resmi)\n• English (Global)\n• Sunda (Lokal)\n• Jawa (Cirebon)", color='#E2E8F0', fontsize=6.8, ha='center')
    ax.text(90.5, 44, "< 0.8 Detik", color='#FDE047', fontsize=7, fontweight='bold', ha='center')

    # Bottom Architecture Summary Pill
    ax.add_patch(FancyBboxPatch((10, 68), 80, 24, boxstyle="round,pad=0.4", facecolor='#0F172A', edgecolor='#334155', linewidth=1))
    ax.text(50, 73, "KEUNGGULAN ARSITEKTURAL DUAL-ENGINE:", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(50, 79, "1. Akurasi Mutlak (Zero Hallucination): Data angka dan jadwal diambil langsung dari MariaDB 20 tabel.", color='#E2E8F0', fontsize=7.5, ha='center')
    ax.text(50, 84, "2. Keamanan Tinggi: Lapisan RBAC menolak kueri yang menyangkut identitas sensitif atau kata sandi.", color='#E2E8F0', fontsize=7.5, ha='center')
    ax.text(50, 89, "3. Responsif & Santun: Respons diformulasikan secara cerdas mengikuti ragam dialek budaya sekolah.", color='#E2E8F0', fontsize=7.5, ha='center')

    plt.tight_layout()
    plt.savefig('Diagram_Arsitektur_AI_Hadirio.png', dpi=300)
    plt.close()
    print("Saved Diagram_Arsitektur_AI_Hadirio.png")

def create_mvc_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    ax.text(50, 7, "POLA ARSITEKTUR MODEL-VIEW-CONTROLLER (MVC) NATIVE PHP 8.2", color='#F8FAFC', fontsize=12, fontweight='bold', ha='center')
    ax.text(50, 12, "Pemisahan Tanggung Jawab Kode Bersih Tanpa Ketergantungan Framework Berat", color='#38BDF8', fontsize=8.5, ha='center')

    # Client Browser
    ax.add_patch(FancyBboxPatch((4, 25), 18, 48, boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#38BDF8', linewidth=1.2))
    ax.text(13, 31, "CLIENT BROWSER", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(13, 38, "HTML5-QRCode\nBootstrap 5 CSS\nVanilla JS AJAX\nAudio Beep FX", color='#E2E8F0', fontsize=7.5, ha='center')
    ax.text(13, 62, "Desktop, Tablet\n& Mobile Responsive", color='#94A3B8', fontsize=6.8, ha='center')

    # Arrows Client <-> Controller
    ax.annotate('', xy=(27, 44), xytext=(23, 44), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=1.8))
    ax.text(25, 41, "HTTP POST/GET", color='#94A3B8', fontsize=6.2, ha='center')
    ax.annotate('', xy=(23, 52), xytext=(27, 52), arrowprops=dict(arrowstyle="->", color='#34D399', lw=1.8))
    ax.text(25, 55, "JSON / HTML", color='#34D399', fontsize=6.2, ha='center')

    # Controller Layer
    ax.add_patch(FancyBboxPatch((28, 22), 22, 54, boxstyle="round,pad=0.3", facecolor='#0F172A', edgecolor='#0284C7', linewidth=1.2))
    ax.text(39, 28, "CONTROLLER LAYER", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(39, 34, "app/controllers/", color='#64748B', fontsize=7, ha='center')
    ax.text(39, 42, "• AuthController.php\n• ScanController.php\n• IzinController.php\n• LaporanController.php\n• ChatController.php", color='#E2E8F0', fontsize=7.2, ha='center')
    ax.text(39, 64, "Logika Bisnis,\nValidasi Jam Masuk/Pulang,\nDual-Sync & Auto-Sync", color='#FDE047', fontsize=6.8, ha='center')

    # Model Layer
    ax.add_patch(FancyBboxPatch((55, 18), 20, 28, boxstyle="round,pad=0.3", facecolor='#064E3B', edgecolor='#10B981', linewidth=1.2))
    ax.text(65, 24, "MODEL LAYER", color='#34D399', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(65, 29, "app/models/ (PDO Prepared)", color='#A7F3D0', fontsize=6.8, ha='center')
    ax.text(65, 37, "• AbsensiModel.php\n• UserModel.php\n• SiswaModel.php\n• GuruModel.php", color='#FFFFFF', fontsize=7.2, ha='center')

    # View Layer
    ax.add_patch(FancyBboxPatch((55, 52), 20, 26, boxstyle="round,pad=0.3", facecolor='#78350F', edgecolor='#F59E0B', linewidth=1.2))
    ax.text(65, 58, "VIEW LAYER", color='#FCD34D', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(65, 63, "app/views/ (Template UI)", color='#FEF3C7', fontsize=6.8, ha='center')
    ax.text(65, 71, "• admin/ /guru/\n• kepsek/ /walikelas/\n• siswa/ /scan.php", color='#FFFFFF', fontsize=7.2, ha='center')

    # Database
    ax.add_patch(FancyBboxPatch((80, 20), 16, 24, boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#38BDF8', linewidth=1.2))
    ax.text(88, 26, "DATABASE", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(88, 31, "db_absensi_smk", color='#F8FAFC', fontsize=7.5, ha='center')
    ax.text(88, 37, "MariaDB / MySQL\n20 Tabel Relasional\nNormalisasi 3NF", color='#94A3B8', fontsize=6.8, ha='center')

    # External Services
    ax.add_patch(FancyBboxPatch((80, 52), 16, 26, boxstyle="round,pad=0.3", facecolor='#3B0764', edgecolor='#C084FC', linewidth=1.2))
    ax.text(88, 58, "LAYANAN EKSTERNAL", color='#E9D5FF', fontsize=7.5, fontweight='bold', ha='center')
    ax.text(88, 64, "• Bot Telegram API\n  (@HadirioBot)\n• NVIDIA NIM API\n  (Nemotron LLM)", color='#FFFFFF', fontsize=6.8, ha='center')

    # Controller to Model and View arrows
    ax.annotate('', xy=(54, 30), xytext=(51, 38), arrowprops=dict(arrowstyle="->", color='#10B981', lw=1.5))
    ax.annotate('', xy=(54, 62), xytext=(51, 52), arrowprops=dict(arrowstyle="->", color='#F59E0B', lw=1.5))
    ax.annotate('', xy=(79, 32), xytext=(76, 32), arrowprops=dict(arrowstyle="<->", color='#38BDF8', lw=1.5))
    ax.annotate('', xy=(79, 64), xytext=(51, 58), arrowprops=dict(arrowstyle="->", color='#C084FC', lw=1.5))

    # Bottom Note
    ax.text(50, 91, "[CLEAN ARCHITECTURE] Ketergantungan mengalir satu arah, controller memisahkan tampilan dan manipulasi data.", color=C_MUTED if 'C_MUTED' in locals() else '#94A3B8', fontsize=7.2, ha='center', style='italic')

    plt.tight_layout()
    plt.savefig('Diagram_Arsitektur_MVC_PHP.png', dpi=300)
    plt.close()
    print("Saved Diagram_Arsitektur_MVC_PHP.png")

def create_time_validation_diagram():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    ax.text(50, 8, "LOGIKA VALIDASI ATURAN WAKTU PRESENSI DAN TOLERANSI KETERLAMBATAN", color='#F8FAFC', fontsize=11.5, fontweight='bold', ha='center')
    ax.text(50, 14, "Verifikasi Jam Server SMK NU Wargabinangun (05:00 s/d 18:00 WIB)", color='#38BDF8', fontsize=8.5, ha='center')

    # Timeline bar
    ax.add_patch(Rectangle((5, 28), 90, 8, facecolor='#1E293B', edgecolor='#475569', linewidth=1))

    # Time slots
    # 05:00 - 07:00 (Hadir Tepat Waktu) -> 5 to 35
    ax.add_patch(Rectangle((5, 28), 30, 8, facecolor='#065F46', edgecolor='#10B981', linewidth=1.2))
    ax.text(20, 33, "05:00 - 07:00 WIB\nHADIR TEPAT WAKTU", color='#A7F3D0', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 07:00 - 12:00 (Terlambat) -> 35 to 65
    ax.add_patch(Rectangle((35, 28), 30, 8, facecolor='#78350F', edgecolor='#F59E0B', linewidth=1.2))
    ax.text(50, 33, "07:01 - 12:00 WIB\nTERLAMBAT (Log Menit)", color='#FDE047', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 12:00 - 15:00 (KBM / Belum Jam Pulang) -> 65 to 80
    ax.add_patch(Rectangle((65, 28), 15, 8, facecolor='#1F2937', edgecolor='#64748B', linewidth=0.8))
    ax.text(72.5, 33, "12:01 - 14:59\nBelum Pulang", color='#94A3B8', fontsize=6.5, ha='center', va='center')

    # 15:00 - 18:00 (Jam Pulang Dibuka) -> 80 to 95
    ax.add_patch(Rectangle((80, 28), 15, 8, facecolor='#1E3A8A', edgecolor='#38BDF8', linewidth=1.2))
    ax.text(87.5, 33, ">= 15:00 WIB\nPULANG", color='#BAE6FD', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # Explanatory Cards Below
    cards = [
        ("KARTU HIJAU: TEPAT WAKTU", "05:00 - 07:00 WIB", "Audio beep sukses (nada tinggi), status dicatat 'Hadir Tepat Waktu', notifikasi Telegram terkirim instan.", '#064E3B', '#10B981'),
        ("KARTU KUNING: TERLAMBAT", "07:01 - 12:00 WIB", "Audio beep peringatan, status 'Terlambat', sistem menghitung durasi selisih menit dari jam 07:00 WIB.", '#78350F', '#F59E0B'),
        ("KARTU BIRU: KEPULANGAN", "Mulai 15:00 WIB", "Mode scan pulang dibuka, mencatat jam kepulangan siswa/guru, menolak scan jika sebelum jam 15:00 WIB.", '#1E3A8A', '#38BDF8')
    ]
    for i, (ctitle, csub, cdesc, cbg, cborder) in enumerate(cards):
        cx = 5 + (i * 31)
        ax.add_patch(FancyBboxPatch((cx, 46), 28, 44, boxstyle="round,pad=0.3", facecolor=cbg, edgecolor=cborder, linewidth=1.2))
        ax.text(cx + 14, 52, ctitle, color='#FFFFFF', fontsize=7.5, fontweight='bold', ha='center')
        ax.text(cx + 14, 58, csub, color=cborder, fontsize=7.2, fontweight='bold', ha='center')
        ax.text(cx + 14, 66, cdesc, color='#E2E8F0', fontsize=6.8, ha='center')

    plt.tight_layout()
    plt.savefig('Diagram_Alur_Validasi_Waktu.png', dpi=300)
    plt.close()
    print("Saved Diagram_Alur_Validasi_Waktu.png")

def create_testing_and_cicd_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    ax.text(50, 7, "VERIFIKASI PENGUJIAN PERANGKAT LUNAK & PIPELINE CI/CD DEVOPS", color='#F8FAFC', fontsize=12, fontweight='bold', ha='center')
    ax.text(50, 12, "Automated Unit Testing 10 Kasus Uji (100% PASS) & GitHub Actions Workflow", color='#38BDF8', fontsize=8.5, ha='center')

    # Left: Testing Summary Card
    ax.add_patch(FancyBboxPatch((4, 20), 44, 72, boxstyle="round,pad=0.4", facecolor='#0F172A', edgecolor='#10B981', linewidth=1.2))
    ax.text(26, 26, "HASIL AUTOMATED UNIT TESTING", color='#34D399', fontsize=9, fontweight='bold', ha='center')
    ax.text(26, 31, "PHPUnit & Custom Test Suite Runner", color='#94A3B8', fontsize=7, ha='center')

    # Badge 100% Pass
    ax.add_patch(FancyBboxPatch((13, 35), 26, 8, boxstyle="round,pad=0.2", facecolor='#065F46', edgecolor='#34D399', linewidth=1))
    ax.text(26, 40, "STATUS: 10 / 10 PASS (100%)", color='#FFFFFF', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Test Cases List
    tests = [
        "TC-01: Otentikasi Password Bcrypt Salah",
        "TC-02: Multi-Role Authorization (5 Role)",
        "TC-03: Scan QR 06:45 -> Hadir Tepat Waktu",
        "TC-04: Scan QR 07:20 -> Terlambat (+20m)",
        "TC-05: Scan Pulang < 15:00 Ditahan Server",
        "TC-06: Dual-Sync Wali Kelas -> Guru & Walas",
        "TC-07: Webhook Telegram Live Notifikasi",
        "TC-08: Auto-Sync Persetujuan Izin Sakit",
        "TC-09: Filter Rekap Efektif Senin - Jumat",
        "TC-10: Interaksi Cerdas Asisten AI 4 Bahasa"
    ]
    for idx, t_str in enumerate(tests):
        ty = 47 + (idx * 4.2)
        ax.text(7, ty, f"[PASS] {t_str}", color='#A7F3D0', fontsize=6.4)

    # Right: GitHub Actions CI/CD Pipeline
    ax.add_patch(FancyBboxPatch((52, 20), 44, 72, boxstyle="round,pad=0.4", facecolor='#0F172A', edgecolor='#0284C7', linewidth=1.2))
    ax.text(74, 26, "GITHUB ACTIONS CI/CD PIPELINE", color='#38BDF8', fontsize=9, fontweight='bold', ha='center')
    ax.text(74, 31, ".github/workflows/ci.yml (Trigger: Push / PR)", color='#94A3B8', fontsize=7, ha='center')

    # Stages in CI/CD
    stages = [
        ("1. Git Commit & Push Trigger", "Developer push ke branch main / pull request", '#1E293B', '#38BDF8'),
        ("2. Setup Runner Environment", "Ubuntu latest runner + PHP 8.2 setup + Extensions", '#1E293B', '#38BDF8'),
        ("3. PHP Linting & Syntax Check", "Verifikasi bebas sintaks error seluruh berkas PHP", '#064E3B', '#10B981'),
        ("4. Automated Unit Testing Suite", "Menjalankan 10 skrip pengujian logika transaksi", '#064E3B', '#10B981'),
        ("5. Deployment & Status Badge", "Badge GitHub Actions hijau (Passing) pada README.md", '#065F46', '#34D399')
    ]
    for i, (s_title, s_desc, s_bg, s_bd) in enumerate(stages):
        sy = 36 + (i * 9.5)
        ax.add_patch(FancyBboxPatch((55, sy), 38, 7.5, boxstyle="round,pad=0.2", facecolor=s_bg, edgecolor=s_bd, linewidth=1))
        ax.text(57, sy + 3.0, s_title, color='#FFFFFF', fontsize=7.2, fontweight='bold')
        ax.text(57, sy + 5.5, s_desc, color='#CBD5E1', fontsize=6.2)
        if i < 4:
            ax.annotate('', xy=(74, sy + 9.5), xytext=(74, sy + 7.5), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=1.2))

    plt.tight_layout()
    plt.savefig('Diagram_Hasil_Testing_Pass.png', dpi=300)
    plt.close()
    print("Saved Diagram_Hasil_Testing_Pass.png")

create_ai_architecture_diagram()
create_mvc_architecture_diagram()
create_time_validation_diagram()
create_testing_and_cicd_diagram()
