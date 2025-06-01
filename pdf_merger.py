import os
from PyPDF2 import PdfMerger
import argparse

def merge_pdfs(pdf_list, output_filename):
    """
    PDF dosyalarını birleştirir.
    
    Args:
        pdf_list (list): Birleştirilecek PDF dosyalarının yol listesi
        output_filename (str): Çıktı dosyasının adı
    """
    merger = PdfMerger()
    
    try:
        for pdf_file in pdf_list:
            if os.path.exists(pdf_file):
                print(f"Ekleniyor: {pdf_file}")
                merger.append(pdf_file)
            else:
                print(f"Uyarı: {pdf_file} dosyası bulunamadı!")
        
        # Birleştirilmiş PDF'i kaydet
        with open(output_filename, 'wb') as output_file:
            merger.write(output_file)
        
        print(f"\nBaşarılı! PDF dosyaları '{output_filename}' olarak birleştirildi.")
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
    
    finally:
        merger.close()

def merge_pdfs_from_folder(folder_path, output_filename):
    """
    Bir klasördeki tüm PDF dosyalarını birleştirir.
    
    Args:
        folder_path (str): PDF dosyalarının bulunduğu klasör yolu
        output_filename (str): Çıktı dosyasının adı
    """
    if not os.path.exists(folder_path):
        print(f"Klasör bulunamadı: {folder_path}")
        return
    
    # Klasördeki PDF dosyalarını bul
    pdf_files = []
    for file in os.listdir(folder_path):
        if file.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(folder_path, file))
    
    # Dosyaları alfabetik sıraya göre sırala
    pdf_files.sort()
    
    if not pdf_files:
        print("Klasörde PDF dosyası bulunamadı!")
        return
    
    print(f"{len(pdf_files)} PDF dosyası bulundu:")
    for pdf in pdf_files:
        print(f"  - {os.path.basename(pdf)}")
    
    merge_pdfs(pdf_files, output_filename)

def main():
    print("=== PDF Birleştirme Uygulaması ===\n")
    
    # Komut satırı argümanları
    parser = argparse.ArgumentParser(description='PDF dosyalarını birleştir')
    parser.add_argument('--files', nargs='+', help='Birleştirilecek PDF dosyaları')
    parser.add_argument('--folder', help='PDF dosyalarının bulunduğu klasör')
    parser.add_argument('--output', default='birlestirilmis.pdf', help='Çıktı dosyası adı')
    
    args = parser.parse_args()
    
    # Komut satırından argüman verilmişse kullan
    if args.files:
        merge_pdfs(args.files, args.output)
    elif args.folder:
        merge_pdfs_from_folder(args.folder, args.output)
    else:
        # İnteraktif mod
        print("1. Dosya listesi girerek birleştir")
        print("2. Klasördeki tüm PDF'leri birleştir")
        
        choice = input("\nSeçiminizi yapın (1 veya 2): ").strip()
        
        if choice == "1":
            print("\nPDF dosyalarının yollarını virgülle ayırarak girin:")
            print("Örnek: dosya1.pdf, dosya2.pdf, dosya3.pdf")
            
            files_input = input("Dosyalar: ").strip()
            if files_input:
                pdf_files = [f.strip() for f in files_input.split(',')]
                output_name = input("Çıktı dosyası adı (varsayılan: birlestirilmis.pdf): ").strip()
                if not output_name:
                    output_name = "birlestirilmis.pdf"
                
                merge_pdfs(pdf_files, output_name)
            else:
                print("Dosya listesi boş!")
        
        elif choice == "2":
            folder = input("PDF dosyalarının bulunduğu klasör yolu: ").strip()
            if folder:
                output_name = input("Çıktı dosyası adı (varsayılan: birlestirilmis.pdf): ").strip()
                if not output_name:
                    output_name = "birlestirilmis.pdf"
                
                merge_pdfs_from_folder(folder, output_name)
            else:
                print("Klasör yolu boş!")
        
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()

# Örnek kullanım:
# python pdf_merger.py --files dosya1.pdf dosya2.pdf --output sonuc.pdf
# python pdf_merger.py --folder ./pdf_klasoru --output sonuc.pdf