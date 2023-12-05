
import sounddevice as sd
import soundfile as sf

DURATION = 10  # Recording duration in seconds

# Record audio


def record(file_path, sample_rate=44100, index=0):

    x = input("Press any key to continue")

    print("Recording...")
    audio = sd.rec(int(sample_rate * DURATION),
                   samplerate=sample_rate, channels=1)
    sd.wait()

    output_file = f"{file_path}/{index}.wav"
    sf.write(output_file, audio, sample_rate)
    print(f"Audio saved as {output_file}")


if __name__ == "__main__":
    wav_file_path = "./raw_data/test/"
    i = 0
    while (i < 1):
        record(wav_file_path, sample_rate=44100, index=i)
        i = i+1
