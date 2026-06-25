import whisper
import json

model = whisper.load_model("small")

result = model.transcribe(
    audio="audios/sample.mp3",
    language="hi",
    task="translate",
    fp16=False
)

print(result["segments"])
chunks=[]
for segment in result["segments"]:
    chunks.append({"start":segment["start"],
                   "end":segment["end"],
                   "text":segment["text"]
                   })
    
print(chunks)
with open("output.json","w", encoding="utf-8") as f:
    json.dump(
        chunks,
        f,
        ensure_ascii=False,
        indent=4
    )

# with open("result.json","w",encoding="utf-8") as f:
#     json.dump(result,f,ensure_ascii=False,indent=4)

    
