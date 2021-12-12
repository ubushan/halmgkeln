import os
import torch
from textwrap import wrap


device = torch.device('cpu')
torch.set_num_threads(8)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/xal/v2_erdni.pt', local_file)  


def text_to_voice(text_value, userid):
    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device) 

    text = text_value

    chunks = wrap(text, 140)

    example_batch = chunks
    sample_rate = 16000

    
    audio_paths = model.save_wav(texts=example_batch, sample_rate=sample_rate)
    
    #print(audio_paths)
    audio_files = []
    for audio in audio_paths:
        audio_files.append(userid + audio)
        os.rename(audio, userid + audio)

    return audio_files