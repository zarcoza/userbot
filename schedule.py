import json
from datetime import datetime

def load_schedule():
    try:
        with open("database/schedule.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_schedule(data):
    with open("database/schedule.json", "w") as f:
        json.dump(data, f, indent=2)

@client.on(events.NewMessage(pattern=r"^/scheduleforward (text|forward) (.+?) (\d+) (\d+) (\d+)-(\d+) (\d+) ([a-z,]+) (\d{1,2}):(\d{2})$"))
async def schedule_forward_cmd(event):
    """Menjadwalkan pengiriman pesan mingguan."""
    mode, konten, jumlah_grup, durasi, jeda_min, jeda_max, perhari, hari_str, jam, menit = event.pattern_match.groups()
    jumlah_grup = int(jumlah_grup)
    durasi = int(durasi)
    jeda_min = int(jeda_min)
    jeda_max = int(jeda_max)
    perhari = int(perhari)
    jam = int(jam)
    menit = int(menit)

    # Cek format hari
    hari_valid = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    hari_list = hari_str.split(",")
    for h in hari_list:
        if h.lower() not in hari_valid:
            await event.reply(f"Hari tidak valid: {h}")
            return

    # Resolve username kalau mode forward
    if mode == "forward":
        try:
            username_channel, message_id = konten.split()
            if not username_channel.startswith("@"):
                username_channel = f"@{username_channel}"
            entity = await client.get_entity(username_channel)
            channel_id = entity.id
            konten = f"{channel_id} {message_id}"
        except Exception as e:
            await event.reply(f"Gagal membaca channel: {e}")
            return

    schedule = load_schedule()
    job_id = str(uuid.uuid4())[:8]
    schedule.append({
        "id": job_id,
        "user_id": event.sender_id,
        "mode": mode,
        "konten": konten,
        "jumlah_grup": jumlah_grup,
        "durasi": durasi,
        "jeda": [jeda_min, jeda_max],
        "perhari": perhari,
        "hari": hari_list,
        "jam": jam,
        "menit": menit
    })
    save_schedule(schedule)
    await event.reply(f"✅ Jadwal berhasil disimpan dengan ID `{job_id}` untuk hari {', '.join(hari_list)} pukul {jam:02d}:{menit:02d}!")

async def scheduler_loop():
    while True:
        now = datetime.now()
        weekday = now.strftime("%A").lower()
        schedule = load_schedule()

        for task in schedule:
            if weekday in task["hari"] and now.hour == task["jam"] and now.minute == task["menit"]:
                asyncio.create_task(
                    mulai_forward(
                        user_id=task["user_id"],
                        mode=task["mode"],
                        konten=task["konten"],
                        jumlah_grup=task["jumlah_grup"],
                        durasi_menit=task["durasi"],
                        jeda_range=task["jeda"],
                        total_perhari=task["perhari"],
                        from_schedule=True
                    )
                )
        await asyncio.sleep(60)