import matplotlib.pyplot as plt

from logic.audio.audio import get_instance


def get_audio_visualization():
    audio = get_instance().audio
    data = audio.get_array_of_samples()
    plt.figure(figsize=(20, 5))
    plt.plot(data, color='lightblue')
    plt.axis('off')
    plt.savefig(r'data\audio_plot.png', transparent=True)
