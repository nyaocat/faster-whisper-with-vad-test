# faster-whisper-with-vad-test

A sample program that combines sililero-VAD and faster-whisper for speech recognition.
I use a browser because it was very cumbersome to handle microphone input directly from Python.

## How to run

GPU and Cuda environment is required, please rewrite nvidia library dependencies in `requirements.txt` according to the CUDA version.

    pip install -r requirements.txt
    uvicorn app:main

Open a web page in your browser and speak into the microphone.
The default microphone is used, so check your settings. Also, I don't know why, but the microphone rarely stops working in the browser. If this happens, please restart your browser.
