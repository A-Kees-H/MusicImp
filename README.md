# MusicImp
## a pydub implementation to programmatically write music using wav samples

I use Audacity to extract the samples from audio files as it's free and has a pleasant interface, but any wav file from any source should work with this program

generate a silent base to add your samples to with generate_base(length_in_ms)

squish or stretch a sample using the stretch_or_squish_sample(sample, new_length_in_ms) function

if you're getting a "permission denied" error or similar when running play(), a simple to fix is to add "f.close()" to line 15 of <your python install>\Lib\site-packages\pydub\playback.py
	as suggested by: https://stackoverflow.com/a/74968568
