from vaultwares_media_processing.stream_wrapper import StreamDiffuser

_STREAM_DIFFUSER = None

def get_stream_diffuser():
    global _STREAM_DIFFUSER
    if _STREAM_DIFFUSER is None:
        _STREAM_DIFFUSER = StreamDiffuser()
    return _STREAM_DIFFUSER

def stylize_video(input_file, prompt, negative_prompt="", output_file=None, progress_callback=None, **kwargs):
    import os
    if not output_file:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_stylized{ext}"
    
    diffuser = get_stream_diffuser()
    return [diffuser.stylize_video(input_file, output_file, prompt, negative_prompt, progress_callback)]
