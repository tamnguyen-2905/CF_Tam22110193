import math


def tinh_dien_tich_hinh_tron(r):
    """
    Hàm tính diện tích hình tròn.
    Công thức: S = π * r^2
    """
    if r < 0:
        raise ValueError("Bán kính không thể âm.")
    return math.pi * (r ** 2)


def main():
    try:
        # Nhập bán kính từ người dùng
        r_str = input("Nhập bán kính hình tròn: ").strip()

        # Kiểm tra dữ liệu nhập
        if not r_str.replace('.', '', 1).isdigit():
            print("Vui lòng nhập số hợp lệ.")
            return

        r = float(r_str)

        # Tính diện tích
        dien_tich = tinh_dien_tich_hinh_tron(r)

        # In kết quả với 2 chữ số thập phân
        print(f"Diện tích hình tròn bán kính {r} là: {dien_tich:.2f}")

    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")


if __name__ == "__main__":
    main()

