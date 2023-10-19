import subprocess
import io
import wave
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize AWS Kinesis Video and S3 clients
kvs = boto3.client('kinesisvideo', region_name='YOUR_REGION')
s3 = boto3.client('s3', region_name='YOUR_REGION')

# Configure your Kinesis Video Stream and S3 bucket
stream_name = 'YOUR_KINESIS_STREAM'
s3_bucket = 'YOUR_S3_BUCKET'
wav_key = 'output.wav'

def extract_and_save_audio(event, context):
    kvs_stream = kvs.get_data_endpoint(StreamName=stream_name, APIName='GET_MEDIA')['DataEndpoint']

    # Fetch video frames
    stream_data = kvs.get_media(StartSelector={'StartSelectorType': 'EARLIEST'})
    
    audio_data = b''  # Initialize audio data buffer
    
    while True:
        frame = next(stream_data)
        if frame:
            frame_data = frame['Payload'].read()
            
            # Extract and decode audio packets from the video frame
            # You will need to implement the specific logic for your codec
            
            # Append the audio data to the buffer
            audio_data += extracted_audio_data
            
        else:
            break
    
    # Save the extracted audio as a WAV file
    with wave.open('/tmp/output.wav', 'wb') as wf:
        wf.setnchannels(2)  # 2 channels for stereo audio
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(44100)  # Sample rate (adjust as needed)
        wf.writeframes(audio_data)
    
    # Upload the WAV file to S3 or perform further actions as needed
    s3.upload_file('/tmp/output.wav', s3_bucket, wav_key)
    
    return {
        'statusCode': 200,
        'body': 'Audio extraction and WAV conversion complete.'
    }
