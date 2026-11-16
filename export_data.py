import sqlite3
import json
import csv
import os
import xml.etree.ElementTree as ET
import yaml

def export_guests_data():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    query = """
        SELECT g.guest_id, g.first_name, g.last_name, g.phone,
               b.booking_id, b.room_id, b.check_in_date, b.check_out_date, b.total_price, b.status
        FROM Guest g
        LEFT JOIN Booking b ON g.guest_id = b.guest_id;
    """
    cursor.execute(query)
    s = cursor.fetchall()
    
    guests_list = []
    for r in s:
        guest_data = {
            "guest_id": r[0],
            "first_name": r[1],
            "last_name": r[2],
            "phone": r[3],
            "booking": {
                "booking_id": r[4],
                "room_id": r[5],
                "check_in_date": r[6],
                "check_out_date": r[7],
                "total_price": r[8],
                "status": r[9]
            } if r[4] else None
        }
        guests_list.append(guest_data)
    conn.close()
    # --- 4. СОХРАНЕНИЕ В JSON ---
    json_path = os.path.join('out', 'data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(guests_list, f, ensure_ascii=False, indent=4)
    print("Сохранено: out/data.json")

    # --- 5. СОХРАНЕНИЕ В CSV ---
    csv_path = os.path.join('out', 'data.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Заголовки таблицы
        writer.writerow(['guest_id', 'first_name', 'last_name', 'phone', 'booking_id', 'room_id', 'check_in_date', 'check_out_date', 'total_price', 'status'])
        for r in s:
            writer.writerow(r)
    print("Сохранено: out/data.csv")

    # --- 6. СОХРАНЕНИЕ В XML ---
    root = ET.Element("Guests")
    for item in guests_list:
        guest_elem = ET.SubElement(root, "Guest")
        ET.SubElement(guest_elem, "guest_id").text = str(item["guest_id"])
        ET.SubElement(guest_elem, "first_name").text = str(item["first_name"])
        ET.SubElement(guest_elem, "last_name").text = str(item["last_name"])
        ET.SubElement(guest_elem, "phone").text = str(item["phone"])
        if item["booking"]:
            booking_elem = ET.SubElement(guest_elem, "Booking")
            for k, v in item["booking"].items():
                ET.SubElement(booking_elem, k).text = str(v) if v is not None else ""
                
    xml_tree = ET.ElementTree(root)
    xml_path = os.path.join('out', 'data.xml')
    xml_tree.write(xml_path, encoding='utf-8', xml_declaration=True)
    print("Сохранено: out/data.xml")
    # --- 7. СОХРАНЕНИЕ В YAML ---
    yaml_path = os.path.join('out', 'data.yaml')
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(guests_list, f, allow_unicode=True, sort_keys=False)
    print("Сохранено: out/data.yaml")
if __name__ == "__main__":
    export_guests_data()