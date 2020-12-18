import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

class googleSTT:
    def run(self,file_name='default'):
        
        client = speech.SpeechClient()
        file_names = file_name
        ip = file_name.split('_')[0]
        file_name = os.path.join(os.path.dirname(__file__), "payload", file_name)

        # Loads the audio into memory
        with io.open(file_name, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MULAW,
            sample_rate_hertz=8000,
            audio_channel_count=1,
            language_code="ko-KR",
            enable_automatic_punctuation=True
        )

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)
        
        text = ""

        for idx, result in enumerate(response.results):
            alternative = result.alternatives[0]
            print("-" * 20)
            print("Transcript: {}".format(alternative.transcript))
            text += alternative.transcript
        # [END speech_quickstart]

        return ip, text

    '''


    from google.cloud import speech

    client = speech.SpeechClient()

    with open('test113', "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="ko-KR",
        audio_channel_count=2,
        enable_separate_recognition_per_channel=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(alternative.transcript))
        print(u"Channel Tag: {}".format(result.channel_tag))
        '''