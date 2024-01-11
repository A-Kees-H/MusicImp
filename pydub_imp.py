from pydub import AudioSegment
from pydub.playback import play



def generate_base(length_ms):
    # Generate an empty audio segment of the specified length
    empty_audio = AudioSegment.silent(duration=length_ms)
    #empty_audio.export(output_file, format="wav")
    return empty_audio

def stretch_or_squish_sample(sample, new_length):
    # Calculate the speed factor required to achieve the new length
    speed_factor = new_length / len(sample)

    # Apply speedup or slowdown based on the calculated factor
    if speed_factor > 1:
        # Stretch the sample to the new length
        stretched_sample = sample.speedup(playback_speed=speed_factor)
        return stretched_sample[:new_length]  # Trim to exactly the new length
    elif speed_factor < 1:
        # Squish the sample to the new length
        squished_sample = sample.slowdown(playback_speed=speed_factor)
        return squished_sample[:new_length]  # Trim to exactly the new length
    else:
        # No stretching or squishing needed
        return sample[:new_length]  # Trim to exactly the new length

# Load audio samples
base = generate_base(180000)
sample1 = AudioSegment.from_file("music.wav", format="wav")
sample2 = AudioSegment.from_file("blueskyopens.wav", format="wav")
sample3 = AudioSegment.from_file("starsample.wav", format="wav")
# Overlay sample2 starting at 5 seconds in sample1 with 10 dB reduced volume
#overlay = base.overlay(sample2, position=5000, gain_during_overlay=-10)
base = base.overlay(sample2)
base = base.overlay(sample3, position=len(sample2))
play(base)