from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def text_to_speech(inpt, lang):
    authenticator = IAMAuthenticator('okICOKJVCAScAoT6ng7FivP5-DDT3ABxfDwpxgX6KBJy')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )
    text_to_speech.set_service_url('https://api.us-east.text-to-speech.watson.cloud.ibm.com')
    with open('audio.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text=input,
                voice='en-US_AllisonV3Voice',
                accept='audio/wav'
        ).get_result().content)


