import math

def calculate_cable_size():
    """
    โปรแกรมคำนวณขนาดสายไฟสำหรับจอ LED
    """
    print("--- โปรแกรมคำนวณขนาดสายไฟสำหรับจอ LED ---")
    print("กรุณาป้อนข้อมูลต่อไปนี้:")

    # 1. ขนาดของจอ
    while True:
        try:
            width = float(input("ป้อนความกว้างของจอ (เมตร): "))
            height = float(input("ป้อนความสูงของจอ (เมตร): "))
            area = width * height
            print(f"พื้นที่ของจอทั้งหมด: {area:.2f} ตารางเมตร")
            break
        except ValueError:
            print("❌ กรุณาป้อนตัวเลขที่ถูกต้อง")

    # 2. กำลังไฟฟ้าต่อตารางเมตร
    while True:
        try:
            power_per_sqm = float(input("ป้อนกำลังไฟฟ้าที่ใช้ต่อ ตร.ม. (วัตต์/ตร.ม.): "))
            break
        except ValueError:
            print("❌ กรุณาป้อนตัวเลขที่ถูกต้อง")

    # คำนวณกำลังไฟฟ้ารวม
    power_watt = area * power_per_sqm
    print(f"กำลังไฟฟ้ารวมของจอทั้งหมด: {power_watt:.2f} วัตต์")

    # 3. จำนวนเฟส (Phase)
    while True:
        try:
            phase = int(input("ป้อนจำนวนเฟส (1 สำหรับเฟสเดียว, 3 สำหรับสามเฟส): "))
            if phase in [1, 3]:
                break
            else:
                print("❌ กรุณาป้อน 1 หรือ 3 เท่านั้น")
        except ValueError:
            print("❌ กรุณาป้อนตัวเลขที่ถูกต้อง")

    # 4. ประเภทการติดตั้ง (Installation Type)
    print("\nประเภทการติดตั้ง:")
    print("1: เดินลอยในอากาศ / ในท่อร้อยสาย (ภายในอาคาร)")
    print("2: เดินลอย / ร้อยท่อ (ภายนอกอาคาร / ต้องการความทนทาน)")
    print("3: เดินฝังดิน / ใต้ดิน")
    while True:
        try:
            installation_type = int(input("ป้อนตัวเลขประเภทการติดตั้ง (1-3): "))
            if installation_type in [1, 2, 3]:
                break
            else:
                print("❌ กรุณาป้อน 1, 2 หรือ 3 เท่านั้น")
        except ValueError:
            print("❌ กรุณาป้อนตัวเลขที่ถูกต้อง")

    # กำหนดค่าคงที่
    pf = 0.95  # Power Factor
    voltage = 220 if phase == 1 else 380  # แรงดันไฟฟ้า

    # 1. คำนวณกระแสไฟฟ้า (Amps)
    if phase == 1:
        current = power_watt / (voltage * pf)
    else:
        current = power_watt / (math.sqrt(3) * voltage * pf)

    print(f"\n✅ ผลการคำนวณเบื้องต้น:")
    print(f"กำลังไฟฟ้ารวม: {power_watt:.2f} วัตต์")
    print(f"แรงดันไฟฟ้า: {voltage} โวลต์")
    print(f"กระแสไฟฟ้าที่คำนวณได้: {current:.2f} แอมแปร์")

    # 2. กำหนดตารางค่าทนกระแสและชนิดสายไฟตามประเภทการติดตั้ง
    derating_factor = 1.0
    cable_type_name = "ไม่ระบุ"
    if installation_type == 1:
        derating_factor = 0.8  # เผื่อ 20% สำหรับการร้อยท่อ
        cable_type_name = "**THW** (ใช้งานทั่วไป, แกนเดี่ยว, เหมาะสำหรับร้อยท่อ)"
        print("ประเภทการติดตั้ง: เดินลอยในอากาศ / ในท่อร้อยสาย")
    elif installation_type == 2:
        derating_factor = 0.9  # เผื่อ 10% สำหรับงานหนัก
        cable_type_name = "**VCT** (ยืดหยุ่นสูง, ทนทาน, เหมาะสำหรับงานที่เคลื่อนที่หรือติดตั้งภายนอกอาคาร)"
        print("ประเภทการติดตั้ง: เดินลอย / ร้อยท่อ (ภายนอกอาคาร)")
    elif installation_type == 3:
        derating_factor = 1.0  # ค่าทนกระแสสำหรับฝังดินแล้ว
        cable_type_name = "**NYY** (แข็งแรงทนทาน, มีเปลือกหุ้ม 2 ชั้น, เหมาะสำหรับฝังดินโดยตรง)"
        print("ประเภทการติดตั้ง: เดินฝังดิน / ใต้ดิน")

    required_current = current / derating_factor
    print(f"กระแสไฟฟ้าที่ต้องเผื่อ: {required_current:.2f} แอมแปร์")

    # ตารางขนาดสายไฟ (ตามมาตรฐาน มอก. 11-2553)
    cable_table = {
        1.5: 18, 2.5: 24, 4: 32, 6: 42, 10: 57, 16: 76,
        25: 101, 35: 125, 50: 155, 70: 190, 95: 230,
        120: 265, 150: 305, 185: 350, 240: 410, 300: 475
    }

    # 3. เลือกขนาดสายไฟที่เหมาะสม
    suitable_cable_size = None
    cable_ampacity = 0
    for size, ampacity in sorted(cable_table.items()):
        if ampacity >= required_current:
            suitable_cable_size = size
            cable_ampacity = ampacity
            break

    # 4. คำนวณจำนวนวงจร (Circuit) ที่เหมาะสม
    breaker_rating = 0
    num_circuits = 1
    if suitable_cable_size:
        breaker_rating = math.floor(cable_ampacity * 0.8) # 80% ของค่าทนกระแสสาย
        if current > breaker_rating:
            num_circuits = math.ceil(current / breaker_rating)
        
    else:
        num_circuits = 1

    # 5. แสดงผลลัพธ์
    print("\n--- สรุปผลการคำนวณ ---")
    if suitable_cable_size:
        print(f"🔹 ชนิดสายไฟที่แนะนำ: {cable_type_name}")
        print(f"🔹 ขนาดสายไฟที่แนะนำ: **{suitable_cable_size} ตร.มม.**")
        print(f"🔹 ค่าทนกระแสของสาย: **{cable_ampacity} แอมแปร์**")
        print(f"🔹 จำนวนวงจรที่เหมาะสม: อย่างน้อย **{num_circuits} วงจร**")
        print(f"🔹 ขนาดเบรกเกอร์ (MCB) ที่แนะนำ: **{breaker_rating:.0f} แอมแปร์** ต่อวงจร")
    else:
        print("⚠️ ไม่พบขนาดสายไฟที่เหมาะสมในตาราง กรุณาปรึกษาวิศวกรไฟฟ้า")
    print("---------------------------------------")

if __name__ == "__main__":
    calculate_cable_size()