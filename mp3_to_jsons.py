import whisper
import json
import os

# create json folder if not exists
os.makedirs("jsons", exist_ok=True)

# load model
model = whisper.load_model("small")

audios = os.listdir("audios")

for audio in audios:

    if audio.endswith(".mp3") and "_" in audio:

        number = audio.split("_")[0]
        title = audio.split("_")[1].replace(".mp3", "")

        print(number, title)

        result = model.transcribe(
            audio=os.path.join("audios", audio),
            language="hi",
            task="translate",
            fp16=False
        )

        chunks = []

        for segment in result["segments"]:
            chunks.append({
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

        chunks_with_metadata = {
            "chunks": chunks,
            "text": result["text"]
        }

        with open(
            f"jsons/{audio}.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                chunks_with_metadata,
                f,
                ensure_ascii=False,
                indent=4
            )

        print("Saved:", audio)