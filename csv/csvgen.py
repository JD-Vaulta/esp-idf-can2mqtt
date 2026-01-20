import csv

# List of baseIDs in hexadecimal (from your image)
base_ids_hex = [
    '0x100', '0x140', '0x180', '0x1c0', '0x200', '0x240', '0x280', '0x2c0', '0x300', '0x340', '0x380', '0x3c0', '0x400', '0x440',
    '0x480', '0x4c0', '0x500', '0x540', '0x580', '0x5c0', '0x600', '0x640', '0x680', '0x6c0', '0x700', '0x740', '0x780', '0x7c0'
]

base_ids = [int(x, 16) for x in base_ids_hex]

rows = []
for base_id in base_ids:
    for offset in range(0x3A):  # from baseID to baseID+0x39
        msg_id = base_id + offset
        rows.append(['S', hex(msg_id), f"/upload/1020ba44874c/can/{hex(msg_id)}/std"])

with open('./csv/can2mqtt.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
