import ctypes, wave, espeakng_loader as E
lib = ctypes.cdll.LoadLibrary(E.get_library_path())
CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_void_p)
_buf = []
@CB
def _cb(wav, n, ev):
    if n > 0: _buf.append(ctypes.string_at(wav, n * 2))
    return 0
rate = lib.espeak_Initialize(2, 0, E.get_data_path().encode(), 0)
lib.espeak_SetSynthCallback(_cb)
def synth(text, path, voice="en-us", speed=160, pitch=50):
    _buf.clear()
    lib.espeak_SetVoiceByName(voice.encode())
    lib.espeak_SetParameter(1, speed, 0); lib.espeak_SetParameter(3, pitch, 0)
    t = text.encode()
    lib.espeak_Synth(t, len(t) + 1, 0, 0, 0, 0x01, None, None)  # espeakCHARS_UTF8
    lib.espeak_Synchronize()
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(b"".join(_buf))
