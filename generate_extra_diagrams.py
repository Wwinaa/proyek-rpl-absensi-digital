# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

def create_dual_sync_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    ax.text(50, 7, "MEKANISME TRANSAKSI ATOMIK DUAL-SYNC PRESENSI WALI KELAS", color='#F8FAFC', fontsize=12, fontweight='bold', ha='center')
    ax.text(50, 12, "Satu Kali Pemindaian Barcode Otomatis Mencatat Kehadiran Guru & Wali Kelas Simultan", color='#38BDF8', fontsize=8.5, ha='center')

    # Step 1: Scan
    ax.add_patch(FancyBboxPatch((4, 22), 22, 28, boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#38BDF8', linewidth=1.2))
    ax.text(15, 27, "1. PEMINDAIAN KARTU", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(15, 33, "Wali Kelas mengarahkan\nbarcode di gerbang sekolah", color='#E2E8F0', fontsize=7.2, ha='center')
    ax.text(15, 41, "Kode: WK-001 (NIP: 1985...)\nTerbaca < 0.3 Detik", color='#FDE047', fontsize=6.8, ha='center')

    # Arrow 1
    ax.annotate('', xy=(30, 36), xytext=(26, 36), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=2))

    # Step 2: Atomic Controller
    ax.add_patch(FancyBboxPatch((31, 18), 34, 38, boxstyle="round,pad=0.4", facecolor='#0F172A', edgecolor='#10B981', linewidth=1.4))
    ax.text(48, 23, "2. KONTROLER ATOMIK (PDO)", color='#34D399', fontsize=9, fontweight='bold', ha='center')
    ax.text(48, 28, "ScanController.php -> processScan()", color='#94A3B8', fontsize=7, ha='center')
    ax.text(48, 35, "$pdo->beginTransaction();\n// 1. Insert/Update absensi_guru\n// 2. Insert/Update absensi_wali_kelas\n$pdo->commit();", color='#A7F3D0', fontsize=7.2, ha='center', family='monospace')
    ax.text(48, 50, "[ACID COMPLIANT] Rollback otomatis bila salah satu gagal", color='#FCD34D', fontsize=6.5, ha='center')

    # Arrow 2 Split
    ax.annotate('', xy=(70, 27), xytext=(65, 32), arrowprops=dict(arrowstyle="->", color='#10B981', lw=1.8))
    ax.annotate('', xy=(70, 44), xytext=(65, 38), arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=1.8))

    # Table 1
    ax.add_patch(FancyBboxPatch((71, 18), 25, 17, boxstyle="round,pad=0.2", facecolor='#064E3B', edgecolor='#10B981', linewidth=1))
    ax.text(83.5, 23, "TABEL: absensi_guru", color='#34D399', fontsize=8, fontweight='bold', ha='center')
    ax.text(83.5, 28, "Menjamin hak kehadiran KBM\ndan tunjangan jam mengajar", color='#E2E8F0', fontsize=6.8, ha='center')

    # Table 2
    ax.add_patch(FancyBboxPatch((71, 38), 25, 17, boxstyle="round,pad=0.2", facecolor='#1E3A8A', edgecolor='#38BDF8', linewidth=1))
    ax.text(83.5, 43, "TABEL: absensi_wali_kelas", color='#BAE6FD', fontsize=8, fontweight='bold', ha='center')
    ax.text(83.5, 48, "Menjamin rekapitulasi pembinaan\nkelas binaan tetap sinkron", color='#E2E8F0', fontsize=6.8, ha='center')

    # Bottom summary box
    ax.add_patch(FancyBboxPatch((8, 62), 84, 30, boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#475569', linewidth=1))
    ax.text(50, 68, "MANFAAT REKAYASA SISTEM DUAL-SYNC:", color='#38BDF8', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(50, 75, "• Efisiensi Gerbang Sekolah: Wali Kelas tidak perlu mengantre atau memindai dua kali kartu identitas berbeda.", color='#E2E8F0', fontsize=7.2, ha='center')
    ax.text(50, 81, "• Konsistensi Data 100%: Meniadakan anomali di mana guru tercatat hadir mengajar namun alpa sebagai wali kelas.", color='#E2E8F0', fontsize=7.2, ha='center')
    ax.text(50, 87, "• Otomasi Pelaporan: Rekap bulanan untuk Kepala Sekolah dan TU langsung terisi secara bersamaan.", color='#E2E8F0', fontsize=7.2, ha='center')

    plt.tight_layout()
    plt.savefig('Diagram_Dual_Sync_Walikelas.png', dpi=300)
    plt.close()
    print("Saved Diagram_Dual_Sync_Walikelas.png")

def create_video_layout_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    ax.text(50, 7, "STANDAR TATA LETAK PEREKAMAN VIDEO PRESENTASI (BAB III PANDUAN)", color='#F8FAFC', fontsize=12, fontweight='bold', ha='center')
    ax.text(50, 12, "Resolusi Full HD 1080p, Audio Jernih & Wajah Mahasiswa Wajib Terlihat (Webcam Aktif)", color='#38BDF8', fontsize=8.5, ha='center')

    # Monitor Screen Simulation
    ax.add_patch(FancyBboxPatch((8, 18), 84, 64, boxstyle="round,pad=0.5", facecolor='#0F172A', edgecolor='#38BDF8', linewidth=1.5))
    
    # Screen inner (Main Screen Recording Area)
    ax.add_patch(Rectangle((10, 20), 80, 52, facecolor='#1E293B', edgecolor='#334155', linewidth=0.8))
    ax.text(42, 35, "[AREA TANGKAPAN LAYAR UTAMA - FULL HD 1080P]", color='#38BDF8', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(42, 42, "Presentasi Slide PRD / Penjelasan 4 UML / Live Demo Scan QR &\nInteraksi Chat Asisten AI Hadir.io Secara Real-Time", color='#E2E8F0', fontsize=7.5, ha='center')
    ax.text(42, 52, "Demonstrasi dilakukan secara LANGSUNG pada peramban web\n(Bukan sekadar menampilkan tangkapan layar / slide statis)", color='#FDE047', fontsize=7, ha='center', style='italic')

    # Webcam Overlay Box in Bottom-Right
    ax.add_patch(FancyBboxPatch((66, 44), 22, 26, boxstyle="round,pad=0.2", facecolor='#0284C7', edgecolor='#FFFFFF', linewidth=1.5))
    ax.text(77, 49, "[WEBCAM AKTIF]", color='#FFFFFF', fontsize=7.5, fontweight='bold', ha='center')
    ax.text(77, 54, "Wajah Mahasiswa\nTerlihat Jelas Sepanjang Video", color='#F0F9FF', fontsize=6.8, ha='center')
    ax.text(77, 62, "Winarti (41257168)\nSunyaragi Nexus", color='#FEF08A', fontsize=6.5, fontweight='bold', ha='center')

    # Bottom Guidelines Bar
    ax.add_patch(FancyBboxPatch((8, 77), 84, 16, boxstyle="round,pad=0.3", facecolor='#111827', edgecolor='#475569', linewidth=1))
    ax.text(50, 82, "DURASI & PEMBAGIAN SEGMEN:", color='#38BDF8', fontsize=7.8, fontweight='bold', ha='center')
    ax.text(50, 88, "• Progres 1: 3 - 5 Menit (PRD)  |  • Progres 2: 5 - 7 Menit (UML & UI/UX)  |  • Final Demo: 8 - 12 Menit (Live Demo Full)", color='#E2E8F0', fontsize=7.2, ha='center')

    plt.tight_layout()
    plt.savefig('Diagram_Layout_Video_Presentasi.png', dpi=300)
    plt.close()
    print("Saved Diagram_Layout_Video_Presentasi.png")

create_dual_sync_diagram()
create_video_layout_diagram()
